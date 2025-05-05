import yfinance as yf
import pandas as pd

def extract_stock_data(ticker="AAPL", period="1y", interval="1d"):
    """
    Extract historical stock data from Yahoo Finance.
    Args:
        ticker (str): Stock ticker symbol (e.g. 'AAPL', 'TSLA')
        period (str): Time span (e.g. '1y', '6mo', '5d')
        interval (str): Data granularity (e.g. '1d', '1wk', '1mo')
    Returns:
        pd.DataFrame: Stock price history
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    df["ticker"] = ticker
    return df
