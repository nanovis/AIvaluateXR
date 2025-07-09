# Battery Test

## 🛠️ How to Use

### 1. Modify `test_consistency_speed.py`
This script handles **consistency testing** and **speed benchmarking**.  
Update these parameters directly in the script:

- `MAGICLEAP, VIVO, QUEST3, ...`: Device serial numbers  
- `output_dir`: Output directory for results  
- `bin_dir, lib_dir, model_dir`: Paths to `llama.cpp` executables, libraries, and model files on device  
  *(Ensure files have read/write/execute permissions)*  
- `time0, time1`: Number of consistency test iterations (default: 20)  
- `time2, time3, time4, time5`: Iteration counts for `pp`, `tg`, `bt`, and `tt` tests (default: 1, llama-bench auto-runs 5 times)  

### 2. Run `test_consistency_speed.py`
In `if __name__ == "__main__":`, configure the `test()` function with:  
1. Device name  
2. Device serial number  
3. Model name *(must match filename on device)*  

Execution generates TXT files containing all test results.

## 📊 Output Results
- `cli-short_prompt-n128.txt`: **Consistency test** (short prompt/output)  
  Fixed prompt + max 128 tokens output. Contains every per-execution logs. 
- `cli-long_prompt-n512.txt`: **Consistency test** (long prompt/output)  
  Fixed prompt + max 512 tokens output. Contains every per-execution logs.
- `bench-pp.txt`: **Prompt Processing (PP)** test results (JSON format)  
- `bench-tg.txt`: **Text Generation (TG)** test results (JSON format)  
- `bench-batch.txt`: **Batch Size (BT)** test results (JSON format)  
- `bench-threads.txt`: **Thread Count (TT)** test results (JSON format)  

ℹ️ These are raw log files. Extract required data manually for **Pareto analysis**.
