---
created: 2025-02-09 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: https://scottaaronson.blog/?p=762

---


# The First Law of Complexodynamics
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## 1. The Paradox: Entropy vs. Complexity

The blog post starts by highlighting a paradox related to the Second Law of Thermodynamics and our intuitive understanding of complexity.

### Diagram 1: Entropy and Complexity over Time

```mermaid
---
title: Entropy (Red) vs. Complexity (Blue) over Time
caption:  Entropy increases monotonically according to the Second Law, while Complexity peaks at an intermediate time, creating a curve.
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    subgraph Entropy
    style Entropy fill:#f392,stroke:#333,stroke-width:2px
        direction LR
        A["Initial State<br>(Low Entropy)"] --> B["Increasing Entropy Monotonically"] --> C["Final State<br>(High Entropy)"]
        B -- Second Law of Thermodynamics --> C
    end

    subgraph Complexity
    style Complexity fill:#c3c4,stroke:#333,stroke-width:2px
        direction LR
        D["Initial State<br>(Low Complexity)"] --> E["Increasing Complexity"] --> F["Peak Complexity<br>(Interesting Structures)"] --> G["Decreasing Complexity"] --> H["Final State<br>(Low Complexity)"]
        E --> F --> G -- "Complexity Curve" --> H
    end

    I["Time Evolution"]
    I --> A & D
    I --> B & E
    I --> C & H

    linkStyle 0,3,6,9  stroke-width:2px,stroke:red,color:red
    linkStyle 1,4,7,10 stroke-width:2px,stroke:blue,color:blue
    linkStyle 2,5,8,11 stroke-width:2px,stroke:green,color:green

    classDef entropy fill:#f399,stroke:#333,stroke-width:2px
    classDef complexity fill:#c3c4,stroke:#333,stroke-width:2px
    class Entropy entropy
    class Complexity complexity

    subgraph Key_Question["Key Question"]
        style Key_Question fill:#e339,stroke:#333,stroke-dasharray: 5 5
        K["Why does complexity follow this curve, unlike entropy?"]
    end
    K --> F

```

#### Explanation

*   **Entropy (Red Line):** Starts low and increases continuously over time, as dictated by the Second Law of Thermodynamics.
*   **Complexity (Blue Line):** Starts low, increases to a peak at an intermediate stage (where "interesting structures" emerge), and then decreases back to a low level in the final, equilibrium state.
*   **Key Question:** The central puzzle is to explain this non-monotonic behavior of complexity in contrast to entropy.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---