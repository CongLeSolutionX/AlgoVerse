---
created: 2025-03-04 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://ieeexplore.ieee.org/document/10856563"
---



# Torque Clustering Framework
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---



## Research Instructions: Analyzing Torque Clustering (TC) Algorithm

### **Keywords:**
- Torque Clustering (TC)
- Hierarchical Clustering
- Parameter-Free Clustering
- Abnormal and Halo Connections
- Mass, Distance, and Torque
- Nearest Neighbor Merging

### **Step 1: Define the Research Scope**

**Objective:**  
Understand the underlying principles of the Torque Clustering (TC) algorithm including its data‐merging mechanism, parameter‐free design, and the use of mass and distance metrics.

**Actions:**
- **Keywords:** Torque Clustering, Hierarchical Clustering, Autonomous Clustering  
- **Resources:** IEEE TPAMI articles, clustering and unsupervised learning literature, astrophysics analogies in galaxy mergers

**Mathematical Focus:**  
Key starting equation:
$$
\theta_i = 1 \quad \forall\, x_i \in X
$$  
Each data point forms an initial cluster with mass 1.

---

### **Step 2: Define Cluster Formation and Merger Process**

**Objective:**  
Detail how individual data points are assigned as initial clusters and iteratively merged using a nearest-neighbor rule.

**Actions:**
- **Cluster Initialization:**  
  Each data point \( x_i \) is assigned as a separate cluster with
  $$\theta_i = 1.$$
- **Connection Formation:**  
  Clusters are connected by finding each cluster’s nearest neighbor with a higher mass.
  
**Mathematical Focus:**
- **Connection Rule (Equation 1):**  
  $$\Gamma = \{ \zeta_i \}, \quad \text{where } \zeta_i \to \text{nearest neighbor with } \theta_j \geq \theta_i.$$
- **New Cluster Formation:**  
  The new cluster set is produced by aggregating connected components:
  $$G' = \Phi(G).$$

---

### **Step 3: Define Connection Properties**

**Objective:**  
Quantify the key properties of connections between clusters to guide merging.

**Actions:**
- **Mass Product Calculation:**  
  For a connection linking clusters \( \zeta_i \) and \( \zeta_j \):
  $$M_{ij} = \theta_i \times \theta_j.$$
- **Distance Measurement:**  
  The distance between clusters is calculated as the squared distance:
  $$D_{ij} = d^2(\zeta_i, \zeta_j).$$  
- **Torque Calculation:**  
  Combining mass and distance:
  $$\tau_{ij} = M_{ij} \times D_{ij}.$$

---

### **Step 4: Identify Abnormal and Halo Connections**

**Objective:**  
Determine which connections are “abnormal” (i.e. result in erroneous or unnatural cluster mergers) and which indicate noise (halo connections).

**Actions:**
- **Abnormal Connections:**  
  These are characterized by both large mass products and long distances.
