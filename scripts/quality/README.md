# Quality Benchmark
We used [perplexity](https://github.com/ggml-org/llama.cpp/tree/master/examples/perplexity) of Llama.cpp to test the quality of LLMs. We tested the **MMLU**, **Hellaswag**, **Winogrande**, **Arc-Challenge**, **wikitext** and **Truthful-QA**. Each test iterated 5 times. Here are all the [datasets](https://github.com/nanovis/LoXR/tree/main/scripts/Android_devices/quality/datasets).

Since the quality of LLMs doesn't vary from the devices where they are deployed, the quality benchmarks can be done on any device, preferably on the host PC for faster performance. Therefore, you will need to compile **llama.cpp for to your host PC** by following instructins [here](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md).
## Usage
You can reproduce our experiment by following these steps:
### 1. Run `python benchmark_quality.py -h` for usage help.
```
usage: benchmark.py [-h] --model MODEL --llama-perplexity LLAMA_PERPLEXITY [--output-dir OUTPUT_DIR] [--hellaswag] [--mmlu] [--arc_challenge] [--truthful-qa] [--winogrande]
                    [--wikitext]

Run llama-perplexity benchmark tests.

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL         Path to the model file
  --llama-perplexity LLAMA_PERPLEXITY
                        Path to the llama-perplexity binary
  --output-dir OUTPUT_DIR
                        Directory to save results
  --hellaswag           Enable the hellaswag benchmark test
  --mmlu                Enable the mmlu benchmark test
  --arc_challenge       Enable the arc_challenge benchmark test
  --truthful-qa         Enable the truthful-qa benchmark test
  --winogrande          Enable the winogrande benchmark test
  --wikitext            Enable the wikitext benchmark test

Example:
python benchmark_quality.py \
--model "path\to\model.gguf" \
--llama-perplexity "path\to\bin\llama-perplexity" \
--mmlu --hellaswag 
```
### 2. Conduct one test
You can do one test at a time by following the command below, for example **Hellaswag**:
```
python benchmark_quality.py \
--model "path\to\model.gguf" \
--llama-perplexity "path\to\bin\llama-perplexity" \
--hellaswag
```
### 3. Conduct multiple tests
You can also run multiple tests at a time, and set the output dir.
```
python benchmark_quality.py \
--model "path\to\model.gguf" \
--llama-perplexity "path\to\bin\llama-perplexity" \
--mmlu --hellaswag --arc_challenge \
--output-dir "path\to\output_folder"
```
