# PythonCore/result_parser.py

import os
import pandas as pd
from bs4 import BeautifulSoup

RESULTS_DIR = "Backtests/results"
OUTPUT_CSV = "Data/parsed_results.csv"


def extract_metrics_from_html(html_path):
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        tables = soup.find_all("table")
        summary_table = tables[0] if tables else None

        if summary_table is None:
            return None

        metrics = {
            "filename": os.path.basename(html_path)
        }

        for row in summary_table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) == 2:
                key = cols[0].get_text(strip=True).replace(":", "")
                value = cols[1].get_text(strip=True).replace("\xa0", " ")
                metrics[key] = value

        return metrics

    except Exception as e:
        print(f"❌ Failed to parse {html_path}: {e}")
        return None


def parse_all_results(results_dir):
    all_metrics = []
    for file in os.listdir(results_dir):
        if file.endswith(".html"):
            full_path = os.path.join(results_dir, file)
            metrics = extract_metrics_from_html(full_path)
            if metrics:
                all_metrics.append(metrics)

    return pd.DataFrame(all_metrics)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    df = parse_all_results(RESULTS_DIR)
    if not df.empty:
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"✅ Parsed {len(df)} result files.")
        print(f"💾 Saved summary to: {OUTPUT_CSV}")
    else:
        print("⚠️ No valid result files found.")
