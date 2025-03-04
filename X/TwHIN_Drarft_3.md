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


## Overview Diagram

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    A["TwHIN:<br>Embedding the Twitter Heterogeneous Information Network"];
    B{"Problem"};
    C["Large Scale of Interactions"];
    D["Lack of Holistic User Representation"];

    E{"Proposed Solution"};
    F["Knowledge Graph Embeddings<br>(KGE)"];
    G["Heterogeneous Information Network<br>(HIN)"];
    H["Scalable Implementation:<br>PyTorch-BigGraph"];

    I{"Contributions"};
    J["Scalable and Flexible KGE Techniques"];
    K["Combining Disparate Network Data"];
    L["Practical Insights/Design Considerations"];

    M{"Applications"};
    N["Candidate Generation<br>(Who to Follow)"];
    O["Recommendation Ranking<br>(Ads, Search)"];
    P["Offensive Content Detection"];

    Q{"Challenges"};
    R["Latency"];
    S["Parameter Drift"];
    
    
    A --> B
    B --> C
    B --> D

    A --> E
    E --> F
    E --> G
    E --> H

    A --> I
    I --> J
    I --> K
    I --> L

    A --> M
    M --> N
    M --> O
    M --> P

    A --> Q
    Q --> R
    Q --> S
```

**Explanation:** This diagram provides a high-level overview.  It shows the problem being addressed (large-scale data/lack of holistic representation), the proposed solution (KGE on HINs), the key contributions, the applications (where TwHIN is used), and the challenges faced.

## Heterogeneous Information Network (HIN) Diagram

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    subgraph HIN["Heterogeneous Information Network (TwHIN) Example"]
    style HIN fill:#f395,stroke:#333,stroke-width:2px
        A[User] -- Follows --> B[User];
        A -- Retweets --> C[Tweet];
        A -- Favorites --> C;
        A -- Replies --> C;
        C -- Authors --> A;
        C -- Mentions --> A;
        D[Advertiser] -- Promotes --> E[Ad];
        A -- Clicks --> E;
        A -- Engages --> D;
        F[Topic] -- Topics --> A;
        B --> F;
    end
    
```

**Explanation:** This diagram visually represents the HIN concept.  It illustrates different entity types (User, Tweet, Advertiser, Ad, Topic) and the various relationship types (Follows, Retweets, Favorites, Replies, Authors, Promotes, Clicks, Topics, Engages) that connect them.  This captures the "heterogeneous" aspect.

## KGE Triplet Scoring Diagram:

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Source Entity<br>(s)"];
    B{"Translating Embedding<br>(TransE)"};
    C["Relation<br>(r)"];
    D["θs + θr"];
    E["Target Entity<br>(t)"];
    F{"Scoring Function<br>(f(s, r, t))"};
    G["Score"];

    A -- θs --> B
    C -- θr --> B;
    B -- Add --> D
    D --> E -- θt --> F
    F --> G

    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style D fill:#c3c5,stroke:#333,stroke-width:1px
    style F fill:#c3c5,stroke:#333,stroke-width:1px

```

**Explanation:**  This diagram describes the core of the KGE approach using TransE. It shows the embedding vectors (θs, θr, θt) for the source, relation, and target entities. The translation step (adding the source and relation embeddings) and the scoring function (e.g., dot product) are visually represented.

## Negative Sampling Objective Diagram

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["HIN Triplet<br>(s, r, t)"];
    B{"Scoring Function<br>(f(s,r,t))"};
    C["Score<br>(f(e))"];
    D["Negative Sampling<br>(N(e))"];
    E["Corrupted Triplet<br>(s', r, t') or (s, r, t')"];
    F{"Scoring Function<br>(f(s',r,t')) or (f(s,r,t'))"};
    G["Score<br>(f(e'))"];
    H{"Log Sigmoid <br>(f(e))"};
    I{"Log Sigmoid <br>(-f(e'))"};
    J["Maximize<br>(Objective)"];


    A --> B
    B --> C

    A --> D
    D --> E
    E --> F
    F --> G

    C --> H
    G --> I

    H --> J
    I --> J

    classDef Elements fill:#c3c5,stroke:#333,stroke-width:1px
    class B,F Elements


    classDef Element_With_Border fill:#c3c5,stroke:#afa,stroke-width:1px
    class C,G,H,I Element_With_Border

```

