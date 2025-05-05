from src.extract import extract_stock_data

# Extract data for Apple (AAPL)
df = extract_stock_data(ticker="AAPL", period="6mo", interval="1d")
print(df.head())

from src.transform import transform_stock_data

# Transform the data
df_transformed = transform_stock_data(df)
print(df_transformed.head())


from src.load import load_to_sqlite

# Load to SQLite
load_to_sqlite(df_transformed)


#visualisation
import matplotlib.pyplot as plt

# Line plot of closing price and moving average
plt.figure(figsize=(12, 6))
plt.plot(df_transformed['Date'], df_transformed['Close'], label='Close Price')
plt.plot(df_transformed['Date'], df_transformed['ma_7'], label='7-Day MA')
plt.title('Stock Price vs Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("images/stock_plot.png", bbox_inches="tight")


