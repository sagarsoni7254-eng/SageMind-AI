from typing import Optional

from pydantic import BaseModel


class CompanyProfile(BaseModel):
    symbol: str
    company_name: str
    exchange: str
    sector: str
    industry: str

    market_cap: Optional[float] = None

    currency: str
    country: str