# data_fetch.py

from binance.client import Client
from binance_client import get_binance_client
import config

def fetch_historical_data(symbol=None, interval=None, lookback=None):
    """
    Fetches historical kline (candlestick) data from Binance.
    Returns a list of lists.
    """
    if symbol is None:
        symbol = config.SYMBOL
    if interval is None:
        interval = config.INTERVAL
    if lookback is None:
        lookback = config.LOOKBACK

    client = get_binance_client()
    data = client.get_historical_klines(symbol, interval, lookback)
    return data
