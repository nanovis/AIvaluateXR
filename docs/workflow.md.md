---

## 📈 Overview

**AIvaluateXR** works in two steps:

1. A **benchmarking module** that generates detailed performance metrics in tabular (CSV) form.
2. A **Pareto analysis module** that identifies the most effective model–device configurations.

This two-step process enables reproducible evaluation and comparison of LLMs across different XR platforms.

---

## ⚙️ Module 1: Results Generation

**Purpose:**  
Collect raw performance data for each model–device pair.

**How it works:**  
This module executes a suite of benchmarking tests on your XR device. It measures:

- Prompt processing speed (tokens per second)
- Token generation speed
- Memory consumption
- Battery consumption
- Error counts and consistency metrics

**Output:**  
A CSV file containing all recorded metrics.

**Example command:**

```bash
python scripts/benchmark.py --model Mistral-7B --device MagicLeap2 --output metrics.csv
