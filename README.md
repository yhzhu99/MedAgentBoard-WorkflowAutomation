# MedAgentBoard-WorkflowAutomation

This repository contains the official implementation and benchmark resources for **Task 4: Clinical Workflow Automation** of the paper "Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks" (currently under review).

## Project Overview
We present a systematic approach to:
1. Generate clinically-relevant analytical tasks using structured prompt engineering
2. Evaluate various LLM-based frameworks (Single LLM, SmolAgents, OpenManus, Owl) 
3. Conduct human evaluation with domain experts

The benchmark covers four key clinical analytical categories:
1. Data Extraction & Statistical Analysis
2. Predictive Modeling
3. Data Visualization
4. Report Generation

## Key Features
- **Structured Task Generation**: Utilizes dataset-specific prompts with real EHR examples

- **Multi-Framework Support**: Implements and tests 4 different problem-solving approaches

- **Comprehensive Evaluation**: Independent and standardized evaluation by multiple experts

## Related Multi-Agent Frameworks and Baselines
This benchmark evaluates three multi-agent frameworks:

- SmolAgents
(https://github.com/huggingface/smolagents)  

- OpenManus 
(https://github.com/FoundationAgents/OpenManus)  

- Owl (https://github.com/camel-ai/owl)

*Note: These links point to the original framework implementations. Our clinical task adaptations are contained in the respective subdirectories under `inference/`.*

## Associated Repositories

- [MedAgentBoard](https://github.com/yhzhu99/MedAgentBoard): Contains the complete code for the project.
- [MedAgentBoard-playground](https://github.com/yhzhu99/MedAgentBoard-playground): Contains the complete code for the project website.


## Repository Structure
```
.
├── task100.json # Generated benchmark tasks (100 tasks)
├── generate/
│  ├── generate.py # Task generation script
│  └── prompt.py # Prompt templates for task construction
│
├── inference/ # Implementation of different frameworks
│  ├── openmanus/ # OpenManus framework implementation
│  ├── owl/ # Owl framework implementation
│  ├── single_llm/ # Single LLM baseline
│  └── smolagents/ # SmolAgents implementation
│
├── results/
│  └── Single_LLM_code.json # Generated code from Single LLM baseline
│
├── evaluation/
│  ├── Chinese_version/ # Chinese evaluation results
│  │   ├── Evaluator_A/
│  │   ├── Evaluator_B/
│  │   ├── Evaluator_C/
│  │   └── Merged.json
│  │
│  └── English_version/ # English evaluation results
│      ├── Evaluator_A/
│      ├── Evaluator_B/
│      ├── Evaluator_C/
│      └── Merged.json
│
└── (Additional model outputs available in GitHub Releases)
```

## Getting Started

### Requirements
- Python 3.10 or higher

## Reproducing Task Generation
1. Navigate to `generate/` directory:
```bash
cd generate/
```
2. Run:
```bash
python generate.py
```

## Running Framework Inference
For OpenManus/SmolAgents/Owl frameworks, you need to clone their respective code and configure environments first. Refer to each framework's documentation for setup requirements.

Each framework directory contains specific instructions:

```bash
# Example for Owl baseline
cd inference/owl
python generate.py
```

## Evaluation Results
Complete evaluation results are available in:

- `evaluation/` directory containing:
  - **Chinese Version** (`Chinese_version/`)
  - **English Version** (`English_version/`)

  Each contain individual evaluations from 3 annotators (A, B, C) and merged consensus results (`Merged.json`)

- GitHub Releases(`Results`) for full model outputs:
  - result_deepseek_tjh.zip (DeepSeek-V3 results)
  - result_qwen_tjh.zip (Qwen-Max results)

## Citation
If you use this work in your research, please cite our paper:

```bibtex
@article{zhu2025medagentboard,
  title={{MedAgentBoard}: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks},
  author={Zhu, Yinghao and He, Ziyi and Hu, Haoran and Zheng, Xiaochen and Zhang, Xichen and Wang, Zixiang and Gao, Junyi and Ma, Liantao and Yu, Lequan},
  journal={arXiv preprint arXiv:2505.12371},
  year={2025}
}
```

