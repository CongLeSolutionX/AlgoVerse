---
created: 2025-03-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Metallic Means - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


This set of diagrams and explanations covers the definition, specific examples (especially the Silver Ratio), mathematical properties, and connections to recursive sequences for the family of Metallic Means.



## 1. Introduction: What are Metallic Means?

Metallic Means (or Metallic Ratios) are a family of irrational numbers that generalize the concept of the Golden Ratio. Each Metallic Mean is defined as the positive solution to a specific quadratic equation, characterized by a natural number 'n'. They often appear as limiting ratios in certain recursively defined sequences, similar to how the Golden Ratio arises from the Fibonacci sequence.

```mermaid
---
title: Metallic Means - High-Level Concept
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'themeVariables': {
      'fontSize': '12px',
      'fontFamily': 'Fantasy'
    }
  }
}%%
mindmap
  root((Metallic Means))
    Definition["Family of irrational numbers"]
    Generalization["Extends the concept of the Golden Ratio (φ)"]
    Origin["Positive solutions to x² - nx - 1 = 0<br/>(for n = 1, 2, 3, ...)"]
    Relation_to_Sequences["Limiting ratio of terms in sequences like aₖ = n⋅aₖ₋₁ + aₖ₋₂"]
    Examples
      Golden_Ratio["n = 1"]
      Silver_Ratio["n = 2"]
      Bronze_Ratio["n = 3"]
      ...["and so on"]
```

---

## 2. Mathematical Definition

The Metallic Mean associated with the natural number *n*, often denoted as $\sigma_n$, is defined as the positive root of the quadratic equation:

$$
x^2 - nx - 1 = 0
$$

Using the quadratic formula ($x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ with a=1, b=-n, c=-1):

$$
x = \frac{-(-n) \pm \sqrt{(-n)^2 - 4(1)(-1)}}{2(1)} = \frac{n \pm \sqrt{n^2 + 4}}{2}
$$

Since we are interested in the *positive* root, the n-th Metallic Mean is:

$$
\sigma_n = \frac{n + \sqrt{n^2 + 4}}{2}
$$

```mermaid
---
title: Derivation of the Metallic Mean Formula
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    A["Defining Equation<br><b>x² - nx - 1 = 0</b>"] --> B["Quadratic Formula<br>x = [-b ± √(b²-4ac)] / 2a"];
    B --> C["Substitute<br>a=1, b=-n, c=-1"];
    C --> D["Intermediate<br>x = [n ± √(n²+4)] / 2"];
    D --> E["Select Positive Root"];
    E --> F["Metallic Mean Formula<br><b>σ<SUB>n</SUB> = [n + √(n²+4)] / 2</b>"];

    style A fill:#eef3,stroke:#333,stroke-width:1px
    style F fill:#dde3,stroke:#333,stroke-width:2px
```

---

## 3. The Golden Ratio (n=1)

The most famous Metallic Mean is the Golden Ratio (φ), which corresponds to the case where **n = 1**.

*   **Equation:** $x^2 - x - 1 = 0$
*   **Value:** $\sigma_1 = \phi = \frac{1 + \sqrt{1^2 + 4}}{2} = \frac{1 + \sqrt{5}}{2} \approx 1.618...$
*   **Associated Sequence (Fibonacci):** $F_k = F_{k-1} + F_{k-2}$ (with $F_0=0, F_1=1$). The ratio of consecutive Fibonacci numbers approaches φ: $\lim_{k \to \infty} \frac{F_k}{F_{k-1}} = \phi$.

```mermaid
---
title: The Golden Ratio (Metallic Mean for n=1)
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    subgraph Golden_Ratio ["Golden Ratio (φ) - Case n=1"]
        style Golden_Ratio fill:#fef4,stroke:#a60,stroke-width:1px
        A["n = 1"] --> B["Equation<br>x² - x - 1 = 0"];
        A --> C["Value<br>φ = [1 + √5] / 2<br>≈ 1.618..."];
        A --> D["Associated Sequence<br>Fibonacci: F<SUB>k</SUB> = F<SUB>k-1</SUB> + F<SUB>k-2</SUB>"];
        D --> E["Limit Property<br>lim (F<SUB>k</SUB> / F<SUB>k-1</SUB>) = φ"];
    end
```

---

## 4. The Silver Ratio (n=2)

The Silver Ratio, often denoted as $\delta_s$ (delta-s), is the Metallic Mean corresponding to the case where **n = 2**.

