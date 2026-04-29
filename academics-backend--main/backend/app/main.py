"""
FastAPI Application Entry Point
DSA Coding Assessment Platform Backend
"""

import sys
import asyncio

# Fix for Windows asyncio subprocess support
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import teacher
from app.routes import health_router
from app.routes.auth import router as auth_router
from app.routes.execute import router as execute_router
from app.routes.admin import router as admin_router
from app.routes.student import router as student_router
from app.routes.practice import router as practice_router
from app.database import initialize_firebase

# Initialize Firebase on startup
initialize_firebase()

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for DSA Coding Assessment Platform",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ✅ FIXED CORS CONFIG (NO LOGIN BREAK)
explicit_origins = sorted(set((settings.ALLOWED_ORIGINS or []) + [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "https://testslashcoder.netlify.app",
    "https://slashcoder.in",
    "https://www.slashcoder.in",
    "https://test.slashcoder.in",
    "https://academics.slashcoder.in",
    "https://academics-frontendtest.vercel.app",  # ✅ ADDED (your current frontend)
]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=explicit_origins,
    allow_origin_regex=r"^https://([a-z0-9-]+\.)?netlify\.app$|^https://([a-z0-9-]+\.)?vercel\.app$|^https://([a-z0-9-]+\.)?slashcoder\.in$|^http://localhost(:\d+)?$|^http://127\.0\.0\.1(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ KEEP THIS (important for auth + fallback)
def _is_allowed_origin(origin: str) -> bool:
    if not origin:
        return False
    if origin in explicit_origins:
        return True
    import re
    return bool(re.match(
        r"^https://([a-z0-9-]+\.)?netlify\.app$|^https://([a-z0-9-]+\.)?vercel\.app$|^https://([a-z0-9-]+\.)?slashcoder\.in$|^http://localhost(:\d+)?$|^http://127\.0\.0\.1(:\d+)?$",
        origin
    ))

@app.middleware("http")
async def force_cors_headers(request: Request, call_next):
    origin = request.headers.get("origin", "")
    allowed = _is_allowed_origin(origin)

    if request.method == "OPTIONS" and allowed:
        return Response(
            status_code=204,
            headers={
                "Access-Control-Allow-Origin": origin,
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": request.headers.get("access-control-request-headers", "*"),
                "Vary": "Origin",
            },
        )

    response = await call_next(request)
    if allowed:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Vary"] = "Origin"
    return response

# Routes
app.include_router(health_router, tags=["Health"])
app.include_router(execute_router, tags=["Code Execution"])
app.include_router(teacher.router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(student_router)
app.include_router(practice_router, tags=["Practice"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to DSA Coding Assessment Platform API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/ping"
    }
