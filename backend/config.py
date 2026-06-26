from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    APP_NAME: str = "PrepWise"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    FRONTEND_URL: str = "http://localhost:5500"

    # Redis (optional for now)
    REDIS_URL: str = "redis://localhost:6379"

    # JWT
    SECRET_KEY: str = "prepwise_dev_secret_key_change_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"   # ignore unknown keys in .env


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
