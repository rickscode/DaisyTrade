import pandas as pd
import vectorbt as vbt

def run_vectorbt_backtest(csv_path="data/BTCUSDT_1m.csv"):
    """
    Runs a breakout strategy backtest using vectorbt.
    """
    # 1. Load data
    df = pd.read_csv(csv_path, parse_dates=["timestamp"], index_col="timestamp")
    price = df['close']

    # 2. Breakout strategy logic
    lookback = 20  # Lookback period for the breakout
    range_high = price.rolling(lookback).max().shift(1)  # Highest high in the last 'lookback' periods
    range_low = price.rolling(lookback).min().shift(1)   # Lowest low in the last 'lookback' periods

    entries = price > range_high  # Buy when price breaks above the range
    exits = price < range_low     # Sell when price drops below the range

    # 3. Build portfolio
    pf = vbt.Portfolio.from_signals(
        close=price,
        entries=entries,
        exits=exits,
        init_cash=10000.0,  # Starting capital
        fees=0.001,         # 0.1% fees
        slippage=0.001,     # 0.1% slippage
        freq='1min'         # Fixed warning by using '1min' instead of '1T'
    )

    # 4. Print stats
    print(pf.stats())

    # 5. Plot results
    pf.plot().show()

if __name__ == "__main__":
    run_vectorbt_backtest()
