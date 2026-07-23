"""
fetch_stock_data.py

Fetches historical stock data using yfinance, calculates technical
indicators (7-day Moving Average, Daily Return %), and inserts the
data into a MySQL table (stock_prices).

Supports multiple tickers — each row is tagged with its ticker symbol,
so RELIANCE.NS, TCS.NS, etc. can all live in the same table.
"""

import getpass
import pandas as pd
import yfinance as yf
import mysql.connector

# ---- Config: Add/remove tickers here ----
TICKERS = ["RELIANCE.NS", "TCS.NS"]
PERIOD = "3mo"  # how much historical data to pull


def fetch_and_prepare(ticker_symbol: str) -> pd.DataFrame:
    """Fetch price history and compute MA7 + Daily Return % for a ticker."""
    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period=PERIOD)

    data["MA7"] = data["Close"].rolling(window=7).mean()
    data["Daily_Return"] = data["Close"].pct_change() * 100

    return data


def insert_into_mysql(ticker_symbol: str, data: pd.DataFrame, cursor) -> int:
    """Insert all rows for one ticker into stock_prices. Returns row count."""
    rows_inserted = 0

    for date, row in data.iterrows():
        ma7 = None if pd.isna(row["MA7"]) else row["MA7"]
        daily_return = None if pd.isna(row["Daily_Return"]) else row["Daily_Return"]

        sql = """
        INSERT INTO stock_prices
            (ticker, date, open_price, high_price, low_price, close_price, volume, ma7, daily_return)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            ticker_symbol,
            date.date(),
            row["Open"],
            row["High"],
            row["Low"],
            row["Close"],
            row["Volume"],
            ma7,
            daily_return,
        )
        cursor.execute(sql, values)
        rows_inserted += 1

    return rows_inserted


def main():
    # ---- Connect to MySQL (password entered securely, never hard-coded) ----
    db_password = getpass.getpass("Enter MySQL password: ")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=db_password,
        database="stock_analytics",
    )
    cursor = connection.cursor()

    for ticker_symbol in TICKERS:
        print(f"Fetching data for {ticker_symbol}...")
        data = fetch_and_prepare(ticker_symbol)

        rows_inserted = insert_into_mysql(ticker_symbol, data, cursor)
        connection.commit()

        print(f"{ticker_symbol}: {rows_inserted} rows inserted into MySQL.")

    cursor.close()
    connection.close()
    print("Done — all tickers processed.")


if __name__ == "__main__":
    main()
