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


## Algorithm 6 - SSSP Tree Construction



```mermaid
---
title: "Algorithm 6 - SSSP Tree Construction"
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
    subgraph Inputs_and_Outputs["Inputs and Outputs"]
    style Inputs_and_Outputs fill:#f0f3,stroke:#333,stroke-width:1px

        A["Input:<br> G(V,E), w, s"]:::yellowCircle --> B{"Compute Dominator Tree T<sub>D</sub>"}
        I["Output:<br> T<sub>G,w</sub><sup>SSSP</sup>"]:::orangeCircle

        style A fill:#f9f3,stroke:#000,stroke-width:1px
        style I fill:#f635,stroke:#000,stroke-width:1px
    end

    subgraph Core_Algorithm["Core Algorithm"]
    style Core_Algorithm fill:#afa3,stroke:#333,stroke-width:1px
        
        B --> C["Drop edges against dominance<br>(uv where v dominates u)"]
        C --> D{"Any node in T<sub>D</sub> with outdegree 1?"}
        D -- Yes --> E["v = the (only) child of u;<br> Contract edge uv in G and T<sub>D</sub>"]
        E --> D
        D -- No --> F["Compute G', w' <br>(Deduplication Algorithm 7)"]
        F --> G["Compute T'<sub>G',w'</sub><sup>SSSP</sup> using Dijkstra's Algorithm"]
        G --> H["Uncontract T'<sub>G',w'</sub><sup>SSSP</sup> to get T<sub>G,w</sub><sup>SSSP</sup>"]
        H --> I
    end

    subgraph Data_Transformations["Data Transformations"]
        style Data_Transformations fill:#ccf3,stroke:#333,stroke-width:1px
        E --> EB["Edge Contraction"]
        EB --> EE1["Combines u and v into [uv]"]
        EE1 --> EE2["Updates edge weights accordingly"]
        F --> FB["Deduplication"]
        FB --> FF1["Removes parallel edges"]
        FF1 --> FF2["Selects minimum weight edge if multiple exist"]
    end

    subgraph Guarantees["Guarantees and Properties"]
        style Guarantees fill:#a2f3,stroke:#333,stroke-width:1px
        G --> GA["T'<sub>G',w'</sub><sup>SSSP</sup> is correct"]
        H --> HA["T<sub>G,w</sub><sup>SSSP</sup> is the correct shortest-path tree for G"]
        F --> FA["Algorithm 7 ensures G' is a simple graph"]
    end
    
```

----

### Key Points & Legend Breakdown

*   **Legend Adherence:**
    *   `Input`:  Yellow Circle
    *   `Output`: Orange Circle
    *   Operations and processes use standard node styles.
*   **Data Flow:**  The diagram clearly illustrates the sequential steps of the algorithm.
*   **Modularity:**  The subgraphs organize the steps into logical blocks (Inputs/Outputs, Core Algorithm, Data Transformations, Guarantees).




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---