# Memory Test

## 🛠️ How to Use

### 1. Run `test_memory.py`
This script generates raw TXT files containing all test results.  

**Directly modify these parameters in the script before running:**
- `VIVO, MAGICLEAP, QUEST`: device serial number (currently 3 predefined, you can add more)
- `base_path`: output directory for TXT files
- `command0, command1`: Update paths to bin files, lib files and model files stored in devices
- `if __name__ == "__main__`: modify parameters in `test`.
  - `device`: Device name
  - `number`: Serial number
  - `model`: Model name (must match device's model file)

### 2. Run tab_memory_test.py
Generates processed results in `memory.xlsx`.

​​**Required modifications:​**
- `input_base_dir`: Raw TXT location
- `output_dir`: Where to save `memory.xlsx`
- `devices`: Match device names in TXT paths
- `models`: Match model names in TXT paths

## 📊 Output Results
After Step 1:
- Raw TXT files stored in `--base_path` directory
After Step 2:
- Processed `memory.xlsx` file generated in `--output_dir`
​​- Features​​:
  - All memory consumption in ​​GB units​​ 📏
  - Results for ​​all devices & models​​
  - Average Data derived from top command during llama.cpp execution

## 🔜 Next Step
Use `memory.xlsx` for ​​Pareto analysis​​ and performance comparisons.
