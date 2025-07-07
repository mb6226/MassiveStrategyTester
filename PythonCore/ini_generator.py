# PythonCore/ini_generator.py

import os
import argparse

TEMPLATE_PATH = "Backtests/configs/template.ini"
OUTPUT_DIR = "Backtests/configs/"
STRATEGY_COUNT = 10  # change as needed

def generate_ini(template_path, output_dir, count):
    with open(template_path, 'r') as file:
        template = file.read()

    for i in range(1, count + 1):
        strategy_id = f"{i:03}"
        output_file = os.path.join(output_dir, f"strategy_{strategy_id}.ini")
        
        # 👇 Simple replacement logic
        ini_content = template.replace("{STRATEGY_ID}", strategy_id)

        with open(output_file, 'w') as f:
            f.write(ini_content)
        print(f"✅ Created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="INI Batch Generator")
    parser.add_argument('--template', type=str, default=TEMPLATE_PATH)
    parser.add_argument('--output', type=str, default=OUTPUT_DIR)
    parser.add_argument('--count', type=int, default=STRATEGY_COUNT)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    generate_ini(args.template, args.output, args.count)
