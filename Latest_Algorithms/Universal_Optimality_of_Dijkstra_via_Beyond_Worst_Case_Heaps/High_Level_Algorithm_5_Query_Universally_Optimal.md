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


## High-Level Algorithm 5 - Query-Universally Optimal




```mermaid
---
title: "The High-Level Algorithm 5 - Query-Universally Optimal"
config:
  layout: elk
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
    subgraph Input
    A["Input:<br> G(V, E), w(E → R<sup>+</sup>), s ∈ V"]:::yellowCircle
    style A fill:#f9f3,stroke:#000,stroke-width:1px
    direction LR
    end
    
    subgraph Algorithm_Flow["Algorithm Flow"]
        B{"Is G Contracted?"}
        style B fill:#ccf33,stroke:#333,stroke-width:1px
        B -- No --> C["Algorithm 6:<br> SSSP Tree Construction"]
        C --> D["T<sub>G,w</sub><sup>SSSP</sup>"]
        B -- Yes --> E["Algorithm 8:<br> Dynamic Programming on T"]
        D --> E
        E --> F["Linearization L"]:::orangeCircle
        style F fill:#f633,stroke:#000,stroke-width:1px
    
    end
    
    subgraph Key_Concepts["Key Concepts"]
    style Key_Concepts fill:#a2a3,stroke:#333,stroke-width:1px
        AA["G(V,E):<br> Graph with vertices V and edges E"]
        AB["w(E → R<sup>+</sup>):<br> Edge weight function<br>(positive reals)"]
        AC["s ∈ V:<br> Source vertex"]
        AD["T<sub>G,w</sub><sup>SSSP</sup>:<br> Shortest Path Tree of G w.r.t. w"]
        AE["Linearization L:<br> Total order of V by distance from s"]
        AF["Algorithm 6 Goal:<br> Construct T<sub>G,w</sub><sup>SSSP</sup> with OPT(Q) queries"]
        AG["Algorithm 8 Goal:<br> Compute L from T<sub>G,w</sub><sup>SSSP</sup> efficiently"]
    end
    
    A --> B
    B --> AF
    B --> AG
    
```

---

### Explanation

*   **Nodes:**
    *   `A`: The starting point, representing the input to the algorithm (Graph G, weights w, source node s). I've added the common notation for what these represent (V, E, R+, etc.)
    *   `B`: Represents the decision point: Has the graph been contracted? This highlights that the algorithm may need to perform contractions before finding the shortest-path tree.
    *   `C`: Represents Algorithm 6, which constructs the shortest-path tree T<sub>G,w</sub><sup>SSSP</sup>.
    *   `D`: Represents the output of Algorithm 6, the shortest-path tree T<sub>G,w</sub><sup>SSSP</sup>.
    *   `E`: Represents Algorithm 8, which performs dynamic programming on the tree to compute the linearization.
    *   `F`: The final output – the linearization L.
*   **Arrows:** The arrows indicate the flow of the algorithm.
*    **Subgraphs** to have clear visualization for what algorithm it is.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---