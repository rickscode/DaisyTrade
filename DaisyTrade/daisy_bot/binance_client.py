# binance_client.py

from binance.client import Client
import config

def get_binance_client():
    """
    Returns a Binance client instance.
    """
    client = Client(config.BINANCE_API_KEY, config.BINANCE_API_SECRET)
    return client
