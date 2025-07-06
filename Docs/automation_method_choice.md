# 🧠 Strategy Automation Method Decision

This document outlines the reasoning behind choosing **Method 4** (`MT5 .ini + terminal.exe`) as the preferred first step for automating massive backtesting in MetaTrader 5 (MT5), and compares it to **Method 2** (`Python + MetaTrader5 API`).

---

## ✅ Preferred Method: Method 4 — `.ini` Configuration + `terminal64.exe`

### 🔍 Why Method 4 First?

| Feature                | Method 4: `.ini + terminal64.exe`        | Method 2: Python + MetaTrader5 API             |
|------------------------|------------------------------------------|------------------------------------------------|
| 🎯 Primary Goal        | Automate massive backtests               | Analyze price data, live integration           |
| 🛠️ MT5 Engine Support  | ✅ Uses built-in MT5 strategy tester      | ❌ Cannot trigger MT5 strategy tester          |
| 📊 Result Reports      | ✅ Auto-generated HTML/XML/CSV            | ❌ Must be implemented manually                |
| 🔁 Batch Testing       | ✅ Easy to automate with Python           | ❌ Requires manual EA logic and looping        |
| ⏱️ Dev Speed           | ✅ Ready to use with existing `.ex5` EAs  | 🚧 Slower, needs custom logic in Python        |
| 🧪 MQL5 Compatibility  | ✅ Direct use of compiled EA strategies   | ❌ Cannot directly run `.ex5` files            |

---

## 🔄 Planned Workflow with Method 4

1. Create a base `.ini` file for Strategy Tester configuration.
2. Automate generating `.ini` files for thousands of strategies using Python.
3. Use `terminal64.exe` (via command line) to batch run backtests.
4. Parse MT5 output reports (HTML/XML/CSV) using Python scripts.
5. Filter & rank strategies based on performance metrics.

---

## 🔍 Alternative: Method 2 — Python + MetaTrader5 API

The **MetaTrader5 Python API** allows for real-time interaction with the MT5 terminal, but does **not support direct backtesting or EA execution**.

### ✅ What It Can Do:
- Fetch real-time and historical data (ticks, candles, indicators)
- Open/modify/close positions (for live trading)
- Monitor account balance, trades, orders
- Analyze signals from AI models or custom logic

### ❌ Limitations:
- Cannot run `.ex5` EA files or use MT5 Strategy Tester
- Backtesting must be implemented from scratch in Python
- No built-in performance reports (HTML/XML)

### ✅ When to Use:
- For analyzing and validating selected strategies after filtering
- When integrating a filtered strategy into a live system
- For live data feeds and custom dashboards

---

## 🔮 Final Recommendation

📌 **Use Method 4 now** for fast, large-scale backtesting.  
📌 **Integrate Method 2 later** for deeper analysis and live integration.

---

## 📁 Related Files
- `Docs/mt5_batch_backtest_setup.md`: How to configure `.ini` and automate MT5 testing.
- `PythonCore/ini_generator.py`: Script to generate multiple `.ini` files.
- `PythonCore/mt5_runner.py`: Script to run MT5 terminal with those files.
- `PythonCore/mt5_connector.py` *(future)*: Will implement Method 2 features (Python API)

