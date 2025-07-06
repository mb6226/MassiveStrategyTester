import pandas as pd

def load_raw_data(file_path):
    """
    Load raw CSV data file (candle format).

    Parameters:
        file_path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Raw data loaded: {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Clean data by removing incomplete rows and fixing data types.

    Parameters:
        df (pd.DataFrame): Raw dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    # Drop rows with missing values
    df_clean = df.dropna()
    
    # Convert date/time columns to datetime objects
    for col in ['Date', 'Time']:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
    
    # Remove rows with invalid dates
    if 'Date' in df_clean.columns:
        df_clean = df_clean.dropna(subset=['Date'])
    
    print(f"Cleaned data: {len(df_clean)} rows after dropping missing/invalid dates")
    return df_clean

def standardize_data(df):
    """
    Standardize data format for pipeline compatibility.

    Parameters:
        df (pd.DataFrame): Cleaned dataframe.

    Returns:
        pd.DataFrame: Standardized dataframe.
    """
    # Define required columns
    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    
    # Check and warn if columns missing
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        print(f"Warning: Missing columns in data: {missing_cols}")
    
    # Keep only required columns if they exist
    df_std = df[[col for col in required_columns if col in df.columns]]
    
    # Sort by Date ascending
    df_std = df_std.sort_values(by='Date')
    
    print(f"Standardized data ready: {len(df_std)} rows")
    return df_std

def save_prepared_data(df, output_path):
    """
    Save prepared data to CSV.

    Parameters:
        df (pd.DataFrame): Standardized dataframe.
        output_path (str): Path to save CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Prepared data saved to: {output_path}")

def load_tick_data(file_path):
    """
    Load tick data where date and time are in two separate columns.
    Expected format:
        Column 0: YYYYMMDD
        Column 1: HH:MM:SS
        Column 2-5: bid, ask, last, volume
    """
    try:
        df = pd.read_csv(
            file_path,
            header=None,
            names=['date', 'time', 'bid', 'ask', 'last', 'volume']
        )

        # Combine date + time into single datetime string
        df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'], format='%Y%m%d %H:%M:%S')

        # Convert prices/volume to numeric
        df[['bid', 'ask', 'last', 'volume']] = df[['bid', 'ask', 'last', 'volume']].apply(pd.to_numeric, errors='coerce')

        print(f"✅ Loaded {len(df)} ticks from file: {file_path}")
        return df[['datetime', 'bid', 'ask', 'last', 'volume']]
    except Exception as e:
        print(f"❌ Error loading tick data: {e}")
        return None

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Prepare raw market data CSV for strategy testing pipeline.")
    parser.add_argument('--input', type=str, default='Data/raw_data.csv', help='Path to raw input CSV file')
    parser.add_argument('--output', type=str, default='Data/prepared_data.csv', help='Path to save prepared CSV file')
    parser.add_argument('--mode', type=str, choices=['candle', 'tick'], default='candle',
                        help='Mode of data preparation: "candle" for OHLC, "tick" for tick data')
    args = parser.parse_args()

    if args.mode == 'candle':
        df_raw = load_raw_data(args.input)
        if df_raw is not None:
            df_clean = clean_data(df_raw)
            df_std = standardize_data(df_clean)
            save_prepared_data(df_std, args.output)

    elif args.mode == 'tick':
        df_tick = load_tick_data(args.input)
        if df_tick is not None:
            # Resample to 1-minute OHLCV using bid price
            df_tick = df_tick.set_index('datetime')
            ohlc = df_tick['bid'].resample('1min').ohlc()
            ohlc['volume'] = df_tick['volume'].resample('1min').sum()
            ohlc.dropna(inplace=True)
            ohlc.reset_index(inplace=True)
            ohlc.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
            save_prepared_data(ohlc, args.output)
