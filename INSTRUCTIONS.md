INSTRUCTIONS for MassiveStrategyTester

Welcome to the Massive Strategy Tester project! This document will guide you step-by-step through setup, usage, and troubleshooting.

---

1. Prerequisites

- Python 3.8 or higher installed
- Git installed
- Internet connection for downloading dependencies

---

2. Clone the repository

Open your terminal or command prompt and run:

```sh
git clone https://github.com/yourusername/MassiveStrategyTester.git
cd MassiveStrategyTester
```

---

3. Install dependencies

Install required Python packages:

```sh
pip install -r requirements.txt
```

---

4. Directory structure overview

```
MassiveStrategyTester/
├── PythonCore/            # Python scripts for strategy generation, backtesting, ML, and reporting
├── Reports/               # Output reports (HTML, PDF, charts)
├── .github/workflows/     # GitHub Actions automation config
├── Templates/             # HTML report templates
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── INSTRUCTIONS.md        # This document
```

---

5. Running the full pipeline

Run the entire workflow in one command:

```sh
python PythonCore/pipeline.py --num_strategies 500 --symbol EURUSD --data Data/EURUSD_M1.csv
```

Optional arguments:

- --num_strategies : Number of strategies to generate (default 1000)
- --symbol : Trading pair symbol (default EURUSD)
- --data : Path to market data CSV
- --no-pdf : Skip PDF report generation

---

6. Using CLI interface

Run interactive terminal menu:

```sh
python PythonCore/cli.py
```

Follow on-screen options to run individual steps or full pipeline.

---

7. Using Web UI (Streamlit)

Install Streamlit if not installed:

```sh
pip install streamlit
```

Run the web dashboard:

```sh
streamlit run PythonCore/app.py
```

Open the shown localhost URL in your browser.

---

8. GitHub Actions setup

Ensure .github/workflows/pipeline.yml and requirements.txt are present.

Push your code to main branch, then:

- Go to Actions tab in GitHub
- Monitor workflow runs automatically triggered on push
- Download reports as artifacts after workflow completion

Optional: enable GitHub Pages in Settings > Pages for public report hosting.

---

9. Viewing reports

Check the Reports/ folder for:

- final_report.html (interactive report)
- final_report.pdf (printable report)
- PNG charts illustrating results

---

10. Troubleshooting

- If a script fails, check terminal or GitHub Actions logs for error details.
- Verify Python and package versions match requirements.
- Ensure data files are correctly formatted CSVs.
- Feel free to open an issue on GitHub for help.

---

11. Contribution & Support

We welcome contributions! Fork the repo, make changes, and submit a pull request.

For questions or bug reports, open an issue.

---

---

## 12. Preparing Market Data

To ensure your raw market data is usable by the pipeline, follow these steps:

1. Place your raw CSV data file (e.g., `raw_data.csv`) inside the `Data/` folder.

2. Run the data preparation script:

   python PythonCore/data_preparation.py --input Data/raw_data.csv --output Data/prepared_data.csv

3. The script will clean, standardize, and save the prepared data as `prepared_data.csv`.

4. Use `prepared_data.csv` as input for the main pipeline, e.g.:

   python PythonCore/pipeline.py --data Data/prepared_data.csv --symbol EURUSD --num_strategies 500

---

Notes:

- The raw CSV should contain columns like Date, Open, High, Low, Close, and Volume.
- The script handles missing data by removing incomplete rows.
- Date columns are parsed into proper datetime format.

---

## Preparing Tick Data for Strategy Pipeline

1. Place your raw tick data file `EURUSD_mt5_ticks.csv` inside the `Data/` folder.

2. Run the tick data preparation script to convert raw tick data to 1-minute OHLCV candles:

python PythonCore/tick_data_preparation.py --input Data/EURUSD_mt5_ticks.csv --output Data/prepared_m1.csv


3. Use the output file `Data/prepared_m1.csv` as input for the main strategy testing pipeline.

---

Notes:

- Raw tick data should be in MT5 tick format without header, with columns: datetime, bid, ask, last, volume, flags.
- The script resamples tick data to 1-minute bars using bid prices and sums volume.
- Empty time intervals without ticks are excluded.



Happy backtesting! 🚀
