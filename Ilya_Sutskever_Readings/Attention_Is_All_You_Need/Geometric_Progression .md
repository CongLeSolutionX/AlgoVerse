---
created: 2025-03-01 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://arxiv.org/pdf/1706.03762"
---



# Geometric Progression
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---

The diagram below clarifies the mathematical construction of the positional encoding scheme. The geometric progression of wavelengths is a key factor that helps the model distinguish different positions in the input sequence.  Critically, it explains how different dimensions of the positional encoding correspond to different frequencies, which are crucial to the model's ability to learn relationships between positions.

```mermaid
---
title: Geometric Progression in Positional Encoding
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
    A["Geometric Progression in Positional Encoding"] --> B{"Positional Encoding Dimensions"}
    B --> C(Dimension i)
    C --> D(Wavelength)
    D --> E(Formula)
    E --> F(Example)
    
    subgraph Formula_Explanation["Formula Explanation"]
        E --  PE(pos, 2i) = sin(pos / 10000<sup>(2i / d<sub>model</sub>)</sup>) --> G
        E --  PE(pos, 2i + 1) = cos(pos / 10000<sup>(2i / d<sub>model</sub>)</sup>) --> H
        
        G -- pos: Position --> I
        G -- i: Dimension --> J
        G -- d<sub>model</sub>: Embedding Dimension --> K
    end
    
    subgraph Example_Illustration["Example Illustration"]
        F -- pos = 1, i = 1, d<sub>model</sub> = 512 --> L("PE(1,2) ≈ sin(1/10000)")
        F -- pos = 1, i = 2, d<sub>model</sub> = 512 --> M("PE(1,3) ≈ cos(1/50)")
        F -- pos = 1, i = 10, d<sub>model</sub> = 512 --> N("PE(1,21) ≈ sin(1/50)")

        F -- pos = 2, i = 1, d<sub>model</sub> = 512 --> O("PE(2,2) ≈ sin(2/10000)")
    end
    
    subgraph Geometric_Progression_Detail["Geometric Progression Detail"]
      F --> P[Geometric Progression in Wavelengths]
      P --> Q{Wavelengths Increase}
      Q -- 2π --> R(2π)
      Q -- 10000*2π --> S(10000*2π)
    end
    
```

----

### Explanation 

* **Clear Node Labels:** Each node represents a specific element in the geometric progression formula and concept.
* **Formula Explanation Subgraph:** This section focuses on the formula itself, explaining the variables (pos, i, d<sub>model</sub>) and their roles in the calculation of positional encodings.
* **Example Illustration Subgraph:**  Illustrates how different values for position (pos), dimension (i), and embedding dimension (d<sub>model</sub>) lead to different sine/cosine values.
* **Geometric Progression Detail Subgraph:**  Focuses on the geometric progression aspect of the wavelengths.  The wavelength is increasing exponentially, allowing the model to distinguish different positions.
* **Connections:** Arrows show the relationships between the concepts.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---