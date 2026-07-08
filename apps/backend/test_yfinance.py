import yfinance as yf

ticker = yf.Ticker("NVDA")

info = ticker.info

print("=" * 50)
print("Company Name :", info.get("longName"))
print("Sector       :", info.get("sector"))
print("Industry     :", info.get("industry"))
print("Country      :", info.get("country"))
print("Currency     :", info.get("currency"))
print("Exchange     :", info.get("exchange"))
print("Market Cap   :", info.get("marketCap"))
print("Current Price:", info.get("currentPrice"))
print("=" * 50)