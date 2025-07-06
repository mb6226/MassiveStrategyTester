import pandas as pd
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os

PARETO_FILE = "Reports/pareto_strategies.csv"
OPTIMIZED_FILE = "Reports/optimized_strategies.csv"
OUTPUT_FILE = "Reports/final_report.html"
TEMPLATE_DIR = "Templates"

def load_data():
    pareto_df = pd.read_csv(PARETO_FILE) if os.path.exists(PARETO_FILE) else None
    opt_df = pd.read_csv(OPTIMIZED_FILE) if os.path.exists(OPTIMIZED_FILE) else None
    return pareto_df, opt_df

def generate_report(pareto_df, opt_df):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report_template.html")

    rendered = template.render(
        title="Strategy Evaluation Report",
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        pareto_data=pareto_df.to_dict(orient="records") if pareto_df is not None else [],
        optimized_data=opt_df.to_dict(orient="records") if opt_df is not None else [],
        image_paths=[
            "Reports/profit_distribution.png",
            "Reports/profit_vs_drawdown.png",
            "Reports/top_10_strategies.png"
        ]
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"Final report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    pareto_df, opt_df = load_data()
    generate_report(pareto_df, opt_df)