**Explanation:** This diagram explains the negative sampling objective. It outlines the process of scoring positive triplets from the HIN and contrasting them with scores from negative sampled triplets. The log-sigmoid function is applied, and the objective is to maximize the difference between the positive and negative scores.

## PyTorch-BigGraph Partitioning Diagram

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Nodes<br>(Users, Tweets, etc.)"];
    B{"Partition Function<br>(π)"};
    C["Partitions<br>(P)"];
    %% C "Nodes Assigned to P Partitions"
    D["Edges<br>(s,r,t)"];
    E{"Bucket Assignment<br>(Bπ(s), π(t))"};
    %% E "Edges Assigned to Buckets based on Source/Target Partitions"
    F[Bucket i,j,k];

    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style C fill:#c3c5,stroke:#afa,stroke-width:1px
    style D fill:#c3c5,stroke:#afa,stroke-width:1px
    style E fill:#c3c5,stroke:#ccf,stroke-width:1px

```

**Explanation:** This diagram illustrates how PyTorch-BigGraph handles the scale of the Twitter network. It shows the partitioning of nodes, the assignment of edges to buckets based on the source and target node partitions, and the loading of these buckets for training on GPU.  This shows how the system scales.

## Multi-Modal Embedding Generation

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["User Embedding<br>(Uni-modal)"];
    B{"Clustering of Non-User Entities<br>(T)<br>e.g., Tweets<br>e.g., k-means on Tweet Embeddings"};
    C["Clusters<br>(C)"];
    D{"Engagement with Clusters"};
    E["Probability Distribution<br>P(c|ui)<br>Proportional to Engagement Count"];
    F["Multi-Modal Mixture of Embeddings"];

    A --> B
    B --> C
    A --> D
    D --> E
    E --> F

    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style D fill:#c3c5,stroke:#333,stroke-width:1px
    style E fill:#c3c5,stroke:#afa,stroke-width:1px
    style F fill:#a3f5,stroke:#333,stroke-width:1px

```

**Explanation:** This diagram outlines the generation of multi-modal embeddings.  It shows how existing embeddings are used with clustering techniques to generate multiple, mixture-based embeddings. This also shows how inductive embedding of new nodes are generated to better represent users with potentially diverse interests.

## End-to-End Framework Diagram

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Disparate Data Sources<br>(Follow, Engagement, Ads)"];
    B{TwHIN Construction};
    C["HIN<br>(Nodes, Relationships)"];
    D{"KGE -<br>Translating Embeddings (TransE)"};
    E["Entity Embeddings<br>(Users, Tweets, Advertisers, etc.)"];
    F{Downstream Tasks};
    G["Candidate Generation<br>(Who to Follow)"];
    H["Recommendation Ranking<br>(Ads, Search)"];
    I[Offensive Content Detection];

    %% Notes:
    %% label A "Social Signals, Content Engagement, Advertiser Data"
    %% label C "Multi-typed Nodes Connected by Multiple Relations"
    %% label E "Dense, Low-Dimensional Representations"

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    F --> H
    F --> I

    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style D fill:#c3c5,stroke:#ccf,stroke-width:1px
    style F fill:#c3c5,stroke:#ccf,stroke-width:1px

