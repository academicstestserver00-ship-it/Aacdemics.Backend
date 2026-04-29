 
import firebase_admin
from firebase_admin import credentials, db
import os
import json
from datetime import datetime, timezone

def initialize_firebase():
    if not firebase_admin._apps:
        firebase_creds = os.environ.get("FIREBASE_CREDENTIALS")
        database_url = os.environ.get("FIREBASE_DATABASE_URL")
        
        if firebase_creds:
            cred_dict = json.loads(firebase_creds)
            cred = credentials.Certificate(cred_dict)
        else:
            # Local development — use the JSON file directly
            cred = cred = credentials.Certificate("H:/DataStructure/DSA/database/test-slashcoder-20a45-firebase-adminsdk-fbsvc-99f93e94d0.json")
            database_url = "https://test-slashcoder-20a45-default-rtdb.firebaseio.com"
        
        firebase_admin.initialize_app(cred, {
            "databaseURL": database_url
        })

initialize_firebase()

def get_db():
    return db.reference("/")


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def log_audit_event(
    *,
    user_id: str,
    action: str,
    resource_id: str | None = None,
    metadata: dict | None = None,
):
    """
    Store auditable admin/teacher actions under /audit_logs.
    """
    entry = {
        "user_id": user_id,
        "action": action,
        "resource_id": resource_id,
        "timestamp": utcnow_iso(),
        "metadata": metadata or {},
    }
    db.reference("/audit_logs").push(entry)
