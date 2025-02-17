import subprocess
import os

prompt = 'Plan a 7-day itinerary for two people traveling from Austria to KAUST (King Abdullah University of Science and Technology) with a budget of 10,000 euros. The itinerary should include details on accommodations, meals, and activities for each day. One person in the group has a seafood allergy, so please ensure that meal recommendations are safe and suitable for them. The plan should be practical, well-balanced, and ready to use.' \


def create_folder(device, model):
    folder_path = f"/Users/xinyu/Documents/chatterbox/battery/{device}/{model}"

    # check if folder exists
    if not os.path.exists(folder_path):
        # 如果目录不存在，则创建目录
        os.makedirs(folder_path)
        print(f"Folder {folder_path} created.")
    else:
        print(f"Folder {folder_path} exists.")

def execute_commands(loop_command, number_of_runs, output_file):
    # run a python terminal
    process = subprocess.Popen(
        ["python", "-i"],  # 启动 Python 交互式终端
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors='replace'
    )

    with open(output_file, 'a', encoding='utf-8', errors='replace') as file:

        for i in range(number_of_runs):
            result = subprocess.run(loop_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors='replace')

            # print result
            print(result.stdout)
            print(result.stderr)

            # write output to the file
            if result.stdout is not None:
                file.write(result.stdout)
            else:
                print("No output captured.")
            file.write(result.stderr)
            file.write(f"***************************TIMES: {i + 1} ****************************\n")

def delete(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"{output_file} deleted")
    else:
        print(f"{output_file} doesn't exist")



def test(device, number, model, stop_event):
    output1 = f"/Users/xinyu/Documents/chatterbox/battery/{device}/{model}/cli-long_prompt-n1024.txt"
    time1 = 1
    command1 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-cli -m /data/local/tmp/models/{model} \
                -p {prompt} \
                -n 1024\""

    create_folder(device, model)

    while True:
        if stop_event.is_set():
            print(f'finish {model}')
            break
        execute_commands(command1, time1, output1)





