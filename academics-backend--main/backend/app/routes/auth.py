"""
Authentication Routes
JWT-based login and registration â€” Firebase Realtime Database
Supports email/password + Google OAuth (via Firebase ID token)
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
import random
import smtplib
import httpx
import bcrypt
import jwt
import os
import uuid
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from firebase_admin import db, auth as firebase_auth

router = APIRouter(prefix="/api/auth", tags=["auth"])

# â”€â”€ Config â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
SECRET_KEY = os.getenv("SECRET_KEY", "dsa-platform-secret-key-change-in-production")
SUPERADMIN_SECRET_KEY = os.getenv("SUPERADMIN_SECRET_KEY", "1122334455")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24
REGISTER_OTP_EXPIRE_MINUTES = int(os.getenv("REGISTER_OTP_EXPIRE_MINUTES", "10"))
REGISTER_OTP_MAX_ATTEMPTS = int(os.getenv("REGISTER_OTP_MAX_ATTEMPTS", "5"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
OTP_SMTP_EMAIL = os.getenv("OTP_SMTP_EMAIL", SMTP_EMAIL)
OTP_SMTP_PASSWORD = os.getenv("OTP_SMTP_PASSWORD", SMTP_PASSWORD)
OTP_SMTP_HOST = os.getenv("OTP_SMTP_HOST", "smtp.gmail.com")
OTP_SMTP_PORT = int(os.getenv("OTP_SMTP_PORT", "465"))
OTP_SMTP_USE_SSL = os.getenv("OTP_SMTP_USE_SSL", "true").strip().lower() in {"1", "true", "yes", "on"}
BREVO_API_KEY = os.getenv("BREVO_API_KEY", "")
BREVO_SENDER_EMAIL = os.getenv("BREVO_SENDER_EMAIL", "")
BREVO_SENDER_NAME = os.getenv("BREVO_SENDER_NAME", "SlashCoder")

security = HTTPBearer()


# â”€â”€ Pydantic schemas â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str | None = None  # ignored â€” all new users are students


class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterVerifyRequest(BaseModel):
    email: str
    code: str


class GoogleAuthRequest(BaseModel):
    id_token: str
    role: str | None = None  # ignored â€” all new Google users are students


class SuperAdminRegisterRequest(BaseModel):
    name: str
    email: str
    password: str


class AuthResponse(BaseModel):
    token: str
    user: dict


class RollNumberUpdateRequest(BaseModel):
    roll_number: str


# â”€â”€ Helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def generate_otp_code() -> str:
    return f"{random.randint(0, 999999):06d}"


def email_to_key(email: str) -> str:
    return hashlib.sha256((email or "").strip().lower().encode()).hexdigest()


def send_signup_otp_email(to_email: str, name: str, otp_code: str) -> tuple[bool, str]:
    html = f"""
<!DOCTYPE html>
<html>
<body style=\"font-family: Arial, sans-serif;\">
  <h2>Verify your SlashCoder account</h2>
  <p>Hi {name},</p>
  <p>Your verification code is:</p>
  <p style=\"font-size: 24px;\"><b>{otp_code}</b></p>
  <p>This code expires in {REGISTER_OTP_EXPIRE_MINUTES} minutes.</p>
  <p>If you did not request this, you can ignore this email.</p>
