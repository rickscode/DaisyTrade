# config.py
import os

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

# Default fallback if needed
SYMBOL = "BTCUSDT"
INTERVAL = "1m"
LOOKBACK = "1 day ago UTC"
