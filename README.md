MassiveStrategyTester

A comprehensive pipeline for massive Forex strategy backtesting, optimization, AI-based selection, and reporting.

---

Project Structure

MassiveStrategyTester/
├── PythonCore/              # Python scripts for data processing and ML
├── Reports/                 # Output reports and charts
├── .github/workflows/       # GitHub Actions workflow files
├── Templates/               # HTML report templates
├── requirements.txt         # Python dependencies
├── README.md                # This documentation file

---

Quick Start

1. Clone the repository

git clone https://github.com/yourusername/MassiveStrategyTester.git
cd MassiveStrategyTester

2. Install dependencies

pip install -r requirements.txt

---

Running the Pipeline Locally

Run the entire strategy testing pipeline:

python PythonCore/pipeline.py --num_strategies 500 --symbol EURUSD --data Data/EURUSD_M1.csv

You can customize parameters:

- --num_strategies: Number of strategies to generate (default 1000)
- --symbol: Trading pair symbol (default EURUSD)
- --data: Path to input market data CSV file
- --no-pdf: Skip PDF report generation

---

Reports and Results

- Reports are saved in the Reports/ directory:
  - final_report.html — Interactive HTML report
  - final_report.pdf — PDF report version
  - Chart images (*.png)

---

Features

- Massive strategy generation and backtesting
- Pareto front filtering for multi-objective optimization
- AI-based ML model for profitable strategy prediction
- Automated report generation with visualizations
- CLI and Web UI (Streamlit) for easier control

---

GitHub Actions CI/CD

This project includes a GitHub Actions workflow to automate running the pipeline on each push to main or master.

- Workflow file path: .github/workflows/pipeline.yml
- Runs the full pipeline and uploads reports as artifacts
- Optionally publishes HTML reports via GitHub Pages

Setup

1. Ensure .github/workflows/pipeline.yml and requirements.txt are in the repository.
2. Push changes to GitHub.
3. Visit the Actions tab to monitor runs.
4. (Optional) Enable GitHub Pages via Settings > Pages selecting the gh-pages branch to serve reports publicly.

---

CLI and Web UI

- Run python PythonCore/cli.py for a terminal menu interface.
- Run streamlit run PythonCore/app.py for a web dashboard.

---

Contact & Support

For questions, feature requests, or contributions, please open an issue or contact me via GitHub.

---

Happy backtesting! 🚀
