---
created: 2025-02-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/2202.05387"
---


# TwHIN: Embedding the Twitter Heterogeneous Information Network for Personalized Recommendation
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---

Based on my understanding, I create a series of Mermaid diagrams and illustrations to visually represent the core concepts of the framework from the original white paper at this [link](https://arxiv.org/pdf/2202.05387)

---


Here's a breakdown of the "TwHIN: Embedding the Twitter Heterogeneous Information Network for Personalized Recommendation" paper using Mermaid diagrams and illustrations, presented in Markdown, to capture the technical intricacies:

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[TwHIN White Paper] --> B(Key Concepts);
    A --> C(Methodology);
    A --> D(Experiments & Results);
    A --> E(Practical Considerations);
    A --> F(Conclusion);
        style A fill:#a2fa,stroke:#333,stroke-width:1px;

    B --> B1(Heterogeneous Information Network - HIN);
    B1 --> B11[Nodes: Users, Tweets, Advertisers, Ads, etc.];
    B1 --> B12[Edges: Follows, Favorites, Retweets, Replies, Clicks, etc.];
    B1 --> B13[Multiple Entity & Relation Types];
    B --> B2(Knowledge Graph Embeddings - KGE);
    B2 --> B21[Representing Entities & Relations as Vectors];
    B2 --> B22["TransE Model: f(s, r, t) = (θs + θr)ᵀθt"];
    B2 --> B23[Negative Sampling for Training];
    B --> B3(Personalized Recommendation);
    B3 --> B31[Candidate Generation];
    B3 --> B32[Ranking & Prediction];
    B --> B4(Data Supplementation);
    B4 --> B41[Leveraging multiple data sources/relations];
    B4 --> B42[Addressing Sparsity];
    B --> B5[Task Reusability]
        B5 --> B51[Embeddings are used across multiple models and platforms];
        B5 --> B52[Embeddings can be generalized and pre-trained]
        B5 --> B53[Less labor-intensive];
    C --> C1(HIN Embedding Approach);
    C1 --> C11[TransE Model Application];
    C1 --> C12[Negative Sampling Objective];
        C12 --> C121[Equation 2 in the paper: Maximize log-likelihood of real vs. fake edges];
    C1 --> C13[Adagrad Optimization];
    C --> C2(Computational Considerations);
    C2 --> C21[PyTorch-BigGraph Framework];
    C2 --> C22[Node Partitioning for Memory Management];
    C --> C3(TwHIN at Twitter);
    C3 --> C31[TwHIN-Follow & TwHIN-Engagement];
    C3 --> C32[High-Coverage vs. Low-Coverage Relations];
        C3 --> C33[Co-embed relations];
    C --> C4(Inductive Multi-Modal Embeddings);
    C4 --> C41[Addressing single embedding and out-of-vocabulary entity limitations];
    C4 --> C42[Clustering Existing Embeddings];
    C4 --> C43["Computing Multiple Embeddings per Node (Mixture Model)"];
        C4 --> C44[Equation 3: Probability distribution over clusters];
        C4 --> C45[More descriptive, can capture multi-modal interests];
    D --> D1(Candidate Generation);
    D1 --> D11["Who to Follow" Task];
    D1 --> D12["Approximate Nearest Neighbor (ANN) Search"];
    D1 --> D13[Unimodal vs. Multi-Modal Embeddings];
    D1 --> D14[Table 1: Multi-Modal > Unimodal in Recall];
    D --> D2(Recommendation & Prediction);
    D2 --> D21[Predictive Advertisement Ranking];
        D21 --> D211["Relative Cross Entropy (RCE) as Metric"];
    D21 --> D212[Online A/B Testing Results: TwHIN Improves RCE];
    D21 --> D213["Offline Entity Ablation Studies (Table 2)"];
    D2 ---> D22(Search Ranking);
    D22 --> D221[MAP & ROC as Metrics];
    D22 --> D222[Table 3: TwHIN Improves Ranking Performance];
    D2 --> D23(Offensive Content Detection);
    D23 --> D231[PR-AUC as Metric];
    D23 --> D232[Table 4: TwHIN Improves Offensive Content Detection];
    E --> E1(Compression for Low Latency);
    E1 --> E11[Product Quantization];
    E1 --> E12[Figures 4a & 4b: Compression vs. Performance Tradeoff];
    E --> E2(Addressing Parameter Drift);
    E2 --> E21[Warm Start vs. Regularization];
    E2 --> E22[Figure 4c: Parameter Drift Mitigation];
    E2 --> E23[Table 5: Effect on Downstream Task];
    F --> F1[Joint embedding better approach];
        F --> F2[KGE are fit for heterogeneous graphs]
        F --> F3[TwHIN deployment at scale]
        F --> F4[Significant A/B Testing results]
        F --> F5[Tricks of the trade are given for effective implementation]

```


**Explanation of Diagram and Key Concepts:**

The above Mermaid diagram breaks down the core concepts of the TwHIN whitepaper into smaller, connected sections.

*   **Heterogeneous Information Network (HIN):** TwHIN model's data as a network where nodes and edges represent *different* types of entities, and edges represent all relevant interactions.
*   **Knowledge Graph Embeddings (KGE):** The HIN uses vector representations that capture the relationship between nodes and edges, leveraging the TransE Model is used for simple calculations. *Negative Sampling* is used to optimize the model and create differentiation between actual and "fake" connections.
*    **Computational Considerations:** The size of the Twitter network needs additional steps to be embedded properly. The HIN can be partitioned in buckets by using `PyTorch-Biggraph` to perform embeddings while conserving space, allowing for training on a single GPU.
*   **Inductive Multi-Modal Embeddings:** To address limitations with classical KGE (failing to capture multi-faceted users, and retraining), the HIN can embed *clusters of entities,* using clustering technique as the probability distribution of the engagement of an entity.
*   **Practical Considerations:** *Compression* is used through product quantization for low latency and efficient performance trade-off.
*   **Parameter Drift:** Embeddings need to be updated regularly to accurately represent entities. *Warm start* or *regularization* is used for stability when versioning.

---

## HIN Structure

```mermaid
graph LR
    subgraph TwHIN["Twitter Heterogeneous Information Network"]
        U[User] -- Follows --> U
        U -- Favorites --> T[Tweet]
        U -- Retweets --> T
        U -- Replies --> T
        U -- Clicks --> A[Advertiser]
        A -- Promotes --> AD[Ad]
        U -- Clicks --> AD
        T -- Authors --> U
        style TwHIN fill:#a2da,stroke:#333,stroke-width:1px;

    end
```

This diagram visually represents the different entity types (User, Tweet, Advertiser, Ad) and the relationships (Follows, Favorites, Retweets, Replies, Clicks, Promotes, Authors) within the TwHIN.

---

## TransE Model

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    S["Source Entity<br>(s)"] --> T["Target Entity<br>(t)"];
    S -- Relation<br>(r) --> T;
    S --> SE["θs:<br>Embedding"];
    T --> TE["θt:<br>Embedding"];
    R["Relation<br>(r)"] --> RE["θr:<br>Embedding"];
 
    SE -- "+" --> ST["θs + θr"];
    ST -- Dot Product --> Score["f(s, r, t) = (θs + θr)ᵀθt"];
    TE -- Dot Product --> Score;

    style S fill:#c2fa,stroke:#333,stroke-width:1px;
    style T fill:#c2fa,stroke:#333,stroke-width:1px;
    style R fill:#c2fa,stroke:#333,stroke-width:1px;
    
```


This diagram illustrates the TransE model's core operation.  It shows how the source entity's embedding is "translated" by the relation embedding, and then a dot product with the target entity's embedding produces a score.

---
## Negative Sampling Objective

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Input HIN:<br>G = (V, E, φ, ψ)"] --> B{"Training Objective"};
    B --> C["Positive Edges<br(s, r, t) ∈ E"];
    B --> D["Negative Edges<br(s, r, t') ∉ E"];
    C --> E["Maximize log σ(f(s, r, t))"];
    D --> F["Maximize log σ(-f(s, r, t'))"];
    E --> G["Learn Parameters θ"];
    F --> G;
    
    style A fill:#c2fa,stroke:#333,stroke-width:1px;
    style B fill:#c2fa,stroke:#333,stroke-width:1px;
    
```


This diagram outlines the negative sampling objective.  It shows the contrast between positive (real) edges and negative (sampled) edges, and how the model learns to differentiate between them.

---

## Multi-Modal Embeddings

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    subgraph Clustering
        A["Target Entities<br>(Tweets, etc.)"] --> B(K-Means Clustering);
        B --> C[Clusters C1, C2, ..., Ck];
            end
                style Clustering fill:#c2fa,stroke:#333,stroke-width:1px;

     subgraph UserRepresentation["User Representation"]
        U["User<br>(ui)"] -- Engages With --> C1;
        U -- Engages With --> C2;
        U -- Engages With --> Ck;
        C1 --> D["P(c1 | ui)"];
        C2 --> D;
        Ck --> D;
        D[Probability Distribution over Clusters] --> E[Mixture of Embeddings];
        E --> F[Multi-Modal Representation];

    end
    style UserRepresentation fill:#c3da,stroke:#333,stroke-width:1px;
    
```


This diagram explains the process of creating multi-modal embeddings.  It shows how target entities are clustered, and then how a user is represented as a probability distribution over these clusters, reflecting their engagement patterns.

---

## End-to-End Framework
```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    subgraph Data_Sources["Data Sources"]
    style Data_Sources fill:#ccf5,stroke:#333,stroke-width:1px;
        A[Follow Graph] --> D;
        B[User-Tweet Engagement] --> D;
        C[Advertisement Interactions] --> D;
        D[TwHIN Construction] --> E;
    end
    
    subgraph TwHIN_Embedding["TwHIN Embedding"]
    style TwHIN_Embedding fill:#a3f5,stroke:#333,stroke-width:1px;
        E["HIN Embedding<br>(Algorithm 1)"] --> F;
        F[Entity Embeddings] --> G;
        G["Multi-Modal Embeddings<br>(Section 4.4)"] --> H;
    end
                
    subgraph Downstream_Tasks["Downstream Tasks"]
        style Downstream_Tasks fill:#cfa2,stroke:#333,stroke-width:1px;
        H --> I[Candidate Generation];
        H --> J[Recommendation Ranking];
        H --> K[Content Classification];
        I --> L[ANN Search];
        J --> M[Deep Learning Models];
        K --> N[Predictive Models];
    end
    
```
This diagram represents how all entities work together from the raw data, to training and embeddings, to downstream tasks.

## Key Takeaways and Contributions Presented Visually

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    A[Key Contributions] --> B(Scalable HIN Embedding);
    
    B --> B1["Simple KGE Techniques<br>(TransE)"];
    B1 --> B11[Contrast to complex alternating CPU-GPU rounds];
    
    B --> B2[Single Multi-GPU Machine];
    B2 --> B21[Contrast from multiple MapReduce jobs];
    
    B --> B3[Efficient and Flexible];
    B3 --> B31[Contrast from Custom OpenMP extension];
    
    A --> C(Heterogeneous Approach);
    
    C --> C1[Combines Disparate Network Data];
    C --> C2[Addresses Data Sparsity];
    C --> C3[Improved Representation Learning];
    A --> D(Practical Insights);
    D --> D1[Productionizing HIN Embeddings];
    D --> D2[Design Considerations];
    D --> D3[Handling Parameter Drift];
    D --> D4[Compression Techniques];

    style A fill:#a2fa,stroke:#333,stroke-width:1px;

```

This diagram summarizes the key takeaways and contributions of with key differences to previous work.

---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---