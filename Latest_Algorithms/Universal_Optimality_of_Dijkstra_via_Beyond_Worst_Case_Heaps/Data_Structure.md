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


## Data Structure: Fibonacci-like priority queue with the working set property


The diagram below emphasizes the relationships between the Fibonacci-like heaps, auxiliary data structures, and the key invariants that guarantee the working set property. The use of different shapes and colors helps visually distinguish the different components.



```mermaid
---
title: "CHANGE_ME_DADDY"
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
    subgraph Heap_Collection["Heap Collection H"]
    style Heap_Collection fill:#3cf3,stroke:#333,stroke-width:1px, color:black
        
        H0[H0 - Rank 0]:::greenCircle --> Aux((Auxiliary Data Structures))
        H1[H1 - Rank 1]:::greenCircle --> Aux
        H2[H2 - Rank 2]:::greenCircle --> Aux
        H3["H3 - Rank r"]:::greenCircle --> Aux
        HR["HR - Rank R"]:::greenCircle --> Aux
    end
    
    subgraph Auxilliary_Data_Structures["Auxiliary Data Structures"]
    style Auxilliary_Data_Structures fill:#9f64,stroke:#333,stroke-width:1px
        Aux --> M["M: Minimum Keeping Array"]
        Aux --> U["U: Interval Data Structure"]
        M --> M_Ops{"Get(i), Decrease(i,x), ChangePrefix(P), FindMin(), Pop()"}
        U --> U_Ops{"Set(a,b,x), Delete(a,b), Get(a,b), Find(t), Prev(t), Next(t)"}
        
        classDef Operation fill:#c22,stroke:#333,stroke-width:1px;
        class M_Ops,U_Ops Operation
    end

    
    subgraph Invariants
        I1["|Hr| ≤ 2^(2r)"]
        I2["R >= 2 => |HR| + |HR-1| >= 2^(2(R-1))"]
        I3["H0 ≻ H1 ≻ ... ≻ HR"]
        I4["U maintains intervals for Heap insertions"]
        %% Invariants --> I1 & I2 & I3 & I4
        style Invariants fill:#a2af,stroke:#333,stroke-width:1px
    end
    
    H0 --> Invariants
    H1 --> Invariants
    H2 --> Invariants
    H3 --> Invariants
    HR --> Invariants

    subgraph Operations
        Insert(x) --> Promotion{Promotion Steps};
        DecreaseKey(x,v) --> Update["Update Key"]
        DeleteMin["DeleteMin()"] --> ExtractMin["ExtractMin"]
    end
    
    subgraph Promotion_Steps["Promotion Steps"]
    style Promotion_Steps fill:#ccf2,stroke:#333,stroke-width:1px
        Promotion --> PS1["C-1 = {(x,t(x))}"]
        Promotion --> PS2["For r = 0, 1, ... : Cr = PromotionStep(r, Cr-1)"]
    end
    
classDef greenCircle fill:#9f62,stroke:#000,stroke-width:1px

```

----

### Key Points & Explanation

*   **`Heap Collection H`**: This is the core, representing the collection of Fibonacci heaps of varying ranks. Each heap (`H0`, `H1`, `H2`, etc.) stores elements with their insertion times.
*   **`Auxiliary Data Structures`**: This is critical. It shows how the Minimum Keeping Array (`M`) and Interval Data Structure (`U`) are *external* to the heaps themselves but essential for efficient operation. The type of operation is listed under each block.
*   **`Invariants`**: These are *crucial* to understanding the data structure.  They maintain the structure of the heap collection, its size properties, and the ordering of elements.
*   **`Operations`**:  This shows the primary operations and their interaction with the rest of the structure.
*    **Promotion Steps:** It shows that for each operation, it need to go through promotion steps.





---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---