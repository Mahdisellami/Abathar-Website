from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator, computed_field
from typing import List


class Settings(BaseSettings):
    """Application settings and configuration"""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_parse_none_str="null",
    )

    # Database
    DATABASE_URL: str = "postgresql://abathar_user:abathar_password@localhost:5432/abathar_website"

    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True

    # CORS - stored as string, parsed to list
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"

    # Future AI features
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None

    @computed_field
    @property
    def allowed_origins_list(self) -> List[str]:
        """Parse ALLOWED_ORIGINS string into a list"""
        if isinstance(self.ALLOWED_ORIGINS, str):
            return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(',') if origin.strip()]
        return self.ALLOWED_ORIGINS


settings = Settings()
