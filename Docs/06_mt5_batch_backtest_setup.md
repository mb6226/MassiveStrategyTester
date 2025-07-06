# 📦 06_mt5_batch_backtest_setup.md

## 🎯 MT5 Batch Backtest Setup

This document explains how to configure MetaTrader 5 (MT5) for automated, large-scale batch backtesting using `.ini` configuration files and the `terminal64.exe` command line interface.

---

## 1. 📘 Overview

Batch backtesting in MT5 is achieved by preparing multiple `.ini` files (one per strategy or configuration) and running MT5 via command-line mode.  
This enables fully automated backtesting of thousands of strategies — no GUI interaction required.

---

## 2. ✅ Prerequisites

- ✅ MetaTrader 5 installed (with `terminal64.exe`)
- ✅ Compiled EA (`.ex5`) placed in `MQL5/Experts/`
- ✅ A manually saved `.ini` file as template
- ✅ This project's Python scripts:
  - `PythonCore/ini_generator.py`
  - `PythonCore/mt5_runner.py`

---

## 3. 🛠️ Create a Base `.ini` File

1. Open MT5, go to Strategy Tester.
2. Set your desired EA, symbol, timeframe, and test range.
3. Save the config via **"Save" → `.ini`** file (e.g. `EMA_RSI_template.ini`).
4. Place it in: `Backtests/configs/`.

---

## 4. 🤖 Automating `.ini` Generation

Use:

```bash
python PythonCore/ini_generator.py --template Backtests/configs/template.ini --output-dir Backtests/configs/
This script generates .ini files with different symbols, timeframes, or strategy parameters.

5. 🚀 Run Batch Tests via CLI
Run each .ini using MT5 in silent mode:

bash
Copy
Edit
start "" "C:\Program Files\MetaTrader 5\terminal64.exe" /config:"C:\Backtests\configs\strategy_01.ini"
Or automate it with:

bash
Copy
Edit
python PythonCore/mt5_runner.py --folder Backtests/configs/
6. 📊 Parsing Results
After all .ini files are processed:

Reports are saved in tester/ folder inside MT5

You can use PythonCore/parse_mt5_results.py to extract .htm/.xml into .csv

Combine results into a unified all_results.csv

7. 🛠️ Troubleshooting
Always close MT5 before running batch mode.

Use double backslashes (\\) in paths on Windows.

Make sure .ex5 file is compiled and in the correct folder.

Run scripts with Admin if needed.

8. 📚 References
MT5 Command-Line Docs

Project files:

PythonCore/ini_generator.py

PythonCore/mt5_runner.py

PythonCore/parse_mt5_results.py

📁 Suggested Folder Structure:

Copy
Edit
Backtests/
├── configs/
│   ├── EMA_RSI_template.ini
│   ├── strategy_01.ini
│   └── ...
├── results/
│   ├── strategy_01.htm
│   └── all_results.csv
