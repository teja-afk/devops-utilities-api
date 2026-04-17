from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "DevOps API"
    DEBUG: bool = False
    PORT: int = 8000
    
    # Business Logic
    CPU_THRESHOLD: int = 10
    S3_RETENTION_DAYS: int = 90

    # Load from .env file
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
