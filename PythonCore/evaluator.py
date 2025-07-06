# PythonCore/evaluator.py

import pandas as pd

def evaluate_results(results_file, profit_thresh=100, max_drawdown=25):
    df = pd.read_csv(results_file)
    filtered = df[
        (df['profit'] >= profit_thresh) &
        (df['drawdown'] <= max_drawdown)
    ]
    ranked = filtered.sort_values(by='profit', ascending=False)
    ranked.to_csv("filtered_results.csv", index=False)
    print(f"{len(ranked)} strategies selected and saved to filtered_results.csv")

if __name__ == "__main__":
    evaluate_results("all_results.csv")
