# strategy.py

def simple_strategy(df, profit_target=0.005):
    """
    Basic example strategy:
    - Buy when RSI < 30 (oversold).
    - Sell when price goes up by 0.5% (default) from buy price.
    """
    position = False
    buy_price = 0.0
    trades = []

    # We iterate through each row in the DataFrame
    for i in range(1, len(df)):
        rsi_value = df['RSI'].iloc[i]
        current_price = df['close'].iloc[i]
        timestamp = df.index[i]

        # Entry condition: RSI < 30, not already in a position
        if not position and rsi_value < 30:
            buy_price = current_price
            position = True
            trades.append(f"[{timestamp}] BUY at {buy_price:.2f}")

        # Exit condition: Price has increased by the profit_target (0.5%)
        if position and current_price >= (buy_price * (1 + profit_target)):
            sell_price = current_price
            position = False
            trade_profit = sell_price - buy_price
            trades.append(
                f"[{timestamp}] SELL at {sell_price:.2f}, Profit: {trade_profit:.2f}"
            )

    return trades
