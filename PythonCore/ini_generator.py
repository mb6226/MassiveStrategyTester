# PythonCore/ini_generator.py

import os
import argparse

def generate_ini(template_path, output_dir, strategies):
    with open(template_path, 'r') as f:
        template = f.read()

    os.makedirs(output_dir, exist_ok=True)

    for i, strategy in enumerate(strategies):
        ini_content = template.replace("{{STRATEGY_PARAMS}}", strategy)
        output_path = os.path.join(output_dir, f"config_{i+1}.ini")
        with open(output_path, 'w') as out:
            out.write(ini_content)
        print(f"✅ Created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate multiple INI files for MT5 backtesting")
    parser.add_argument('--template', type=str, required=True, help='Path to base .ini file (template)')
    parser.add_argument('--output_dir', type=str, default='Backtests/configs', help='Directory to save generated INI files')
    parser.add_argument('--strategies', nargs='+', required=True, help='List of strategy parameter strings to inject')

    args = parser.parse_args()

    generate_ini(args.template, args.output_dir, args.strategies)
