# Battery Test

## 🛠️ How to Use

### 1. Modify `battery.py`
**Directly modify these parameters in the script before running:**
- `command1`: Update paths to bin files, lib files and model files stored in devices

### 2. Modify `test_battery.py`

**Directly modify these parameters in the script before running:**
- `DEVICE_ADDR`: Device IP address
- `models`: Model name and model ID (must match the model file name stored in the device)
- `command`: Select for Windows or macOS
- `output_dir`: Output directory for results
- `test_num`: Number of records to take
- `time_sleep`: Interval between power records

### 3. Run `test_battery.py`
This script generates TXT files containing all battery test results.

## 📊 Output Results
After running `test_battery.py`, you will get TXT files under `output_dir`. The structure of these files is like `/device/model_id.txt`. 
Each TXT file contains the device's current battery percentage recorded at every `time_sleep` interval.  
This allows you to calculate **percentage battery consumption** over any fixed time period.
