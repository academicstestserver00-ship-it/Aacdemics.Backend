"""
Admin Routes
Role and platform governance endpoints.
"""

from datetime import datetime, timezone
import os
import random
import smtplib
import string
import uuid

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import APIRouter, Depends, HTTPException, Query
from firebase_admin import db
from pydantic import BaseModel

from app.database import log_audit_event
from app.routes.auth import get_user_by_email, hash_password, require_superadmin
from app.utils.rbac import (
    PRIMARY_ROOT_EMAIL,
    PRIMARY_ROOT_FLAG,
    ROLE_ROOT_SUPERADMIN,
    ROLE_STUDENT,
    ROLE_SUPERADMIN,
    ROLE_TEACHER,
    can_modify_target_role,
    count_root_superadmins,
    has_permission,
    is_primary_root_superadmin,
    normalize_role,
)

router = APIRouter(prefix="/api/admin", tags=["admin"])

SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
PLATFORM_URL = os.getenv("PLATFORM_URL", "https://testslashcoder.netlify.app")


class RoleUpdateRequest(BaseModel):
    email: str
    role: str


class AddTeacherRequest(BaseModel):
    name: str
    email: str


class RoleActionRequest(BaseModel):
    user_id: str


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def require_root_superadmin(current_user: dict = Depends(require_superadmin)) -> dict:
    if normalize_role(current_user.get("role")) != ROLE_ROOT_SUPERADMIN:
        raise HTTPException(status_code=403, detail="Root superadmin access required.")
    return current_user


def _all_users() -> dict:
    return db.reference("/users").get() or {}


def _user_by_id(user_id: str) -> dict | None:
    data = db.reference(f"/users/{user_id}").get()
    if not data:
        return None
    data = dict(data)
    data["id"] = user_id
    data["role"] = normalize_role(data.get("role"))
    return data


def _user_by_email(email: str) -> tuple[str | None, dict | None]:
    target = (email or "").strip().lower()
    for uid, data in _all_users().items():
        if (data.get("email") or "").strip().lower() == target:
            user = dict(data)
            user["id"] = uid
            user["role"] = normalize_role(user.get("role"))
            return uid, user
    return None, None


def _assert_not_primary_root(target_user: dict):
    if is_primary_root_superadmin(target_user):
        raise HTTPException(status_code=403, detail="Operation not allowed on primary root superadmin")


def _ensure_not_last_root_removal(target_user: dict, new_role: str | None = None):
    target_is_root = normalize_role(target_user.get("role")) == ROLE_ROOT_SUPERADMIN
    removing_root = target_is_root and (new_role is None or normalize_role(new_role) != ROLE_ROOT_SUPERADMIN)
    if not removing_root:
        return

    users = _all_users()
    roots = count_root_superadmins(users)
    if roots <= 1:
        raise HTTPException(status_code=400, detail="Operation blocked: system must have at least one root_superadmin")


def _can_modify_user(actor: dict, target: dict):
    actor_role = normalize_role(actor.get("role"))
    target_role = normalize_role(target.get("role"))
    if actor_role == ROLE_ROOT_SUPERADMIN and target_role == ROLE_ROOT_SUPERADMIN:
        return
    if not can_modify_target_role(actor_role, target_role):
        raise HTTPException(status_code=403, detail="Insufficient role hierarchy to modify target user")


def _set_role(actor: dict, target: dict, new_role: str):
    actor_role = normalize_role(actor.get("role"))
    old_role = normalize_role(target.get("role"))
    new_role = normalize_role(new_role)

    if old_role == new_role:
        return target

    _assert_not_primary_root(target)
    _ensure_not_last_root_removal(target, new_role)

    if actor_role != ROLE_ROOT_SUPERADMIN:
        if new_role in {ROLE_SUPERADMIN, ROLE_ROOT_SUPERADMIN}:
            raise HTTPException(status_code=403, detail="Only root superadmin can manage superadmin/root_superadmin roles")
        # superadmin can only assign/revoke teacher
        if not has_permission(actor_role, "assign_teacher"):
            raise HTTPException(status_code=403, detail="Insufficient permission")
        if old_role not in {ROLE_STUDENT, ROLE_TEACHER}:
            raise HTTPException(status_code=403, detail="Superadmin can only manage teacher/student roles")
        if new_role not in {ROLE_STUDENT, ROLE_TEACHER}:
            raise HTTPException(status_code=403, detail="Superadmin can only assign/revoke teacher role")

    _can_modify_user(actor, target)

    db.reference(f"/users/{target['id']}").update({"role": new_role})

    action = "role_assignment" if new_role in {ROLE_TEACHER, ROLE_SUPERADMIN, ROLE_ROOT_SUPERADMIN} and old_role != new_role else "role_revocation"
    log_audit_event(
        user_id=actor["id"],
        action=action,
        resource_id=target["id"],
        metadata={"from_role": old_role, "to_role": new_role},
    )

    target["role"] = new_role
    return target


