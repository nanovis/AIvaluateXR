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
For each device you have to run the benchmarking scripts and get results in CSV. After this you have to merge the results and give them to the Pareto analysis module.

## 🛠️ **Benchmarking on Android XR Devices**  
For Magic Leap 2, Meta Quest 3 and Vivo X100 Pro, see the [Andriod Instructions](scripts/Android_devices/android_readme.md).

## 🛠️ **Benchmarking on Apple Vision Pro**  
For AVP see [Apple Vision Pro Instructions](scripts/avp/avp_readme.md).

**Step 2 – Merge results:**

```bash
python scripts/merge_metrics.py \
  --inputs metrics_pp.csv metrics_tg.csv metrics_bt.csv metrics_tt.csv \
  --output metrics.csv


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
│   └── workflow.md
├── images/
│   └── (images for documentation)
├── scripts/
│   ├── Android_devices/
│   │   ├── battery_test/
│   │   ├── memory_test/
│   │   ├── speed_and_consistency_test/
│   │   └── android_readme.md     # ✅ Shows how to use LLMs on ML2, MQ3, and Vivoo X100 Pro 
│   │
│   ├── AVP/
│   │   ├── battery_test/
│   │   ├── memory_test/
│   │   ├── speed_and_consistency_test/
│   │   └── avp_readme.md         # ✅ hows how to use LLMs on AVP 
│   │
│   ├── quality/
│   │   └── datasets/
│   │
│   ├── merge_metrics.py
│   └── pareto.py
│
├── README.md
└── requirements.txt              # 

```

---

## 📘 Additional Resources

- [LoXR README](../README.md)
- [Llama.cpp Repository](https://github.com/ggerganov/llama.cpp)
- [Paper (arXiv)](https://arxiv.org/abs/2502.15761)
- [Paper (IEEE VR Poster)](https://ieeexplore.ieee.org/abstract/document/10973004)
- [Project Website](https://www.nanovis.org/Loxr.html)

---

If you encounter any issues or have suggestions, please open an issue or pull request on GitHub.

Enjoy exploring the capabilities of on-device LLMs in XR!
