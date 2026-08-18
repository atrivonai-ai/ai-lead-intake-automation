"""
Application entry point for the AI Lead Intake and Qualification Automation.
"""

from fastapi import FastAPI

from python.api.leads import router as leads_router
from python.api.webhook import router as webhook_router
from python.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description=(
        "API service supporting the AI Lead Intake and "
        "Qualification Automation."
    ),
)

app.include_router(leads_router)
app.include_router(webhook_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the current application health status."""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "environment": settings.app_env,
    }
