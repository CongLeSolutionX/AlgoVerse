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


I will translate the algorithmic steps and data structure relationships of the Dijkstra algorithm with the working set property into Mermaid diagrams.

Here's a breakdown of the diagrams:

----


## 1. High-Level Algorithm 5 - Query-Universally Optimal

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
    A[Input:<br> G, w, s]:::yellowCircle --> B{"Is graph contracted?"}
    style A fill:#f9f3,stroke:#000,stroke-width:1px
    B -- No --> C["Algorithm 6:<br> SSSP Tree Construction"]
    C --> D["T<sub>G,w</sub><sup>SSSP</sup>"]
    B -- Yes --> E["Algorithm 8:<br> Dynamic Programming on Tree"]
    D --> E
    E --> F["Linearization L"]:::orangeCircle
    style F fill:#f633,stroke:#000,stroke-width:1px
    
```

**Explanation:**

* `A`: The starting point, the input to the query-universally optimal algorithm.
* `B`: Main algorithm (query-universally optimal).
* `C`: SSSP tree construction, as a subroutine of the main algorithm.
* `D`: Linearization of the graph is done.


-----

## 2. Algorithm 6 - SSSP Tree Construction

```mermaid
---
title: "Algorithm 6 - SSSP Tree Construction"
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
    A["Input:<br> G, w, s"]:::yellowCircle --> B{"Compute Dominator Tree T"}
    
    B --> C["Drop edges against dominance"]
    C --> D{"Any node with outdegree 1?"}
    D -- Yes --> E["Contract edge uv"]
    E --> D
    D -- No --> F["Compute G', w' <br>(Deduplication Algorithm 7)"]
    F --> G["Compute SSSP Tree T' using Dijkstra"]
    G --> H["Uncontract T' to get T<sub>G,w</sub><sup>SSSP</sup>"]
    H --> I["T<sub>G,w</sub><sup>SSSP</sup>"]:::orangeCircle

style A fill:#f9f2,stroke:#000,stroke-width:1px
style I fill:#f633,stroke:#000,stroke-width:1px

```

**Explanation:**

* `A`: Input graph, edge weights, and source node.
* `B`: Core part of the SSSP construction.
* `C`: Perform the construction of the tree.
* `D`: Output SSSP tree of the original graph.

-----


## 3. Algorithm 7 - Multiedge Deduplication

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
graph TD
    A["Input:<br> Multigraph G, edge weights w"]:::yellowCircle --> B{"Initialize G', w' as empty"}
     style A fill:#f9f3,stroke:#000,stroke-width:1px;
    B --> C{"For all vertices u,v in G:<br>  Is there an edge from u to v?"}
    C -- Yes --> D["Add edge e=uv to G'"]
    D --> E["w'(e) = min(w(e<sub>i</sub>))<br>(e<sub>i</sub> is an edge from u to v)"]
    C -- No --> F["Next pair of vertices"]
    F --> C
    E --> F
    F --> G["Output:<br> Simple Graph G', weights w'"]:::orangeCircle

style G fill:#f635,stroke:#000,stroke-width:1px
     
```

**Explanation:**

* `A`: Input multigraph.
* `B`: Set to create the graph for the next algorithm.
* `C`: Create the graph.
* `D`: Final simple graph with proper weight assignment.

-----


## 4. Algorithm 8 - Dynamic Programming on Tree

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
graph LR
    A["Input:<br>Tree T, root r, distances d"]:::yellowCircle --> B{"L = []"}

    B --> C{"For each child u<sub>i</sub> of r"}
    C --> D["Recursively call DP(T(u<sub>i</sub>), u<sub>i</sub>, d)"]
    D --> E["L = MergeSortedLists(L, DP(T(u<sub>i</sub>)))"]
    C --> E
    C -- All children processed --> F["L = [r] + L"]
    F --> G["Output:<br>Linearization L"]:::orangeCircle

style A fill:#f9f3,stroke:#000,stroke-width:1px
style G fill:#f633,stroke:#000,stroke-width:1px

```

**Explanation:**

* `A`: A rooted tree is the input
* `B`: Initialize and go through every child node.
* `C`: Dynamic programming for the final output.

----


## 5. Data Structure: Fibonacci-like priority queue with the working set property

```mermaid
---
title: "Data Structure: Fibonacci-like priority queue with the working set property"
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
    A["Fibonacci-like priority queue"] --> B{"Has the working set property?"}
    B --> C["Interval Maintenance<br>(Theorem A.1)"]
    C --> D["Minimum-keeping<br>(Theorem A.2)"]
    B --> E["Insert:<br>O(1)"]
    B --> F["DeleteMin:<br>O(1 + log|W<sub>x</sub>|)"]
    B --> G["FindMin:<br>O(1)"]
    B --> H["DecreaseKey:<br>O(1)"]
    style A fill:#3c35,stroke:#000,stroke-width:1px, color:black
```

**Explanation:**

* auxiliary data structure

----


## 6. Equations related to DeleteMin

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
    A["Working set of an element x"] --> B("Wx,t = { [ℓy, ry] ∈ I | ℓx ≤ ℓy ≤ t ≤ ry }")
    A --> C["Wx = Wx,t∗ for arbitrary t∗ = arg max(t∈x) |Wx,t|"]
    B --> D["Cost(DeleteMin) = O(1 + log |Wx|)"]

style A fill:#3cf5,stroke:#000,stroke-width:1px, color:black
```

**Explanation:**

* This digram shows the relationship between the working set and DeleteMin


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---