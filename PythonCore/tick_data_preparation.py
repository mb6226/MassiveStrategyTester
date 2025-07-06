import pandas as pd

def load_tick_data(file_path):
    """
    Load raw tick data from a CSV file without header.
    Expected datetime format: '2025.07.01 23:59:55.000'
    """
    try:
        date_parser = lambda x: pd.to_datetime(x, format='%Y.%m.%d %H:%M:%S.%f')
        df = pd.read_csv(
            file_path,
            names=['datetime', 'bid', 'ask', 'last', 'volume', 'flags'],
            parse_dates=['datetime'],
            date_parser=date_parser
        )
        df[['bid', 'ask', 'last', 'volume']] = df[['bid', 'ask', 'last', 'volume']].apply(pd.to_numeric, errors='coerce')
        print(f"✅ Loaded {len(df)} ticks from file: {file_path}")
        return df
    except Exception as e:
        print(f"❌ Error loading tick data: {e}")
        return None

def resample_to_m1(df):
    """
    Resample tick data into 1-minute OHLCV candles using 'bid' price.
    """
    df = df.set_index('datetime')
    ohlc = df['bid'].resample('1min').ohlc()
    ohlc['volume'] = df['volume'].resample('1min').sum()
    ohlc.dropna(inplace=True)
    print(f"📊 Resampled to {len(ohlc)} M1 candles.")
    return ohlc.reset_index()

def save_candles(df, output_path):
    """
    Save the resampled OHLCV data to CSV.
    """
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df.to_csv(output_path, index=False)
    print(f"💾 Saved to: {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='Data/EURUSD_mt5_ticks.csv')
    parser.add_argument('--output', type=str, default='Data/prepared_m1.csv')
    args = parser.parse_args()

    df_tick = load_tick_data(args.input)
    if df_tick is not None:
        df_m1 = resample_to_m1(df_tick)
        save_candles(df_m1, args.output)
