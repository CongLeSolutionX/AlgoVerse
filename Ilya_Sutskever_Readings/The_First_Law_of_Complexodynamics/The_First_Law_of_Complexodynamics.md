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

# 2. The Coffee Cup Analogy

Sean Carroll illustrated this concept with the coffee cup example, showing milk mixing into coffee over time.

## Diagram 2: Coffee Cup Complexity Evolution

```mermaid
---
title: Coffee Cup Complexity Over Time
caption: Visual representation of the coffee cup example, showing complexity peaking in the intermediate stage during mixing
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    TS1["Stage 1: Initial<br>(Ordered)"];
    TS2["Stage 2: Intermediate<br>(Complex)"];
    TS3["Stage 3: Final<br>(Mixed/Disordered)"];

    S1A["Coffee & Milk Separated"];
    S1B["Low Entropy"];
    S1C["Low Complexity"];

    S2A["Milk Tendrils Mixing"];
    S2B["Increasing Entropy"];
    S2C["High Complexity"];

    S3A["Uniform Mixture"];
    S3B["High Entropy"];
    S3C["Low Complexity"];


    subgraph Time_Stages
    style Time_Stages fill:#f3f3,stroke:#333,stroke-width:1px
        TS1 --> TS2 --> TS3
    end

    subgraph Stage_1["Stage 1: Initial<br>(Ordered)"]
    style Stage_1 fill:#f3f3,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3
        S1A --> S1B & S1C
    end

    subgraph Stage_2 ["Stage 2: Intermediate<br>(Complex)"]
    style Stage_2 fill:#f3f3,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3
        S2A --> S2B & S2C
    end

    subgraph Stage_3 ["Stage 3: Final<br>(Mixed/Disordered)"]
    style Stage_3 fill:#f3f3,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3
        S3A --> S3B & S3C
    end

    Time_Stages --> Stage_1
    Time_Stages --> Stage_2
    Time_Stages --> Stage_3

    linkStyle 0 stroke-width:2px,stroke:black
    linkStyle 1 stroke-width:2px,stroke:black
    linkStyle 2 stroke-width:2px,stroke:black 
```

### Explanation

*   **Stage 1 (Initial):** Coffee and milk are separate - ordered, low entropy, low complexity.
*   **Stage 2 (Intermediate):** Milk starts mixing, forming intricate tendrils - increasing entropy, high complexity (visually interesting).
*   **Stage 3 (Final):** Uniform mixture of coffee and milk - high entropy, low complexity (homogeneous, less interesting).


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---