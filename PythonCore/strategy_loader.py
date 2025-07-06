# PythonCore/strategy_loader.py

import json
import pandas as pd
from backtester import backtest_strategy

RESULTS_FILE = "Reports/all_results.csv"
STRATEGY_FILE = "strategies.json"
DATA_FILE = "Data/prepared_m1.csv"  # Updated to use prepared M1 data

def load_data():
    df = pd.read_csv(DATA_FILE)
    df.rename(columns=lambda x: x.strip(), inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])  # Changed from 'Time' to 'Date'
    df.set_index('Date', inplace=True)
    return df

def run_batch_backtest():
    with open(STRATEGY_FILE, "r") as f:
        strategies = json.load(f)

    data = load_data()
    results = []

    for strategy in strategies:
        result = backtest_strategy(data.copy(), strategy)
        results.append(result)

    df_results = pd.DataFrame(results)
    df_results.to_csv(RESULTS_FILE, index=False)
    print(f"✅ Backtest completed for {len(results)} strategies. Results saved to {RESULTS_FILE}")

if __name__ == "__main__":
    run_batch_backtest()
