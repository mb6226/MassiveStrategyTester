# PythonCore/cli.py

import subprocess
import sys

SCRIPTS = [
    "generator.py",
    "strategy_loader.py",
    "plot_results.py",
    "optimizer.py",
    "pareto_filter.py",
    "ml_model_trainer.py",
    "report_generator.py",
    "pdf_generator.py"
]

def run_script(script_name):
    print(f"🚀 Running {script_name}...")
    result = subprocess.run([sys.executable, f"PythonCore/{script_name}"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {script_name} completed successfully.\n")
    else:
        print(f"❌ Error running {script_name}:\n{result.stderr}")
        exit(1)

def main():
    while True:
        print("\n=== Massive Strategy Tester CLI ===")
        print("1) Generate Strategies")
        print("2) Run Backtests")
        print("3) Plot Results")
        print("4) Optimize Strategies")
        print("5) Pareto Filtering")
        print("6) Train ML Model")
        print("7) Generate Report (HTML)")
        print("8) Generate PDF Report")
        print("9) Run Full Pipeline")
        print("0) Exit")

        choice = input("Select an option: ").strip()

        if choice == "0":
            print("Exiting. Bye!")
            break
        elif choice == "1":
            run_script("generator.py")
        elif choice == "2":
            run_script("strategy_loader.py")
        elif choice == "3":
            run_script("plot_results.py")
        elif choice == "4":
            run_script("optimizer.py")
        elif choice == "5":
            run_script("pareto_filter.py")
        elif choice == "6":
            run_script("ml_model_trainer.py")
        elif choice == "7":
            run_script("report_generator.py")
        elif choice == "8":
            run_script("pdf_generator.py")
        elif choice == "9":
            for script in SCRIPTS:
                run_script(script)
            print("🎉 Full pipeline completed.")
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
