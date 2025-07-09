import subprocess
from time import sleep
import os

# device serial number
MAGICLEAP=""
VIVO=""
QUEST3=""

# set output dir
output_dir = "/Users/Consistency_&_Speed"

# set path to llama.cpp binary/library/model files on device
bin_dir = "/data/local/tmp/adb-cpu/mcpu-cortex-x1/bin"
lib_dir = "/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib"
model_dir = "/data/local/tmp/adb-cpu/model"

# switch of tests
TEST_CONS = True
TEST_PP = True
TEST_TG = True
TEST_BT = True
TEST_TT = True

def create_folder(device, model):
    folder_path = os.path.join(output_dir, device, model)
    print(folder_path)
    # make sure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"folder {folder_path} created")
    else:
        print(f"folder {folder_path} exists")
    return folder_path

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
    # create folder for TXT results
    output_path = create_folder(device, model)

    # consistency-short_prompt-n128
    output0 = os.path.join(output_path, "cli-short_prompt-n128.txt")
    time0 = 20  # count for test
    command0 = f"adb -s {number} shell \"cd {bin_dir} && export LD_LIBRARY_PATH={lib_dir}:$LD_LIBRARY_PATH && ./llama-cli -m {model_dir}/{model} \
                -p 'Three advice on keeping healthy:' \
                -n 128\""

    # consistency-long_prompt-n512
    output1 = os.path.join(output_path, "cli-long_prompt-n512.txt")
    time1 = 20  # count for test
    command1 = f"adb -s {number} shell \"cd {bin_dir} && export LD_LIBRARY_PATH={lib_dir}:$LD_LIBRARY_PATH && ./llama-cli -m {model_dir}/{model} \
                -p 'Plan a 7-day itinerary for two people traveling from Austria to KAUST (King Abdullah University of Science and Technology) with a budget of 10,000 euros. The itinerary should include details on accommodations, meals, and activities for each day. One person in the group has a seafood allergy, so please ensure that meal recommendations are safe and suitable for them. The plan should be practical, well-balanced, and ready to use.' \
                -n 512\""

    # bench-pp
    output2 = os.path.join(output_path, "bench-pp.txt")
    time2 = 1  # llama-bench for once is to do the test for 5 times
    command2 = f"adb -s {number} shell \"cd {bin_dir} && export LD_LIBRARY_PATH={lib_dir}:$LD_LIBRARY_PATH && ./llama-bench -m {model_dir}/{model}  -n 0 -p 64,128,256,512,1024 -o json\""

    # bench-tg
    output3 = os.path.join(output_path, "bench-tg.txt")
    time3 = 1
    command3 = f"adb -s {number} shell \"cd {bin_dir} && export LD_LIBRARY_PATH={lib_dir}:$LD_LIBRARY_PATH && ./llama-bench -m {model_dir}/{model} -p 0 -n 64,128,256,512,1024 -o json\""

    # bench-batch size
    output4 = os.path.join(output_path, "bench-batch.txt")
    time4 = 1
    command4 = f"adb -s {number} shell \"cd {bin_dir} && export LD_LIBRARY_PATH={lib_dir}:$LD_LIBRARY_PATH && ./llama-bench -m {model_dir}/{model} -n 0 -p 64 -b 128,256,512,1024 -o json\""

    # bench-threads
    output5 = os.path.join(output_path, "bench-threads.txt")
    time5 = 1
    command5 = f"adb -s {number} shell \"cd {bin_dir} && export LD_LIBRARY_PATH={lib_dir}:$LD_LIBRARY_PATH && ./llama-bench -m {model_dir}/{model} -n 0 -n 16 -p 64 -t 1,2,4,8,16,32 -o json\""

    if TEST_CONS:
        delete(output0)
        execute_commands(command0, time0, output0)
        sleep(60 * 10)  # 10 min, for cooling down
        delete(output1)
        execute_commands(command1, time1, output1)
        sleep(60 * 10)

    if TEST_PP:
        delete(output2)
        execute_commands(command2, time2, output2)
        sleep(60 * 10)

    if TEST_TG:
        delete(output3)
        execute_commands(command3, time3, output3)
        sleep(60 * 10)

    if TEST_BT:
        delete(output4)
        execute_commands(command4, time4, output4)
        sleep(60 * 10)


    if TEST_TT:
        delete(output5)
        execute_commands(command5, time5, output5)
        sleep(60 * 10)

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
