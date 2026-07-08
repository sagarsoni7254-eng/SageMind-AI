from app.providers.provider_type import ProviderType
from app.providers.yahoo_provider import YahooFinanceProvider


class ProviderFactory:

    @staticmethod
    def create(provider: ProviderType):

        if provider == ProviderType.YAHOO:
            return YahooFinanceProvider()

        raise ValueError(f"Unsupported provider: {provider}")