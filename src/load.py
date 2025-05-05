import sqlite3


def load_to_sqlite(df, db_name="stock_data.db", table_name="stocks"):
    """
    Load a DataFrame into a local SQLite database.

    Args:
        df (pd.DataFrame): Transformed DataFrame
        db_name (str): Name of SQLite database file
        table_name (str): Table name to write to
    """
    try:
        # Connect to SQLite database (or create if it doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Write DataFrame to SQL table (replace if already exists)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        print(f"✅ Data loaded into {db_name} -> table: {table_name}")

        # Optional: show number of rows
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        print("📊 Rows in table:", cursor.fetchone()[0])

        conn.commit()
        conn.close()

    except Exception as e:
        print("❌ Error loading to SQLite:", e)
