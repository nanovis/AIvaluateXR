import os
import re
import pandas as pd

input_base_dir = r"C:\User\results\memory_test"
output_dir = r'C:\Users\results\memory_test'


def extract_memory_usage(file_path, is_s128):
    """
    Extract physical memory usage from the file and group by PID,
    returning the maximum and average values for each PID
    """
    memory_usage = {}
    if not os.path.exists(file_path):
        print(f"warning: {file_path} doesn't exist, skip")
        return {}, {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # match llama-cli line
            if is_s128:
                prompt_pattern = r'Three advice on keeping healthy: -n 128' # You may need to reset the pattern
            else:
                prompt_pattern = r'Plan a 7-day itinerary for two people traveling from Austria to KAUST.*-n 1024' # You may need to reset the pattern

            if re.search(prompt_pattern, line) and 'export' not in line:
                match = re.search(
                    r'(\d+)\s+shell\s+(\d+)\s+(\d+)\s+(\d+(\.\d+)?[A-Z])\s+(\d+(\.\d+)?[A-Z])\s+(\d+(\.\d+)?[A-Z])\s+[A-Z]\s+\d+(\.\d+)?\s+\d+(\.\d+)?\s+\d+[:]\d+(\.\d+)?\s+llama-cli',
                    line)

                if match:
                    pid = match.group(1)  # PID
                    res_memory = match.group(6)  # RES
                    if res_memory is not None:
                        if 'G' in res_memory:
                            res_memory = float(res_memory.replace('G', ''))
                        elif 'M' in res_memory:
                            res_memory = float(res_memory.replace('M', ''))/1024  # MB to GB
                        res_memory = round(float(res_memory), 1)  # accuracy to 0.1 GB

                        # record the memory use to dictionary according to PID
                        if pid not in memory_usage:
                            memory_usage[pid] = []
                        memory_usage[pid].append(res_memory)
                    else:
                        print(f"warning: unable to extract memory info from this line: {line.strip()}")

    if not memory_usage:
        print(f"warning: unable to extract any memory info from this file: {file_path}")
        return {}, {}

    # calculate the max and avg data of each PID
    max_usage = {pid: max(usages) for pid, usages in memory_usage.items()}
    avg_usage = {pid: sum(usages) / len(usages) for pid, usages in memory_usage.items()}

    return max_usage, avg_usage


def calculate_average(data):
    """Compute the average memory data for each device and model combination."""
    avg_data = {}
    for model, device_data in data.items():
        avg_data[model] = {}
        for device, values in device_data.items():
            if values:
                avg_data[model][device] = sum(values) / len(values)
            else:
                avg_data[model][device] = None
    return avg_data


def generate_excel_for_memory_usage(devices, models):
    """generate excel files"""
    s128_max_data = {}
    l1024_max_data = {}
    s128_avg_data = {}
    l1024_avg_data = {}

    for model in models:
        s128_max_data[model] = {}
        l1024_max_data[model] = {}
        s128_avg_data[model] = {}
        l1024_avg_data[model] = {}

        for device in devices:
            base_path = fr'{input_base_dir}\{device}\{model}'
            s128_file = os.path.join(base_path, f'{model}-s128.txt')
            l1024_file = os.path.join(base_path, f'{model}-l1024.txt')

            # extract the value of memory use of s128 and l1024
            max_s128, avg_s128 = extract_memory_usage(s128_file, is_s128=True)
            max_l1024, avg_l1024 = extract_memory_usage(l1024_file, is_s128=False)

            # set null as default value
            s128_max_data[model][device] = list(max_s128.values()) if max_s128 else []
            l1024_max_data[model][device] = list(max_l1024.values()) if max_l1024 else []
            s128_avg_data[model][device] = list(avg_s128.values()) if avg_s128 else []
            l1024_avg_data[model][device] = list(avg_l1024.values()) if avg_l1024 else []

    # mean
    s128_max_avg = calculate_average(s128_max_data)
    l1024_max_avg = calculate_average(l1024_max_data)

    # create Excel file and store data
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'memory.xlsx')

    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        pd.DataFrame(s128_max_data).T.to_excel(writer, sheet_name='s128-max')
        pd.DataFrame(l1024_max_data).T.to_excel(writer, sheet_name='l1024-max')
        pd.DataFrame(s128_max_avg).T.to_excel(writer, sheet_name='s128-avg')
        pd.DataFrame(l1024_max_avg).T.to_excel(writer, sheet_name='l1024-avg')


if __name__ == "__main__":
    # devices and models
    devices = ["magicleap", "vivo", "quest3"]
    models = [
        "llama-2-7b-chat.Q2_K.gguf", "llama-2-7b-chat.Q3_K_S.gguf",
        "Mistral-7B-Instruct-v0.3.IQ1_M.gguf", "Mistral-7B-Instruct-v0.3.IQ2_XS.gguf",
        "Mistral-7B-Instruct-v0.3.IQ3_XS.gguf", "Mistral-7B-Instruct-v0.3.IQ4_XS.gguf",
        "Phi-3.1-mini-4k-instruct-Q2_K.gguf", "Phi-3.1-mini-4k-instruct-Q3_K_L.gguf",
        "Phi-3.1-mini-4k-instruct-Q4_K_L.gguf", "Phi-3.1-mini-4k-instruct-Q5_K_L.gguf",
        "Phi-3.1-mini-4k-instruct-Q6_K.gguf", "Phi-3.1-mini-4k-instruct-Q8_0.gguf",
        "qwen2-0_5b-instruct-fp16.gguf",
        "Vikhr-Gemma-2B-instruct-Q3_K_M.gguf", "Vikhr-Gemma-2B-instruct-Q4_0.gguf",
        "Vikhr-Gemma-2B-instruct-Q5_0.gguf", "Vikhr-Gemma-2B-instruct-Q6_K.gguf"
    ]

    # process raw txt files
    generate_excel_for_memory_usage(devices, models)
