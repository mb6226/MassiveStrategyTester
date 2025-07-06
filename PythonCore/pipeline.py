import subprocess
import os
import argparse

def run_script(script_name, args=None):
    script_path = os.path.join("PythonCore", script_name)
    cmd = ["python", script_path]
    if args:
        cmd += args
    print(f"🚀 Running {script_name}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ {script_name} finished successfully.")
    else:
        print(f"❌ Error in {script_name}:\n{result.stderr}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Massive Strategy Tester Pipeline")

    parser.add_argument("--num_strategies", type=int, default=1000, help="Number of strategies to generate")
    parser.add_argument("--symbol", type=str, default="EURUSD", help="Trading symbol")
    parser.add_argument("--data", type=str, default="Data/EURUSD_M1.csv", help="Path to input data CSV")
    parser.add_argument("--no-pdf", action="store_true", help="Skip generating PDF report")

    args = parser.parse_args()

    print("🔁 Starting pipeline with parameters:")
    print(f"  Strategies: {args.num_strategies}")
    print(f"  Symbol: {args.symbol}")
    print(f"  Data File: {args.data}")
    print()

    # Step 1: generator.py ← پاس دادن تعداد
    run_script("generator.py", ["--count", str(args.num_strategies)])

    # Step 2: strategy_loader.py ← پاس دادن داده
    run_script("strategy_loader.py", ["--data", args.data])

    # سایر مراحل بدون پارامتر اضافی
    for script in [
        "plot_results.py",
        "optimizer.py",
        "pareto_filter.py",
        "ml_model_trainer.py",
        "report_generator.py"
    ]:
        run_script(script)

    # Remove or comment out PDF generation step
    # if not args.no_pdf:
    #     run_script("pdf_generator.py")
    print("\nPipeline completed. Report is ready in Reports/")

if __name__ == "__main__":
    main()
