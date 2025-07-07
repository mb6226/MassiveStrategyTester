import pandas as pd
import argparse
import os

def filter_strategies(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"❌ Input file does not exist: {input_file}")
        return

    df = pd.read_csv(input_file)

    # ✅ Filtering criteria (customize as needed)
    filtered = df[
        (df['Profit'] > 0) &
        (df['MaxDrawdown(%)'] < 30) &
        (df['TotalTrades'] >= 10)
    ]

    if filtered.empty:
        print("⚠️ No strategies passed the filter criteria.")
    else:
        print(f"✅ {len(filtered)} strategies passed the filter criteria.")

    filtered.to_csv(output_file, index=False)
    print(f"📄 Filtered strategies saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter Pareto-optimal strategies")
    parser.add_argument("--input_file", type=str, required=True, help="Path to summary.csv")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save filtered strategies")

    args = parser.parse_args()

    filter_strategies(args.input_file, args.output_file)
