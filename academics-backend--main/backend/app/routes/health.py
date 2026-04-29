"""
Health Check Route
Simple endpoint to verify server is running
"""

from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()


@router.get("/ping")
async def health_check():
    """
    Health check endpoint
    Returns server status and timestamp
    """
    return {
        "status": "ok",
        "message": "pong",
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "service": "DSA Coding Assessment Platform"
    }
