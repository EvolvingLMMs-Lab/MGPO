# High-Resolution Visual Reasoning via Multi-Turn Grounding-Based Reinforcement Learning

[![MGPO](https://img.shields.io/badge/Blog-MGPO-blue)](https://www.notion.so/High-Resolution-Visual-Reasoning-via-Multi-Turn-Grounding-Based-Reinforcement-Learning-1ee5d3508b4b80e9ba2effa4f7598512?pvs=4)

<!-- Authors: [Xinyu Huang](https://xinyu1205.github.io/), [Yuhao Dong](https://scholar.google.com/citations?user=kMui170AAAAJ&hl=zh-CN), Wei Li, Jinming Wu, Zihao Deng, [Bo Li](https://brianboli.com/), Zejun Ma -->


## Introduction

Inspired by the human visual system's top-down, task-driven search, we propose **Multi-turn Grounding-based Policy Optimization (MGPO)**. MGPO equips LMMs with interpretable, iterative visual grounding: the model predicts key regions, crops sub-images, and reasons over both the original and focused views.

**Key advantages:**
- **Interpretable, Top-down Visual Reasoning:** MGPO highlights which image regions are attended to at each step.
- **Breaks Pixel Limits:** Even if the full image is blurry due to resizing, MGPO identifies and crops clear sub-images for further analysis.
- **No Extra Grounding Annotations Needed:** MGPO is trained only with binary answer correctness, yet learns robust grounding.


---

## Experiments

### Visualizations

<p align="center">
 <table class="tg">
  <tr>
    <td class="tg-c3ow"><img src="images/visualizations.pdf" align="center" width="800" ></td>
  </tr>
</table>
  <p align="center">(Examples of models trained with multi-turn grounding-based RL on high-resolution realworld tasks. The model first identifies key regions, which are then automatically cropped and returned as sub-images. Notably, despite only a binary reward function derived from the correctness of the final answer, the model gradually emerge robust grounding capability throughout the RL process.)</p>
</p>


### Main Results

- **MGPO outperforms both SFT and GRPO** on high-resolution tasks.
- **+5.4%** on MME-Realworld (ID), **+5.2%** on V* Bench (OOD) over GRPO baseline.
- Surpasses OpenAI’s o1 and GPT-4o on V* Bench, despite using a smaller model and less data.

<p align="center">
 <table class="tg">
  <tr>
    <td class="tg-c3ow"><img src="images/visualizations.pdf" align="center" width="800" ></td>
  </tr>
</table>
  <p align="center">(Examples of models trained with multi-turn grounding-based RL on high-resolution realworld tasks. The model first identifies key regions, which are then automatically cropped and returned as sub-images. Notably, despite only a binary reward function derived from the correctness of the final answer, the model gradually emerge robust grounding capability throughout the RL process.)</p>
</p>


## Training Code
Code will be made public within one week.

