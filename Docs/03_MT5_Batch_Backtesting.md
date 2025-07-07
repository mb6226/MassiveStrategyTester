# MT5 Batch Backtest Setup

This document will explain how to configure MetaTrader 5 (MT5) for automated, large-scale batch backtesting using `.ini` configuration files and the `terminal64.exe` command line interface.

---

## 1. Overview

Batch backtesting in MT5 is achieved by preparing multiple `.ini` files (one per strategy or configuration) and running the MT5 terminal in command line mode. This allows for fully automated, large-scale testing of many strategies without manual intervention.

---

## 2. Prerequisites
- MetaTrader 5 installed on your system
- Access to `terminal64.exe` (the MT5 executable)
- Compiled Expert Advisor (`.ex5` file) for your strategy
- Python scripts from this project:
  - `PythonCore/ini_generator.py`
  - `PythonCore/mt5_runner.py`

---

## 3. Creating the Base `.ini` File

1. Open MT5 and configure a single backtest manually in the Strategy Tester.
2. Save the configuration as an `.ini` file (usually via the "Save" button in the Strategy Tester window).
3. This file will serve as a template for batch generation.

Example template content:

```ini
[Tester]
Expert=MyStrategy.ex5
Symbol=EURUSD
Model=0
StartDate=2025.06.01
EndDate=2025.06.20
Deposit=10000
Inputs=Risk=0.01;Magic={STRATEGY_ID};
```

---

## 4. Automating `.ini` File Generation

Use the provided Python script `PythonCore/ini_generator.py` to generate multiple `.ini` files, each with different strategy parameters or symbols.

Minimal version of `ini_generator.py`:

```python
# PythonCore/ini_generator.py
import os
import argparse

TEMPLATE_PATH = "Backtests/configs/template.ini"
OUTPUT_DIR = "Backtests/configs/"
STRATEGY_COUNT = 10

def generate_ini(template_path, output_dir, count):
    with open(template_path, 'r') as file:
        template = file.read()

    for i in range(1, count + 1):
        strategy_id = f"{i:03}"
        output_file = os.path.join(output_dir, f"strategy_{strategy_id}.ini")
        ini_content = template.replace("{STRATEGY_ID}", strategy_id)
        with open(output_file, 'w') as f:
            f.write(ini_content)
        print(f"✅ Created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', type=str, default=TEMPLATE_PATH)
    parser.add_argument('--output', type=str, default=OUTPUT_DIR)
    parser.add_argument('--count', type=int, default=STRATEGY_COUNT)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    generate_ini(args.template, args.output, args.count)
```

Run with:
```bash
python PythonCore/ini_generator.py --count 20
```

---

## 5. Running Batch Backtests

Use the provided Python script `PythonCore/mt5_runner.py` to run MT5 in batch mode:

```bash
python PythonCore/mt5_runner.py --terminal_path "C:\Path\To\terminal64.exe" --config_dir "Backtests/configs/"
```

This script will loop over all `.ini` files in the specified directory and execute them one by one using MT5.

---

## 6. Parsing and Analyzing Results

After all backtests are complete, use the Python scripts in this project to parse, filter, and analyze the output reports.

---

## 7. Troubleshooting
- Ensure all file paths in `.ini` files are correct and use double backslashes (`\\`) on Windows.
- Make sure MT5 is closed before running batch tests to avoid conflicts.
- Check the output folder for result files after each run.

---

## 8. References
- [MetaTrader 5 Command Line Documentation](https://www.metatrader5.com/en/terminal/help/start_advanced/command_line)
- Project files:
  - `PythonCore/ini_generator.py`
  - `PythonCore/mt5_runner.py`

---

## 9. Example Directory Structure

```
MassiveStrategyTester/
├── Backtests/
│   └── configs/
│       ├── template.ini
│       ├── strategy_001.ini
│       ├── strategy_002.ini
│       └── ...
├── PythonCore/
│   ├── ini_generator.py
│   └── mt5_runner.py
```

---

## 10. Sample Output Command

```bash
python PythonCore/mt5_runner.py --terminal_path "C:\Program Files\MetaTrader 5\terminal64.exe" --config_dir "Backtests/configs"
```

> Each strategy will run inside MT5 with the specified `.ini` file. Results (e.g. HTML/CSV) will be saved in the path defined in each `.ini`.
