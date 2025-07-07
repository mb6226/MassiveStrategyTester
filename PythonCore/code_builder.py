# PythonCore/code_builder.py

import os
import json
import argparse
import subprocess

# Default paths (adjust if needed)
TEMPLATE_PATH = "MQL5/Experts/MyStrategyTemplate.mq5"
OUTPUT_DIR = "MQL5/Experts/Generated"
METAEDITOR_PATH = "C:/Program Files/Assets Global MetaTrader 5 Terminal/metaeditor64.exe"


def load_strategies(json_path):
    with open(json_path, "r") as f:
        return json.load(f)


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_mq5_file(strategy):
    with open(TEMPLATE_PATH, "r") as template_file:
        template = template_file.read()

    strategy_code = template.format(
        EMA=strategy["ema_period"],
        RSI=strategy["rsi_period"],
        ATR=strategy["atr_period"],
        TP=strategy["take_profit"],
        SL=strategy["stop_loss"]
    )

    name = strategy["name"]
    output_path = os.path.join(OUTPUT_DIR, f"{name}.mq5")
    with open(output_path, "w") as out_file:
        out_file.write(strategy_code)

    return output_path


def compile_mq5_file(mq5_path):
    try:
        subprocess.run([
            METAEDITOR_PATH,
            "/compile:" + mq5_path
        ], check=True)
        print(f"✅ Compiled: {mq5_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Compile failed: {mq5_path}\n{e}")


def main():
    parser = argparse.ArgumentParser(description="Generate and compile MQ5 files for strategies")
    parser.add_argument("--input", type=str, default="strategies.json", help="Path to strategy JSON file")
    args = parser.parse_args()

    ensure_output_dir()
    strategies = load_strategies(args.input)

    for strategy in strategies:
        mq5_file = generate_mq5_file(strategy)
        compile_mq5_file(mq5_file)

    print("\n🎯 All strategies processed.")


if __name__ == "__main__":
    main()
