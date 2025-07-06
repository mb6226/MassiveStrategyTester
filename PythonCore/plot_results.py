# PythonCore/plot_results.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

RESULTS_FILE = "Reports/all_results.csv"
OUTPUT_DIR = "Reports/"

def plot_profit_distribution(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df['profit'], bins=30, kde=True, color='skyblue')
    plt.title("Profit Distribution of Strategies")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.savefig(f"{OUTPUT_DIR}profit_distribution.png")
    plt.close()

def plot_profit_vs_drawdown(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="drawdown", y="profit", size="winrate", hue="winrate", data=df, palette="coolwarm", legend=False)
    plt.title("Profit vs Drawdown")
    plt.xlabel("Max Drawdown (%)")
    plt.ylabel("Total Profit")
    plt.savefig(f"{OUTPUT_DIR}profit_vs_drawdown.png")
    plt.close()

def plot_top_strategies(df, top_n=10):
    top_df = df.sort_values(by="profit", ascending=False).head(top_n)
    plt.figure(figsize=(10, 5))
    sns.barplot(x="profit", y="strategy_name", data=top_df, palette="viridis")
    plt.title(f"Top {top_n} Profitable Strategies")
    plt.xlabel("Profit")
    plt.ylabel("Strategy Name")
    plt.savefig(f"{OUTPUT_DIR}top_{top_n}_strategies.png")
    plt.close()

def main():
    df = pd.read_csv(RESULTS_FILE)
    plot_profit_distribution(df)
    plot_profit_vs_drawdown(df)
    plot_top_strategies(df)
    print("Charts saved to Reports/ folder.")

if __name__ == "__main__":
    main()
