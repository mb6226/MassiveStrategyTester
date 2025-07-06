# Project Description: Massive Forex Strategy Tester v1

## 🧭 Project Overview

The **Massive Forex Strategy Tester** is a modular framework for generating, testing, and filtering thousands of trading strategies on Forex historical data using both **MetaTrader 5 (MQL5)** and **Python** environments. It is designed for scalable experimentation, AI-enhanced filtering, and performance analysis of rule-based strategies.

---

## 🎯 Project Objectives

1. Automatically generate thousands of rule-based trading strategies.
2. Perform fast, accurate backtests in both MetaTrader 5 and Python.
3. Evaluate and rank strategies based on performance metrics.
4. Use AI models to filter and cluster promising strategies.
5. Build visual reports for top-performing strategies.

---

## 🛠 Tools and Technologies

| Category           | Tools / Frameworks                        |
|--------------------|-------------------------------------------|
| Backtesting Engine | MetaTrader 5 (MQL5), Python (Backtrader, Pandas) |
| Strategy Logic     | EMA, RSI, ATR, Bollinger Bands, Rule Combinations |
| Data Source        | Tickstory historical data (CSV, M1 resolution or higher) |
| AI / ML Models     | Scikit-learn, XGBoost, KMeans, TensorFlow |
| Storage            | CSV, JSON, SQLite                         |
| Visualization      | Matplotlib, Seaborn, Plotly               |

---

## 🧩 Folder Structure

```
MassiveStrategyTester/
├── Docs/           # Documentation (you are here)
├── Data/           # Historical data from Tickstory
├── PythonCore/     # Python-based strategy engine
│   ├── generator.py
│   ├── backtester.py
│   ├── evaluator.py
│   └── ai_module.py
├── MT5_Core/       # MQL5 code for MetaTrader
│   ├── StrategyTemplate.mq5
│   ├── BatchBacktest.mq5
│   └── ResultsLogger.mqh
├── Reports/        # Test results and plots
├── README.md       # Project overview
└── .gitignore
```

---

## 🗺️ Roadmap (Project Phases)

### ✅ Phase 1: Planning & Setup
- Define project scope and structure
- Prepare historical data from Tickstory
- Design rule-based strategy format

### ✅ Phase 2: Documentation
- Write `README.md`, `project_description.md`, and planning docs

### 🔄 Phase 3: Strategy Generator
- Build rule combinator engine
- Output strategy definitions (JSON or dict format)

### 🔄 Phase 4: Backtest Engine
- Develop Python-based backtester using Pandas/Backtrader
- Develop MQL5 Expert Advisor for MT5 testing

### 🔄 Phase 5: Evaluator Module
- Parse and rank test results using:
  - Net Profit
  - Drawdown
  - Sharpe Ratio
  - Stability

### 🔄 Phase 6: AI Module
- Train ML models to score or classify strategies
- Use clustering (e.g., KMeans) to detect robust patterns

### 🔄 Phase 7: Forward Test & Reporting
- Select top strategies and monitor live performance
- Export reports and plots for best candidates

---

## 🔐 Licensing and Contribution

- License: MIT
- Contributions: Open to community members and collaborators
- Suggestions and pull requests welcome!

