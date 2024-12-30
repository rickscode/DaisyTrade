import pandas as pd
import vectorbt as vbt

def run_vectorbt_backtest(csv_path="data/BTCUSDT_1m.csv"):
    """
    Loads OHLCV data from CSV and performs a simple vectorbt backtest.
    """
    # 1. Load data
    df = pd.read_csv(csv_path, parse_dates=["timestamp"], index_col="timestamp")
    price = df['close']

    # 2. Create simple entry/exit signals
    entries = price > price.shift(1)  # Buy when today's close > yesterday's close
    exits = price < price.shift(1)    # Sell when today's close < yesterday's close

    # 3. Build portfolio
    pf = vbt.Portfolio.from_signals(
        close=price,
        entries=entries,
        exits=exits,
        init_cash=10000.0,  # starting capital
        fees=0.001,         # 0.1% fees
        slippage=0.001,     # 0.1% slippage
        freq='1T'           # 1-minute data
    )

    # 4. Print stats
    print(pf.stats())

    # 5. Plot
    pf.plot().show()

if __name__ == "__main__":
    run_vectorbt_backtest()
