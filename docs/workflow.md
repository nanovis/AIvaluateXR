# 📈 AIvaluateXR Workflow

**AIvaluateXR** operates in **three steps**, supporting reproducible performance benchmarking and comparative analysis of LLMs on XR platforms.

---

## ⚙️ Step 1: Test Suite Execution

**Purpose:**  
Run multiple benchmarking tests for each model–device pair.

**Tests included:**
- Prompt Processing (PP) Speed
- Token Generation (TG) Speed
- Battery Consumption (BT)
- Total Throughput (TT)
- Others as configured

**Output:**  
Each test generates its own raw CSV file.

---

## ⚙️ Step 2: Metrics Consolidation

**Purpose:**  
Combine all test outputs into a unified dataset.

**How it works:**  
Use the provided merge script to aggregate and align results:

```bash
python scripts/merge_metrics.py \
  --inputs metrics_pp.csv metrics_tg.csv metrics_bt.csv metrics_tt.csv \
  --output metrics.csv
```

---

## ⚙️ Step 3: Pareto Front Analysis

**Purpose:**  
Identify the most effective model–device pairs across all performance criteria.

**How it works:**  
Run the Pareto analysis module:

```bash
python scripts/pareto.py \
  --input metrics.csv \
  --output pareto_front.csv
```

**Output:**  
A `pareto_front.csv` file highlighting configurations that offer optimal trade-offs.

---

## ✅ Example Workflow

**Step 1 – Run benchmarks:**

```bash
python scripts/benchmark.py --model Mistral-7B --device MagicLeap2 --test PP
python scripts/benchmark.py --model Mistral-7B --device MagicLeap2 --test TG
python scripts/benchmark.py --model Mistral-7B --device MagicLeap2 --test BT
python scripts/benchmark.py --model Mistral-7B --device MagicLeap2 --test TT
```

**Step 2 – Merge results:**

```bash
python scripts/merge_metrics.py \
  --inputs metrics_pp.csv metrics_tg.csv metrics_bt.csv metrics_tt.csv \
  --output metrics.csv
```

**Step 3 – Perform Pareto analysis:**

```bash
python scripts/pareto.py \
  --input metrics.csv \
  --output pareto_front.csv
```

---

## 🖼️ Workflow Diagram

```
+----------------------------+
|   Step 1: Benchmarking     |
| Run tests on XR devices    |
+-------------+--------------+
              |
              v
+----------------------------+
|  Step 2: Metrics Merge     |
| Combine all CSV outputs    |
+-------------+--------------+
              |
              v
+----------------------------+
| Step 3: Pareto Analysis    |
| Identify optimal configs   |
+----------------------------+
```

---

## 📂 Project Directory Structure

Below is the recommended directory layout for **AIvaluateXR**:

```
AIvaluateXR/
├── docs/
│   └── workflow.md               # Workflow documentation
├── scripts/
│   ├── benchmark.py              # Runs benchmarking tests and generates CSVs
│   ├── merge_metrics.py          # Merges test outputs into a single CSV
│   └── pareto.py                 # Performs Pareto front analysis
├── models/                       # (Optional) Pretrained model files
│   └── ...
├── results/                      # (Optional) Output CSVs and analysis results
│   └── ...
├── README.md                     # Project overview and instructions
├── requirements.txt              # Python dependencies
└── ...
```

---

## 📘 Additional Resources

- [LoXR README](../README.md)
- [Llama.cpp Repository](https://github.com/ggerganov/llama.cpp)
- [LoXR Paper (arXiv)](https://arxiv.org/abs/2025.xxxxx)

---

If you encounter any issues or have suggestions, please open an issue or pull request on GitHub.

Enjoy exploring the capabilities of on-device LLMs in XR!
