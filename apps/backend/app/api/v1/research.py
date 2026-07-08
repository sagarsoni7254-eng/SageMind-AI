from fastapi import APIRouter

from app.services.research_service import research_service

router = APIRouter(
    prefix="/api/v1/research",
    tags=["Research"],
)


@router.get("/{symbol}")
def analyze(symbol: str):
    return research_service.analyze_stock(symbol)