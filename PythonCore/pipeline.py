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
    parser.add_argument("--terminal_path", type=str, required=True, help="Path to MT5 terminal64.exe")
    parser.add_argument("--no-pdf", action="store_true", help="Skip generating PDF report")

    args = parser.parse_args()

    print("🔁 Starting pipeline with parameters:")
    print(f"  Strategies: {args.num_strategies}")
    print(f"  Symbol: {args.symbol}")
    print(f"  Data File: {args.data}")
    print(f"  MT5 Terminal: {args.terminal_path}")
    print()

    # Step 1: generator.py ← pass number of strategies
    run_script("generator.py", ["--count", str(args.num_strategies)])

    # Step 2: strategy_loader.py ← pass data file
    run_script("strategy_loader.py", ["--data", args.data])

    # Step 3: Run MT5 Runner (pass terminal path)
    run_script("mt5_runner.py", ["--terminal_path", args.terminal_path, "--config_dir", "Backtests/configs"])

    # Step 4+
    for script in [
        "plot_results.py",
        "optimizer.py",
        "pareto_filter.py",
        "ml_model_trainer.py",
        "report_generator.py"
    ]:
        run_script(script)

    # Step 5: result_parser
    run_result_parser()

    # Optional: PDF generation (currently disabled)
    # if not args.no_pdf:
    #     run_script("pdf_generator.py")

    print("\n✅ Pipeline completed. Report is ready in Reports/")

if __name__ == "__main__":
    main()
