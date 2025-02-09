---
created: 2025-02-09 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Task: Execute the Collective Monte Carlo Tree Search (CoMCTS) Algorithm for Reasoning - Structured Instruction Framework
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---

**Role:** You are an AI agent tasked with executing the Collective Monte Carlo Tree Search (CoMCTS) algorithm to find the most promising reasoning path for answering a given multimodal question.

**Input:**

1. **Policy Models:** You have access to the policy models of [Number] Multimodal Large Language Models (MLLMs): $\{\pi_1, \pi_2, ..., \pi_K\}$, where K = [Number]. Assume you can query these models for generating and evaluating reasoning steps.
2. **Multimodal Question:** A multimodal question $Q = (I, T)$, where:
    *   $I$: [Specify the nature of the input, e.g., an image, a set of images, etc.] - Example: "an image of a cat".
    *   $T$: [Specify the text task instruction] - Example: "What color is the cat?".

**Algorithm: Collective Monte Carlo Tree Search (CoMCTS)**

The CoMCTS algorithm proceeds in rounds, performing the following steps iteratively:

**For each round:**

**Step 1: Expansion**

*   **Condition:** If the current node in the search tree is a leaf node (not a terminal node), perform expansion.
*   **Action:**
    *   Given the current leaf node $s_m$ (the node selected for expansion), prompt each of the K MLLMs in parallel to generate candidate reasoning steps.
    *   Use a prompting strategy suitable for your capabilities. Assume you can provide the current state and request the next logical reasoning step.
    *   Gather the candidate reasoning steps from each MLLM: $\mathcal{S}_{\text{candidate}}^k$ from model $\pi_k$.
    *   Combine these candidate sets into a single set: $\mathcal{S}_{\text{candidate}} = \bigcup_{k=1}^{K} \mathcal{S}_{\text{candidate}}^k$.

**Step 2: Simulation and Error Positioning**

*   **Action:** Evaluate each candidate reasoning node $s' \in \mathcal{S}_{\text{candidate}}$ using the collective knowledge of the K MLLMs.
*   **Scoring:** Calculate the score for each candidate node $s'$ using the following function:
    $$
    r(s') = \frac{1}{K} \sum_{k=1}^{K} I(\text{prompt}_{\text{eval}}, Q, \text{Parent}(s'), s')
    $$
    *   Here, $I(\cdot)$ is an indicator function. Assume you can prompt each MLLM to evaluate the validity of the reasoning step $s'$ given the question $Q$ and the parent reasoning step. A value of 1 indicates the step is considered valid by the MLLM, and 0 otherwise.
    *   $\text{Parent}(s')$ refers to the preceding reasoning node before $s'$.
*   **Thresholding:** Apply a threshold $\tau$ [Specify the value or method for determining $\tau$]. Filter out any candidate reasoning nodes $s'$ where $r(s') < \tau$. These are considered potentially erroneous.

**Step 3: Backpropagation**

*   **Action:** Update the statistics of the nodes in the search tree, from the newly expanded parts back to the root node.
*   **Updates:** For each node $s$ along the reasoning path:
    *   Update the number of visits $N(s)$:
        $$
        N(s) \leftarrow N(s) + \sum_{s' \in \text{Children}(s)} N(s')
        $$
    *   Update the value $V(s)$:
        $$
        V(s) \leftarrow V(s) + r(S_{\text{best}})
        $$
        *   $r(S_{\text{best}})$ is the reward obtained from the best reasoning path through the children of $s$. Assume you can determine a reward based on the perceived progress towards answering the question or the correctness of the final answer.

**Step 4: Selection**

*   **Action:** Select the next node to explore further in the next round.
*   **UCB Calculation:** Calculate the Upper Confidence Bound (UCB) value for each valid candidate node $s'$ in $\mathcal{S}_{\text{candidate}}$:
    $$
    \text{UCB}(s') = V(s') + c \cdot \sqrt{\frac{\log N(s)}{N(s')}}
    $$
    *   $c$ is the exploration constant. Use $c = $[Specify the value].
    *   $N(s)$ is the number of times the parent of $s'$ has been visited.
    *   $N(s')$ is the number of times node $s'$ has been visited.
*   **Next Node Selection:** Choose the candidate node with the highest UCB value as the starting node $s_m$ for the next round:

$$
s_m = \underset{s' \in \mathcal{S}_{\text{candidate}}}{\arg \max} \left( V(s') + c \cdot \sqrt{\frac{\log N(s)}{N(s')}} \right)
$$


**Reflective Reasoning (Optional, if applicable to the task):**

*   **Identifying Negative Siblings:** If instructed to perform reflective reasoning, after identifying an effective reasoning step $s_m$, identify the negative sibling node $s_{\text{neg}}$:
$$
s_{\text{neg}} = \arg \max_{s_{\text{sibling}} \in \text{Sibling}(s_m)} \text{UCB}(s_{\text{sibling}})
$$
*   **Constructing Reflective Reasoning Path:** Create a reflective reasoning node $y_{\text{reflect}}$:
    $$
    y_{\text{reflect}} = \text{Replace}(Y, \{s_{\text{neg}}, \text{prompt}_{\text{reflect}}\}, s_m)
    $$
    *   Assume you have a mechanism to implement the $\text{Replace}$ operation, which conceptually involves correcting a previous reasoning step based on the identified negative example.

**Termination:**

*   Continue the CoMCTS rounds for a fixed number of iterations [Specify the number of iterations] or until a satisfactory reasoning path leading to an answer is found.

**Output:**

*   The most promising reasoning path found by the CoMCTS algorithm, presented as a sequence of reasoning steps. Clearly indicate the final answer derived from this path, if applicable.

**Constraints and Parameters:**

*   Number of MLLMs (K): [Specify the number]
*   Threshold ($\tau$): [Specify the value or method]
*   Exploration Constant (c): [Specify the value]
*   Maximum number of CoMCTS rounds: [Specify the number]
*   [Add any other relevant constraints or parameters, e.g., maximum depth of the search tree].

**Example Multimodal Question for Demonstration:**

*   $I$: [Provide an example image or description of the image]
*   $T$: [Provide the text instruction related to the image]

**Begin!**  Execute the CoMCTS algorithm as described above for the given multimodal question.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---