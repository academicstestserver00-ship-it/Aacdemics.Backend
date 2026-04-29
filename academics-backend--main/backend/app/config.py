"""
Application Configuration
Centralized settings for the DSA Coding Assessment Platform
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    
    # Server Configuration
    APP_NAME: str = "DSA Coding Assessment Platform"
    APP_VERSION: str = "1.0.0"
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    DEBUG: bool = True
    
    # CORS Settings
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "https://testslashcoder.netlify.app",
        "https://test.slashcoder.in",
        "https://thriving-hamster-86353b.netlify.app",
        "https://inquisitive-paletas-5ecd40.netlify.app",
    ]
    
    # Execution Limits
    DEFAULT_TIME_LIMIT_MS: int = 2000  # 2 seconds
    MAX_TIME_LIMIT_MS: int = 10000     # 10 seconds
    MAX_MEMORY_MB: int = 256           # 256 MB
    MAX_OUTPUT_SIZE_KB: int = 1024     # 1 MB
    
    # Code Execution
    ENABLE_DOCKER_SANDBOX: bool = False  # Will enable later
    TEMP_CODE_DIR: str = "/tmp/dsa_code_exec"
    
    # Supported Languages
    SUPPORTED_LANGUAGES: list[str] = ["python", "c", "cpp", "java"]
    
    # Database (Future)
    DATABASE_URL: Optional[str] = None
    
    # Authentication (Future)
    JWT_SECRET_KEY: Optional[str] = None
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
