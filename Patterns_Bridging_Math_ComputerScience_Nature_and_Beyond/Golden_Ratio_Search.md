---
created: 2025-03-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Golden Ratio Search - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## 1. What is Golden Ratio Search? (High-Level Overview)

Golden Ratio Search is an efficient numerical optimization technique used to find the extremum (minimum or maximum) of a **unimodal function** within a given bounded interval. A unimodal function on an interval has only one peak (for maximum) or valley (for minimum). The key idea is to iteratively narrow down the interval containing the extremum by strategically placing two interior "probe" points based on the **Golden Ratio (φ)**. Unlike methods like Newton's method, it does not require the function's derivative.

```mermaid
---
title: Golden Ratio Search - High Level Concept
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
    subgraph Inputs
        style Inputs fill:#dde,stroke:#333
        F["Unimodal Function f(x)"]
        I["Initial Interval [a, b]"]
        T["Tolerance ε"]
    end

    subgraph Process["Golden Ratio Search"]
        style Process fill:#eef3,stroke:#333,stroke-width:2px
        P1["Iteratively Shrink Interval"]
        P2["Use Golden Ratio (φ) for Probe Points"]
        P3["Compare f(x) at Probe Points"]
        P4["No Derivatives Needed"]
    end

    subgraph Output
        style Output fill:#ded3,stroke:#333
        O["Interval containing the extremum<br>(size < ε)"]
        O2["Approximate location of Minimum/Maximum"]
    end

    Inputs --> Process
    Process --> Output
    Process -- Relies on --> K1[Unimodality]
    Process -- Uses --> K2[Golden Ratio φ]

    style K1 fill:#fcc3, stroke:#c33
    style K2 fill:#fcc3, stroke:#c33
```

---

## 2. Key Concepts and Terminology

*   **Unimodal Function:** A function `f(x)` is unimodal on an interval `[a, b]` if it has exactly one local minimum or maximum within that interval. For minimization, it means the function decreases, hits a minimum, and then increases.
*   **Interval `[a, b]`:** The initial range within which the extremum is known to exist.
*   **Golden Ratio (φ):** An irrational number approximately equal to **1.6180339887...**. It's defined as `(1 + √5) / 2`. A key property used is its reciprocal: `1/φ = φ - 1 ≈ 0.618`.
*   **Probe Points (c, d):** Two points chosen *inside* the current interval `[a, b]` where the function `f(x)` is evaluated. Their placement is determined by the Golden Ratio to ensure efficient interval reduction.
*   **Tolerance (ε):** A small positive number defining the desired precision. The search stops when the interval width (`b - a`) is less than ε.

```mermaid
---
title: Golden Ratio Search - Terminology
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
  root((Golden Ratio Search Concepts))
    Unimodal_Function
      Definition["Function with a single minimum OR maximum in the interval"]
      Importance["Essential prerequisite for the algorithm to guarantee convergence"]
      Visualization["Looks like a single 'valley' (min) or 'hill' (max)"]
    Interval_[a, b]
      Definition["The search space containing the extremum"]
      Role["Shrinks iteratively during the search"]
    Golden_Ratio_(φ)
      Value["(1 + √5) / 2 ≈ 1.618"]
      Reciprocal["1/φ = φ - 1 ≈ 0.618"]
      Usage["Determines placement of probe points `c` and `d`"]
    Probe_Points_(c, d)
      Location["Inside the current interval [a, b]"]
      Placement["c = a + (1 - 1/φ)*(b-a)<br>d = a + (1/φ)*(b-a)"]
      Symmetry["Symmetrically placed relative to interval scaled by φ"]
      Purpose["Function values f(c) and f(d) are compared to eliminate part of the interval"]
    Tolerance_(ε)
      Definition["Desired precision or stopping criterion"]
      Condition["Algorithm stops when b - a < ε"]
```

---

## 3. The Core Idea (How Interval Reduction Works)

The algorithm maintains an interval `[a, b]` known to contain the minimum. Two interior points `c` and `d` are chosen such that `a < c < d < b`. Their positions are calculated using the golden ratio's reciprocal (`1/φ ≈ 0.618`):

*   `c = a + (1 - 1/φ) * (b - a)`  (which is `a + (1/φ^2) * (b-a)`)
*   `d = a + (1/φ) * (b - a)`

This placement ensures symmetry and allows for efficient reuse. The function is evaluated at `c` and `d`.

1.  **If `f(c) < f(d)`:** The minimum *cannot* be in the interval `(d, b]`. The new interval becomes `[a, d]`. Notice that the *old* `c` becomes the *new* `d` (approximately, due to scaling) for the next iteration.
2.  **If `f(c) ≥ f(d)`:** The minimum *cannot* be in the interval `[a, c)`. The new interval becomes `[c, b]`. Notice that the *old* `d` becomes the *new* `c` for the next iteration.

In each step, the interval is reduced by a factor of `1/φ ≈ 0.618`, and crucially, **only one *new* function evaluation** is needed in the next iteration because one of the previous probe points and its function value are reused.

