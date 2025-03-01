---
created: 2025-03-01 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/1706.03762"
---



# Attention Mechanisms
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


```mermaid
---
title: Attention Mechanisms
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%{
  init: {
    'fontFamily': 'verdana',
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
    subgraph Attention_Mechanisms["Attention Mechanisms"]
    style Attention_Mechanisms fill:#f2551,stroke:#333,stroke-width:2px
        A[Attention Function] --> B(Query, Key, Value)
        B --> C(Compatibility Function)
        C --> D(Weights)
        D --> E[Softmax Function]
        E --> F(Output)
        B -- Key-Value Pairs --> G[Values]
        B -- Query --> H[Query]
        
        subgraph Scaled_Dot_Product_Attention["Scaled Dot Product Attention"]
        style Scaled_Dot_Product_Attention fill:#2599,stroke:#333,stroke-width:2px
            I[Scaled Dot-Product Attention] --> J(Queries Q, Keys K, Values V)
            J -- QK<sup>T</sup> --> K[Scaled Dot Product]
            K -- 1/√d<sub>k</sub> --> L[Scaled Dot Product]
            L --> M[Softmax]
            M --> N[Output]
            J -- V --> O[Output Weighted Sum]
        end

        subgraph Multi_Head_Attention["Multi-Head Attention"]
        style Multi_Head_Attention fill:#c259,stroke:#333,stroke-width:2px
            P[Multi-Head Attention] --> Q(Queries Q, Keys K, Values V)
            Q -- W<sub>Q</sub>, W<sub>K</sub>, W<sub>V</sub> --> R[Linear Projections]
            R --> S[Scaled Dot-Product Attention]
            S --> T[Concatenated Heads]
            T -- W<sub>O</sub> --> U[Final Projection]
            U --> V[Multi-Head Output]
        end

        subgraph Comparison_of_Attention_Functions["Comparison of Attention Functions"]
        style Comparison_of_Attention_Functions fill:#cc24,stroke:#333,stroke-width:2px
            W[Additive Attention] --> X(Query, Key)
            X -- Feedforward Network --> Y[Compatibility Function]
            Y --> Z[Softmax]
            Z --> AA[Output]
            
            BB[Dot-Product Attention] --> CC(Query, Key)
            CC -- Dot Product --> DD[Softmax]
            DD --> EE[Output]
        end

        subgraph Applications_of_Attention["Applications of Attention"]
        style Applications_of_Attention fill:#cf33,stroke:#333,stroke-width:2px
            FF[Encoder-Decoder Attention] --> GG(Queries from Decoder, Keys/Values from Encoder)
            GG --> HH[Global Context Attention]
            
            II[Encoder Self-Attention] --> JJ(Keys/Values/Queries from Encoder)
            JJ --> KK[Information Aggregation]
            
            LL[Decoder Self-Attention] --> MM(Keys/Values/Queries from Decoder)
            MM --> NN[Auto-regressive Masking]
        end
    end
    
```

----


### Explanation

*   **Overall Structure:** The main subgraph "Attention Mechanisms" now encompasses various types and aspects of attention.
*   **Scaled Dot-Product Attention:** This section is clearly depicted as a subgraph, illustrating the core components: Queries, Keys, Values, scaled dot product, and softmax.  Critically, it highlights the scaling factor 1/√d<sub>k</sub>.
*   **Multi-Head Attention:**  A subgraph dedicated to multi-head attention, emphasizing the parallel processing of multiple attention heads through linear projections (W<sub>Q</sub>, W<sub>K</sub>, W<sub>V</sub>) and concatenation.  The final projection (W<sub>O</sub>) is also shown.
*   **Comparison of Attention Functions:** A subgraph that contrasts scaled dot-product attention with additive attention, highlighting the computational benefits of the dot-product approach (speed and space efficiency).
*   **Applications of Attention:** This crucial section is now clearly visualized, with subgraphs for encoder-decoder attention, encoder self-attention, and decoder self-attention, showing how attention is used in different parts of the Transformer architecture, including auto-regressive masking in the decoder.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---