</body>
</html>
"""
    subject = "SlashCoder signup verification code"

    # Primary: Brevo transactional email API
    if BREVO_API_KEY and BREVO_SENDER_EMAIL:
        try:
            payload = {
                "sender": {"name": BREVO_SENDER_NAME, "email": BREVO_SENDER_EMAIL},
                "to": [{"email": to_email, "name": name or to_email}],
                "subject": subject,
                "htmlContent": html,
            }
            headers = {
                "accept": "application/json",
                "api-key": BREVO_API_KEY,
                "content-type": "application/json",
            }
            with httpx.Client(timeout=15.0) as client:
                resp = client.post("https://api.brevo.com/v3/smtp/email", json=payload, headers=headers)
            if 200 <= resp.status_code < 300:
                return True, ""
            return False, f"Brevo API error {resp.status_code}: {resp.text[:200]}"
        except Exception as e:
            return False, f"Brevo send failed: {e}"

    # Fallback: SMTP credentials
    if not OTP_SMTP_EMAIL or not OTP_SMTP_PASSWORD:
        return False, "Neither Brevo nor SMTP credentials are configured"

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"SlashCoder Platform <{OTP_SMTP_EMAIL}>"
        msg["To"] = to_email
        msg.attach(MIMEText(html, "html"))

        if OTP_SMTP_USE_SSL:
            with smtplib.SMTP_SSL(OTP_SMTP_HOST, OTP_SMTP_PORT) as server:
                server.login(OTP_SMTP_EMAIL, OTP_SMTP_PASSWORD)
                server.sendmail(OTP_SMTP_EMAIL, to_email, msg.as_string())
        else:
            with smtplib.SMTP(OTP_SMTP_HOST, OTP_SMTP_PORT) as server:
                server.starttls()
                server.login(OTP_SMTP_EMAIL, OTP_SMTP_PASSWORD)
                server.sendmail(OTP_SMTP_EMAIL, to_email, msg.as_string())
        return True, ""
    except Exception as e:
        print(f"[EMAIL ERROR] Signup OTP send failed for {to_email}: {e}")
        return False, str(e)


def create_student_user(name: str, email: str, password_hash: str) -> dict:
    user_id = str(uuid.uuid4())
    user_data = {
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "role": "student",  # always student - superadmin promotes to teacher
        "created_at": utcnow_iso()
    }
    db.reference(f"/users/{user_id}").set(user_data)
    token = create_token(user_id, "student", name, email)
    return {
        "token": token,
        "user": {"id": user_id, "name": name, "email": email, "role": "student", "roll_number": None}
    }


def create_token(user_id: str, role: str, name: str, email: str) -> str:
    payload = {
        "sub": str(user_id),
        "role": role,
        "name": name,
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired. Please login again.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token.")


def get_user_by_email(email: str):
    """Find a user in Firebase by email"""
    target = (email or "").strip().lower()
    users_ref = db.reference("/users")
    all_users = users_ref.get() or {}
    for user_id, user_data in all_users.items():
        if (user_data.get("email") or "").strip().lower() == target:
            user_data["id"] = user_id
            return user_data
    return None


def get_user_by_id(user_id: str):
    """Find a user in Firebase by ID"""
    user_ref = db.reference(f"/users/{user_id}")
    user = user_ref.get()
    if user:
        user["id"] = user_id
    return user


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """Dependency: extract and validate JWT, return user dict"""
    payload = decode_token(credentials.credentials)
    user = get_user_by_id(payload["sub"])
    if not user:
        raise HTTPException(status_code=401, detail="User not found.")
    return user


def require_teacher(current_user: dict = Depends(get_current_user)) -> dict:
    """Dependency: ensure current user is a teacher"""
    if current_user.get("role") != "teacher":
        raise HTTPException(status_code=403, detail="Teacher access required.")
    return current_user


def require_student(current_user: dict = Depends(get_current_user)) -> dict:
    """Dependency: ensure current user is a student"""
    if current_user.get("role") != "student":
        raise HTTPException(status_code=403, detail="Student access required.")
    return current_user


def require_superadmin(current_user: dict = Depends(get_current_user)) -> dict:
    """Dependency: ensure current user is a superadmin"""
    if current_user.get("role") != "superadmin":
        raise HTTPException(status_code=403, detail="Superadmin access required.")
    return current_user


# â”€â”€ Routes â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
@router.post("/register", response_model=AuthResponse)
def register(data: RegisterRequest):
    """Register a new account - all users default to student role"""
    email = (data.email or "").strip().lower()
    existing = get_user_by_email(email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return create_student_user(data.name, email, hash_password(data.password))


@router.post("/register/start")
def register_start(data: RegisterRequest):
    """Start signup: generate OTP and send to email."""
    email = (data.email or "").strip().lower()
    name = (data.name or "").strip()
    password = data.password or ""

    if not name:
        raise HTTPException(status_code=400, detail="Name is required.")
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters.")

    if get_user_by_email(email):
        raise HTTPException(status_code=400, detail="Email already registered.")

    code = generate_otp_code()
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(minutes=REGISTER_OTP_EXPIRE_MINUTES)
    pending_key = email_to_key(email)

    db.reference(f"/auth/pending_registrations/{pending_key}").set(
        {
            "name": name,
            "email": email,
            "password_hash": hash_password(password),
            "otp_code": code,
            "created_at": now.isoformat(),
            "expires_at": expires_at.isoformat(),
            "attempts": 0,
        }
    )

    sent, reason = send_signup_otp_email(email, name, code)
    if not sent:
        raise HTTPException(status_code=500, detail=f"Could not send verification code: {reason}")

    return {"message": f"Verification code sent to {email}."}


@router.post("/register/verify", response_model=AuthResponse)
def register_verify(data: RegisterVerifyRequest):
    """Verify OTP and create student account."""
    email = (data.email or "").strip().lower()
    code = (data.code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="Verification code is required.")

    pending_key = email_to_key(email)
    pending_ref = db.reference(f"/auth/pending_registrations/{pending_key}")
    pending = pending_ref.get()
    if not pending:
        raise HTTPException(status_code=400, detail="No pending signup found. Please request a new code.")

    try:
        expires_at = datetime.fromisoformat((pending.get("expires_at") or "").replace("Z", "+00:00"))
    except Exception:
        pending_ref.delete()
        raise HTTPException(status_code=400, detail="Signup session is invalid. Please restart signup.")

    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    if datetime.now(timezone.utc) > expires_at:
        pending_ref.delete()
        raise HTTPException(status_code=400, detail="Verification code expired. Please request a new code.")

    attempts = int(pending.get("attempts") or 0)
    if attempts >= REGISTER_OTP_MAX_ATTEMPTS:
        pending_ref.delete()
        raise HTTPException(status_code=400, detail="Too many invalid attempts. Please request a new code.")

    if code != str(pending.get("otp_code") or ""):
        pending_ref.update({"attempts": attempts + 1})
        raise HTTPException(status_code=400, detail="Invalid verification code.")

    if get_user_by_email(email):
        pending_ref.delete()
        raise HTTPException(status_code=400, detail="Email already registered.")

    name = pending.get("name") or email.split("@")[0]
    password_hash = pending.get("password_hash") or ""
    if not password_hash:
        pending_ref.delete()
        raise HTTPException(status_code=400, detail="Signup session is invalid. Please restart signup.")

    result = create_student_user(name, email, password_hash)
    pending_ref.delete()
    return result


@router.post("/superadmin/signup", response_model=AuthResponse)
def superadmin_signup(data: SuperAdminRegisterRequest, key: str = Query(...)):
    """
    Secret superadmin signup â€” only accessible with correct key.
    URL: POST /api/auth/superadmin/signup?key=1122334455
    """
    if key != SUPERADMIN_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid superadmin key.")

    existing = get_user_by_email(data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")

    user_id = str(uuid.uuid4())
    user_data = {
        "name": data.name,
        "email": data.email,
        "password_hash": hash_password(data.password),
        "role": "superadmin",
        "created_at": utcnow_iso()
    }

    db.reference(f"/users/{user_id}").set(user_data)

    token = create_token(user_id, "superadmin", data.name, data.email)
    return {
        "token": token,
        "user": {"id": user_id, "name": data.name, "email": data.email, "role": "superadmin", "roll_number": None}
    }


@router.post("/login", response_model=AuthResponse)
def login(data: LoginRequest):
    """Login with email and password, returns JWT token"""
    user = get_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    # Google-only accounts have no password_hash â€” direct them to Google login
    if not user.get("password_hash"):
        raise HTTPException(status_code=400, detail="This account uses Google sign-in. Please use 'Continue with Google'.")

    if not verify_password(data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    token = create_token(user["id"], user["role"], user["name"], user["email"])
    return {
        "token": token,
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "roll_number": user.get("roll_number"),
        }
    }


@router.post("/google")
def google_auth(data: GoogleAuthRequest):
    """
    Authenticate with Google.
    - Verifies Firebase ID token
    - If user exists â†’ return JWT
    - If new user â†’ auto-register as student, return JWT
    """
    try:
        decoded = firebase_auth.verify_id_token(data.id_token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Google token.")

    firebase_uid = decoded["uid"]
    email = decoded.get("email", "")
    name = decoded.get("name", email.split("@")[0])

    # Existing user â€” return JWT directly
    existing = get_user_by_email(email)
    if existing:
        token = create_token(existing["id"], existing["role"], existing["name"], existing["email"])
        return {
            "token": token,
            "user": {
                "id": existing["id"],
                "name": existing["name"],
                "email": existing["email"],
                "role": existing["role"],
                "roll_number": existing.get("roll_number"),
            }
        }

    # New Google user â€” auto-register as student
    user_id = str(uuid.uuid4())
    user_data = {
        "name": name,
        "email": email,
        "password_hash": "",
        "role": "student",  # always student
        "auth_provider": "google",
        "firebase_uid": firebase_uid,
        "created_at": utcnow_iso()
    }
    db.reference(f"/users/{user_id}").set(user_data)

    token = create_token(user_id, "student", name, email)
    return {
        "token": token,
        "user": {"id": user_id, "name": name, "email": email, "role": "student", "roll_number": None}
    }


@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    """Get current logged-in user info"""
    return {
        "id": current_user["id"],
        "name": current_user["name"],
        "email": current_user["email"],
        "role": current_user["role"],
        "roll_number": current_user.get("roll_number"),
    }


@router.patch("/me/roll-number")
def update_roll_number(data: RollNumberUpdateRequest, current_user: dict = Depends(get_current_user)):
    roll_number = (data.roll_number or "").strip()
    if not roll_number:
        raise HTTPException(status_code=400, detail="Roll number is required.")
    db.reference(f"/users/{current_user['id']}").update({"roll_number": roll_number})
    return {"message": "Roll number updated successfully.", "roll_number": roll_number}



