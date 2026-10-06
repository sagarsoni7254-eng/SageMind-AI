from fastapi import APIRouter

from app.services.stock_service import stock_service

router = APIRouter(
    prefix="/api/v1/stocks",
    tags=["Stocks"],
)


@router.get("/search")
def search_company(query: str):
    """
    Search companies by name.
    """
    return stock_service.search_company(query)


@router.get("/profile/{symbol}")
def company_profile(symbol: str):
    """
    Get company profile.
    """
    return stock_service.get_company_profile(symbol)


@router.get("/history/{symbol}")
def historical_prices(
    symbol: str,
    period: str = "1mo",
):
    """
    Get historical stock prices.
    """
    return stock_service.get_historical_prices(
        symbol=symbol,
        period=period,
    )