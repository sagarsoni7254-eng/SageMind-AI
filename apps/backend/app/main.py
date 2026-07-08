from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.logging import logger, setup_logging
from app.api.v1.stocks import router as stocks_router
from app.api.v1.research import router as research_router
setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered multi-agent stock research platform",
)

logger.info("🚀 SageMind AI backend started successfully.")

app.include_router(health_router)
app.include_router(stocks_router)
app.include_router(research_router)