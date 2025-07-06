### 📊 Result File Format (`all_results.csv`)

Each row in the result file represents the performance of a single backtested strategy:

| Column         | Description                                      |
|----------------|--------------------------------------------------|
| `strategy_name`| Unique identifier for the strategy configuration |
| `profit`       | Total net profit from the backtest               |
| `drawdown`     | Maximum drawdown in percentage (%)               |
| `winrate`      | Percentage of winning trades                     |
| `trades`       | Total number of trades executed                  |
