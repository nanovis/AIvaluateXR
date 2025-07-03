import os
import subprocess
from time import sleep
from battery import test
import threading


DEVICE_ADDR = '192.168.1.49:7777' # set the addr of the device

models_num = [1,2,5,6,11,12,13,17]  # models for test

# set the device
device_name = 'magic leap'
device_addr = DEVICE_ADDR


# set the command (choose one)
command = f"adb -s {DEVICE_ADDR} shell dumpsys battery | findstr /R /C:\"level\"" # for Windows
# command = f"adb -s {DEVICE_ADDR} shell dumpsys battery | grep \"level\""          # for Mac

# set the output file path
output_dir = r"C:\Users\adb-cpu\results\Battery\magic leap"

# set count of test
test_num = 3

# set interval
time_sleep = 60 * 5 # 5 min
# duration: time_sleep * (test_num - 1)





model_aliases = {
    "qwen2-0_5b-instruct-fp16.gguf": "m1", "Vikhr-Gemma-2B-instruct-Q3_K_M.gguf": "m2",
    "Vikhr-Gemma-2B-instruct-Q4_0.gguf": "m3", "Vikhr-Gemma-2B-instruct-Q5_0.gguf": "m4",
    "Vikhr-Gemma-2B-instruct-Q6_K.gguf": "m5", "Phi-3.1-mini-4k-instruct-Q2_K.gguf": "m6",
    "Phi-3.1-mini-4k-instruct-Q3_K_L.gguf": "m7", "Phi-3.1-mini-4k-instruct-Q4_K_L.gguf": "m8",
    "Phi-3.1-mini-4k-instruct-Q5_K_L.gguf": "m9", "Phi-3.1-mini-4k-instruct-Q6_K.gguf": "m10",
    "Phi-3.1-mini-4k-instruct-Q8_0.gguf": "m11", "llama-2-7b-chat.Q2_K.gguf": "m12",
    "llama-2-7b-chat.Q3_K_S.gguf": "m13", "Mistral-7B-Instruct-v0.3.IQ1_M.gguf": "m14",
    "Mistral-7B-Instruct-v0.3.IQ2_XS.gguf": "m15", "Mistral-7B-Instruct-v0.3.IQ3_XS.gguf": "m16",
    "Mistral-7B-Instruct-v0.3.IQ4_XS.gguf": "m17"
}

reverse_model_aliases = {value: key for key, value in model_aliases.items()}

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def delete(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"{output_file} deleted")
    else:
        print(f"{output_file} doesn't exist")


def run_battery_check(check_command):
    try:
        result = subprocess.run(check_command, shell=True, capture_output=True, text=True)

        # write output to file
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(result.stdout)
            print(result)
            if result.stderr:
                f.write("\n[Error Output]\n")
                f.write(result.stderr)

        print(f"output saved to: {output_file}")
    except Exception as e:
        print(f"error: {e}")



def run_battery_checks(command, stop_event):
    for _ in range(test_num):
        run_battery_check(command)
        sleep(time_sleep)
    stop_event.set()

for model_num in models_num:
    model_id = f'm{model_num}'
    output_file = os.path.join(output_dir, f"{model_id}.txt")
    delete(output_file)
    model = reverse_model_aliases.get(model_id)
    stop_event = threading.Event()

    # start test process
    test_thread = threading.Thread(target=test, args=(f'{device_name}', f'{device_port}', model, stop_event))
    test_thread.start()

    run_battery_checks(command, stop_event)

    # wait for the test process to finish
    test_thread.join()


