---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---



# Insertion Sort Algorithm - Mermaid diagrams

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## **1. Flowchart of Insertion Sort Algorithm**

This flowchart illustrates the step-by-step process of the standard Insertion Sort algorithm.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> InitializeVariables[/"Set n = length(A)"/]
    InitializeVariables --> OuterLoopStart{i = 1; i < n?}
    OuterLoopStart -->|Yes| SetKey[/"key = A[i]"/]
    SetKey --> SetJ[/"j = i - 1"/]
    SetJ --> InnerLoopStart{"j ≥ 0 and A[j] > key?"}
    
    InnerLoopStart -->|Yes| ShiftA[/"A[j + 1] = A[j]"/]
    ShiftA --> DecrementJ[/j = j - 1/]
    DecrementJ --> InnerLoopStart

    InnerLoopStart -->|No| InsertKey[/"A[j + 1] = key"/]
    InsertKey --> IncrementI[/"i = i + 1"/]
    IncrementI --> OuterLoopStart

    OuterLoopStart -->|No| End([End])
    
```

**Explanation:**

- **Outer Loop:** Iterates from `i = 1` to `i = n - 1`.
- **Inner Loop:** Moves elements greater than `key` one position ahead to make space for the insertion.
- **Operations:**
  - Comparisons occur at the condition `A[j] > key`.
  - Shifts (assignments) happen when moving `A[j]` to `A[j + 1]`.

---

## **2. Worst-Case Time Complexity Visualization**

The worst-case occurs when the input array is in reverse order. Each new element is compared with all the sorted elements and shifted.

```mermaid
graph TD
    subgraph Comparisons
        direction LR
        Level1[First element] -->|0 comparisons| Level2[Second element]
        Level2 -->|1 comparison| Level3[Third element]
        Level3 -->|2 comparisons| Level4[Fourth element]
        Level4 -->|3 comparisons| Level5[Fifth element]
        Level5 -->|...| LevelN[n-th element]
    end
```

**Total Comparisons in Worst Case:**

$$
C_{\text{worst}} = \frac{n(n - 1)}{2} = O(n^2)
$$

---

## **3. Best-Case Time Complexity Visualization**

The best case occurs when the input array is already sorted. Each element needs only one comparison.

```mermaid
graph TD
    subgraph Comparisons
        direction LR
        Level1[First element] -->|0 comparisons| Level2[Second element]
        Level2 -->|1 comparison| Level3[Third element]
        Level3 -->|1 comparison| Level4[Fourth element]
        Level4 -->|1 comparison| Level5[Fifth element]
        Level5 -->|...| LevelN[n-th element]
    end
```

**Total Comparisons in Best Case:**

$$
C_{\text{best}} = n - 1 = O(n)
$$

---

## **4. Average-Case Time Complexity Visualization**

On average, the number of comparisons and shifts is approximately half that of the worst case.

```mermaid
graph TD
    subgraph Comparisons
        direction LR
        Level1[First element] -->|0 comparisons| Level2[Second element]
        Level2 -->|~0.5 comparisons| Level3[Third element]
        Level3 -->|~1 comparison| Level4[Fourth element]
        Level4 -->|~1.5 comparisons| Level5[Fifth element]
        Level5 -->|...| LevelN[n-th element]
    end
```

**Total Comparisons in Average Case:**

$$
C_{\text{avg}} \approx \frac{n(n - 1)}{4} = O(n^2)
$$

---

## **5. Comparison Between Standard and Binary Insertion Sort**

### **5.1 Standard Insertion Sort**

```mermaid
flowchart TD
    StartStandard([Start Standard Insertion Sort]) --> TotalComparisonsStandard[/"Total Comparisons ≈ n^2"/]
    TotalComparisonsStandard --> TotalShiftsStandard[/"Total Shifts ≈ n^2"/]
    TotalShiftsStandard --> TimeComplexityStandard[/"Time Complexity O(n^2)"/]
    TimeComplexityStandard --> EndStandard([End])
    
```


### **5.2 Binary Insertion Sort**

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    StartBinary([Start Binary Insertion Sort]) --> TotalComparisonsBinary[/"Total Comparisons ≈ n log n"/]
    TotalComparisonsBinary --> TotalShiftsBinary[/"Total Shifts ≈ n^2"/]
    TotalShiftsBinary --> TimeComplexityBinary[/"Time Complexity O(n^2)"/]
    TimeComplexityBinary --> EndBinary([End])
    
```


**Explanation:**

- **Standard Insertion Sort:**
  - Uses linear search to find the insertion point.
  - Comparisons: $O(n^2)$
  - Shifts: $O(n^2)$
  - Time Complexity: $O(n^2)$

- **Binary Insertion Sort:**
  - Uses binary search to find the insertion point.
  - Comparisons: $O(n \log n)$
  - Shifts: $O(n^2)$
  - Time Complexity: $O(n^2)$ (dominated by shifts)

