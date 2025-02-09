---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---


# Quick Sort Algorithm Framework  - Mermaid diagrams

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## **1. Flowchart of the Quick Sort Algorithm**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> A["QuickSort(array, low, high)"]
    A --> B{low < high}
    B -- Yes --> C[Partition the array]
    C --> D[pi = partition index]
    D --> E["QuickSort(array, low, pi - 1)"]
    E --> F["QuickSort(array, pi + 1, high)"]
    F --> G[Merge results]
    G --> H[Return]
    B -- No --> H[Return]
    H --> End([End])
    
```


**Explanation:**

- **Start:** Begin the Quick Sort algorithm.
- **Check Condition:** If `low < high`, proceed to partitioning; else, return.
- **Partition:** The array is partitioned around a pivot element.
- **Recursive Calls:** Quick Sort is called recursively on the left and right subarrays.
- **Merge and Return:** Results are merged (though Quick Sort is an in-place sort and doesn't explicitly merge) and the function returns.

---

## **2. Recursion Tree in Best-Case Scenario**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TB
    A[Array Size: n]
    A -->|Divide| B[Size: n/2]
    A -->|Divide| C[Size: n/2]
    B -->|Divide| D[Size: n/4]
    B -->|Divide| E[Size: n/4]
    C -->|Divide| F[Size: n/4]
    C -->|Divide| G[Size: n/4]
    D --> H[...]
    E --> I[...]
    F --> J[...]
    G --> K[...]
    
```


**Explanation:**

- The array is divided into two equal halves at each level.
- The height of the recursion tree is `log n`.
- Total work at each level is `n`.
- **Total Time Complexity:** $O(n \log n)$

---

## **3. Recursion Tree in Worst-Case Scenario**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    A[Array Size: n] --> B["Size: n - 1"]
    B --> C["Size: n - 2"]
    C --> D["Size: n - 3"]
    D --> E[...]
    E --> F["Size: 1"]
    
```


**Explanation:**

- The pivot always partitions the array into sizes `n-1` and `0`.
- The recursion tree is skewed, resembling a linked list.
- The height of the recursion tree is `n`.
- **Total Time Complexity:** $O(n^2)$.

---

## **4. Comparison of Time Complexities**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    A[Quick Sort Time Complexities]
    A --> B(Best Case)
    A --> C(Average Case)
    A --> D(Worst Case)

    B --> B1[Balanced Partitions]
    C --> C1[Random Partitions]
    D --> D1[Unbalanced Partitions]

    B1 --> B2["Time: O(n log n)"]
    C1 --> C2["Time: O(n log n)"]
    D1 --> D2["Time: O(n²)"]
    
```


**Explanation:**

- **Best Case:** Occurs with perfectly balanced partitions; time complexity is $O(n \log n)$.
- **Average Case:** With random data, the expected time complexity is $O(n \log n)$.
- **Worst Case:** Occurs with unbalanced partitions (e.g., sorted array and bad pivot selection); time complexity is $O(n^2)$.

---

## **5. Space Complexity Visualization**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    S[Space Complexity]
    S --> B(Best Case)
    S --> W(Worst Case)

    B --> B1["Recursion Depth: log n"]
    W --> W1["Recursion Depth: n"]

    B1 --> B2["Space: O(log n)"]
    W1 --> W2["Space: O(n)"]
    
```


**Explanation:**

- **Best Case Space Complexity:** The recursion stack depth is $\log n$, leading to space complexity $O(\log n)$.
- **Worst Case Space Complexity:** The recursion stack depth is $n$, leading to space complexity $O(n)$.

---

## **Additional Diagram: Impact of Pivot Selection**

**6. Effect of Pivot Selection on Time Complexity**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    P[Pivot Selection Strategies]
    P --> R[Random Pivot]
    P --> F[First Element]
    P --> L[Last Element]
    P --> M[Median-of-Three]
    P --> MM[Median-of-Medians]

    R --> RA["Expected Time: O(n log n)"]
    F --> FA["May Cause Worst Case: O(n²)"]
    L --> LA["May Cause Worst Case: O(n²)"]
    M --> MA[Improved Partitioning]
    MM --> MMA[Guaranteed Balanced Partitions]

    MA --> MB["Time: O(n log n)"]
    MMA --> MMB["Time: O(n log n)"]
    
```


**Explanation:**

