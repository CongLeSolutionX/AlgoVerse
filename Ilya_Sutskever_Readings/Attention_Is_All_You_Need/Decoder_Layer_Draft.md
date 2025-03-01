---
created: 2025-03-01 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/1706.03762"
---



# Decoder Layer
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
title: Decoder Layer
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
    subgraph Decoder_Layer["Decoder Layer"]
        A[Input] --> B(Decoder Embeddings)
        B --> C[Positional Encodings]
        C --> D[Layer 1]

        subgraph Layer_i["Layer i"]
        style Layer_i fill:#c221,stroke:#333,stroke-width:2px
            E["Multi-Head Self-Attention<br>(Masked)"] --> F[Output]
            F --> G[Layer Normalization]
            G --> H[Encoder-Decoder Attention]
            H --> I[Output]
            I --> G
            G --> J[Position-wise Feed-Forward Network]
            J --> G
        end

        D --> E
        D --> H
        
        D --> K[Layer 2]
        
        subgraph Layer_i["Layer i"]
        style Layer_i fill:#c221,stroke:#333,stroke-width:2px
            L["Multi-Head Self-Attention<br>(Masked)"] --> M[Output]
            M --> N[Layer Normalization]
            N --> O[Position-wise Feed-Forward Network]
            O --> N
        end
        
        K --> L
        
        %% Repeat the Layer_i subgraph for Layer 3, 4, ..., N-1

        subgraph Layer_i["Layer i"]
        style Layer_i fill:#cf33,stroke:#333,stroke-width:2px
            P["Multi-Head Self-Attention<br>(Masked)"] --> Q[Output]
            Q --> R[Layer Normalization]
            R --> S[Position-wise Feed-Forward Network]
            S --> R
            
            %% Final Output of the Decoder Layer
            R --> T[Output]
        end

        K --> P
    end
    
```

Note: FIX_ME_LATER


----

### Explanation

*   **Input:** The input to the decoder layer is the output of the previous layer in the decoder stack (or the initial input embeddings if it's the first layer).
*   **Positional Encodings:** As in the encoder, positional encodings are added to the decoder embeddings for positional information.
*   **Multi-Head Self-Attention (Masked):** Critically, the self-attention in the decoder is masked.  The `Masked` label signifies that connections to *future* positions in the output sequence are blocked (i.e., positions to the right).  This is essential to preserve the auto-regressive nature of the decoder.  This is *very* important, and often missed in visualizations.
*   **Encoder-Decoder Attention:** This attention mechanism allows the decoder to attend to the output of the entire encoder stack.
*   **Position-wise Feed-Forward Network:** The same structure as in the encoder.
*   **Layer Normalization:**  Applied after each sub-layer.
*   **Repeated Layers (Ellipsis):**  The `...` indicates that identical layers are repeated for each decoder layer.  The key takeaway here is that the layers are functionally equivalent.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---