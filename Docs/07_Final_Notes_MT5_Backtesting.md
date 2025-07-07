# 07_Final_Notes_MT5_Backtesting

### ✅ Key Points and Lessons Learned in Final Pipeline Execution with MT5

After implementing and fully testing the batch backtesting stage with MetaTrader 5, the following key lessons and critical notes were extracted:

---

### 🧠 1. Successful Pipeline Execution

* Now, running the following command executes the entire pipeline from strategy generation to the final report:

  ```bash
  python PythonCore/pipeline.py --num_strategies 50
  ```
* This run successfully completes the following steps:

  * Generation of strategy `.ini` files
  * Loading strategies on offline data
  * Automated execution of terminal64.exe
  * Producing results and a summary report in `summary.csv`
  * ML model training and final HTML report generation

---

### ⚙️ 2. Setting `terminal64.exe` in `mt5_runner.py`

* To avoid having to enter the terminal path every time, the path is set as a **default** in `mt5_runner.py`:

  ```python
  default="C:\\Program Files\\Assets Global MetaTrader 5 Terminal\\terminal64.exe"
  ```
* Therefore, there is no need to pass `--terminal_path` on the command line.

---

### 💾 3. Using Offline Data in the Standard MetaTrader Path

* Data is stored in the following path:

  ```
  C:\Users\Administrator\AppData\Roaming\MetaQuotes\Terminal\{InstanceID}\bases\Custom\history\EURUSD1
  ```
* To use offline data:

  * In `.ini` files, `UseLocal=1` is set.
  * The symbol `EURUSD1` is chosen to match the offline data.

---

### ⚠️ 4. Preventing MT5 Hang

* If `--terminal_path` is defined in both the pipeline and `mt5_runner.py`, it can cause **conflicts in running terminal64.exe** and hang the program.
* Solution:

  * Only manage `--terminal_path` in `mt5_runner.py`.
  * The pipeline should not send this argument.

---

### 🔁 5. Removing Dependency on Data Files in `Data/`

* Since the actual run uses offline data, `--data` is no longer needed in the pipeline. For compatibility, an empty file like `Data/dummy.csv` is defined to prevent crashes.

---

### 📄 6. Final Commit in GitHub:

```bash
git add PythonCore/pipeline.py
git commit -m "Do not pass --terminal_path from pipeline.py; let mt5_runner.py handle terminal path to avoid MT5 hang"
git push
```

---

### 🎯 Final Result

Now, with a single command, the entire process is performed end-to-end, and all modules work seamlessly with MT5 and offline data.
