# Massive Forex Strategy Tester v1

This project is designed to generate, backtest, evaluate, and select the best-performing trading strategies for the Forex market. It supports both **MetaTrader 5 (MQL5)** and **Python-based** backtesting engines and utilizes high-quality historical data extracted via **Tickstory**.

---

## 🚀 Project Goals

- Automatically generate thousands of rule-based trading strategies
- Backtest strategies on historical data (in both Python and MT5)
- Analyze results and filter high-performance strategies using key metrics
- Use AI-based models to enhance strategy selection and avoid overfitting
- Store and visualize strategy performance reports

---

## 🧩 Project Structure

MassiveStrategyTester/
├── Docs/ # Project documentation
│ └── project_description.md
├── Data/ # Historical data (from Tickstory)
├── PythonCore/ # Python engine for generation, testing, AI filtering
│ ├── generator.py
│ ├── backtester.py
│ ├── evaluator.py
│ └── ai_module.py
├── MT5_Core/ # MQL5 code for strategy testing in MetaTrader
│ ├── StrategyTemplate.mq5
│ ├── BatchBacktest.mq5
│ └── ResultsLogger.mqh
├── Reports/ # Output results and charts
├── README.md # This file
└── .gitignore

yaml
Copy
Edit

---

## 🛠 Technologies Used

| Component       | Stack                            |
|----------------|-----------------------------------|
| Backtesting     | MetaTrader 5 (MQL5), Python (Backtrader, Pandas) |
| Data Source     | Tickstory CSV (M1+)               |
| Strategy Logic  | Rule-based strategies (EMA, RSI, ATR, etc.) |
| AI Modules      | Scikit-learn / XGBoost / TensorFlow (optional) |
| Evaluation      | Python + Pandas + Matplotlib      |
| Storage         | CSV, SQLite, or JSON              |

---

## 🧠 AI Integration

The project plans to use AI models in the following areas:
- Strategy performance prediction (meta-learning)
- Filtering overfit strategies based on forward test simulation
- Clustering similar strategies and finding robust groups

---

## 📌 Roadmap (Phase Plan)

### Phase 1: Project Planning
- Define rules, inputs, and test metrics
- Organize folders and toolchains

### Phase 2: Strategy Generator
- Create a combinatorial engine for technical rule generation

### Phase 3: Backtest Engine
- Implement backtesting logic in both Python and MQL5

### Phase 4: Result Evaluation
- Analyze results and rank strategies using performance metrics

### Phase 5: AI-Based Filtering
- Train AI models to score, cluster, and refine strategy selection

### Phase 6: Visualization & Reporting
- Create graphs and export results for top strategies

---

## 📎 License

MIT License - feel free to use, share, and contribute.

---

## 🤝 Contributions

Pull requests, ideas, and forks are welcome!  
If you like the project, give it a ⭐ on GitHub!
