---
created: 2025-03-19 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Mathematical Art - Pythons Syntax Solution
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


The Python code maintains the same logic, efficiency, and correctness as the Swift code.  The time and space complexity analysis remains the same: O(N^3) time complexity and O(N) space complexity. The core algorithm and data structures are equivalent.


```python
from typing import List, Set, Tuple

def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    # 1. Represent Lines (using tuples: (x1, y1, x2, y2))
    horizontal_lines: Set[Tuple[int, int, int, int]] = set()
    vertical_lines: Set[Tuple[int, int, int, int]] = set()

    # 2. Keep track of all used x and y coordinates
    all_x = set()
    all_y = set()

    # 3. Draw Lines
    current_x = 0
    current_y = 0
    all_x.add(0)
    all_y.add(0)

    for i in range(N):
        length = L[i]
        direction = D[i]
        next_x = current_x
        next_y = current_y

        if direction == "U":
            next_y += length
            vertical_lines.add((current_x, min(current_y, next_y), current_x, max(current_y, next_y)))
        elif direction == "D":
            next_y -= length
            vertical_lines.add((current_x, min(current_y, next_y), current_x, max(current_y, next_y)))
        elif direction == "L":
            next_x -= length
            horizontal_lines.add((min(current_x, next_x), current_y, max(current_x, next_x), current_y))
        elif direction == "R":
            next_x += length
            horizontal_lines.add((min(current_x, next_x), current_y, max(current_x, next_x), current_y))

        all_x.add(next_x)
        all_y.add(next_y)
        current_x = next_x
        current_y = next_y

    # 4. Check for Plus Signs
    plus_count = 0

    for x in all_x:
        for y in all_y:
            # Check for lines in all four directions
            has_up = False
            has_down = False
            has_left = False
            has_right = False

            for line in vertical_lines:
                if line[0] == x and line[1] <= y <= line[3] and line[1] != line[3]:
                    if y < line[3]:
                        has_up = True
                    if y > line[1]:
                        has_down = True

            for line in horizontal_lines:
                if line[1] == y and line[0] <= x <= line[2] and line[0] != line[2]:
                    if x < line[2]:
                        has_right = True
                    if x > line[0]:
                        has_left = True
            
            if has_up and has_down and has_left and has_right:
                plus_count += 1

    return plus_count

# Test Cases
N1 = 9
L1 = [6, 3, 4, 5, 1, 6, 3, 3, 4]
D1 = "ULDRULURD"
print(getPlusSignCount(N1, L1, D1))  # Output: 4

N2 = 8
L2 = [1, 1, 1, 1, 1, 1, 1, 1]
D2 = "RDLUULDR"
print(getPlusSignCount(N2, L2, D2))  # Output: 1

N3 = 8
L3 = [1, 2, 2, 1, 1, 2, 2, 1]
D3 = "UDUDLRLR"
print(getPlusSignCount(N3, L3, D3))  # Output: 1

N4 = 2
L4 = [1000000000, 999999999]
D4 = "UL"
print(getPlusSignCount(N4, L4, D4))  # 0

N5 = 4
L5 = [1,1,1,1]
D5 = "RULD"
print(getPlusSignCount(N5, L5, D5)) # 1

N6 = 4
L6 = [2, 1, 1, 3]
D6 = "ULRD"
print(getPlusSignCount(N6, L6, D6))#0
```

Key changes and explanations:

*   **Type Hinting:**  Used `from typing import List, Set, Tuple` for type hinting, improving code readability and maintainability.
*   **Sets:**  Used Python's built-in `set` data structure for `horizontal_lines` and `vertical_lines`.  Sets provide efficient membership testing (checking if a line is present).
*   **Tuples:** Represented lines as tuples `(x1, y1, x2, y2)`. Tuples are immutable and hashable, making them suitable for use in sets.
*   **String Indexing:**  `D` is a string in the Python version, so we directly access characters using indexing (e.g., `D[i]`).
*   **`if/elif/else`:**  Used `if/elif/else` for the direction checking, which is the standard way to handle mutually exclusive conditions in Python.
* **Consistent Naming:** All variables follow the Python naming convention.
*   **Test Cases:**  The test cases are adapted to the Python function signature.





---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---