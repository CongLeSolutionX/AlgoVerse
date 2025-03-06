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


## Algorithm 7 - Multiedge Deduplication



```mermaid
---
title: "Algorithm 7 - Multiedge Deduplication"
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
graph LR
    A["Input:<br> Multigraph G, edge weights w"]:::yellowCircle --> B{"Initialize G' and w' as empty"}
    B --> C{"For all u, v ∈ V(G) such that an edge from u to v exists in G"}
    C --> D{"Add edge e = uv to G'"}
    D --> E["w'(e) = Compute min(w(ei)) <br>(e<sub>i</sub>∈E(G), start(e<sub>i</sub>) = u, end(e<sub>i</sub>) = v)"]
    C --> F["Next pair of vertices u,v"]
    F --> C
    E --> F
    F --> G["Output:<br> Simple Graph G', weights w'"]:::orangeCircle
    
    style A fill:#f9f3,stroke:#000,stroke-width:1px
    style G fill:#f632,stroke:#000,stroke-width:1px
    
```

----


### Explanation and breakdown of the changes

1.  **Input and Output:**
    *   Input: `Multigraph G`, `edge weights w` (marked as yellow input).
    *   Output: `Simple Graph G'`, `weights w'` (marked as orange output).
2.  **Initialization:**
    *   `Initialize G' and w' as empty`: Clear starting state.
3.  **Main Loop:**
    *   `For all u, v ∈ V(G) such that an edge from u to v exists in G`: Iterates through all possible vertex pairs in the input multigraph. The condition ensures we only process pairs connected by at least one edge.
4.  **Edge Addition:**
    *   `Add edge e = uv to G'`: Add an edge between `u` and `v` in the simple graph `G'`.
5.  **Weight Computation:**
    *   `w'(e) = Compute min(w(ei)) (ei∈E(G), start(ei) = u, end(ei) = v)`: This step computes the weight of the edge `e` in the simple graph `G'`. It finds the minimum weight among all edges in the multigraph `G` that connect `u` to `v`.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---