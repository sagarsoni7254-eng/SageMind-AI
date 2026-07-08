import yfinance as yf

from app.providers.base_provider import MarketDataProvider
from app.schemas.company_profile import CompanyProfile


class YahooFinanceProvider(MarketDataProvider):

    def search_stock(self, query: str):
        """
        Temporary search implementation.
        Later we'll replace this with a real search API.
        """
        return {
            "provider": "Yahoo Finance",
            "query": query,
            "results": [
                {
                    "symbol": query.upper(),
                    "company": query.upper(),
                }
            ],
        }

    def company_profile(self, symbol: str) -> CompanyProfile:
        """
        Fetch live company profile from Yahoo Finance.
        """

        ticker = yf.Ticker(symbol)

        info = ticker.info

        return CompanyProfile(
            symbol=info.get("symbol", symbol.upper()),
            company_name=info.get("longName", "Unknown"),
            exchange=info.get("exchange", "Unknown"),
            sector=info.get("sector", "Unknown"),
            industry=info.get("industry", "Unknown"),
            market_cap=info.get("marketCap"),
            currency=info.get("currency", "Unknown"),
            country=info.get("country", "Unknown"),
        )