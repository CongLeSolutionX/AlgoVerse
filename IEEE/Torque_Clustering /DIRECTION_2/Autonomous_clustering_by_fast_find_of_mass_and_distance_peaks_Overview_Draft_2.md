---
created: 2025-02-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://ieeexplore.ieee.org/document/10856563"
---



# Autonomous Clustering by Fast Find of Mass and Distance Peaks Paper Overview - Draft 1
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## Autonomous Clustering by Fast Find of Mass and Distance Peaks - A Diagram Structure


### 1. Torque Clustering (TC) Algorithm Overview

```mermaid
---
title: "Autonomous clustering by fast find of mass and distance peaks"
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
    "graph": { "htmlLabels": true, 'curve': 'linear' },
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
    A["Data Set"] --> B{"Initialize Clusters<br>(Each point)"}
    B --> C{"Apply Connection Rule<br>(Eq. 1: Nearest Higher Mass)"}
    C --> D{"Calculate M_i, D_i<br>(Eqs. 3, 4)"}
    D --> E{"Compute Torque<br>(Eq. 5)"}
    E --> F{"Identify Abnormal Connections<br>(TGap)"}
    F --> G{"Remove Abnormal Connections"}
    G --> H{"Identify Halo Connections<br>(Noise)"}
    H --> I["Final Clusters"]

    style A fill:#ccf3,stroke:#333,stroke-width:1px
    style I fill:#ccf3,stroke:#333,stroke-width:1px

    subgraph Equations
        EE1["$$M_i = Mass Product$$"]
        EE2["$$D_i = Distance^2$$"]
        EE3["$$τ_i = M_i * D_i$$"]
        EE4["$$TGap_i = ω_i * (τ'_i - τ'_{i+1})$$"]

        EE1 -- "Eq. 3" --> EE3
        EE2 -- "Eq. 4" --> EE3

        EE3 -- "Calculates Torque Gap + Clustering Resolution" --> EE4
    end

    F --> EE1
    F --> EE2
    F --> EE3
    F --> EE4

    classDef detail fill:#f9f3,stroke:#333,stroke-width:1px
    class A,I detail
    
```


*   **Type:** Basic flowchart representing the TC process.
*   **Emphasis:** Flow of operations, highlighting key steps.
*   **Equations:** Separate subgraph focusing on equations, demonstrating how they influence "Identify abnormal Connections"

----


### 2. TC Parameters and Metrics

```mermaid
---
title: "Autonomous clustering by fast find of mass and distance peaks"
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
    "graph": { "htmlLabels": true, 'curve': 'linear' },
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
    A["Torque Clustering<br>(TC)"] --> B{"Key Parameters"}
    B --> C["Mass<br>(θ)"]
    C --> C1["Number of points in a cluster"]
    B --> D["Distance<br>(d)"]
    D --> D1["Min distance between clusters"]
    B --> E["Torque<br>(τ)"]
    E --> E1["$$M_i * D_i$$"]
    B --> F["Torque Gap<br>(TGap)"]
    F --> F1["Determines cut point"]
    B --> G["Halo Connections"]
    G --> G1["Noise Identification"]

    H["Evaluation Metrics"] --> I["NMI<br>(Normalized Mutual Information)"]
    H --> J["ACC<br>(Accuracy)"]
    H --> K["AMI<br>(Adjusted Mutual Information)"]
    style H fill:#ffc3,stroke:#333,stroke-width:1px;
    
```

*   **Type:** Simple graph to show what metrics are important for TC.


----

### 3. Algorithm Comparison (Conceptual)

```mermaid
---
title: "Autonomous clustering by fast find of mass and distance peaks"
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
    "graph": { "htmlLabels": true, 'curve': 'linear' },
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
    A["Torque Clustering<br>(TC)"] --> B{"Comparison with Other Algorithms"}
    B --> C[Advantages]
    C --> C1[Parameter-Free]
    C --> C2[Handles Diverse Clusters]
    C --> C3[Constrained Merging]
    C --> C4[Auto Cluster Number]
    C --> C5[Robust to Noise]

    B --> D[Competitors]
    D --> D1[K-means++]
    D --> D2[Spectral Clustering]
    D --> D3[Hierarchical Clustering]
    D --> D4[DPC Variants]
    D --> D5[FINCH]
    D --> D6[DBSCAN]
    D --> D7[AP, BP, RCC]
    D --> D8[Deep Clustering]

    style A fill:#afa3,stroke:#333,stroke-width:1px
    style D fill:#aaf3,stroke:#333,stroke-width:1px
    
```

*   **Type:** Graph to summarize comparison.


----


### 4. Torque Clustering and DPC Differences

```mermaid
---
title: "Autonomous clustering by fast find of mass and distance peaks"
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
    "graph": { "htmlLabels": true, 'curve': 'linear' },
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
    A["Torque Clustering<br>(TC)"] --> B{Cluster-Level Mass}
    B --> C[Global Perspective]
    B --> D[Robust to Density Variation]
    B --> E[Avoids Cutoff Distance]

    F[DPC] --> G{Point-Level Density}
    G --> H[Local Perspective]
    G --> I[Sensitive to Density Variation]
    G --> J[Requires Cutoff Distance]

    style A fill:#afa3,stroke:#333,stroke-width:1px
    style F fill:#faa3,stroke:#333,stroke-width:1px
    
```

*   **Type:**  Comparison graph focusing on the core differences.


----


### 5. Torque Clustering Future Enhancements

```mermaid
---
title: "Autonomous clustering by fast find of mass and distance peaks"
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
    "graph": { "htmlLabels": true, 'curve': 'linear' },
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
    A[Future Torque Clustering Enhancements] --> B{Adaptive Thresholds}
    B --> C[Non-Uniform Noise]
    A --> D{Deep Torque Clustering Clustering}
    D --> E[Large Cluster Datasets]
    D --> F[Unclear Boundaries]
    D --> G[Neural Network Representation]
    
```

*   **Type:** Simple listing of future work items.




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---