🦙🌲🤏 Guanaco-LoRA: Low-Rank LLaMA Instruct-Tuning
---------------------------------------------------

*   This is a fork of the [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) repo, where I have created my own language model dataset using Stack Overflow data (90% of JavaScript), parsed with some scripts.
*   **Disclaimer:** This is my first data and I'm still a beginner. I'm not sure about the quality of the dataset, but I'll keep improving it. I'm open to constructive criticism and welcome pro pull requests.

*   Objects: 39,670
*   Total Tokens: 42.63M (TODO: double-check this)
*   Average Tokens per Object: 1,074.67

### Setup

1.  Clone or download the repository from [here](https://github.com/Valdex/guanaco-lora).
2.  Install dependencies with:

```
pip install -r requirements.txt
```

### Inference (`generate.py`)

This file reads the model weights from the Hugging Face model hub and runs a Gradio interface for inference on a specified input. Users should treat this as example code for the use of the model and modify it as needed.

### Training (`finetune.py`)

This file contains a straightforward application of the low-rank adaptation (LoRA) method to the LLaMA model. It fine-tunes the model on the custom dataset using Hugging Face's [PEFT](https://github.com/huggingface/peft) and Tim Dettmers' [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) to enable cheap and efficient fine-tuning.

Near the top of this file is a set of hardcoded hyperparameters that you can feel free to modify.

### Checkpoint export (`export_*_checkpoint.py`)

These files contain scripts that export the model weights to Hugging Face format and to PyTorch `state_dicts`. They should help users who want to run inference in their projects.

### Credits

The original repository was created by [tloen](https://github.com/tloen), and the results were reproduced using low-rank adaptation (LoRA), as described in the paper [Low-Rank Adaptation of Large Language Models: Non-Asymptotic Analysis and Practical Algorithms](https://arxiv.org/pdf/2106.09685.pdf).

### Acknowledgements

*   This is a fork of the [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) repo, which provides code for reproducing the original results using low-rank adaptation (LoRA).
*   I used data from Stack Overflow (90% of JavaScript) to create my custom dataset.
*   The training code is adapted from the original Alpaca repo, with modifications to use my custom dataset.