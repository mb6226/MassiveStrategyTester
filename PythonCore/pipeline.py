import subprocess
import os
import argparse

def get_venv_python():
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    return venv_python if os.path.isfile(venv_python) else "python"

def run_script(script_name, args=None):
    script_path = os.path.join("PythonCore", script_name)
    cmd = [get_venv_python(), script_path]
    if args:
        cmd += args
    print(f"🚀 Running {script_name}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ {script_name} finished successfully.")
    else:
        print(f"❌ Error in {script_name}:\n{result.stderr}")
        exit(1)

def run_mt5_runner(terminal_path, config_dir):
    print("🚀 Running mt5_runner.py for batch backtests with MT5...")
    try:
        subprocess.run([
            get_venv_python(),
            "PythonCore/mt5_runner.py",
            "--terminal_path", terminal_path,
            "--config_dir", config_dir
        ], check=True)
        print("✅ mt5_runner.py finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in mt5_runner.py:\n{e}")
        exit(1)

def run_result_parser():
    print("🚀 Running result_parser.py...")
    try:
        subprocess.run([
            get_venv_python(),
            "PythonCore/result_parser.py",
            "--input_dir", "Backtests/results",
            "--output_file", "Backtests/summary.csv"
        ], check=True)
        print("✅ result_parser.py finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in result_parser.py:\n{e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Massive Strategy Tester Pipeline")

    parser.add_argument("--num_strategies", type=int, default=1000, help="Number of strategies to generate")
    parser.add_argument("--symbol", type=str, default="EURUSD", help="Trading symbol")
    parser.add_argument("--data", type=str, default="Data/EURUSD_M1.csv", help="Path to input data CSV")
    parser.add_argument("--terminal_path", type=str, required=True, help="Full path to MT5 terminal64.exe")
    parser.add_argument("--config_dir", type=str, default="Backtests/configs", help="Directory of .ini config files")
    parser.add_argument("--no-pdf", action="store_true", help="Skip generating PDF report")

    args = parser.parse_args()

    print("🔁 Starting pipeline with parameters:")
    print(f"  Strategies: {args.num_strategies}")
    print(f"  Symbol: {args.symbol}")
    print(f"  Data File: {args.data}")
    print(f"  MT5 Terminal: {args.terminal_path}")
    print(f"  Config Dir: {args.config_dir}")
    print()

    # Step 1: Generate strategies
    run_script("generator.py", ["--count", str(args.num_strategies)])

    # Step 2: Prepare/load data in Python (optional preprocessing)
    run_script("strategy_loader.py", ["--data", args.data])

    # Step 3: Run batch backtests on MT5 offline data
    run_mt5_runner(args.terminal_path, args.config_dir)

    # Step 4: Continue with plotting, optimization, filtering, ML, reporting
    for script in [
        "plot_results.py",
        "optimizer.py",
        "pareto_filter.py",
        "ml_model_trainer.py",
        "report_generator.py"
    ]:
        run_script(script)

    # Step 5: Parse MT5 results from Backtests/results folder
    run_result_parser()

    # PDF generation skipped (optional)
    # if not args.no_pdf:
    #     run_script("pdf_generator.py")

    print("\nPipeline completed. Report is ready in Reports/")

if __name__ == "__main__":
    main()