*   **Equation:** $x^2 - 2x - 1 = 0$
*   **Value:** $\sigma_2 = \delta_s = \frac{2 + \sqrt{2^2 + 4}}{2} = \frac{2 + \sqrt{8}}{2} = \frac{2 + 2\sqrt{2}}{2} = 1 + \sqrt{2} \approx 2.414...$
*   **Associated Sequence (Pell Numbers):** $P_k = 2 P_{k-1} + P_{k-2}$ (with $P_0 = 0, P_1 = 1$). The sequence starts 0, 1, 2, 5, 12, 29, 70, ... The ratio of consecutive Pell numbers approaches $\delta_s$: $\lim_{k \to \infty} \frac{P_k}{P_{k-1}} = \delta_s$.
*   **Geometry:** The Silver Ratio appears in the regular octagon. The ratio of the long diagonal to the side length is $1 + \sqrt{2}$ ($\delta_s$).

```mermaid
---
title: The Silver Ratio (Metallic Mean for n=2)
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    subgraph Silver_Ratio ["Silver Ratio (δ<SUB>s</SUB>) - Case n=2"]
        style Silver_Ratio fill:#eff3,stroke:#33a,stroke-width:1px
        A["n = 2"] --> B["Equation<br>x² - 2x - 1 = 0"];
        A --> C["Value<br>δ<SUB>s</SUB> = 1 + √2<br>≈ 2.414..."];
        A --> D["Associated Sequence<br>Pell Numbers: P<SUB>k</SUB> = 2⋅P<SUB>k-1</SUB> + P<SUB>k-2</SUB>"];
        D --> E["Limit Property<br>lim (P<SUB>k</SUB> / P<SUB>k-1</SUB>) = δ<SUB>s</SUB>"];
        A --> F["Geometric Link<br>Regular Octagon<br>(Diagonal / Side)"]
    end
```

---

## 5. Other Metallic Means (n=3, 4, ...)

Following the pattern for increasing values of *n*:

*   **Bronze Ratio (n=3):**
    *   Equation: $x^2 - 3x - 1 = 0$
    *   Value: $\sigma_3 = \frac{3 + \sqrt{3^2 + 4}}{2} = \frac{3 + \sqrt{13}}{2} \approx 3.303...$
    *   Sequence: $a_k = 3 a_{k-1} + a_{k-2}$

*   **Copper Ratio (n=4) (Note: Less standard terminology):**
    *   Equation: $x^2 - 4x - 1 = 0$
    *   Value: $\sigma_4 = \frac{4 + \sqrt{4^2 + 4}}{2} = \frac{4 + \sqrt{20}}{2} = 2 + \sqrt{5} \approx 4.236...$
    *   Sequence: $a_k = 4 a_{k-1} + a_{k-2}$

*   ...and so on for n = 5, 6, ...

```mermaid
---
title: Family of Metallic Means
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    Root("Metallic Means σ<SUB>n</SUB>");

    subgraph Mean_Examples
    style Mean_Examples fill:#fff4,stroke:#555,stroke-width:1px
        N1("n=1") --> G["Golden Ratio (φ)<br>[1 + √5] / 2"];
        N2("n=2") --> S["Silver Ratio (δ<SUB>s</SUB>)<br>1 + √2"];
        N3("n=3") --> B["Bronze Ratio<br>[3 + √13] / 2"];
        N4("n=4") --> C["'Copper' Ratio<br>2 + √5"];
        N5("n=...") --> D["... and so on"];
    end

    Root --> N1;
    Root --> N2;
    Root --> N3;
    Root --> N4;
    Root --> N5;

    style G fill:#fc33,stroke:#a60
    style S fill:#ef33,stroke:#33a
    style B fill:#fc33,stroke:#a60
    style C fill:#fd33,stroke:#a60
```

---

## 6. General Properties

Metallic means share several interesting properties:

*   **Irrational Numbers:** All metallic means ($\sigma_n$ for $n \ge 1$) are irrational numbers.
*   **Continued Fractions:** They have simple periodic continued fraction representations:
    $$
    \sigma_n = n + \frac{1}{n + \frac{1}{n + \frac{1}{n + \ddots}}} = [n; n, n, n, ...]
    $$
    For example:
    *   Golden Ratio (n=1): $\phi = [1; 1, 1, 1, ...]$
    *   Silver Ratio (n=2): $\delta_s = [2; 2, 2, 2, ...]$
*   **Algebraic Integers:** They are algebraic integers, specifically Pisot–Vijayaraghavan numbers under certain conditions.

