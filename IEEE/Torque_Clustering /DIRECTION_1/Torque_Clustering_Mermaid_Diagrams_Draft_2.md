---
created: 2025-02-16 05:31:26
original source: "https://ieeexplore.ieee.org/document/10856563"
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---




# Autonomous clustering by fast find of mass and distance peaks - Mermaid diagrams
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## 1. Overview of the Torque Clustering (TC) Algorithm

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Torque Clustering (TC) Algorithm"] --> B{"Goal:<br>Autonomous Clustering"};
    B --> C["Parameter-Free"];
    B --> D["Handles Various Cluster Shapes and Sizes"];
    B --> E["Identifies Noise and Determines Optimal Cluster Number"];
    B --> F["Inspired by Galaxy Mergers"];
    F --> G["Hierarchical Structure of Merging Clusters"];
    A --> H["Key Steps:"];
    H --> I["Step 1:<br>Define Clusters and Connections"];
    H --> J["Step 2:<br>Define Properties (Mass, Distance) of Connections"];
    H --> K["Steo 3:<br>Calculate Torque and Sort Connections"];
    H --> L["Step 4:<br>Identify Abnormal Connections<br>(Torque Gap)"];
    H --> M["Step 5:<br>Identify Noise (Halo Connections)"];
    
```


**Explanation:** This diagram provides a high-level overview of the TC algorithm, its purpose, key features, and the main steps of the process.

---

## 2. Algorithm Details: Defining Clusters and Connections

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Data Set X = {x1, x2, ..., xn}"];
    B{"Each data point xi is a cluster"};
    C["Initial Mass θi = 1 for all clusters"];
    D["Connect each cluster ζi to its 1-nearest cluster ζj<br>(θi <= θj)"];
    E["Formation of Connected Graph G<br>(each cluster vertex)"];

    F["Apply Eq. (2):<br>Forming new clusters G' from connected components of G<br>(ζi -> Φ(G))"];
    G["Mass of new cluster = number of points"];
    H["Repeat steps until one cluster"];

    A --> B
    
    subgraph Initial_Mass["Initial Mass"]
    style Initial_Mass fill:#c322,stroke:#333,stroke-width:2px
        B --> C
    end
    
    subgraph Connections["Connections"]
    style Connections fill:#c662,stroke:#333,stroke-width:2px
        C --> D
        D --> E
    end
    
    subgraph New_Clusters["New Clusters"]
    style New_Clusters fill:#cf52,stroke:#333,stroke-width:2px
        E --> F
        F --> G
        G --> H
    end
    
```

**Explanation:** This diagram focuses on the initial steps of TC, including how clusters are defined, how connections are established based on nearest neighbors, and how the cluster set evolves through merging. Eq. (1) and Eq. (2) from the paper are referenced here implicitly.

---

## 3. Algorithm Details: Torque, Properties, and Decision Graph

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Connection Properties"];
    B["Mass (Mi) = θi * θj <br>(Product of cluster masses)"];
    C["Distance (Di) = d(ζi, ζj)<br>(Minimum distance between points in clusters)"];
    D{"Decision Graph:<br>Plot Mi vs Di"};

    E["Torque (τi) = Mi * Di^2"];
    F["Sort Connections by τi (Descending) -> Torque Sorted Connections List (TSCL)"];
    G["Large Mi and Di -> High τi<br>(Abnormal Connections Appear at Top of TSCL)"];

    A --> B
    A --> C
    A --> D

    subgraph Torque["Torque"]
        D --> E
        E --> F
    end
    
    subgraph Identify_Abnormal_Connections["Identify Abnormal Connections"]
        F --> G
    end
    
```

**Explanation:** This diagram breaks down the calculation of torque and how connection properties (mass and distance) are used to construct a decision graph and identify potential abnormal connections. The sorting of connections based on torque is emphasized.

----

## 4. Algorithm Details: Torque Gap and Halo Connections

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Torque Gap<br>(TGap)"];
    B{"Calculate TGap between consecutive connections in TSCL"};
    C["TGap Formula:<br>TGap = ωi * (τi - τi+1)<br>(Eq. 6)"];
    D{"ωi:<br>Clustering Resolution<br>(proportion of TSCL connections with large Mi, Di)"};
    E["Find Largest TGap -> Identify L abnormal connections<br>(remove)"];

    F["Define Halo Connections (Halo_C):<br>Large Mi, and Small Di"];
    G["Halo_C Formula(Eq.10):<br>Mi <= mean_M and  Di <= mean_D"];
    H["Remove Halo Connections -> Identify noise from clustering"];

    A --> B
    B --> C
    C --> D
    D --> E
    
    subgraph Noise_Detection["Noise Detection"]
        E --> F
        F --> G
        G --> H
    end
```

**Explanation:** This diagram describes how the Torque Gap is calculated to identify abnormal connections and how halo connections are defined and used for noise detection. The roles of ωi and the global means from the paper are visualized.

---

