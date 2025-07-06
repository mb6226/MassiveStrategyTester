# PythonCore/ini_generator.py

import os
import configparser

def generate_ini(template_path, output_path, params):
    config = configparser.ConfigParser()
    config.read(template_path)

    for section, values in params.items():
        if section not in config:
            config.add_section(section)
        for key, value in values.items():
            config[section][key] = str(value)

    with open(output_path, 'w') as configfile:
        config.write(configfile)
    print(f"✅ INI file saved to: {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--template', type=str, default='Backtests/configs/example.ini')
    parser.add_argument('--output_dir', type=str, default='Backtests/configs/generated')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    strategies = [
        {'Expert': {'Inputs': 'MA=50;TP=100;SL=30'}},
        {'Expert': {'Inputs': 'MA=20;TP=80;SL=20'}},
        {'Expert': {'Inputs': 'MA=10;TP=50;SL=15'}}
    ]

    for i, params in enumerate(strategies):
        output_file = os.path.join(args.output_dir, f'strategy_{i+1}.ini')
        generate_ini(args.template, output_file, params)
