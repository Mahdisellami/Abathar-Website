from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings and configuration"""

    # Database
    DATABASE_URL: str = "postgresql://abathar_user:abathar_password@localhost:5432/abathar_website"

    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    # Future AI features
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