```

**Explanation:** This diagram summarizes the complete process, from data sources to the final applications. It shows the inputs, the key steps (TwHIN construction, KGE), and the downstream tasks where the embeddings are utilized.

## Candidate Generation Process (Who to Follow)

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["User"];
    B{"Query:<br>TwHIN User Embedding"};
    C{"Approximate Nearest Neighbor (ANN) Search"};
    D["Candidate Users"];
    E{"Multi-Modal Embeddings for Diversity"};
    F["Final Candidate List"];

    %% Notes
    %% label B "User's Mixture over KGE Embeddings"
    %% label C "HNSW or FAISS with Product Quantization"
   
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style C fill:#c3c5,stroke:#ccf,stroke-width:1px
    style E fill:#c3c5,stroke:#ccf,stroke-width:1px

  
```

**Explanation:** This diagram focuses on the "Who to Follow" candidate generation. It demonstrates how the embeddings are used to find similar users, leveraging ANN search and multi-modal mixtures for candidate diversity.

## Recommendation and Prediction Task Diagram

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["User & Contextual Info"];
    B{"Features<br>(Continuous, Categorical)"};
    C{"Categorical Features -> Embedding Lookup"};
    D["TwHIN Embeddings<br>(Pretrained, Frozen)"];
    E["Continuous Features"];
    F["Concatenation<br>(D + E)"];
    G{"Deep Neural Network<br>(DNN)<br>e.g., MLP"};
    H["Output:<br>Ranked List or Prediction Score"];

    A --> B
    B --> C
    C --> D
    B --> E
    E --> F
    F --> G
    G --> H

    style C fill:#c3c5,stroke:#333,stroke-width:1px
    style G fill:#c3c5,stroke:#ccf,stroke-width:1px
    style D fill:#c3c5,stroke:#afa,stroke-width:1px
    
    %% notes
    %% label H "Engagement or Click Probability"
```

**Explanation:** This diagram demonstrates how the TwHIN embeddings are used as features in recommendation and prediction tasks. It illustrates the DNN model architecture and details the role of the frozen embeddings, which are concatenated with other features and fed into the DNN.

## Compression for Low Latency

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["TwHIN Embeddings<br>(High Dim)"];
    B{"Product Quantization"}; 
    %% Note: label B is "FAISS"
    
    C["Codebook<br>(Centers)"];
    D{"Downstream Task Training<br>(Codebook Available)"};
    E["Compressed Embeddings"];
    F{"Inference Time:<br>Codebook Lookup"};
    G["Decompressed Embeddings"];
    H{"Downstream Task"};


    A --> B
    B --> C
    C --> D
    A --> E
    E --> F
    F --> G
    G --> H

    style B fill:#c3c5,stroke:#333,stroke-width:1px
    style F fill:#c3c5,stroke:#ccf,stroke-width:1px
    style G fill:#c3c5,stroke:#afa,stroke-width:1px

```

**Explanation:**  This diagram provides the compression strategy.  It demonstrates how product quantization is used to compress the embeddings, reducing latency, and how the codebook is utilized during both training and inference. The visual makes this easy to understand.

## Parameter Drift Mitigation

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["TwHIN v1 Embeddings"];
    B{"Update TwHIN<br>(New Data, New Network)"};
    C{"Naive Retraining<br>(High Drift)"};
    D{"Warm Start<br>(Initialize with v1)"};
    E["L2 Regularization<br>(Penalize Deviation)"];
    F["High Drift"];
    G["Low Drift"];


    %% Notes
    %% label B "Evolving Network Structure and Relationships"
    %% label D "New embeddings initialized with prior version"
    %% label G "Embeddings are stable and maintain previous properties"

    A --> B
    B --> C
    B --> D
    D --> E
    C --> F
    E --> G

    style C,D fill:#c3c5,stroke:#333,stroke-width:1px
    style E fill:#c3c5,stroke:#afa,stroke-width:1px
    style B fill:#c3c5,stroke:#ccf,stroke-width:1px
    
```

**Explanation:** This diagram illustrates the two methods used to address parameter drift: warm start (initializing the new version with the previous version's embeddings) and L2 regularization (penalizing large deviations).


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---