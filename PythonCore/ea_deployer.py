import os
import argparse
import shutil
from pathlib import Path

def find_mt5_terminal_paths():
    """
    جستجوی مسیرهای نصب MetaTrader 5 از روی پوشه‌های AppData
    """
    base_path = Path(os.getenv("APPDATA")) / "MetaQuotes" / "Terminal"
    instances = list(base_path.glob("*"))
    if not instances:
        print("❌ هیچ ترمینال MetaTrader 5 نصب‌شده‌ای در مسیر AppData پیدا نشد.")
        return []
    return instances

def deploy_ea_to_all(terminals, ea_file):
    success = 0
    for terminal in terminals:
        expert_path = terminal / "MQL5" / "Experts"
        if expert_path.exists():
            try:
                shutil.copy(ea_file, expert_path)
                print(f"✅ EA copied to: {expert_path}")
                success += 1
            except Exception as e:
                print(f"❌ Failed to copy EA to {expert_path}: {e}")
        else:
            print(f"⚠️ Experts folder not found: {expert_path}")
    if success == 0:
        print("❌ EA deployment failed for all terminals.")
    else:
        print(f"✅ EA successfully deployed to {success} terminal(s).")

def main():
    parser = argparse.ArgumentParser(description="Deploy .ex5 EA to MetaTrader 5 terminals")
    parser.add_argument("--ea_file", type=str, required=True, help="Path to the compiled .ex5 EA file")

    args = parser.parse_args()
    ea_file = Path(args.ea_file)

    if not ea_file.exists():
        print(f"❌ EA file not found: {ea_file}")
        return

    print(f"📦 Deploying EA: {ea_file}")
    terminals = find_mt5_terminal_paths()
    if not terminals:
        return

    deploy_ea_to_all(terminals, ea_file)

if __name__ == "__main__":
    main()
