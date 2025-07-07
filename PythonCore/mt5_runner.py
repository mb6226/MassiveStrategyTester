# PythonCore/mt5_runner.py

import os
import argparse
import subprocess

def run_backtests(terminal_path, config_dir):
    if not os.path.isfile(terminal_path):
        print(f"❌ terminal64.exe not found at: {terminal_path}")
        return

    if not os.path.isdir(config_dir):
        print(f"❌ Config directory not found: {config_dir}")
        return

    ini_files = [f for f in os.listdir(config_dir) if f.endswith('.ini')]
    if not ini_files:
        print("⚠️ No INI files found in the config directory.")
        return

    print(f"🚀 Starting batch backtests ({len(ini_files)} configurations)...")
    for ini_file in ini_files:
        config_path = os.path.join(config_dir, ini_file)
        print(f"▶ Running: {ini_file}")
        try:
            subprocess.run(
                [terminal_path, f"/config:{config_path}"],
                check=True
            )
            print(f"✅ Completed: {ini_file}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running {ini_file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MT5 batch backtests using terminal64.exe")
    parser.add_argument('--terminal_path', type=str, required=False, default="C:\\Program Files\\Assets Global MetaTrader 5 Terminal\\terminal64.exe", help='Full path to terminal64.exe')
    parser.add_argument('--config_dir', type=str, required=True, help='Directory containing .ini config files')
    args = parser.parse_args()

    run_backtests(args.terminal_path, args.config_dir)
