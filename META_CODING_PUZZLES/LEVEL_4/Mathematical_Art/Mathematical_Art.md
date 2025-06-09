---
created: 2025-03-19 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Mathematical Art
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---

You are creating a special painting on a canvas which may be represented as a 2D Cartesian plane. You start by placing a thin brush at the origin (0,0)(0,0) and then make NN axis-aligned strokes without lifting the brush off of the canvas. For the iith stroke, you'll move your brush LiLi​ units from its current position in a direction indicated by the character DiDi​, which is either U (up), D (down), L (left), or R (right), while leaving behind a line segment of paint between the brush's current and new positions. For example, if L1=5L1​=5 and D1=D1​= L, you'll draw a stroke between coordinates (0,0)(0,0) and (−5,0)(−5,0), with your brush ending up at coordinates (−5,0)(−5,0). Note that each stroke is either horizontal or vertical, and that each stroke (after the first) begins where the previous stroke ended.

This painting is being marketed as a work of mathematical art, and its value is based on the number of times a certain mathematical symbol appears in it −− specifically, the plus sign. A plus sign is considered to be present at a certain position if and only if, for each of the 4 cardinal directions (up, down, left, and right), there's paint leading from the point in that direction (or, vice versa, leading to that point from that direction). Note that the paint from arbitrarily many strokes of your brush might come together to form any given plus sign, and that at most one plus sign may be considered to exist at any given position.

Determine the number of positions in the painting at which a plus sign is present.

## Constraints

```latex
2≤N≤2,000,000
1≤L_i​≤1,000,000,000
D_i​∈ {U, D, L, R}
```

## Sample test case #1

```md
N = 9 L = [6, 3, 4, 5, 1, 6, 3, 3, 4] 
D = ULDRULURD
```

```md
Expected Return Value = 4
```

## Sample test case #2

```md
N = 8 L = [1, 1, 1, 1, 1, 1, 1, 1]
D = RDLUULDR
```

```md
Expected Return Value = 1
```

## Sample test case #3

```md
N = 8 L = [1, 2, 2, 1, 1, 2, 2, 1]
D = UDUDLRLR
```

```md
Expected Return Value = 1
```

## Sample Explanation

The first case is depicted below, with blue arrows indicating brush strokes and the 44 plus signs highlighted in red:


![[Diagram_1.png]]

The second case is depicted below, with blue arrows indicating brush strokes and the single plus sign highlighted in red:

![[Diagram_2.png]]


In the third case, a single plus sign exists at coordinates (0,0)(0,0).


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---