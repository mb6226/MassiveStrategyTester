import pandas as pd

def load_tick_data(file_path):
    """
    Load raw tick data from a CSV file without header.
    The expected columns are:
    datetime, bid, ask, last, volume, flags
    """
    try:
        df = pd.read_csv(
            file_path,
            names=['datetime', 'bid', 'ask', 'last', 'volume', 'flags'],
            parse_dates=['datetime'],
            infer_datetime_format=True
        )
        print(f"✅ Loaded {len(df)} ticks from file: {file_path}")
        return df
    except Exception as e:
        print(f"❌ Error loading tick data: {e}")
        return None

def resample_to_m1(df):
    """
    Resample tick data into 1-minute OHLCV candles based on 'bid' price.
    
    Parameters:
    - df: DataFrame with tick data indexed by datetime
    
    Returns:
    - DataFrame with columns: Date, Open, High, Low, Close, Volume
    """
    # Set datetime as index
    df = df.set_index('datetime')
    
    # Create OHLC for bid price
    ohlc = df['bid'].resample('1T').ohlc()
    
    # Sum volume over each minute
    volume = df['volume'].resample('1T').sum()
    
    # Combine OHLC and volume
    ohlc['volume'] = volume
    
    # Drop intervals with no data
    ohlc = ohlc.dropna()
    
    print(f"📊 Resampled tick data into {len(ohlc)} 1-minute candles.")
    return ohlc.reset_index()

def save_candles(df, output_path):
    """
    Save the resampled OHLCV data to CSV with standard column names.
    """
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df.to_csv(output_path, index=False)
    print(f"💾 Saved prepared data to: {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert MT5 tick data CSV to 1-minute OHLCV candles.")
    parser.add_argument('--input', type=str, default='Data/EURUSD_mt5_ticks.csv', help='Path to input tick CSV file')
    parser.add_argument('--output', type=str, default='Data/prepared_m1.csv', help='Path to output 1-minute CSV file')
    args = parser.parse_args()
    
    tick_df = load_tick_data(args.input)
    if tick_df is not None:
        m1_df = resample_to_m1(tick_df)
        save_candles(m1_df, args.output)
