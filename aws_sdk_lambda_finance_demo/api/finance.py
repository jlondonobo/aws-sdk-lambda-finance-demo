import datetime
import random


def call_api():
    # Fixed set of three tickers
    tickers = ["AAPL", "MSFT", "TSLA"]

    # Generate data for each ticker
    data_collection = []
    for ticker in tickers:
        data = {
            "date": datetime.date.today().isoformat(),
            "ticker": ticker,
            "stock_price": round(random.uniform(100, 500), 2),
            "trading_volume": random.randint(1000, 10000),
        }
        data_collection.append(data)
    return data_collection