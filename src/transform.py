import pandas as pd


def transform_stock_data(df):
    """
    Cleans and enriches stock price data with new metrics.

    Args:
        df (pd.DataFrame): Raw stock data from yfinance

    Returns:
        pd.DataFrame: Transformed data with extra features
    """
    df = df.copy()

    # Ensure Date column is datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    # Calculate daily percent change
    df['daily_return_%'] = df['Close'].pct_change() * 100

    # 7-day moving average of closing price
    df['ma_7'] = df['Close'].rolling(window=7).mean()

    # Format volume (optional, e.g. in millions)
    df['volume_million'] = df['Volume'] / 1_000_000

    # Drop rows with NaN (from rolling window)
    df.dropna(inplace=True)

    return df
