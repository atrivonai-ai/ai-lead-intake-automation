"""
Application configuration for the AI Lead Intake and Qualification Automation.
"""

from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = Field(
        default="AI Lead Intake and Qualification Automation",
        validation_alias="APP_NAME",
    )
    app_env: str = Field(
        default="development",
        validation_alias="APP_ENV",
    )
    app_host: str = Field(
        default="127.0.0.1",
        validation_alias="APP_HOST",
    )
    app_port: int = Field(
        default=8000,
        validation_alias="APP_PORT",
    )

    ai_api_key: str = Field(
        default="",
        validation_alias="AI_API_KEY",
    )
    ai_model: str = Field(
        default="",
        validation_alias="AI_MODEL",
    )

    notion_api_key: str = Field(
        default="",
        validation_alias="NOTION_API_KEY",
    )
    notion_database_id: str = Field(
        default="",
        validation_alias="NOTION_DATABASE_ID",
    )

    n8n_webhook_url: str = Field(
        default="",
        validation_alias="N8N_WEBHOOK_URL",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return the cached application settings."""
    return Settings()