# PythonCore/generator.py

import itertools
import json

# Define parameter ranges
emas = [20, 50, 100, 200]
rsis = [7, 14, 21]
atr_periods = [14]
take_profits = [50, 100, 150]
stop_losses = [30, 60, 90]

def generate_strategies():
    strategies = []
    for ema, rsi, atr, tp, sl in itertools.product(emas, rsis, atr_periods, take_profits, stop_losses):
        strategy = {
            "name": f"EMA{ema}_RSI{rsi}_ATR{atr}_TP{tp}_SL{sl}",
            "ema_period": ema,
            "rsi_period": rsi,
            "atr_period": atr,
            "take_profit": tp,
            "stop_loss": sl
        }
        strategies.append(strategy)
    return strategies

def save_strategies(strategies, output_file="strategies.json"):
    with open(output_file, "w") as f:
        json.dump(strategies, f, indent=2)

if __name__ == "__main__":
    strategies = generate_strategies()
    save_strategies(strategies)
    print(f"{len(strategies)} strategies generated and saved to strategies.json")
