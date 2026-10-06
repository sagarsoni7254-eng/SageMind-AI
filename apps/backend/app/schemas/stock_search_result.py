from pydantic import BaseModel


class StockSearchResult(BaseModel):
    symbol: str
    company_name: str
    exchange: str