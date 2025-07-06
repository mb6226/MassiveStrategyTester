# 01_data_preparation.md

# Data Preparation

## Objective
Prepare raw tick or candle data to standardized OHLCV CSV format for backtesting pipeline.

## Steps
1. Inspect raw data file format (columns, date/time format)
2. Load raw data with pandas:
   - For candle data: read CSV with headers
   - For tick data: load date/time columns separately, combine and parse datetime
3. Clean data:
   - Remove rows with missing values
   - Convert date/time columns to datetime objects
4. Resample tick data to 1-minute OHLCV candles (using bid prices)
5. Save prepared data CSV for pipeline input

## Commands to run

```bash
python PythonCore/data_preparation.py --mode tick --input Data/EURUSD_mt5_ticks.csv --output Data/prepared_m1.csv
or for candle data

bash
Copy
Edit
python PythonCore/data_preparation.py --mode candle --input Data/raw_data.csv --output Data/prepared_data.csv
Output
File saved: Data/prepared_m1.csv (tick mode) or Data/prepared_data.csv (candle mode)

Format: CSV with columns: Date, Open, High, Low, Close, Volume

Notes
Input tick data expected format: no header, columns:
YYYYMMDD, HH:MM:SS, bid, ask, last, volume

Uses pandas resampling for aggregation to 1-minute bars

Cleaning removes rows with missing or invalid dates

