from app.providers.provider_factory import ProviderFactory
from app.providers.provider_type import ProviderType


class StockService:

    def __init__(self):
        self.provider = ProviderFactory.create(
            ProviderType.YAHOO
        )

    def search_stock(self, query: str):
        return self.provider.search_stock(query)

    def company_profile(self, symbol: str):
        return self.provider.company_profile(symbol)

stock_service = StockService()