- **Torque Gap Metric:**  
  A metric to automatically detect an optimal cutting point:
  $$TGap_i = \omega_i \times (\tau'_i - \tau'_{i+1}),$$  
  where \(\omega_i\) is a weighting factor and \(\tau'_i\) is the sorted torque value.
- **Halo Connections:**  
  Identified based on criteria such as a very small mass relative to distance, used to isolate noise.

---

### **Step 5: Hierarchical Merging and Final Partitioning**

**Objective:**  
Traverse the merging process until a hierarchical tree is constructed and then prune the tree to obtain the final clustering partition.

**Actions:**
- **Iterative Merging:**  
  Gradually merge connected clusters using the connection rule until only one overall cluster remains.
- **Pruning:**  
  Remove abnormal connections (from Step 4) and halo connections to finalize the partition.
  
**Mathematical Focus:**
- **Hierarchical Tree Formation:**  
  $$\text{Final Hierarchical Tree} = \bigcup_{k=1}^{L} G_k,$$  
  where \(L\) is the number of levels in the clustering hierarchy.

---

### **Step 6: Theoretical Analysis and Complexity**

**Objective:**  
Derive and analyze the time and space complexity of TC and discuss its parallelization potential.

**Actions:**
- **Time Complexity Analysis:**  
  Assume \(n\) data points, cost \(H\) for nearest neighbor search, and \(T\) iterations for merging:
  $$ T(TC) \approx O(n \cdot H \cdot T). $$
- **Space Complexity:**  
  Depends on storage of cluster sets, the sparse adjacency graph, and the connection properties (mass, distance, torque).

---

### **Step 7: Experimental Studies and Performance Comparison**

**Objective:**  
Benchmark TC against various clustering algorithms on both synthetic and real-world datasets.

**Actions:**
- **Evaluation Metrics:**  
  Accuracy (ACC), Normalized Mutual Information (NMI), and Adjusted Mutual Information (AMI).
- **Datasets:**  
  Synthetic (e.g., overlapping, unbalanced, noisy) and real-world data (e.g., MNIST, YTF, COIL-100).
  
**Mathematical Focus:**
- **Empirical Comparison Equation:**  
  $$ T_{\text{empirical}} \approx k \cdot (n \cdot H \cdot T),$$  
  where \(k\) is a constant based on hardware and implementation.

---

### **Step 8: Document Findings and Formulate Conclusions**

**Objective:**  
Summarize the strengths of the TC algorithm as well as propose directions for future research.

**Actions:**
- **Conclusions:**  
  TC is parameter‑free, robust, and efficiently determines the correct number of clusters via its constrained merging strategy and Torque Gap metric.
- **Future Research:**  
  Explore adaptive (per-cluster) halo thresholds for noise detection and extend TC into Deep TC Clustering by incorporating deep representation learning.
  
**Mathematical Focus:**
- **Performance Improvement:**
  $$ \text{TC Performance} \gg \text{Other Methods} \quad \text{(on average across benchmarks)}. $$

---

### **Step 9: Constraints and Cautions**

**Objective:**  
List key constraints and cautions drawn from the original document that must be considered during implementation and evaluation.

**Actions and Considerations:**

1. **Global Threshold Dependence:**
   - TC uses global mean values for mass, distance, and torque to detect abnormal and halo connections.  
   - **Caution:** For datasets with highly non-uniform noise, the global thresholds might not adapt well. Consider adaptive thresholds for each cluster if needed.

2. **Nearest Neighbor Ambiguity:**
   - The merging rule relies on the nearest neighbor with higher mass. Ambiguities may arise if multiple neighbors are nearly identical.  
   - **Caution:** Ensure the nearest neighbor search is robust; additional verification may be useful in ambiguous cases.

3. **Unclear Cluster Boundaries:**
   - In datasets with many clusters and unclear boundaries, the decision graph may not show a clear torque gap for pruning.  
   - **Caution:** Supplementary criteria or manual intervention might be required to finalize the clustering.

4. **Computational Complexity:**
   - TC’s runtime is influenced by the efficiency of the nearest neighbor search and handling of the full distance matrix.  
   - **Caution:** Use efficient approximate nearest neighbor methods (e.g., kd-trees, locality-sensitive hashing) for large datasets.

5. **Preprocessing Sensitivity:**
   - The algorithm assumes that each data point begins as its own cluster with a mass of 1. Poor preprocessing (lack of normalization or scaling) can skew mass and distance calculations.  
   - **Caution:** Carefully preprocess (normalize/standardize) input data to ensure meaningful metric computations.

6. **Interpretability of Merging Process:**
   - The merging and pruning process relies heavily on the definitions of mass, distance, and torque.  
   - **Caution:** Maintain clear documentation and visualization of intermediate metrics to ensure that the clustering behavior aligns with domain expectations.

---

## **Example Equations and Syntax in TC**

### **Initial Mass Assignment:**
$$
\theta_i = 1, \quad \forall\, x_i \in X
$$

### **Connection Rule:**
$$
\Gamma = \{ \zeta_i: \zeta_i \rightarrow \text{nearest neighbor with } \theta_j \geq \theta_i \}
$$

### **Mass and Distance for Connections:**
$$
M_{ij} = \theta_i \times \theta_j, \quad D_{ij} = d^2(\zeta_i, \zeta_j)
$$

### **Torque Calculation:**
$$
\tau_{ij} = M_{ij} \times D_{ij}
$$

### **Torque Gap Metric:**
$$
TGap_i = \omega_i \times (\tau'_i - \tau'_{i+1})
$$

### **Hierarchical Merging:**
$$
G' = \Phi(G)
$$

### **Time Complexity (Conceptual):**
$$
T(TC) \approx O(n \cdot H \cdot T)
$$

---

## **Summary Table of TC Research Steps**

| **Step** | **Objective**                                   | **Keywords**                                     | **Mathematical Focus**                                                                                    |
| -------- | ----------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| 1        | Define Research Scope                           | Torque Clustering, Parameter-Free                | \( \theta_i = 1, \forall\, x_i \in X \)                                                                   |
| 2        | Define Cluster Formation and Merger Process     | Initial Clusters, Nearest Neighbor Rule          | \(\Gamma = \{ \zeta_i \}\); \(G' = \Phi(G)\)                                                              |
| 3        | Define Connection Properties                    | Mass Product, Distance, Torque                   | \(M_{ij} = \theta_i \times \theta_j,\; D_{ij} = d^2(\zeta_i,\zeta_j),\; \tau_{ij} = M_{ij} \cdot D_{ij}\) |
| 4        | Identify Abnormal and Halo Connections          | Abnormal Connections, Torque Gap, Noise          | \(TGap_i = \omega_i \times (\tau'_i - \tau'_{i+1})\)                                                      |
| 5        | Hierarchical Merging and Final Partitioning     | Merging Process, Tree Pruning                    | Final tree: \( \bigcup_{k=1}^{L} G_k\)                                                                    |
| 6        | Theoretical Analysis and Complexity             | Time/Space Complexity, Parallelization           | \(T(TC) \approx O(n \cdot H \cdot T)\)                                                                    |
| 7        | Experimental Studies and Performance Comparison | Benchmarking, ACC, NMI, AMI                      | Empirical comparison via ranking and metric averages                                                      |
| 8        | Document Findings and Formulate Conclusions     | Summary, Future Extensions                       | Future improvements: Adaptive thresholds, Deep TC Clustering                                              |
| 9        | Incorporate Constraints and Cautions            | Global Threshold, Nearest Neighbor Ambiguity,    | See detailed cautions regarding preprocessing, computational, and                                         |
|          |                                                 | Unclear Boundaries, Complexity, Interpretability | merging process above                                                                                     |

---




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---