---
created: 2025-02-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/2311.11793"
---



# End-to-End Algorithm Flow and Data Transformation
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


The diagram below captures the core end-to-end flow and major data transformations described in the original algorithm.


```mermaid
---
title: "End-to-End Algorithm Flow and Data Transformation"
config:
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    "graph": {"htmlLabels": false, 'curve': 'natural'},
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
    subgraph Input["Input:<br> G(V,E), w, s"]
    style Input fill:#f9f3,stroke:#000,stroke-width:1px
        A["G(V,E), w, s"]:::yellowCircle
    end

    A --> B{"Contract Graph?"}
    B -- No --> C["Compute Dominator Tree T<sub>D</sub>"]
    C --> D["Drop edges against dominance"]
    D --> E{"Any outdegree-1 node?"}
    E -- Yes --> F["Contract Edge"]
    F --> E
    E -- No --> G["Deduplicate Edges<br>(Alg 7)"]
    G --> H["Compute T'<sub>G',w'</sub><sup>SSSP</sup> <br>(Dijkstra)"]
    
    H --> Aux
    H --> I["Uncontract T'<sub>G',w'</sub><sup>SSSP</sup>"]
    I --> J["T<sub>G,w</sub><sup>SSSP</sup>"]
    B -- Yes --> J
    
    Aux((Fibonacci-like Queue)):::queue
    
    J --> K["DP on T<sub>G,w</sub><sup>SSSP</sup> <br>(Alg 8)"]
    K --> L["Linearization L"]:::orangeCircle

    subgraph Outputs
    style Outputs fill:#fff3,stroke:#000,stroke-width:1px
        L:::orangeCircle
    end

    subgraph Key_Processes["Key Processes"]
    style Key_Processes fill:#aff3,stroke:#333,stroke-width:1px
        C --> C1[Dominator Tree Computation]
        E --> E1[Check if every node in G is reachable from s]
        G --> G1[Remove the parallel edges]
        H --> H1[Applying Dijkstra algorithm and priority queue operations]
        I --> I1[Find the shorest path in the graph]
        K --> K1[Building the final tree]
    end
  
    
classDef yellowCircle fill:#f9f3,stroke:#000,stroke-width:1px;
classDef orangeCircle fill:#f633,stroke:#000,stroke-width:1px;
classDef queue fill:#ff22,stroke:#333,stroke-width:1px

style B fill:#ccf3,stroke:#333,stroke-width:1px
style C fill:#ccf3,stroke:#333,stroke-width:1px
style D fill:#ccf3,stroke:#333,stroke-width:1px
style E fill:#ccf3,stroke:#333,stroke-width:1px
style F fill:#ccf3,stroke:#333,stroke-width:1px
style G fill:#ccf3,stroke:#333,stroke-width:1px
style H fill:#ccf3,stroke:#333,stroke-width:1px
style I fill:#ccf3,stroke:#333,stroke-width:1px
style K fill:#ccf3,stroke:#333,stroke-width:1px

```

---


## Key Elements

*   **Input:** The initial graph G, weights w, and source s.
*   **Decision:** "Contract Graph?" reflects the Algorithm 5 high-level control flow.
*   **Contraction Steps:** The Dominator Tree computation, edge dropping, and edge contraction steps mirror Algorithm 6.
*   **Deduplication:** Algorithm 7 is represented as a single "Deduplicate Edges" step.
*   **Dijkstra's Algorithm:**  Algorithm 6 culminates in running Dijkstra's, creating T'<sub>G',w'</sub><sup>SSSP</sup>
*    **Data Flow:** There are steps for Dominator Tree Computation, checking if every node is reachable from s, etc.
*   **Outputs:** Linearization L (Orange).
*   **Fibonacci-like Queue:** The queue is represented as a database shape.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---