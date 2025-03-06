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




## A. Diagram 1: High-Level Algorithm 5 (Query-Universally Optimal)

```mermaid
---
title: "High-Level Algorithm 5 - Query-Universally Optimal"
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

*   **Changes**: Added a `Key Concepts` section to define the notations. Also, the `Input` section is created.


----


## B. Diagram 2: Algorithm 6 (SSSP Tree Construction)

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

*   **Changes**: Created 4 sections for better visual presentation.

---


## C. Diagram 3: Algorithm 7 (Multiedge Deduplication)

```mermaid
---
title: "Algorithm 7 - Multiedge Deduplication"
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

---

## D. Diagram 4: Algorithm 8 (Dynamic Programming on Tree)

```mermaid
---
title: "Algorithm 8 - Dynamic Programming on Tree"
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


## E. Data Structure: Fibonacci-like priority queue with the working set property

```mermaid
---
title: "Data Structure: Fibonacci-like priority queue with the working set property"
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

---

## F. Equations related to DeleteMin

```mermaid
---
title: "Equations related to DeleteMin"
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
graph LR
    A["DeleteMin Operation"] --> B{"Time Complexity"}
    style A fill:#3cf2,stroke:#000,stroke-width:1px, color:black;
    B --> C["O(1 + log |W<sub>x</sub>|)"]
    C --> D["Working Set<br>(W<sub>x</sub>)"]
    D --> E["Elements inserted after x and still present"]
    B --> F["Amortized time complexity"]
    B --> G["Applies to Fibonacci-like priority queue with working set property"]
    
```




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---