## 5. Algorithm Steps Illustrated with Figure 2

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Fig 2. Step-by-Step Example"];
    B["Fig. 2A:<br>Initial Data, each point as a cluster"];
    C["Eq.(1) Connections, graph formation<br>(Fig. 2B)"];
    D["Apply Eq.(2) - Forming new clusters<br>(Fig. 2B)"];
    E["Fig. 2C, Fig. 2D:<br>Connections and Cluster properties"];
    F["Properties Table 1A, Table 1B"];
    G["Decision Graph (Fig. 2G): <br>Mi vs Di"];
    H["Abnormal Connections Removed<br>(Fig. 2H)"];
    I["Clustering Tree(Fig 2H), final partitioning<br>(Fig 2I)"];

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
```

**Explanation:** This diagram uses the visual example from Figure 2 in the paper to illustrate the step-by-step application of the TC algorithm.  It references figures and tables in the paper to make the process visual.

---

## 6. Time and Space Complexity

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Time Complexity<br>(TC)"];
    B["Distance matrix input:<br>O(n^2)"];
    C["Steps 6,8,9 (inside loop):<br>O(m*H)"]; 
    %% Note: H is the average # of neighbors

    D["Step 7(nearest neighbor search):<br>O(H)"];
    E["Steps 10,16,18 (cluster set update/remove)<br>O(n)"];
    F["If using fast-approximate KNN:<br>complexity is slightly different"];
    G["Overall (Distance Matrix):<br>O(n^2) + O(mH)"];
    H["Best case O of TC ≈ O(nH)"];
    I["Space Complexity<br>(TC)"];
    J["Store:<br>Clusters, connections (sparse matrix), Mi, Di, TGap"];
    K["Basic space O = O(n)"];
    %% note: linear to n, data points.

    L["with Distance Matrix, Space = O(n^2)"];
    
    A --> B
    B --> C
    
    C --> D
    D --> E
    A --> F
    A --> G
    A --> H

    I --> J
    J --> K
    
    J --> L
    K --> L
    
```

**Explanation:** This diagram presents  the time complexity of the TC process, the space complexity, in terms of Big O notation.

---

## 7. Performance Comparison Diagram

```mermaid
pie
    title TC Performance Summary
    "TC Achieved Highest Performance on Synthetic Data" : 70
    "TC Achieved Highest Performance on Real-World Data" : 80
    "Automatic Cluster Number Determination (Lowest Error)" : 75
    "Competitive Execution Time (Second Fastest)" : 60
    "Comparable to Deep Clustering Algorithms" : 70
```

**Explanation:** A pie chart summarizing key performance highlights of TC, relative to other algorithms discussed in the paper. The percentages are approximate. The percentages reflect the quantitative performance compared to other algorithms as reported in the research.

---

## 8.  Visual Comparison of Clustering Algorithms (Figure 4)

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Figure 4<br>(Synthetic Data)"];
    B["Original Data Distribution"];
    C["AC-S<br>(Agglomerative Clustering -<br> Single Linkage)"];
    D["AC-W<br>(Agglomerative Clustering -<br>Ward Linkage)"];
    E["FINCH<br>(Efficient Parameter-Free Clustering)"];
    F["DPC<br>(Density Peak Clustering)"];
    G["TC<br>(Torque Clustering) -<br>Stage 1 to 5"];

    B1["Depict Clusters in various colors"];
    C1["AC-S:<br>Sensitive to outliers which leads to inaccurate clusters"];
    D1["AC-W:<br>Difficult to detect complex shapes of clusters"];
    E1["FINCH:<br>Produces incorrect mergers with constrained merging approach"];
    F1["Sensitivity towards data with varying densities"];
    G1["TC:<br>Illustrates step-by-step merging process and correct clustering results"];

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    A --> G
    
    B --> B1
    C --> C1
    D --> D1
    E --> E1
    F --> F1
    G --> G1

    style A fill:#f395,stroke:#333,stroke-width:2px
    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style C fill:#c3c5,stroke:#333,stroke-width:1px
    style D fill:#c3c5,stroke:#333,stroke-width:1px
    style E fill:#c3c5,stroke:#333,stroke-width:1px
    style F fill:#c3c5,stroke:#333,stroke-width:1px
    style G fill:#c3c5,stroke:#333,stroke-width:1px
```

**Explanation:** This graph represents the result comparisons in the paper, highlighting the advantages and disadvantages of each method and how accurately they cluster the synthetic data.

---

## 9. Limitations and Future Work

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Potential Limitations"];
    B["Halo connection thresholding might not identify all types of non-uniform noise"];
    C["Challenges with datasets with large cluster count lack clear boundaries"];
    D["TC - relies on global mean values"];

    E["Future Work"];
    F["Adaptive Threshold for Halo Connections<br>(Improve noise handling)"];
    G["Deep TC Clustering<br>(Integrate deep learning for better representation learning and improved boundary detection)"];

    A --> B
    A --> C
    A --> D

    E --> F
    E --> G
```

**Explanation:** This diagram highlights the limitations of the current TC algorithm and proposes future research directions.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---