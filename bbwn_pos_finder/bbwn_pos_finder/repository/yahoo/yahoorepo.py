import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta


class YahooRepo:
    def get_data(self, symbol, interval):
        start_date_str = (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")
        end_date_str = datetime.now().strftime("%Y-%m-%d")
        data = yf.download(tickers=symbol, interval=interval, start=start_date_str, end=end_date_str, auto_adjust=True, progress=False)['Close']
        return data.values.tolist()

    def list_pairs(self):
        tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
        return tickers["Symbol"].values.tolist()
