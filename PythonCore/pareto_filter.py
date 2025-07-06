import pandas as pd

INPUT_FILE = "Reports/all_results.csv"
OUTPUT_FILE = "Reports/pareto_strategies.csv"

def is_pareto_efficient(df, metrics):
    is_efficient = [True] * len(df)
    for i, row_i in df.iterrows():
        for j, row_j in df.iterrows():
            if i != j:
                # شرط: سود بیشتر، دراودان کمتر (winrate اختیاری)
                better_or_equal = all(row_j[metric] >= row_i[metric] if metric == "profit" or metric == "winrate"
                                      else row_j[metric] <= row_i[metric] for metric in metrics)
                strictly_better = any(row_j[metric] > row_i[metric] if metric == "profit" or metric == "winrate"
                                      else row_j[metric] < row_i[metric] for metric in metrics)
                if better_or_equal and strictly_better:
                    is_efficient[i] = False
                    break
    return is_efficient

def main():
    df = pd.read_csv(INPUT_FILE)
    metrics = ["profit", "drawdown", "winrate"]
    efficient_mask = is_pareto_efficient(df, metrics)
    pareto_df = df[efficient_mask].copy()
    pareto_df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ {len(pareto_df)} Pareto-optimal strategies saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
