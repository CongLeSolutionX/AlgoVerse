---
created: 2025-03-12 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://www.packtpub.com/en-us/product/python-data-structures-and-algorithms-9781786467355"
---



# Algorithm Design Paradigms
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## A Diagrammatic Guide 



Here's an expanded Mermaid diagram detailing the "Algorithm Design Paradigms," drawing heavily from the original document and elaborating on each paradigm with related concepts:

```mermaid
---
title: "Python Data Structures and Algorithms"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    "graph": { "htmlLabels": false, 'curve': 'linear' },
    'themeVariables': {
        'fontFamily': 'Comic Sans MS',
        'fontSize': '20px',
        'primaryColor': '#ffff',
        'primaryTextColor': '#55ff',
        'primaryBorderColor': '#7c2',
        'lineColor': '#F8B229',
        'secondaryColor': '#006100',
        'tertiaryColor': '#fff'
    }
  }
}%%
graph LR
    subgraph Algorithm_Design_Paradigms["Algorithm Design Paradigms"]
    style Algorithm_Design_Paradigms fill:#cfa3,stroke:#333,stroke-width:1px
        A["Divide & Conquer"] --> A1{"Problem Decomposition"}
        A1 --> A2["Recursion"]
        A1 --> A3["Smaller Subproblems"]
        A --> A4{"Key Concepts"}
        A4 --> A5["Base Case"]
        A4 --> A6["Recursive Step"]
        A4 --> A7["Merge Solutions"]
        A --> A8{"Examples"}
        A8 --> A9["Merge Sort"]
        A8 --> A10["Quick Sort"]
        A8 --> A11["Binary Search"]
        A8 --> A12["Strassen's Matrix Multiplication"]

        B["Dynamic Programming"] --> B1{"Overlapping Subproblems"}
        B1 --> B2["Memoization"]
        B1 --> B3["Tabulation"]
        B --> B4{"Key Concepts"}
        B4 --> B5["Optimal Substructure"]
        B4 --> B6["Overlapping Subproblems"]
        B4 --> B7["Bottom-Up Approach"]
        B --> B8{"Examples"}
        B8 --> B9["Fibonacci Sequence"]
        B8 --> B10["Knapsack Problem"]
        B8 --> B11["Shortest Path Algorithms<br>(e.g., Floyd-Warshall)"]
        B8 --> B12["Sequence Alignment<br>(e.g., Needleman-Wunsch)"]

        C["Greedy Algorithms"] --> C1{"Local Optimality"}
        C1 --> C2["Short-Sighted Decisions"]
        C --> C3{"Key Concepts"}
        C3 --> C4["Feasible Solutions"]
        C3 --> C5["Locally Optimal Choice"]
        C3 --> C6["Irrevocable Decisions"]
        C --> C7{"Examples"}
        C7 --> C8["Coin Changing<br>(Suboptimal)"]
        C7 --> C9["Dijkstra's Algorithm<br>(Shortest Path)"]
        C7 --> C10["Prim's Algorithm<br>(Minimum Spanning Tree)"]
        C7 --> C11["Huffman Coding"]
    end
    
```

----


**Key Improvements and Expansion:**

*   **Divide & Conquer (A):** Added specific examples of algorithms that use this paradigm. Added more key concepts such as breaking problems down into smaller subproblems and the recursion aspect to it.
*   **Dynamic Programming (B):** Specified core components and how they achieve optimal substructure.
*   **Greedy Algorithms (C):** Specified core components, how they are the result of local optimizations that are later put together in order to obtain a global solution.
*   **Clearer Organization:** Used more distinct node labels and organized them hierarchically to improve readability.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---