def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%"),
    ]
    password += random.choices(chars, k=length - 4)
    random.shuffle(password)
    return "".join(password)


def send_teacher_welcome_email(to_email: str, name: str, password: str) -> bool:
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Welcome to SlashCoder - Your Teacher Account is Ready"
        msg["From"] = f"SlashCoder Platform <{SMTP_EMAIL}>"
        msg["To"] = to_email

        html = f"""
<!DOCTYPE html>
<html>
<body style=\"font-family: Arial, sans-serif;\">
  <h2>Welcome to SlashCoder</h2>
  <p>Hi {name}, your teacher account has been created.</p>
  <p><b>Email:</b> {to_email}</p>
  <p><b>Password:</b> {password}</p>
  <p><a href=\"{PLATFORM_URL}\">Login to SlashCoder</a></p>
</body>
</html>
"""
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, to_email, msg.as_string())

        return True
    except Exception as e:
        print(f"[EMAIL ERROR] Failed to send to {to_email}: {e}")
        return False


@router.get("/users/search")
def search_user_by_email(email: str = Query(...), current_user: dict = Depends(require_root_superadmin)):
    user_id, user_data = _user_by_email(email)
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found.")
    return {
        "id": user_id,
        "name": user_data.get("name"),
        "email": user_data.get("email"),
        "role": normalize_role(user_data.get("role")),
        "created_at": user_data.get("created_at"),
        "auth_provider": user_data.get("auth_provider", "email"),
        PRIMARY_ROOT_FLAG: bool(user_data.get(PRIMARY_ROOT_FLAG)),
    }


@router.get("/users")
def get_all_users(current_user: dict = Depends(require_root_superadmin)):
    all_users = _all_users()
    result = []
    for user_id, user_data in all_users.items():
        role = normalize_role(user_data.get("role"))
        result.append(
            {
                "id": user_id,
                "name": user_data.get("name"),
                "email": user_data.get("email"),
                "role": role,
                "created_at": user_data.get("created_at"),
                "auth_provider": user_data.get("auth_provider", "email"),
                PRIMARY_ROOT_FLAG: bool(user_data.get(PRIMARY_ROOT_FLAG)),
            }
        )
    result.sort(key=lambda x: x.get("created_at") or "", reverse=True)
    return result


@router.post("/add-teacher")
def add_teacher(data: AddTeacherRequest, current_user: dict = Depends(require_superadmin)):
    if not has_permission(current_user.get("role"), "assign_teacher"):
        raise HTTPException(status_code=403, detail="Insufficient permission")

    existing = get_user_by_email(data.email)
    if existing:
        raise HTTPException(status_code=400, detail="A user with this email already exists.")

    password = generate_password()
    user_id = str(uuid.uuid4())
    user_data = {
        "name": data.name,
        "email": data.email,
        "password_hash": hash_password(password),
        "role": ROLE_TEACHER,
        PRIMARY_ROOT_FLAG: False,
        "auth_provider": "email",
        "created_by": current_user.get("email"),
        "created_at": utcnow_iso(),
    }

    db.reference(f"/users/{user_id}").set(user_data)

    log_audit_event(
        user_id=current_user["id"],
        action="role_assignment",
        resource_id=user_id,
        metadata={"from_role": None, "to_role": ROLE_TEACHER, "reason": "add_teacher"},
    )

    email_sent = send_teacher_welcome_email(data.email, data.name, password)

    return {
        "message": "Teacher account created successfully.",
        "email_sent": email_sent,
        "generated_password": password,
        "user": {
            "id": user_id,
            "name": data.name,
            "email": data.email,
            "role": ROLE_TEACHER,
        },
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: str, current_user: dict = Depends(require_root_superadmin)):
    user_ref = db.reference(f"/users/{user_id}")
    target_user = user_ref.get()

    if not target_user:
        raise HTTPException(status_code=404, detail="User not found.")

    target = dict(target_user)
    target["id"] = user_id
    target["role"] = normalize_role(target.get("role"))

    _assert_not_primary_root(target)
    _ensure_not_last_root_removal(target, None)

    if user_id == current_user.get("id"):
        raise HTTPException(status_code=403, detail="You cannot delete your own account.")

    user_ref.delete()

    log_audit_event(
        user_id=current_user["id"],
        action="role_revocation",
        resource_id=user_id,
        metadata={"deleted_user_role": target.get("role")},
    )

    return {
        "message": "User deleted successfully.",
        "deleted_user": {
            "id": user_id,
            "name": target.get("name"),
            "email": target.get("email"),
            "role": target.get("role"),
        },
    }


