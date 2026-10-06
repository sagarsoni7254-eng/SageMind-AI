from app.providers.provider_factory import ProviderFactory
from app.providers.provider_type import ProviderType


class StockService:
    """
    Handles all stock-related business logic.
    """

    def __init__(self):
        self.provider = ProviderFactory.create(
            ProviderType.YAHOO
        )

    def search_company(self, query: str):
        """
        Search companies by name.
        """
        return self.provider.search_company(query)

    def get_company_profile(self, symbol: str):
        """
        Get detailed company profile.
        """
        return self.provider.get_company_profile(symbol)

    def get_historical_prices(
        self,
        symbol: str,
        period: str = "1mo",
    ):
        """
        Get historical stock prices.
        """
        return self.provider.get_historical_prices(
            symbol=symbol,
            period=period,
        )


stock_service = StockService()