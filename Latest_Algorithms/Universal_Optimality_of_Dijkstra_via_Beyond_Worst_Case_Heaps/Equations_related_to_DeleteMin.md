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


## Equations related to DeleteMin

The diagram below captures the essential equation related to the `DeleteMin` operation, along with the context of its time complexity and the working set property.


```mermaid
---
title: "Equations related to DeleteMin"
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
    A["DeleteMin Operation"] --> B{"Time Complexity"}
    style A fill:#3c2552,stroke:#000,stroke-width:1px, color:black;
    B --> C["O(1 + log |W<sub>x</sub>|)"]
    C --> D["Working Set<br>(W<sub>x</sub>)"]
    D --> E["Elements inserted after x and still present"]
    B --> F["Amortized time complexity"]
    B --> G["Applies to Fibonacci-like priority queue with working set property"]
    
```

---


### Explanation of the Diagram

*   **A:** `DeleteMin Operation` is the central concept.
*   **B:** `Time Complexity` highlights the key performance metric.
*   **C:** `O(1 + log |Wx|)` This is the core equation. The cost of DeleteMin depends on the size of the working set.
*   **D:** `Working Set (Wx)` provides a brief definition, emphasizing elements inserted after `x`.
*   **F:** The definition of the time complexity is amortized.
*   **G:** Only work on Fibonacci-like priority queue with working set property.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---