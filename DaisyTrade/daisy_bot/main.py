# main.py

import pandas as pd
from data_fetch import fetch_historical_data
from data_processing import process_data
from indicators import add_indicators
from strategy import simple_strategy


def run_bot():
    # 1. Fetch historical data
    raw_data = fetch_historical_data()

    # 2. Convert to DataFrame
    df = process_data(raw_data)

    # 3. Add indicators
    df = add_indicators(df)

    # 4. Run strategy
    trades = simple_strategy(df, profit_target=0.005)  # 0.5% target

    # 5. Print results
    for trade in trades:
        print(trade)


if __name__ == "__main__":
    run_bot()
