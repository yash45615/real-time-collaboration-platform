import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_NAME: str = "Real-Time Collaboration Platform"

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/collaboration_db",
    )

    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key",
    )

    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0",
    )

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()