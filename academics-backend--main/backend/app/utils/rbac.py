"""
RBAC helpers and role constants for the platform.
"""

from __future__ import annotations

from typing import Dict, Optional

PRIMARY_ROOT_EMAIL = "sahuaditya2305@gmail.com"
PRIMARY_ROOT_FLAG = "is_primary_root_superadmin"

ROLE_ROOT_SUPERADMIN = "root_superadmin"
ROLE_SUPERADMIN = "superadmin"
ROLE_TEACHER = "teacher"
ROLE_STUDENT = "student"

VALID_ROLES = {
    ROLE_ROOT_SUPERADMIN,
    ROLE_SUPERADMIN,
    ROLE_TEACHER,
    ROLE_STUDENT,
}

ROLE_LEVEL = {
    ROLE_STUDENT: 1,
    ROLE_TEACHER: 2,
    ROLE_SUPERADMIN: 3,
    ROLE_ROOT_SUPERADMIN: 4,
}

# Note: explicit grants; hierarchy is only for conflict checks, not implicit grants.
ROLE_PERMISSIONS = {
    ROLE_ROOT_SUPERADMIN: {
        "assign_teacher",
        "revoke_teacher",
        "create_test",
        "attempt_test",
        "assign_root_superadmin",
        "revoke_root_superadmin",
        "assign_superadmin",
        "revoke_superadmin",
        "view_all_tests",
        "get_all_test_records",
        "get_teacher_test_mapping",
    },
    ROLE_SUPERADMIN: {
        "assign_teacher",
        "revoke_teacher",
        "create_test",
        "attempt_test",
    },
    ROLE_TEACHER: {
        "create_test",
        "attempt_test",
    },
    ROLE_STUDENT: {
        "attempt_test",
    },
}


def normalize_role(value: Optional[str]) -> str:
    role = (value or "").strip().lower()
    if role in VALID_ROLES:
        return role
    # Legacy fallback
    if role == "root":
        return ROLE_ROOT_SUPERADMIN
    if role == "admin":
        return ROLE_SUPERADMIN
    return ROLE_STUDENT


def role_level(role: Optional[str]) -> int:
    return ROLE_LEVEL.get(normalize_role(role), ROLE_LEVEL[ROLE_STUDENT])


def has_permission(role: Optional[str], permission: str) -> bool:
    normalized = normalize_role(role)
    return permission in ROLE_PERMISSIONS.get(normalized, set())


def is_root_superadmin(user: Optional[Dict]) -> bool:
    if not user:
        return False
    return normalize_role(user.get("role")) == ROLE_ROOT_SUPERADMIN


def is_primary_root_superadmin(user: Optional[Dict]) -> bool:
    if not user:
        return False
    if bool(user.get(PRIMARY_ROOT_FLAG)):
        return True
    email = (user.get("email") or "").strip().lower()
    return email == PRIMARY_ROOT_EMAIL.lower()


def normalize_user_record(user: Optional[Dict]) -> tuple[Dict, bool]:
    """
    Normalize stored user role/flags and return (normalized_user, changed).
    """
    data = dict(user or {})
    changed = False

    normalized_role = normalize_role(data.get("role"))
    if data.get("role") != normalized_role:
        data["role"] = normalized_role
        changed = True

    if is_primary_root_superadmin(data):
        if data.get("role") != ROLE_ROOT_SUPERADMIN:
            data["role"] = ROLE_ROOT_SUPERADMIN
            changed = True
        if not data.get(PRIMARY_ROOT_FLAG):
            data[PRIMARY_ROOT_FLAG] = True
            changed = True

    return data, changed


def can_modify_target_role(actor_role: Optional[str], target_role: Optional[str]) -> bool:
    """
    Lower/equal roles cannot modify higher/equal roles.
    """
    return role_level(actor_role) > role_level(target_role)


def count_root_superadmins(all_users: Dict[str, Dict]) -> int:
    return sum(
        1
        for user in (all_users or {}).values()
        if normalize_role(user.get("role")) == ROLE_ROOT_SUPERADMIN
    )

