---
created: 2025-03-01 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/1706.03762"
---



# Wavelength
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


The diagram below visually summarizes the crucial aspect of wavelength in the Transformer's positional encoding:  a carefully chosen geometric progression of frequencies to encode both absolute and relative positions in the sequence.


```mermaid
---
title: Wavelengths
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
    A[Positional Encoding] --> B{Sine/Cosine Functions}
    B --> C(Wavelengths)
    C --> D[Geometric Progression]
    D --> E(2π)
    D --> F(10000 * 2π)
    
    subgraph Wavelength_Details["Wavelength Details"]
        E --> G{Frequency}
        F --> H{Frequency}
        G -.-> I[Increased by factor of 10000]
        H -.-> I
        
        G --> J(Dimension i)
        H --> J

        G -.-> K[pos/10000<sup>2i/d<sub>model</sub></sup>]
        H -.-> K
    end
    
```

----


### Explanation

The positional encoding in the Transformer uses sine and cosine functions with a specific pattern of increasing frequencies.  The diagram represents this as follows:

* **Positional Encoding:**  The starting point; it's the overall concept requiring positional information.
* **Sine/Cosine Functions:**  The mechanism used to embed positional information.
* **Wavelengths (Geometric Progression):**  The key characteristic highlighted; the frequencies of the sinusoids form a geometric progression.
* **2π, 10000 * 2π:**  These are the lower and upper bounds of the wavelengths, marking the beginning and end of the progression.
* **Frequency (Increased by Factor of 10000):** The diagram emphasizes that the frequency of the sine/cosine function in each dimension (i) increases exponentially.  This is crucial for the model to distinguish different positions in the sequence.
* **Dimension i:**  Each dimension of the positional encoding corresponds to a different frequency/wavelength.
* **Formula (pos/10000<sup>2i/d<sub>model</sub></sup>):** The formula for calculating the argument (angle) of the sine and cosine functions in each dimension (i) shows the geometric progression.  The `pos` represents the position of the token. `i` is the current dimension, and `d<sub>model</sub>` is the embedding dimension.

---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---