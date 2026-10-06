from abc import ABC, abstractmethod

from app.schemas.company_profile import CompanyProfile
from app.schemas.stock_search_result import StockSearchResult


class BaseProvider(ABC):

    @abstractmethod
    def get_company_profile(self, symbol: str) -> CompanyProfile:
        """
        Return detailed company profile.
        """
        pass

    @abstractmethod
    def search_company(self, query: str) -> list[StockSearchResult]:
        """
        Search companies by name.
        """
        pass