```mermaid
---
title: General Properties of Metallic Means
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'themeVariables': {
      'fontSize': '12px',
      'fontFamily': 'Fantasy'
    }
  }
}%%
mindmap
  root(("Properties of σ<SUB>n</SUB> = [n + √(n²+4)] / 2"))
    Basic
      Irrationality["Always irrational for n ≥ 1"]
      Algebraic_Integers["Algebraic Integers:<br> Roots of monic polynomials with integer coefficients"]
    Continued_Fractions
      Simple_Form["Simple Form:<br>[n; n, n, n, ...]"]
      Examples
        Golden_n1["Golden n1:<br> φ = [1; 1, 1, ...]"]
        Silver_n2["Silver n2:<br> δ<SUB>s</SUB> = [2; 2, 2, ...]"]
        Bronze_n3["Bronze n3:<br> σ<SUB>3</SUB> = [3; 3, 3, ...]"]
```

---

## 7. Associated Recursive Sequences

Each Metallic Mean $\sigma_n$ is the limiting ratio of consecutive terms in a generalized Fibonacci-like sequence defined by:

$$
a_k = n \cdot a_{k-1} + a_{k-2}
$$

Given appropriate starting values (like $a_0 = 0, a_1 = 1$), the limit holds:

$$
\lim_{k \to \infty} \frac{a_k}{a_{k-1}} = \sigma_n = \frac{n + \sqrt{n^2 + 4}}{2}
$$

```mermaid
---
title: "Associated Recursive Sequences"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    "flowchart": { "htmlLabels": false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    A["Metallic Mean σ<SUB>n</SUB>"] -- arises from --> B["Recursive Sequence<br><b>a<SUB>k</SUB> = n ⋅ a<SUB>k-1</SUB> + a<SUB>k-2</SUB></b>"]
    B -- "For initial values like a<sub>0</sub>=0, a<SUB>1</SUB>=1" --> C["Ratio of Consecutive Terms"]
    C --> D["Limit Property<br><b>lim (a<SUB>k</SUB> / a<SUB>k-1</SUB>) = σ<SUB>n</SUB></b><br>as k → ∞"]

    subgraph Examples_Lookup["Examples<br>(n → Sequence Name → Limit)"]
     style Examples_Lookup fill:#ffa3,stroke:#777,stroke-width:1px
        E["n=1 → Fibonacci → Golden Ratio (φ)"]
        F["n=2 → Pell Numbers → Silver Ratio (δ<SUB>s</SUB>)"]
        G["n=3 → 'Bronze' Sequence → Bronze Ratio (σ<SUB>3</SUB>)"]
    end

    A -.-> E & F & G

    style B fill:#ccf3,stroke:#00a
    style D fill:#cfc3,stroke:#0a0
    
```


---

## 8. Summary Mind Map

This mind map brings together the core concepts related to the Silver Ratio and the broader family of Metallic Means.

```mermaid
---
title: Metallic Means - Comprehensive Summary
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'themeVariables': {
      'fontSize': '12px',
      'fontFamily': 'Fantasy'
    }
  }
}%%
mindmap
  root((Metallic Means / Ratios))
    Definition["Generalization of Golden Ratio"]
    Core_Equation["Positive root of <b>x² - nx - 1 = 0</b> (n=1, 2, 3,...)"]
    Formula["<b>σ<SUB>n</SUB> = [n + √(n²+4)] / 2</b>"]
    Specific_Means
      Golden_Ratio (n=1)
        Value["φ ≈ 1.618"]
        Sequence["Fibonacci"]
      Silver_Ratio (n=2)
        Value["δ<SUB>s</SUB> = 1 + √2 ≈ 2.414"]
        Sequence["Pell Numbers"]
        Geometry["Octagon"]
      Bronze_Ratio (n=3)
        Value["σ<SUB>3</SUB> ≈ 3.303"]
        Sequence["a<SUB>k</SUB> = 3a<SUB>k-1</SUB> + a<SUB>k-2</SUB>"]
      Higher_Means["n=4, 5, ..."]
    Associated_Sequences
      Recurrence["<b>a<SUB>k</SUB> = n ⋅ a<SUB>k-1</SUB> + a<SUB>k-2</SUB></b>"]
      Limit_Ratio["lim (a<SUB>k</SUB> / a<SUB>k-1</SUB>) = σ<SUB>n</SUB>"]
    Properties
      Irrationality["All are irrational"]
      Continued_Fractions["Simple periodic: [n; n, n, ...]"]
      Algebraic_Integers

```


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---