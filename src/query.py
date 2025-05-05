import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect("stock_data.db")

# Fixed SQL query — wraps column with % using double quotes
query = """
SELECT 
    Date, 
    Close, 
    "daily_return_%" AS daily_return, 
    ma_7 
FROM stocks 
ORDER BY Date DESC 
LIMIT 5;
"""

# Run the query and store the result
try:
    df_query = pd.read_sql(query, conn)
    print(df_query)
except Exception as e:
    print("❌ Error running query:", e)

# Close the connection
conn.close()
