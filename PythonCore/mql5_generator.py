import json
import os

TEMPLATE_PATH = "Templates/MyStrategyTemplate.mq5"
OUTPUT_DIR = "GeneratedStrategies"

def load_template():
    with open(TEMPLATE_PATH, "r") as f:
        return f.read()

def load_strategies(json_file="strategies.json"):
    with open(json_file, "r") as f:
        return json.load(f)

def generate_mql5_files(strategies):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    template = load_template()

    for strat in strategies:
        code = template.format(
            ema_period=strat["ema_period"],
            rsi_period=strat["rsi_period"],
            atr_period=strat["atr_period"],
            take_profit=strat["take_profit"],
            stop_loss=strat["stop_loss"]
        )

        filename = f"{strat['name']}.mq5"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w") as f:
            f.write(code)
        print(f"Generated {filename}")

if __name__ == "__main__":
    strategies = load_strategies()
    generate_mql5_files(strategies)
