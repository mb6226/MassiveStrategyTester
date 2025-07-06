# PythonCore/app.py

import streamlit as st
import subprocess
import os

SCRIPTS = {
    "Generate Strategies": "generator.py",
    "Run Backtests": "strategy_loader.py",
    "Plot Results": "plot_results.py",
    "Optimize Strategies": "optimizer.py",
    "Pareto Filtering": "pareto_filter.py",
    "Train ML Model": "ml_model_trainer.py",
    "Generate Report (HTML)": "report_generator.py",
    "Generate PDF Report": "pdf_generator.py",
    "Run Full Pipeline": None  # special handling
}

def run_script(script_name):
    if script_name is None:
        # Run all scripts in order
        for script in SCRIPTS.values():
            if script:
                st.write(f"🚀 Running {script}...")
                result = subprocess.run(["python", f"PythonCore/{script}"], capture_output=True, text=True)
                if result.returncode == 0:
                    st.success(f"{script} completed successfully.")
                else:
                    st.error(f"Error running {script}:\n{result.stderr}")
                    return False
        st.success("🎉 Full pipeline completed.")
        return True
    else:
        st.write(f"🚀 Running {script_name}...")
        result = subprocess.run(["python", f"PythonCore/{script_name}"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success(f"{script_name} completed successfully.")
            return True
        else:
            st.error(f"Error running {script_name}:\n{result.stderr}")
            return False

def main():
    st.title("Massive Strategy Tester Dashboard")

    action = st.selectbox("Select Action", list(SCRIPTS.keys()))

    if st.button("Run"):
        run_script(SCRIPTS[action])

    st.markdown("---")
    st.header("Reports Preview")

    img_files = [
        "Reports/profit_distribution.png",
        "Reports/profit_vs_drawdown.png",
        "Reports/top_10_strategies.png"
    ]

    for img in img_files:
        if os.path.exists(img):
            st.image(img)
        else:
            st.warning(f"Image not found: {img}")

    report_html = "Reports/final_report.html"
    if os.path.exists(report_html):
        with open(report_html, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.markdown("### Final Report (HTML)", unsafe_allow_html=True)
        st.components.v1.html(html_content, height=600)
    else:
        st.warning("Final HTML report not found.")

if __name__ == "__main__":
    main()
