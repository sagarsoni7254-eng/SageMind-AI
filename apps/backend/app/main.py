from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.logging import logger, setup_logging

setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered multi-agent stock research platform",
)

logger.info("🚀 SageMind AI backend started successfully.")

app.include_router(health_router)