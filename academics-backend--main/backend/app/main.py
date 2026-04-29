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
from app.routes.execute import router as execute_router   # ✅ Judge0 router
from app.routes.admin import router as admin_router       # ✅ superadmin routes
from app.routes.student import router as student_router   # ✅ student routes
from app.routes.practice import router as practice_router # ✅ practice routes
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

# Configure CORS
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
]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=explicit_origins,
    # Allow preview/branch domains and other subdomains without redeploying backend each time.
    allow_origin_regex=r"^https://([a-z0-9-]+\.)?netlify\.app$|^https://([a-z0-9-]+\.)?slashcoder\.in$|^http://localhost(:\d+)?$|^http://127\.0\.0\.1(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _is_allowed_origin(origin: str) -> bool:
    if not origin:
        return False
    if origin in explicit_origins:
        return True
    import re
    return bool(re.match(r"^https://([a-z0-9-]+\.)?netlify\.app$|^https://([a-z0-9-]+\.)?slashcoder\.in$|^http://localhost(:\d+)?$|^http://127\.0\.0\.1(:\d+)?$", origin))


@app.middleware("http")
async def force_cors_headers(request: Request, call_next):
    """
    Fallback CORS guard:
    ensures preflight and error responses still include CORS headers for allowed origins.
    """
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

# Register routes
app.include_router(health_router, tags=["Health"])
app.include_router(execute_router, tags=["Code Execution"])
app.include_router(teacher.router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(student_router)
app.include_router(practice_router, tags=["Practice"])    # ✅ practice routes


@app.on_event("startup")
async def startup_event():
    print("=" * 60)
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION}")
    print("=" * 60)
    print(f"📍 Server running on: http://{settings.HOST}:{settings.PORT}")
    print(f"📚 API Docs: http://{settings.HOST}:{settings.PORT}/docs")
    print(f"🔧 Debug Mode: {settings.DEBUG}")
    print(f"💻 Supported Languages: {', '.join(settings.SUPPORTED_LANGUAGES)}")
    print(f"⏱️  Default Time Limit: {settings.DEFAULT_TIME_LIMIT_MS}ms")
    print(f"🔐 Auth: JWT enabled")
    print(f"🔥 Firebase: Realtime Database connected")
    print(f"⚡ Execution: Judge0 CE")
    print("=" * 60)


@app.on_event("shutdown")
async def shutdown_event():
    print("\n" + "=" * 60)
    print("🛑 Shutting down DSA Assessment Platform...")
    print("=" * 60)


@app.get("/")
async def root():
    return {
        "message": "Welcome to DSA Coding Assessment Platform API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/ping"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
