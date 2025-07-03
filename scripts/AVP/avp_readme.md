# 📘 Apple Vision Pro Benchmarking Instructions

This document provides guidance for running **AIvaluateXR** benchmarking tests on Apple Vision Pro.

---

## 🛠️ Prerequisites

✅ Make sure you have:
- Updated **Llama.cpp** to the latest build compatible with AVP.
- Installed all necessary dependencies.

---

## ⚙️ Test Configuration

Below are the instructions for configuring each test:

---

### 1️⃣ Prompt Processing (PP) Test

**Purpose:** Measure prompt processing performance at different prompt sizes.

✅ **Settings:**
- **PP values:**  
  `32, 64, 128, 512, 1024`
- **TG value:**  
  Fixed to `64`

> **Example Command:**
> ```bash
> ./main -m ./models/your_model.gguf --pp 32 --tg 64
> ```

---

### 2️⃣ Token Generation (TG) Test

**Purpose:** Measure token generation throughput.

✅ **Settings:**
- **TG values:**  
  `32, 64, 128, 512, 1024`
- **PP value:**  
  Fixed to `64`

> **Example Command:**
> ```bash
> ./main -m ./models/your_model.gguf --pp 64 --tg 128
> ```

---

### 3️⃣ Battery Consumption (BT) Test

**Purpose:** Evaluate battery drain under load.

✅ **Settings:**
- **Batch sizes:**  
  Use any of the batch values you want to test.

> **Example Command:**
> ```bash
> ./main -m ./models/your_model.gguf --batch 8
> ```

---

### 4️⃣ Total Throughput (TT) Test

**Purpose:** Measure overall throughput with different threading configurations.

✅ **Settings:**
- **Threads:**  
  Specify the thread counts you want to test.

> **Example Command:**
> ```bash
> ./main -m ./models/your_model.gguf --threads 4
> ```

---

## 📝 Notes

- Adjust `--pp`, `--tg`, `--batch`, and `--threads` as needed for each test run.
- Save the output CSVs after each test.
- Proceed to merge and Pareto analysis as described in the [Workflow Guide](../../docs/workflow.md).

---

✅ **Questions or issues?**  
Open an issue in the repository or contact the maintainers.
