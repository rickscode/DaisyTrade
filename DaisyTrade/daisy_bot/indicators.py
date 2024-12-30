# indicators.py

import talib as ta

def add_indicators(df):
    """
    Adds desired technical indicators to the DataFrame in-place.
    Example: RSI
    """
    df['RSI'] = ta.RSI(df['close'], timeperiod=14)
    return df
