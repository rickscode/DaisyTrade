# data_processing.py

import pandas as pd

def process_data(raw_data):
    """
    Takes a list of kline data from Binance and returns a pandas DataFrame
    with nicely formatted columns and proper index.
    """
    df = pd.DataFrame(raw_data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume',
        'number_of_trades', 'taker_buy_base',
        'taker_buy_quote', 'ignore'
    ])

    # Convert timestamp to datetime and set as index
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    # Convert numeric columns from strings to floats
    float_cols = ['open', 'high', 'low', 'close', 'volume',
                  'quote_asset_volume', 'taker_buy_base', 'taker_buy_quote']
    df[float_cols] = df[float_cols].astype(float)

    # We’ll keep only essential columns for now
    df = df[['open', 'high', 'low', 'close', 'volume']]
    return df
