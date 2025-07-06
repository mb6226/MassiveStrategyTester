import pandas as pd

def load_tick_data(file_path):
    """
    Load raw tick data (without header) in MetaTrader 5 tick format.

    Columns: [DateTime, Bid, Ask, Last, Volume, Flags]
    """
    df = pd.read_csv(
        file_path,
        names=['datetime', 'bid', 'ask', 'last', 'volume', 'flags'],
        parse_dates=['datetime'],
        infer_datetime_format=True
    )
    print(f"✅ Loaded {len(df)} ticks from file.")
    return df


def resample_to_m1(df):
    """
    Resample tick data into 1-minute candles using the 'bid' price.

    Returns OHLCV: Open, High, Low, Close, Volume
    """
    df.set_index('datetime', inplace=True)

    ohlcv = df['bid'].resample('1T').ohlc()
    ohlcv['volume'] = df['volume'].resample('1T').sum()

    # Drop empty candles
    ohlcv.dropna(inplace=True)

    print(f"📊 Resampled to {len(ohlcv)} M1 candles.")
    return ohlcv.reset_index()


def save_candles(df, output_path):
    """
    Save M1 candles as CSV with standard structure.
    """
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df.to_csv(output_path, index=False)
    print(f"💾 Saved M1 candles to: {output_path}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Prepare M1 candles from MT5 Tickstory CSV.")
    parser.add_argument('--input', type=str, default='Data/tickdata.csv', help='Path to raw tick CSV')
    parser.add_argument('--output', type=str, default='Data/prepared_m1.csv', help='Path to save resampled M1 CSV')
    args = parser.parse_args()

    df_tick = load_tick_data(args.input)
    df_m1 = resample_to_m1(df_tick)
    save_candles(df_m1, args.output)
