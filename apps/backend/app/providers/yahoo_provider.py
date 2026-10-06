import yfinance as yf

from app.providers.base_provider import BaseProvider
from app.schemas.company_profile import CompanyProfile
from app.schemas.stock_search_result import StockSearchResult
from app.schemas.historical_price import HistoricalPrice


class YahooFinanceProvider(BaseProvider):
    """
    Yahoo Finance implementation of the Market Data Provider.
    """

    def search_company(self, query: str) -> list[StockSearchResult]:
        """
        Search companies using Yahoo Finance.
        """

        try:
            search = yf.Search(query)

            quotes = search.quotes

            results = []

            for item in quotes:

                symbol = item.get("symbol")
                company_name = item.get("shortname") or item.get("longname")
                exchange = item.get("exchange", "Unknown")

                if symbol and company_name:
                    results.append(
                        StockSearchResult(
                            symbol=symbol,
                            company_name=company_name,
                            exchange=exchange,
                        )
                    )

            return results

        except Exception as e:
            print(f"Yahoo Finance Search Error: {e}")
            return []

    def get_company_profile(self, symbol: str) -> CompanyProfile:
        """
        Fetch a live company profile from Yahoo Finance.
        """

        try:
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

        except Exception as e:
            print(f"Yahoo Finance Profile Error: {e}")

            return CompanyProfile(
                symbol=symbol.upper(),
                company_name="Unknown",
                exchange="Unknown",
                sector="Unknown",
                industry="Unknown",
                market_cap=None,
                currency="Unknown",
                country="Unknown",
            )

    def get_historical_prices(
                self,
                symbol: str,
                period: str = "1mo",
        ) -> list[HistoricalPrice]:
            """
            Fetch historical stock prices from Yahoo Finance.
            """

            try:
                ticker = yf.Ticker(symbol)

                history = ticker.history(period=period)

                results = []

                for index, row in history.iterrows():
                    results.append(
                        HistoricalPrice(
                            date=index.date(),
                            open=float(row["Open"]),
                            high=float(row["High"]),
                            low=float(row["Low"]),
                            close=float(row["Close"]),
                            volume=int(row["Volume"]),
                        )
                    )

                return results

            except Exception as e:
                print(f"Yahoo Finance Historical Data Error: {e}")
                return []