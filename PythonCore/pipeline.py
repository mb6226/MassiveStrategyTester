import subprocess
import os

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
    script_path = os.path.join("PythonCore", script_name)
    print(f"🚀 Running {script_name}...")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ {script_name} finished successfully.")
    else:
        print(f"❌ Error in {script_name}:")
        print(result.stderr)
        exit(1)

def main():
    print("🔁 Starting full strategy testing pipeline...\n")
    for script in SCRIPTS:
        run_script(script)
    print("\n🎉 Pipeline completed. Final report ready in Reports/.")

if __name__ == "__main__":
    main()