- **Random Pivot:** Reduces the chance of worst-case; expected $O(n \log n)$.
- **First/Last Element Pivot:** Can cause worst-case $O(n^2)$ if the array is already sorted.
- **Median-of-Three:** Improves partitioning by choosing a better pivot.
- **Median-of-Medians:** Ensures balanced partitions, guaranteeing $O(n \log n)$ time complexity.

---

## **Visualizing the Master Theorem Application**

**7. Applying Master Theorem to Best Case**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    A[Recurrence Relation]
    A --> B[\"T(n) = 2T(n/2) + cn "\]
    B --> C["Divide: a = 2"]
    B --> D["Subproblem Size: b = 2"]
    B --> E["Work at Each Level: <br> \( f(n) = cn \)"]
    CDE --> F[Case 2 of Master Theorem]
    F --> G[\" T(n) = O(n \log n) "\]
    
```


**Explanation:**

- The recurrence relation for the best case fits **Case 2** of the Master Theorem.
- This results in the time complexity \( O(n \log n) \).

---

## **Visualizing the Recurrence Unfolding in Worst Case**

**8. Unfolding the Recurrence for Worst Case**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Tn[\" T(n) = T(n - 1) + cn "\]
    Tn --> Tn1[\" T(n - 1) = T(n - 2) + c(n - 1) "\]
    Tn1 --> Tn2[\" T(n - 2) = T(n - 3) + c(n - 2) "\]
    Tn2 --> Tnk[\" \vdots "\]
    Tnk --> T1[\" T(1) "\]
    T1 --> Sum[\" T(n) = \sum_{k=1}^{n} c \cdot k "\]
    Sum --> Result[\" T(n) = O(n^2) "\]
    
```


**Explanation:**

- Unfolding the recurrence shows that the total time is proportional to the sum of the sequence $n + (n - 1) + (n - 2) + \dots + 1$.
- This sum equals $\frac{n(n + 1)}{2}$, leading to $O(n^2)$ time complexity.

---

## **Recursion Tree Depth Comparison**

**9. Recursion Depth in Best and Worst Cases**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    A[Recursion Depth]
    A --> B(Best Case)
    A --> C(Worst Case)

    B --> D["Depth: \( \log n \)"]
    C --> E["Depth:  n "]
    
```


**Explanation:**

- **Best Case Recursion Depth:** The recursion tree's height is $\log n$ due to balanced partitions.
- **Worst Case Recursion Depth:** The recursion tree's height is $n$ due to unbalanced partitions.

---

## **Visualization of Hybrid Sorting Approach**

**10. Introsort Algorithm Overview**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> A[Set recursion depth limit]
    A --> B[QuickSort with depth limit]
    B --> C{Recursion depth exceeded?}
    C -- No --> D[Proceed with QuickSort]
    D --> E[Partition and Recurse]
    C -- Yes --> F[Switch to HeapSort]
    E --> G[Return]
    F --> G[Return]
    G --> End([End])
    
```


**Explanation:**

- **Introsort** starts with Quick Sort but switches to Heap Sort when the recursion depth exceeds a certain limit to ensure $O(n \log n)$ time complexity in the worst case.

---

## **Visual Representation of Algorithm Complexities**

**11. Summary of Quick Sort Complexities**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    QS[Quick Sort]
    QS --> TimeComplexity
    QS --> SpaceComplexity

    TimeComplexity --> BestCaseTC["Best Case: O(n log n)"]
    TimeComplexity --> AverageCaseTC["Average Case: O(n log n)"]
    TimeComplexity --> WorstCaseTC["Worst Case: O(n²)"]

    SpaceComplexity --> BestCaseSC["Best Case: O(log n)"]
    SpaceComplexity --> WorstCaseSC["Worst Case: O(n)"]
```

---

**Note on Diagram Usage:**

- Use these diagrams to visualize how Quick Sort operates under different conditions.
- They illustrate how the algorithm's time and space complexities are affected by factors like pivot selection and partitioning strategy.

---

## **How to Render Mermaid Diagrams**

To view these diagrams visually, you can:

- Use an online Mermaid renderer such as [Mermaid Live Editor](https://mermaid.live/).
- Integrate Mermaid diagrams into Markdown documents using tools like VSCode with the Mermaid plugin.
- Use the `mermaid` command-line tool to generate images from the syntax.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---