---
created: 2025-03-01 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/1706.03762"
---



# Positional Encodings
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---

The diagram below captures the essence of the positional encoding scheme, emphasizing the key elements of the method and their relationships. It's vital to remember that this is a simplified visual representation. The actual implementation involves embedding vectors, summing them with positional encoding vectors, and applying this to the input sequences.


```mermaid
---
title: Positional Encodings
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
    A["Positional Encodings"] --> B(Purpose)
    B --> C["Incorporating Order"]
    B --> D["Learning Relative/Absolute Position"]

    A --> E(Method)
    E --> F[Sine and Cosine Functions]
    F --> G{Frequency}
    G -- pos/10000<sup>2i/d<sub>model</sub></sup> --> H(Sine, Cosine)
    
    subgraph Positional_Encoding_Example["Positional Encoding Example"]
    style Positional_Encoding_Example fill:#2c24,stroke:#333,stroke-width:2px
        H --> I(PE<sub>pos, 2i</sub>)
        I -- sin(pos/10000<sup>2i/d<sub>model</sub></sup>) --> J[Example]
        H --> K(PE<sub>pos, 2i+1</sub>)
        K -- cos(pos/10000<sup>2i/d<sub>model</sub></sup>) --> J
        
        J -- pos: Position, i: Dimension --> L[Example]
    end
    
    E --> M[Learned Positional Embeddings]
    M --> N(Alternative Method)
    M --> O[Nearly Identical Results]
    
    E --> P(Wavelengths)
    P --> Q[Geometric Progression]
    Q --> R[2π to 10000*2π]
    
    E --> S[Extrapolation]
    S --> T[Longer Sequences]

```


----

### Explanation


* **Purpose (B):**  Positional encodings are crucial because the Transformer architecture lacks recurrence and convolution.  They provide the model with information about the order and relative position of tokens in the input sequence.
* **Method (E):** The method used in the paper is a learned positional embedding based on sine and cosine functions of different frequencies.
* **Sine and Cosine Functions (F):** The positional encoding for each position and dimension (i) is calculated using sine and cosine functions.
* **Frequency (G):** The frequency of the sinusoid in each dimension increases in a geometric progression, creating unique encoding for different positions.
* **Positional Encoding Example (Subgraph):**  This subgraph illustrates the calculation for PE<sub>pos, 2i</sub> and PE<sub>pos, 2i+1</sub>.  It shows that the position and dimension (i) are input parameters, and the calculated PE values are outputs.
* **Learned Positional Embeddings (M):** This provides an alternative method that learned position embeddings directly instead of using sinusoids.
* **Wavelengths (P):** The wavelengths form a geometric progression.
* **Extrapolation (S):**  The use of sine/cosine allows the model to potentially extrapolate to sequence lengths beyond those seen during training.

---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---