```mermaid
---
title: Golden Ratio Interval Reduction Principle
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
    A["Start with Interval [a, b]"]
    A --> B["Calculate probe points:<br>c = a + (1 - 1/φ)*(b-a)<br>d = a + (1/φ)*(b-a)"]
    B --> C["Evaluate f(c) and f(d)"]
    C --> D{"Compare f(c) vs f(d)"}

    subgraph Case1["If f(c) < f(d)"]
    style Case1 fill:#efe3, stroke:#393
        D -- "f(c) < f(d)" --> E["Minimum cannot be in (d, b]"]
        E --> F["New Interval:<br> [a, d]"]
        F --> G["Old 'c' can become new 'd'<br>Only need one new probe point"]
    end

    subgraph Case2["If f(c) ≥ f(d)"]
    style Case2 fill:#eff3, stroke:#339
        D -- "f(c) ≥ f(d)" --> H["Minimum cannot be in [a, c)"]
        H --> I["New Interval:<br> [c, b]"]
        I --> J["Old 'd' can become new 'c'<br>Only need one new probe point"]
    end

    G --> K((Next Iteration))
    J --> K
    K --> B

    note1["Note:<br> The new interval's width is approx.<br> 0.618 times the old width"]
    C -- Has --> note1
```

---

## 4. Algorithm Steps (Finding Minimum)

1.  **Initialization:**
    *   Define the unimodal function `f(x)`.
    *   Set the initial interval `[a, b]`.
    *   Choose the tolerance `ε > 0`.
    *   Calculate `invphi = 1/φ = (√5 - 1) / 2`.
    *   Calculate initial probe points:
        *   `c = a + (1 - invphi) * (b - a)`
        *   `d = a + invphi * (b - a)`
    *   Evaluate `fc = f(c)` and `fd = f(d)`.

2.  **Iteration Loop:** While `(b - a) > ε`:
    *   **Compare:**
        *   If `fc < fd`:
            *   Update `b = d` (discard `(d, b]`).
            *   Update `d = c` (old `c` is the new `d`).
            *   Update `fd = fc`.
            *   Calculate *new* `c = a + (1 - invphi) * (b - a)`.
            *   Evaluate *new* `fc = f(c)`.
        *   Else (`fc ≥ fd`):
            *   Update `a = c` (discard `[a, c)`).
            *   Update `c = d` (old `d` is the new `c`).
            *   Update `fc = fd`.
            *   Calculate *new* `d = a + invphi * (b - a)`.
            *   Evaluate *new* `fd = f(d)`.

3.  **Termination:** When `(b - a) ≤ ε`, the loop stops.
4.  **Result:** The minimum lies within the final interval `[a, b]`. Return the midpoint `(a + b) / 2` as the approximate location of the minimum.

```mermaid
---
title: Golden Ratio Search Algorithm Flowchart (Minimization)
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB28',
      'primaryTextColor': '#299',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
flowchart TD
    Start["Start"] --> INIT["Initialize a, b, ε<br>invphi = 1/φ<br>c = a + (1-invphi)*(b-a)<br>d = a + invphi*(b-a)<br>fc = f(c), fd = f(d)"]
    INIT --> LOOP_COND{b - a > ε?}
    LOOP_COND -- No --> TERM[Stop]
    TERM --> RESULT["Return (a + b) / 2"]

    LOOP_COND -- Yes --> COMPARE{fc < fd?}

    subgraph Update_Left["Update based on f(c) < f(d)"]
        style Update_Left fill:#efe3, stroke:#393
        COMPARE -- Yes --> B_UPDATE["b = d<br>(Discard right part)"]
        B_UPDATE --> D_UPDATE["d = c<br>(Reuse old c)"]
        D_UPDATE --> FD_UPDATE["fd = fc"]
        FD_UPDATE --> C_NEW["Calculate NEW c:<br>c = a + (1-invphi)*(b-a)"]
        C_NEW --> FC_NEW["Evaluate NEW fc = f(c)"]
    end

    subgraph Update_Right["Update based on f(c) ≥ f(d)"]
        style Update_Right fill:#eff3, stroke:#339
        COMPARE -- No --> A_UPDATE["a = c<br>(Discard left part)"]
        A_UPDATE --> C_UPDATE["c = d<br>(Reuse old d)"]
        C_UPDATE --> FC_UPDATE["fc = fd"]
        FC_UPDATE --> D_NEW["Calculate NEW d:<br>d = a + invphi*(b-a)"]
        D_NEW --> FD_NEW["Evaluate NEW fd = f(d)"]
    end

    FC_NEW --> LOOP_COND
    FD_NEW --> LOOP_COND
```

---

## 5. Example Illustration (Conceptual)

Imagine searching for the minimum in `[0, 10]`.

*   **Iter 0:** `[a=0, b=10]`. Calculate `c ≈ 3.82`, `d ≈ 6.18`. Evaluate `f(c)`, `f(d)`.
    *   Assume `f(c) > f(d)`.
*   **Iter 1:** New interval is `[c, b] = [3.82, 10]`. The *old* `d` (6.18) becomes the *new* `c`. We only need to calculate a *new* `d` within `[3.82, 10]` (around 7.64) and evaluate `f` at this new `d`.
    *   Assume `f(new_c) < f(new_d)`.
