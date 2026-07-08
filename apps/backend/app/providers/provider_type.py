from enum import Enum


class ProviderType(str, Enum):
    YAHOO = "yahoo"
    ALPHA_VANTAGE = "alpha_vantage"
    FINNHUB = "finnhub"
    POLYGON = "polygon"