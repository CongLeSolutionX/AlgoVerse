---
created: 2025-02-16 05:31:26
original source: "https://ieeexplore.ieee.org/document/10856563"
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---




# Autonomous clustering by fast find of mass and distance peaks
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---

Based on my understanding, I create a series of Mermaid diagrams and illustrations to visually represent the core concepts of Search-o1 framework from the original white paper at this [link](#)


## Document Breakdown

The paper introduces Torque Clustering (TC), a novel, parameter-free clustering algorithm. It's designed as an alternative to existing methods, addressing limitations in existing approaches like K-means, hierarchical clustering, and density-based methods. TC's central idea is inspired by galaxy mergers:

1.  **Define Clusters & Connections:** Data points initially form individual clusters. Connections between clusters are established based on 1-nearest neighbor relationships, where a cluster merges with its nearest neighbor if the neighbor has a lower or equal mass (number of points).
2.  **Two Properties:** Each connection (merger) is characterized by two properties:
    *   Mass: Product of the masses (number of points) of the connected clusters.
    *   Distance: Square of the distance between the connected clusters.
3.  **Torque Calculation and Sorting:** A "torque" value is calculated for each connection, based on its mass and distance. Connections are then sorted in descending order by torque, creating a Torque Sorted Connections List (TSCL).
4.  **Torque Gap and Abnormal Connection Detection:** The algorithm calculates a "Torque Gap" (TGap) between consecutive connections in the TSCL. The largest TGap identifies "abnormal" connections—those representing mergers between large clusters that are far apart. These are removed.
5.  **Halo Connections and Noise:** The algorithm defines "halo connections" based on mass and distance to identify points that are considered noise.

The paper evaluates TC extensively on synthetic and real-world datasets, comparing it with various state-of-the-art clustering algorithms. The evaluation metrics include NMI, ACC, and AMI. The results show TC's superior performance in accuracy, automatic cluster number determination and robustness to noise, outliers, and high dimensionality. The algorithm also demonstrates good computational efficiency.

## Mermaid Diagrams


Below is the collection of diagrams and illustrations in Mermaid syntax which cover the architecture, the agentic RAG and Reason-in-Documents mechanisms, the inference process, comparative approaches, and simplified representations of the experimental results.

I have aimed for a balance of technical detail and visual clarity for effective communication.


----



[Torque_Clustering_Mermaid_Diagrams_Draft_1](Torque_Clustering_Mermaid_Diagrams_Draft_1.md)


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---