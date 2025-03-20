---
created: 2025-03-19 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Conveyor Chaos
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


A distribution center moves packages around using a system of conveyor belts, which can be represented as line segments on the 2D Cartesian plane. The `ith` conveyor belt runs from coordinates `(A_i,H_i)` to `(B_i,H_i)`. No two conveyor belts share any points in common, including endpoints or interior points. Gravity points in the direction of the negative y-axis, meaning that objects normally fall vertically downwards, with their y-coordinate decreasing over time.

Each conveyor belt runs to either the left or the right. A package can be considered to occupy a single point on the plane. If a package lands strictly within conveyor belt `i` (excluding its endpoints), then it will be transported to its left or right end (either `(A_i,H_i)` or `(B_i,H_i)`), depending on the conveyor belt's direction, before continuing to fall vertically downwards.

You'll start by selecting a single conveyor belt and choosing a fixed direction (either left or right) for it to run in. Then, random directions will be independently chosen for each of the remaining `N−1` conveyor belts (each being either left or right with equal probability). Finally, a single package will be dropped into the system from high above, at coordinates `(x,1,000,000)`, where x is a real value drawn uniform randomly from the inclusive interval `[0,1,000,000]`. Your objective is to minimize the expected horizontal distance which this package will travel along conveyor belts before hitting the ground (any point with `y-coordinate 0`).

For example, consider the following system of conveyor belts (as are present in the second sample case):

![[Conveyor_Chaos/Diagram_1.png]]

Consider picking the conveyor belt at y-coordinate `5` and causing it to run to the left. If it then so happens that the bottommost conveyor belt also runs to the left while the other three run to the right and the package falls at x-coordinate  `3,000`, then the package will travel a total of `6,000` units horizontally across conveyor belts, as illustrated below:

![[Conveyor_Chaos/Diagram_2.png]]

Determine the minimum achievable expected horizontal distance traveled by the package assuming an ideal initial choice of conveyor belt and direction.

Note: Your return value must have an absolute or relative error of at most `10^−6` to be considered correct.

## Constraints

```md
1≤N≤500,000
1≤H_i​≤999,999
0≤A_i​<B_i​≤1,000,000
```

## Sample test case #1

```md
N = 2
H = [10, 20]
A = [100000, 400000]
B = [600000, 800000]
```

```md
Expected Return Value = 155000.00000000
```

## Sample test case #2

```md
N = 5
H = [2, 8, 5, 9, 4]
A = [5000, 2000, 7000, 9000, 0]
B = [7000, 8000, 11000, 11000, 4000]
```

```md
Expected Return Value = 36.50000000
```

## Sample Explanation

In the first case, there are two conveyor belts, as depicted below:

![[Diagram_3.png]]

You should pick the second conveyor belt and cause it to run to the right. Packages falling at x-coordinates in the intervals `[0,100,000]` and `[800,000,1,000,000]` will fall directly to the ground (with 0 horizontal travel distance), while packages falling at x-coordinates in the interval `(400,000,800,000)` will have an average horizontal travel distance of `200,000` units. This leaves packages falling at x-coordinates in the interval `(100,000,400,000]`, which will have an average horizontal travel distance of either `150,000` units (if the first conveyor belt runs to the left) or `350,000` units (if it runs to the right). This yields an overall expected horizontal travel distance of `0∗0.3+200,000∗0.4+((150,000+350,000)/2)∗0.3=155,000`, which is the minimum achievable expected horizontal travel distance.

The second case is depicted above. In it, you should pick the third conveyor belt and cause it to run to the left.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---