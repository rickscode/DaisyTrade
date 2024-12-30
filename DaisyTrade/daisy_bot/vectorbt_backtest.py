# main.py

from data_fetch import fetch_historical_data
from data_processing import process_data
from indicators import add_indicators
from strategy import simple_strategy

def run_bot():
    # 1. Fetch raw data
    raw_data = fetch_historical_data()
    if not raw_data:
        print("No data fetched. Check your API config or internet connection.")
        return

    # 2. Process into a DataFrame
    df = process_data(raw_data)
    print(f"Number of rows fetched: {len(df)}")
    if df.empty:
        print("DataFrame is empty. Exiting.")
        return

    # Debug print sample
    print("Data sample:\n", df.head())

    # 3. Add indicators (e.g., RSI)
    df = add_indicators(df)
    print("\nLast 5 rows with RSI:\n", df[['close', 'RSI']].tail())

    # 4. Run the strategy
    trades = simple_strategy(df, profit_target=0.005)  # 0.5% target
    print("\nTrade Signals:")
    for trade in trades:
        print(trade)

if __name__ == "__main__":
    run_bot()
