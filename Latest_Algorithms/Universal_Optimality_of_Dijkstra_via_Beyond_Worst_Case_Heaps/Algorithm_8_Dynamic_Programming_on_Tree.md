---
created: 2025-02-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/2311.11793"
---



# Universal Optimality of Dijkstra via Beyond-Worst-Case Heaps
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## Algorithm 8 - Dynamic Programming on Tree



```mermaid
---
title: "Algorithm 8 - Dynamic Programming on Tree"
config:
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    "graph": { "htmlLabels": false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    A["Input:<br> Tree T, root r, distances d"]:::yellowCircle --> B{"L = [] (Partial Linearization)"}
    B --> C{"For each child u<sub>i</sub> of r"}
    C --> D["Recursively call DP(T(u<sub>i</sub>), u<sub>i</sub>, d)"]:::greenCircle
    D --> E["L = MergeSortedLists(L, DP(T(u<sub>i</sub>)))"]
    E --> F{"Use distances d for comparisons"}
    C -- All children processed --> G["L = [r] + L  <br>(Add root to the front)"]:::blueCircle
    G --> H["Output:<br> Linearization L"]:::orangeCircle


style A fill:#f9f3,stroke:#000,stroke-width:1px
style D fill:#9f63,stroke:#000,stroke-width:1px
style E fill:#3cf3,stroke:#000,stroke-width:1px, color:black
style G fill:#3cf3,stroke:#000,stroke-width:1px, color:black
style H fill:#f263,stroke:#000,stroke-width:1px


```

----


### Explanation and Element Types

*   **Yellow Circle (A):** The `Input` to the algorithm. Represents the initial data:
    *   `Tree T`: The shortest path tree we want to linearize.
    *   `root r`: The root node of the tree.
    *   `distances d`: The distances from the source to each node, used for comparisons.
*   **Blue Circle (B, E, G):** Represents operations on lists (data structures)
    *   `B`: The list L.
    *   `E`: Merge Sorted List.
    *   `G`: Add the root node to the list L.
*   **Green Circle (D):** Represents the recursive call to the `DP` algorithm itself. This is a key processing step.
*   **Orange Circle (H):** The final `Output`: the linearized ordering of the tree's nodes.

----

### Key improvements in this version

*   **Data Flow:** It shows more clearly how the partial linearizations are built up at each step.
*   **Focus on Element Types:** Aligns with the requested structure by indicating what each node represents (input, processing, output, data structure).






---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---