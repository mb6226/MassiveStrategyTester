# PythonCore/optimizer.py

import pandas as pd

INPUT_FILE = "Reports/all_results.csv"
OUTPUT_FILE = "Reports/optimized_strategies.csv"

# وزن‌دهی معیارها (قابل تنظیم توسط کاربر)
WEIGHTS = {
    "profit": 0.5,
    "drawdown": 0.3,
    "winrate": 0.2
}

# حداقل فیلتر
THRESHOLDS = {
    "profit": 100,
    "drawdown": 30,
    "winrate": 40
}

def normalize(series):
    return (series - series.min()) / (series.max() - series.min() + 1e-6)

def rank_strategies(df):
    df = df.copy()

    # اعمال فیلتر اولیه
    df = df[
        (df["profit"] >= THRESHOLDS["profit"]) &
        (df["drawdown"] <= THRESHOLDS["drawdown"]) &
        (df["winrate"] >= THRESHOLDS["winrate"])
    ]

    if df.empty:
        print("⚠️ No strategy passed the initial thresholds.")
        return df

    # نرمال‌سازی
    df["norm_profit"] = normalize(df["profit"])
    df["norm_drawdown"] = 1 - normalize(df["drawdown"])  # کمتر بهتره
    df["norm_winrate"] = normalize(df["winrate"])

    # امتیاز نهایی
    df["score"] = (
        WEIGHTS["profit"] * df["norm_profit"] +
        WEIGHTS["drawdown"] * df["norm_drawdown"] +
        WEIGHTS["winrate"] * df["norm_winrate"]
    )

    df = df.sort_values(by="score", ascending=False)
    return df

def main():
    df = pd.read_csv(INPUT_FILE)
    ranked_df = rank_strategies(df)

    if not ranked_df.empty:
        ranked_df.to_csv(OUTPUT_FILE, index=False)
        print(f"✅ {len(ranked_df)} strategies saved to {OUTPUT_FILE}")
    else:
        print("❌ No strategies saved.")

if __name__ == "__main__":
    main()
