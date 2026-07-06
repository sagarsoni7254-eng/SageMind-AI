from fastapi import APIRouter

from app.core.config import settings
from app.core.logging import logger

router = APIRouter(tags=["Health"])


@router.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
        "message": f"Welcome to {settings.PROJECT_NAME} 🚀",
    }


@router.get("/health")
def health():
    logger.info("Health endpoint checked")

    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }