# PythonCore/backtester.py

import pandas as pd

def backtest_strategy(data, strategy):
    ema = data['Close'].ewm(span=strategy['ema_period']).mean()
    rsi = compute_rsi(data['Close'], strategy['rsi_period'])
    atr = compute_atr(data, strategy['atr_period'])

    position = None
    entry_price = 0
    profit = 0
    trades = 0
    stop_loss = strategy['stop_loss']
    take_profit = strategy['take_profit']

    for i in range(len(data)):
        if i < max(strategy['ema_period'], strategy['rsi_period'], strategy['atr_period']):
            continue

        if position is None:
            if ema[i] > data['Close'][i-1] and rsi[i] < 30:
                position = 'long'
                entry_price = data['Close'][i]
                trades += 1
            elif ema[i] < data['Close'][i-1] and rsi[i] > 70:
                position = 'short'
                entry_price = data['Close'][i]
                trades += 1
        else:
            current_price = data['Close'][i]
            if position == 'long':
                if current_price >= entry_price + take_profit:
                    profit += take_profit
                    position = None
                elif current_price <= entry_price - stop_loss:
                    profit -= stop_loss
                    position = None
            elif position == 'short':
                if current_price <= entry_price - take_profit:
                    profit += take_profit
                    position = None
                elif current_price >= entry_price + stop_loss:
                    profit -= stop_loss
                    position = None

    return {"strategy_name": strategy["name"], "profit": profit, "trades": trades}

def compute_rsi(series, period):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def compute_atr(df, period):
    high_low = df['High'] - df['Low']
    high_close = (df['High'] - df['Close'].shift()).abs()
    low_close = (df['Low'] - df['Close'].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(period).mean()
    return atr
