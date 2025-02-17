import subprocess
from time import sleep
import os

MAGICLEAP="GA62XT0100BM"
VIVO="10AE6J27L4000L3"
QUEST3="2G0YC5ZFB709C6"
def create_folder(device, model):
    folder_path = f"/Users/xinyu/Documents/chatterbox/speed/{device}/{model}"

    # make sure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"folder {folder_path} created")
    else:
        print(f"folder {folder_path} exists")

def execute_commands(loop_command, number_of_runs, output_file):
    # run a python terminal
    process = subprocess.Popen(
        ["python", "-i"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors='replace'
    )

    with open(output_file, 'a', encoding='utf-8', errors='replace') as file:
        for i in range(number_of_runs):
            # wait
            sleep(60)   # sleep time of every test
            print("waited")

            result = subprocess.run(loop_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors='replace')

            # print result
            print(result.stdout)
            print(result.stderr)

            # write output to file
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



def test(device, number, model):
    # consistency-short_prompt-n128
    output0 = f"C:\\Users\\Xinyu\\Desktop\\adb-cpu\\results\\{device}\\{model}\\cli-short_prompt-n128.txt"
    time0 = 20  # count for test
    command0 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-cli -m /data/local/tmp/models/{model} \
                -p 'Three advice on keeping healthy:' \
                -n 128\""

    # consistency-long_prompt-n512
    output1 = f"C:\\Users\\Xinyu\\Desktop\\adb-cpu\\results\\{device}\\{model}\\cli-long_prompt-n512.txt"
    time1 = 20  # count for test
    command1 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-cli -m /data/local/tmp/models/{model} \
                -p 'Plan a 7-day itinerary for two people traveling from Austria to KAUST (King Abdullah University of Science and Technology) with a budget of 10,000 euros. The itinerary should include details on accommodations, meals, and activities for each day. One person in the group has a seafood allergy, so please ensure that meal recommendations are safe and suitable for them. The plan should be practical, well-balanced, and ready to use.' \
                -n 512\""

    # bench-pp
    output2 = f"C:\\Users\\Xinyu\\Desktop\\adb-cpu\\results\\{device}\\{model}\\bench-pp.txt"
    time2 = 1  # llama-bench for once is to do the test for 5 times
    command2 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-bench -m /data/local/tmp/models/{model}  -n 0 -p 64,128,256,512,1024 -o json\""

    # bench-tg
    output3 = f"C:\\Users\\Xinyu\\Desktop\\adb-cpu\\results\\{device}\\{model}\\bench-tg.txt"
    time3 = 1
    command3 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-bench -m /data/local/tmp/models/{model} -p 0 -n 64,128,256,512,1024 -o json\""

    # bench-batch sizes
    output4 = f"/Users/xinyu/Documents/chatterbox/speed/new-BT-on-{device}/{model}/bench-batch.txt"
    create_folder(device, model)
    time4 = 1
    command4 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-bench -m /data/local/tmp/models/{model} -n 0 -p 64 -b 128,256,512,1024 -o json\""

    # bench-threads
    output5 = f"C:\\Users\\Xinyu\\Desktop\\adb-cpu\\results\\{device}\\{model}\\bench-threads.txt"
    time5 = 1
    command5 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-bench -m /data/local/tmp/models/{model} -n 0 -n 16 -p 64 -t 1,2,4,8,16,32 -o json\""

    delete(output0)
    delete(output1)
    delete(output2)
    delete(output3)
    delete(output4)
    delete(output5)
    execute_commands(command0, time0, output0)
    sleep(60 * 10)  # 10 min, for cooling down
    execute_commands(command1, time1, output1)
    sleep(60 * 10)
    execute_commands(command2, time2, output2)
    sleep(60 * 10)
    execute_commands(command3, time3, output3)
    sleep(60 * 10)
    execute_commands(command4, time4, output4)
    sleep(60 * 10)
    execute_commands(command5, time5, output5)

if __name__ == "__main__":
    # test("ml2", MAGICLEAP, "Meta-Llama-3.1-8B-Instruct-IQ2_M.gguf")
    # test("vivo", VIVO, "Meta-Llama-3.1-8B-Instruct-IQ2_M.gguf")
    test("quest3", QUEST3, "Meta-Llama-3.1-8B-Instruct-IQ2_M.gguf")
    test("quest3", QUEST3, "Mistral-7B-Instruct-v0.3.Q3_K_S.gguf")
    test("quest3", QUEST3, "llama-2-7b-chat.Q2_K.gguf")
    test("quest3", QUEST3, "llama-2-7b-chat.Q3_K_S.gguf")
    test("quest3", QUEST3, "Vikhr-Gemma-2B-instruct-Q3_K_M.gguf")
    test("quest3", QUEST3, "Vikhr-Gemma-2B-instruct-Q4_0.gguf")
    test("quest3", QUEST3, "Vikhr-Gemma-2B-instruct-Q5_0.gguf")
    test("quest3", QUEST3, "Vikhr-Gemma-2B-instruct-Q6_K.gguf")
    test("quest3", QUEST3, "Mistral-7B-Instruct-v0.3.IQ1_M.gguf")
    test("quest3", QUEST3, "Mistral-7B-Instruct-v0.3.IQ2_XS.gguf")
    test("quest3", QUEST3, "Mistral-7B-Instruct-v0.3.IQ3_XS.gguf")
    test("quest3", QUEST3, "Mistral-7B-Instruct-v0.3.IQ4_XS.gguf")
    test("quest3", QUEST3, "Phi-3.1-mini-4k-instruct-Q2_K.gguf")
    test("quest3", QUEST3, "Phi-3.1-mini-4k-instruct-Q3_K_L.gguf")
    test("quest3", QUEST3, "Phi-3.1-mini-4k-instruct-Q4_K_L.gguf")
    test("quest3", QUEST3, "Phi-3.1-mini-4k-instruct-Q5_K_L.gguf")
    test("quest3", QUEST3, "Phi-3.1-mini-4k-instruct-Q6_K.gguf")
    test("quest3", QUEST3, "Phi-3.1-mini-4k-instruct-Q8_0.gguf")
    test("quest3", QUEST3, "qwen2-0_5b-instruct-fp16.gguf")




