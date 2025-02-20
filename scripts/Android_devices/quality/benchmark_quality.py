import os
import argparse
import subprocess
from time import sleep

# Define the dataset paths for each benchmark test
DEFAULT_DATA_PATHS = {
    'hellaswag': r'hellaswag_val_full.txt',
    'mmlu': r'mmlu-validation.bin',
    'arc_challenge': r'arc-challenge-validation.bin',
    'truthful-qa': r'truthful-qa-validation.bin',
    'winogrande': r'winogrande-debiased-eval.csv',
    'wikitext':r'wiki.test.raw',
    'output': os.path.join(os.getcwd(), 'benchmark_results')
}

# Define the command templates for each benchmark test
COMMAND_TEMPLATES = {
    'hellaswag': '--hellaswag -ngl 99 -m "{model}" -f "{data_path}" --temp 1',
    'mmlu': '--multiple-choice -bf "{data_path}" -ngl 99 -m "{model}"',
    'arc_challenge': '--multiple-choice -bf "{data_path}" -ngl 99 -m "{model}"',
    'truthful-qa': '--multiple-choice -bf "{data_path}" -ngl 99 -m "{model}"',
    'winogrande': '--winogrande -f "{data_path}" -ngl 99 -m "{model}"',
    'wikitext':'-f "{data_path}" -ngl 99 -m "{model}"'
}


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run llama-perplexity benchmark tests, only for the specified model.")
    parser.add_argument("--model", required=True, help="Path to the model file")
    parser.add_argument("--llama-perplexity", required=True, help="Path to the llama-perplexity binary")
    parser.add_argument("--output-dir", default=DEFAULT_DATA_PATHS['output'], help="Directory to save results")

    # Enable switches for each test (default is off)
    for test in COMMAND_TEMPLATES.keys():
        parser.add_argument(f"--{test}", action="store_true", help=f"Enable the {test} benchmark test")

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Get the script's directory and set the dataset file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(script_dir, "datasets")  # path to the 'data' folder
    os.makedirs(dataset_dir, exist_ok=True)

    # Iterate through each benchmark test and execute based on whether it is enabled
    for test, command_template in COMMAND_TEMPLATES.items():
        if getattr(args, test, False):  # If the test is enabled
            # Get the dataset file path
            data_path = os.path.join(dataset_dir, DEFAULT_DATA_PATHS[test])
            if not os.path.exists(data_path):
                print(f"Error: Dataset file {data_path} does not exist. Please verify the file path.")
                continue

            # Set the output file path
            test_result_dir = os.path.join(args.output_dir, f"{test}")
            os.makedirs(test_result_dir, exist_ok=True)
            output_file = os.path.join(test_result_dir, f"{os.path.basename(args.model)}.txt")

            # Format the command
            command = f'"{args.llama_perplexity}" ' + command_template.format(model=args.model, data_path=data_path)

            print(f"Running {test} benchmark test for model {args.model}, using dataset: {data_path}")

            # Execute the command and capture output
            with open(output_file, 'w', encoding='utf-8', errors='replace') as f_out:
                for i in range(5):
                    print(f"Iteration {i + 1}...")

                    # Run the command
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    f_out.write(f"Iteration {i + 1}:\n")
                    f_out.write(result.stdout + "\n")

                    # If there is any error output, write it to the file
                    if result.stderr:
                        f_out.write(f"Iteration {i + 1} error:\n{result.stderr}\n")


    print("All enabled tests have been successfully executed.")


# Execute the main function
if __name__ == "__main__":
    main()