---

## **6. Time Complexity Summary Diagram**

This diagram summarizes the time complexities in different cases.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    InsertionSort[Insertion Sort Algorithm] --> BestCase[Best Case]
    InsertionSort --> AverageCase[Average Case]
    InsertionSort --> WorstCase[Worst Case]

    BestCase --> TimeBest["Time Complexity: O(n)"]
    AverageCase --> TimeAverage["Time Complexity: O(n^2)"]
    WorstCase --> TimeWorst["Time Complexity: O(n^2)"]
```

---

## **7. Operation Count Flowchart**

This flowchart demonstrates how the number of operations increases with each element inserted.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> ForEachElement[For each element i from 1 to n - 1]
    ForEachElement --> InnerLoopOperations[/"Number of Operations for element i ≈ i"/]
    InnerLoopOperations --> AccumulateOperations[Accumulate total operations]
    AccumulateOperations --> NextElement{Is i < n - 1?}
    NextElement -->|Yes| ForEachElement
    NextElement -->|No| ComputeTotalOperations[Compute Total Operations]
    ComputeTotalOperations --> End([End])
    
```


**Total Operations:**

$$
T(n) \approx \sum_{i=1}^{n-1} i = \frac{n(n - 1)}{2} = O(n^2)
$$

---

## **8. Shell Sort vs. Insertion Sort**

Illustrating how Shell Sort improves upon Insertion Sort using gap sequences.

```mermaid
%% ---
%% config:
%%   layout: elk
%%   look: handDrawn
%%   theme: dark
%% ---
flowchart TD
    StartShell([Start Shell Sort]) --> SetGapSequence[/"Set gap sequence: e.g., n/2, n/4, ..., 1"/]
    SetGapSequence --> ForEachGap[For each gap value]
    ForEachGap --> PerformGapInsertionSort[Perform Insertion Sort on elements with the specified gap]
    PerformGapInsertionSort --> NextGap{More gaps?}
    NextGap -->|Yes| ForEachGap
    NextGap -->|No| EndShell([End])

    StartInsertion([Start Insertion Sort]) --> ProcessElements[Process elements with gap = 1]
    ProcessElements --> EndInsertion([End])

    StartComparison([Comparison]) --> InsertionSortPath["Insertion Sort: O(n^2)"]
    StartComparison --> ShellSortPath["Shell Sort: O(n\log^2 n) or better"]

    InsertionSortPath --> EndComparison([Shell Sort is faster for larger n])
    ShellSortPath --> EndComparison
    
```


---

## **9. Space Complexity Illustration**

Showing that Insertion Sort operates in-place with constant additional space.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> AllocateInputArray[/"Allocate input array of size n"/]
    AllocateInputArray --> InsertionSortProcess[Perform Insertion Sort]
    InsertionSortProcess --> InPlaceOperation{Operations In-Place?}
    InPlaceOperation -->|Yes| SpaceComplexity[/"Space Complexity: O(1)"/]
    SpaceComplexity --> End([End])
    
```


---

## **10. Stability Characteristic**

Demonstrating that Insertion Sort is stable.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    InputArray[Input Array with equal elements] --> InsertionSortProcess[Perform Insertion Sort]
    InsertionSortProcess --> OutputArray[Output Array]

    InputArray -- "Relative order preserved" --> OutputArray

    subgraph Legend
        A["Element A<sub>i</sub>"] -- "Remains before" --> B["Element A<sub>j</sub> <br> (if A<sub>i</sub> = A<sub>j</sub> and i < j)"]
    end
    
```


---

## **11. Algorithm Comparison Chart**

Although Mermaid doesn't support plotting graphs directly, we can create a conceptual diagram to compare time complexities.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    nSquared["O(n^2) Time Complexity <br> (Insertion Sort)"] --> QuadraticGrowth[Quadratic Growth]
    nLogn["O(n log n) Time Complexity <br> (Efficient Sorts)"] --> LogLinearGrowth[Log-Linear Growth]

    QuadraticGrowth -->|Higher time for large n| PerformanceImpact[Performance Impact]
    LogLinearGrowth -->|Lower time for large n| PerformanceImpact

    PerformanceImpact --> Recommendation{Use Efficient Sorts for Large n}
    
```


---

## **Explanation of Diagrams**

The provided diagrams use Mermaid syntax to visualize key aspects of the Insertion Sort algorithm and its complexities:

- **Flowcharts:** Outline the steps of the algorithm, showing loops and conditions.
- **Graphs (Conceptual):** Illustrate how comparisons and shifts increase with the number of elements.
- **Comparisons:** Highlight the differences between standard and binary insertion sorts.
- **Time Complexity Summaries:** Summarize best-case, average-case, and worst-case complexities.
- **Additional Characteristics:** Display properties like space complexity and stability.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---