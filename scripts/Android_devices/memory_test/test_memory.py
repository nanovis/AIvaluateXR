import subprocess
from time import sleep
import os

# set serial number
MAGICLEAP = "GA62XT01M"
VIVO = ""
QUEST3 = ""
# set output path
base_path = r"C:\User\results\memory_test"

def execute_commands(loop_command, number_of_runs, output_file, number, log_dir):
    # run command "top"
    if "qwen2-0_5b-instruct-fp16.gguf" in loop_command:
        mem_command = f"adb -s {number} shell \"top -b -d 0.5 | grep 'llama-cli -m' > {output_file}\""
    else:
        mem_command = f"adb -s {number} shell \"top -b | grep 'llama-cli -m' > {output_file}\""
    print(f"recording memory: {mem_command}")

    # use subprocess.Popen to start top command, and keep it running
    top_process = subprocess.Popen(mem_command, shell=True)

    # another cmd to run llama.cpp
    for i in range(number_of_runs):
        sleep(10)

        subprocess.run(loop_command, shell=True)
        print(f"***************************TIMES: {i + 1} ****************************")

    # end top cmd
    if top_process.poll() is None:
        print("end top and grep process")
        kill_command = f"adb -s {number} shell \"pkill top\""
        subprocess.run(kill_command, shell=True)
    if top_process.poll() is None:
        print("end top and CMD")
        top_process.terminate()
        top_process.wait()

    # pull reslut to PC
    push_command = fr"adb -s {number} pull {output_file} {log_dir}"
    print(f"recorded memory test pull to: {log_dir}")
    subprocess.run(push_command, shell=True)


def delete(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"{output_file} deleted")
    else:
        print(f"{output_file} doesn't exist")


def test(device, number, model):
    # cli-short_prompt-n128
    output0 = f"/sdcard/{model}-s128.txt"
    time0 = 3
    command0 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-cli -m /data/local/tmp/models/{model} \
            -p 'Three advice on keeping healthy:' \
            -n 128\""


    # cli-long_prompt-n512
    output1 = f"/sdcard/{model}-l1024.txt"
    time1 = 3
    command1 = f"adb -s {number} shell \"cd /data/local/tmp/adb-cpu/mcpu-cortex-x1/bin && export LD_LIBRARY_PATH=/data/local/tmp/adb-cpu/mcpu-cortex-x1/lib:$LD_LIBRARY_PATH && ./llama-cli -m /data/local/tmp/models/{model} \
            -p 'Plan a 7-day itinerary for two people traveling from Austria to KAUST (King Abdullah University of Science and Technology) with a budget of 10,000 euros. The itinerary should include details on accommodations, meals, and activities for each day. One person in the group has a seafood allergy, so please ensure that meal recommendations are safe and suitable for them. The plan should be practical, well-balanced, and ready to use.' \
            -n 1024\""

    log_dir = fr"{base_path}\{device}\{model}"

    execute_commands(command0, time0, output0, number, log_dir)
    sleep(60 * 2)
    execute_commands(command1, time1, output1, number, log_dir)



if __name__ == "__main__":
    # test("magic leap", MAGICLEAP, "qwen2-0_5b-instruct-fp16.gguf")
    # test("vivo", VIVO, "qwen2-0_5b-instruct-fp16.gguf")

    test("quest3", QUEST3, "qwen2-0_5b-instruct-fp16.gguf")
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

