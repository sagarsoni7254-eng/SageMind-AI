from fastapi import APIRouter

from app.services.stock_service import stock_service

router = APIRouter(
    prefix="/api/v1/stocks",
    tags=["Stocks"],
)


@router.get("/search")
def search_stock(query: str):
    return stock_service.search_stock(query)


@router.get("/profile/{symbol}")
def company_profile(symbol: str):
    return stock_service.company_profile(symbol)