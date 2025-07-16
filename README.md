# **AIvaluateXR: An Evaluation Framework for on-Device AI in XR with Benchmarking Results**  
![Teaser](images/LoXR.jpg)

## 🏆 **Acknowledgment**
AIvaluateXR is built upon **[`llama.cpp`](https://github.com/ggml-org/llama.cpp)**.  [`llama.cpp`](https://github.com/ggml-org/llama.cpp) is an excellent C++ implementation for running LLMs efficiently on various hardware. 
We deployed **LLMs** locally on **XR devices** by customizing the **[`llama.cpp`](https://github.com/ggml-org/llama.cpp)** for four different XR devices. 

## 🚀 **Overview**  

**AIvaluateXR** is a framework for deploying and benchmarking **Large Language Models (LLMs) on XR devices**. It enables **on-device execution** of LLMs and provides tools for **performance analysis** across different XR platforms including:  

-  **Apple Vision Pro**  
-  **Magic Leap 2**  
- **Vivo X100 Pro**  
-  **Meta Quest 3**  

---


## 🎥 **LoXR Video Demo**
[AIvaluateXR Video](https://youtu.be/7TrXLekrEyI)  
 ---

## 🔥 Script for the the Key Tests, including:  

✅ **Prompt Processing Test** – Measures the efficiency of input processing.  
✅ **Token Generation Test** – Evaluates LLM inference speed in tokens per second.  
✅ **Batch Test & Thread Test** – Analyzes the impact of batch sizes and thread configurations.  
✅ **Battery & Memory Consumption Analysis** – Tracks resource utilization on XR devices.  

---





## 🛠️ **Installation**  

Clone the repository and install dependencies:

```bash
git clone https://github.com/nanovis/AIvaluateXR.git
cd AIvaluateXR


#pareto analysis
python scripts/pareto.py --csv metrics.csv
```


## 🛠️ **How to use it**  
For detailed workflow instructions, see [Workflow Documentation](docs/workflow.md).




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
- [Llama.cpp Repository](https://github.com/ggerganov/llama.cpp)
- [Paper (arXiv)](https://arxiv.org/abs/2502.15761)
- [Paper (IEEE VR Poster)](https://ieeexplore.ieee.org/abstract/document/10973004)
- [Project Website](https://www.nanovis.org/AIvaluateXR.html)


## Publications

  Dawar Khan, Xinyu Liu, Omar Mena, Donggang Jia, Alexandre Kouyoumdjian, Ivan Viola,
"LoXR: Performance Evaluation of Locally Executing LLMs on XR Devices",
arXiv preprint, 2025.

If you find our work useful, please consider citing our paper:
```bibtex


@article{LoXR2025ArXiv,
  title        = {LoXR: Performance Evaluation of Locally Executing LLMs on XR Devices},
  author       = {Khan, Dawar and Liu, Xinyu and Mena, Omar and Jia, Donggang and Kouyoumdjian, Alexandre and Viola, Ivan},
  year         = 2025,
  journal      = {arxiv.org preprint },
}

@INPROCEEDINGS{LoXR:2025IEEVR,
  author={Liu, Xinyu and Khan, Dawar and Mena, Omar and Jia, Donggang and Kouyoumdjian, Alexandre and Viola, Ivan},
  booktitle={2025 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW)}, 
  title={LLMs on XR (LoXR): Performance Evaluation of LLMs Executed Locally on Extended Reality Devices}, 
  year={2025},
  volume={},
  number={},
  pages={1212-1213}, 
  doi={10.1109/VRW66409.2025.00252}}

