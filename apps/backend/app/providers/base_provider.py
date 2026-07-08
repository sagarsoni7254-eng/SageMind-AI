from abc import ABC, abstractmethod

from app.schemas.company_profile import CompanyProfile


class MarketDataProvider(ABC):

    @abstractmethod
    def search_stock(self, query: str):
        pass

    @abstractmethod
    def company_profile(self, symbol: str) -> CompanyProfile:
        pass