*   **Iter 2:** New interval is `[a, d] = [3.82, 7.64]`. The *old* `c` (6.18) becomes the *new* `d`. We only need to calculate a *new* `c` within `[3.82, 7.64]` (around 5.28) and evaluate `f` at this new `c`.
*   ... and so on, until the interval is sufficiently small.

```mermaid
---
title: Conceptual Illustration of Interval Shrinking
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
graph LR
    subgraph Iteration_0 ["Iteration 0: [a₀, b₀]"]
        I0["a₀ --- c₀ --- d₀ --- b₀"]
    end
    subgraph Evaluation_0 ["Evaluate f(c₀), f(d₀)<br>Assume f(c₀) ≥ f(d₀)"]
    end
    subgraph Iteration_1 ["Iteration 1: [a₁, b₁] = [c₀, b₀]"]
        I1["a₁ (=c₀) --- c₁ (=d₀) --- d₁ --- b₁ (=b₀)"]
    end
     subgraph Evaluation_1 ["Evaluate f(d₁)<br>Reuse f(c₁) = f(d₀)<br>Assume f(c₁) < f(d₁)"]
    end
     subgraph Iteration_2 ["Iteration 2: [a₂, b₂] = [a₁, d₁]"]
        I2["a₂ (=a₁) --- c₂ --- d₂ (=c₁) --- b₂ (=d₁)"]
    end
    subgraph Evaluation_2 ["Evaluate f(c₂)<br>Reuse f(d₂) = f(c₁)"]
    end


    Iteration_0 --> Evaluation_0
    Evaluation_0 --> Iteration_1
    Iteration_1 --> Evaluation_1
    Evaluation_1 --> Iteration_2
    Iteration_2 --> Evaluation_2
    Evaluation_2 --> Final["...Continue until b - a < ε"]

    style Iteration_0 fill:#eee3
    style Evaluation_0 fill:#ffe3
    style Iteration_1 fill:#eee3
    style Evaluation_1 fill:#ffe3
    style Iteration_2 fill:#eee3
    style Evaluation_2 fill:#ffe3
    style Final fill:#ddd3

```

---

## 6. Why the Golden Ratio?

The choice of the Golden Ratio is not arbitrary. It's the *unique* ratio that allows the interval reduction property where one of the *interior* points from the current step becomes one of the *interior* points for the next step, perfectly positioned according to the same ratio. This symmetry means that after the first iteration, **each subsequent iteration requires only *one* new function evaluation**, making it more efficient than a naive ternary search (which requires two new evaluations per step).

---

## 7. Time and Space Complexity

*   **Time Complexity:** The interval width is reduced by a constant factor (approximately 0.618) in each iteration. To reduce the interval from an initial width `W = b - a` down to `ε`, we need `k` iterations such that `W * (1/φ)^k ≤ ε`. Taking logarithms, this gives `k >= log(W/ε) / log(φ)`. Therefore, the time complexity is **O(log( (b-a)/ε ))**, which is logarithmic with respect to the ratio of the initial interval width to the desired precision. Since each iteration involves a constant number of calculations (one function evaluation after the first step, plus comparisons/assignments), the overall time is logarithmic.
*   **Space Complexity:** The algorithm only needs to store a few variables (a, b, c, d, fc, fd, ε, invphi). This is independent of the interval size or tolerance. Therefore, the space complexity is **O(1)** (constant).

---

## 8. Key Terms and Concepts (Summary Mind Map)

```mermaid
---
title: Golden Ratio Search - Concepts Summary
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
  root((Golden Ratio Search))
    Goal["Find min/max of a unimodal function in [a, b]"]
    Key_Features
      Iterative_Interval_Reduction
      Uses_Golden_Ratio_φ["≈ 1.618"]
      Requires_Unimodality
      No_Derivatives_Needed
    Core_Mechanism
      Probe_Points["c, d based on φ"]
      Comparison["Compare f(c) and f(d)"]
      Elimination["Discard part of interval based on comparison"]
      Reuse["One old probe point becomes a new probe point"]
      Efficiency["Only 1 new f(x) evaluation per iteration (after first)"]
    Prerequisites
      Function_f_x_["Functionf(x):<br> Must be Unimodal on [a, b]"]
      Interval_a_b["Interval [a, b]:<br>Initial bounds"]
      Tolerance_ε["Stopping criterion"]
    Algorithm_Steps
      Initialize["a, b, ε, calculate initial c, d, fc, fd"]
      Loop["While (b - a > ε)"]
        Compare["f(c) vs f(d)"]
        Update["a or b, reuse one point (c or d), calculate one new point"]
        Evaluate["New f(c) or f(d)"]
      Terminate["Return midpoint (a+b)/2"]
    Complexity
      Time["O(log((b-a)/ε)) - Logarithmic"]
      Space["O(1) - Constant"]
    Advantages
      Efficient["Converges linearly with rate ≈ 0.618"]
      Simple["Conceptually straightforward"]
      No_Derivatives
    Limitations
      Requires_Unimodality["Doesn't work for multi-modal functions"]
      Requires_Interval["Need initial bracket for the extremum"]

```



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---