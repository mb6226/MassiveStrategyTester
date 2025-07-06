06_mt5_batch_backtest_setup.txt

🎯 MT5 Batch Backtest Setup

This document explains how to configure MetaTrader 5 (MT5) for automated, large-scale batch backtesting using `.ini` configuration files and the `terminal64.exe` command line interface.

────────────────────────────────────────────

1. 📘 Overview

Batch backtesting in MT5 is done using `.ini` files (each representing one backtest) and running MT5 via command-line.  
This enables fully automated testing of hundreds or thousands of strategies.

────────────────────────────────────────────

2. ✅ Prerequisites

- MetaTrader 5 installed (including `terminal64.exe`)
- Expert Advisor compiled into `.ex5`
- A saved `.ini` file (from manual backtest in MT5)
- These scripts from this project:
  - PythonCore/ini_generator.py
  - PythonCore/mt5_runner.py

────────────────────────────────────────────

3. 🛠️ Create a Base `.ini` File

1. Open MT5
2. Configure any backtest manually in Strategy Tester
3. Click “Save” to export the `.ini` (e.g., EMA_template.ini)
4. Put it into `Backtests/configs/`

────────────────────────────────────────────

4. 🤖 Generate `.ini` Files Automatically

Use this command:

python PythonCore/ini_generator.py --template Backtests/configs/template.ini --output-dir Backtests/configs/

It generates multiple `.ini` configs for different parameter sets or symbols.

────────────────────────────────────────────

5. 🚀 Run MT5 in Batch Mode

You can run one `.ini`:

"C:\Program Files\MetaTrader 5\terminal64.exe" /config:"C:\Backtests\configs\strategy_01.ini"

Or use this script to run all:

python PythonCore/mt5_runner.py --folder Backtests/configs/

────────────────────────────────────────────

6. 📊 Parse and Analyze Results

- Output reports saved in `tester/` folder
- Use `parse_mt5_results.py` to extract summary from HTML/XML
- Collect all results into one CSV like `all_results.csv`

────────────────────────────────────────────

7. 🛠️ Troubleshooting

- Close MT5 before running batch tests
- Use valid paths with double backslashes (`\\`)
- Ensure `.ex5` file is compiled and placed correctly
- If needed, run as Administrator

────────────────────────────────────────────

8. 📚 References

- https://www.metatrader5.com/en/terminal/help/start_advanced/command_line
- Scripts:
  - PythonCore/ini_generator.py
  - PythonCore/mt5_runner.py
  - PythonCore/parse_mt5_results.py

────────────────────────────────────────────

📁 Suggested Folder Structure:

Backtests/
├── configs/
│   ├── EMA_RSI_template.ini
│   ├── strategy_01.ini
│   └── ...
├── results/
│   ├── strategy_01.htm
│   └── all_results.csv