@router.patch("/users/role")
def update_user_role(data: RoleUpdateRequest, current_user: dict = Depends(require_superadmin)):
    target_id, target_user = _user_by_email(data.email)
    if not target_id:
        raise HTTPException(status_code=404, detail="User not found.")

    new_role = normalize_role(data.role)
    if new_role not in {ROLE_STUDENT, ROLE_TEACHER, ROLE_SUPERADMIN, ROLE_ROOT_SUPERADMIN}:
        raise HTTPException(status_code=400, detail=f"Invalid role '{data.role}'.")

    updated = _set_role(current_user, target_user, new_role)

    return {
        "message": "Role updated successfully.",
        "user": {
            "id": updated["id"],
            "name": updated.get("name"),
            "email": updated.get("email"),
            "role": updated.get("role"),
        },
    }


@router.post("/users/{user_id}/assign-teacher")
def assign_teacher(user_id: str, current_user: dict = Depends(require_superadmin)):
    target = _user_by_id(user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found.")
    updated = _set_role(current_user, target, ROLE_TEACHER)
    return {"message": "Teacher role assigned successfully.", "user_id": updated["id"], "role": updated["role"]}


@router.post("/users/{user_id}/revoke-teacher")
def revoke_teacher(user_id: str, current_user: dict = Depends(require_superadmin)):
    target = _user_by_id(user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found.")
    updated = _set_role(current_user, target, ROLE_STUDENT)
    return {"message": "Teacher role revoked successfully.", "user_id": updated["id"], "role": updated["role"]}


@router.post("/users/{user_id}/assign-root-superadmin")
def assign_root_superadmin(user_id: str, current_user: dict = Depends(require_root_superadmin)):
    target = _user_by_id(user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found.")
    updated = _set_role(current_user, target, ROLE_ROOT_SUPERADMIN)
    return {"message": "Root superadmin assigned successfully.", "user_id": updated["id"], "role": updated["role"]}


@router.post("/users/{user_id}/revoke-root-superadmin")
def revoke_root_superadmin(user_id: str, current_user: dict = Depends(require_root_superadmin)):
    target = _user_by_id(user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found.")
    updated = _set_role(current_user, target, ROLE_SUPERADMIN)
    return {"message": "Root superadmin revoked successfully.", "user_id": updated["id"], "role": updated["role"]}


@router.post("/users/{user_id}/assign-superadmin")
def assign_superadmin(user_id: str, current_user: dict = Depends(require_root_superadmin)):
    target = _user_by_id(user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found.")
    updated = _set_role(current_user, target, ROLE_SUPERADMIN)
    return {"message": "Superadmin assigned successfully.", "user_id": updated["id"], "role": updated["role"]}


@router.post("/users/{user_id}/revoke-superadmin")
def revoke_superadmin(user_id: str, current_user: dict = Depends(require_root_superadmin)):
    target = _user_by_id(user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found.")
    updated = _set_role(current_user, target, ROLE_STUDENT)
    return {"message": "Superadmin revoked successfully.", "user_id": updated["id"], "role": updated["role"]}


@router.get("/submissions")
def get_all_submissions(limit: int = 100, current_user: dict = Depends(require_root_superadmin)):
    all_subs = db.reference("/submissions").get() or {}
    all_users = db.reference("/users").get() or {}
    all_questions = db.reference("/questions").get() or {}

    user_map = {uid: u for uid, u in all_users.items()}
    question_map = {qid: q for qid, q in all_questions.items()}

    result = []
    for sub_id, sub in all_subs.items():
        student = user_map.get(sub.get("student_id"), {})
        question = question_map.get(sub.get("question_id"), {})
        result.append(
            {
                "id": sub_id,
                "student_name": student.get("name", "Unknown"),
                "student_email": student.get("email", ""),
                "question_title": question.get("title", "Unknown"),
                "test_id": sub.get("test_id"),
                "language": sub.get("language"),
                "score": sub.get("score"),
                "passed": sub.get("passed"),
                "total": sub.get("total"),
                "submitted_at": sub.get("submitted_at"),
            }
        )

    result.sort(key=lambda x: x.get("submitted_at") or "", reverse=True)
    return result[:limit]


@router.get("/analytics")
def get_platform_analytics(current_user: dict = Depends(require_root_superadmin)):
    all_users = _all_users()
    all_tests = db.reference("/tests").get() or {}
    all_questions = db.reference("/questions").get() or {}
    all_submissions = db.reference("/submissions").get() or {}

    role_counts = {ROLE_STUDENT: 0, ROLE_TEACHER: 0, ROLE_SUPERADMIN: 0, ROLE_ROOT_SUPERADMIN: 0}
    for u in all_users.values():
        role = normalize_role(u.get("role"))
        role_counts[role] = role_counts.get(role, 0) + 1

    active_tests = sum(1 for t in all_tests.values() if t.get("is_active"))
    inactive_tests = len(all_tests) - active_tests

    lang_counts = {}
    for s in all_submissions.values():
        lang = s.get("language", "unknown")
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    scores = [s.get("score", 0) for s in all_submissions.values() if s.get("score") is not None]
    avg_score = round(sum(scores) / len(scores), 2) if scores else 0

    return {
        "users": {
            "total": len(all_users),
            "students": role_counts.get(ROLE_STUDENT, 0),
            "teachers": role_counts.get(ROLE_TEACHER, 0),
            "superadmins": role_counts.get(ROLE_SUPERADMIN, 0),
            "root_superadmins": role_counts.get(ROLE_ROOT_SUPERADMIN, 0),
        },
        "tests": {
            "total": len(all_tests),
            "active": active_tests,
            "inactive": inactive_tests,
        },
        "questions": {
            "total": len(all_questions),
        },
        "submissions": {
            "total": len(all_submissions),
            "average_score": avg_score,
            "by_language": lang_counts,
        },
    }


@router.get("/root/tests-overview")
def get_root_tests_overview(current_user: dict = Depends(require_root_superadmin)):
    all_tests = db.reference("/tests").get() or {}
    all_users = _all_users()
    all_questions = db.reference("/questions").get() or {}
    all_submissions = db.reference("/submissions").get() or {}

    tests = []
    tests_by_teacher = {}

    for test_id, test in all_tests.items():
        teacher_id = test.get("teacher_id") or test.get("created_by")
        teacher = all_users.get(teacher_id, {}) if teacher_id else {}
        question_count = sum(1 for q in all_questions.values() if q.get("test_id") == test_id)
        submission_count = sum(1 for s in all_submissions.values() if s.get("test_id") == test_id)

        row = {
            "id": test_id,
            "title": test.get("title"),
            "description": test.get("description"),
            "is_active": bool(test.get("is_active")),
            "created_at": test.get("created_at"),
            "assessment_id": test.get("assessment_id", ""),
            "duration_minutes": test.get("duration_minutes", 60),
            "teacher_id": teacher_id,
            "teacher_name": teacher.get("name") or "Unknown",
            "teacher_email": teacher.get("email") or "",
            "question_count": question_count,
            "submission_count": submission_count,
        }
        tests.append(row)

        key = teacher_id or "unknown"
        if key not in tests_by_teacher:
            tests_by_teacher[key] = {
                "teacher_id": teacher_id,
                "teacher_name": teacher.get("name") or "Unknown",
                "teacher_email": teacher.get("email") or "",
                "tests_created": 0,
                "total_questions": 0,
                "total_submissions": 0,
            }
        tests_by_teacher[key]["tests_created"] += 1
        tests_by_teacher[key]["total_questions"] += question_count
        tests_by_teacher[key]["total_submissions"] += submission_count

    tests.sort(key=lambda t: t.get("created_at") or "", reverse=True)
    teacher_rows = sorted(
        tests_by_teacher.values(),
        key=lambda t: (t.get("tests_created", 0), t.get("teacher_name") or ""),
        reverse=True,
    )

    return {
        "totals": {
            "tests": len(tests),
            "teachers_with_tests": len([x for x in teacher_rows if x.get("teacher_id")]),
            "questions": sum(t.get("question_count", 0) for t in tests),
            "submissions": sum(t.get("submission_count", 0) for t in tests),
        },
        "teachers": teacher_rows,
        "tests": tests,
    }
