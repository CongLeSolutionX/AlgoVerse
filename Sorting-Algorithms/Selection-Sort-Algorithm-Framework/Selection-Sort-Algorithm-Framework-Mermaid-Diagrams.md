---
created: 2024-12-28 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---


Below are several Mermaid diagrams that illustrate the complexities of the Selection Sort algorithm.

---


## 1. Flowchart of the Selection Sort Algorithm

This flowchart visualizes the step-by-step process of the Selection Sort algorithm.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start])
    End([End])
    Start --> Initialize_i[Initialize i = 0]
    Initialize_i --> OuterLoop{Is i < N - 1?}
    OuterLoop -- Yes --> SetMinIndex[Set minIndex = i]
    SetMinIndex --> Initialize_j[Initialize j = i + 1]
    Initialize_j --> InnerLoop{Is j < N?}
    InnerLoop -- Yes --> CompareValues{"Is arr[j] < arr[minIndex]?"}
    CompareValues -- Yes --> UpdateMinIndex[Set minIndex = j]
    CompareValues -- No --> NoUpdate[Leave minIndex unchanged]
    UpdateMinIndex --> Increment_j[Increment j by 1]
    NoUpdate --> Increment_j
    Increment_j --> InnerLoop
    InnerLoop -- No --> CheckSwap{Is minIndex != i?}
    CheckSwap -- Yes --> SwapElements["Swap arr[i] and arr[minIndex]"]
    CheckSwap -- No --> NoSwap[No action needed]
    SwapElements --> Increment_i[Increment i by 1]
    NoSwap --> Increment_i
    Increment_i --> OuterLoop
    OuterLoop -- No --> End
    
```



---

## 2. Visualization of Comparisons and Swaps per Iteration

This diagram shows how the number of comparisons and swaps accumulate over each iteration.

```mermaid
graph TD
    subgraph "Selection Sort Iterations"
        direction TB
        I1[Iteration i = 0] --> C1[Comparisons: N - 1] --> S1[Swaps: 1]
        I2[Iteration i = 1] --> C2[Comparisons: N - 2] --> S2[Swaps: 1]
        I3[Iteration i = 2] --> C3[Comparisons: N - 3] --> S3[Swaps: 1]
        I4[...]
        In[Iteration i = N - 2] --> Cn[Comparisons: 1] --> Sn[Swaps: 1]
    end
```

---

## 3. Total Comparisons Calculation

Illustrating the derivation of the total number of comparisons in Selection Sort.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start])
    Start --> A["Total Comparisons C(N)"]
    A --> B[Sum over i from 0 to N - 2]
    B --> C["C(N) = Σ(N - i - 1) for i = 0 to N - 2"]
    C --> D["Total Comparisons: C(N) = (N^2 - N) / 2"]
    D --> End([End])
    
```


---

## 4. Time Complexity Representation

A diagram representing the time complexity of Selection Sort in different cases.

```mermaid
graph LR
    A[Selection Sort]
    A --> B[Best Case]
    A --> C[Average Case]
    A --> D[Worst Case]
    B --> B1["Time Complexity: O(N²)"]
    C --> C1["Time Complexity: O(N²)"]
    D --> D1["Time Complexity: O(N²)"]
```

---

## 5. Space Complexity Representation

Diagram illustrating that Selection Sort is an in-place algorithm with constant space complexity.

```mermaid
graph TD
    A[Selection Sort] --> B[Space Complexity]
    B --> C[Auxiliary Space Used]
    C --> D["O(1) Constant Space"]
```

---

## 6. Big O Notation Conceptual Graph

A conceptual representation of how the time complexity scales with the input size.

```mermaid
graph TD
    A[Input Size N] --> B["Operations O(N²)"]
    B --> C[Quadratic Growth]
    A --> D["Time Complexity T(N)"]
    D --> C
```

---

## 7. Comparison with Other Sorting Algorithms

A diagram comparing Selection Sort's time complexity with other common sorting algorithms.

```mermaid
flowchart TD
    A[Sorting Algorithms]
    A --> B[Selection Sort]
    A --> C[Insertion Sort]
    A --> D[Bubble Sort]
    A --> E[Merge Sort]
    A --> F[Quick Sort]
    A --> G[Heap Sort]
    
    B --> B1["Time: O(N²)"]
    C --> C1["Time: O(N²)"]
    D --> D1["Time: O(N²)"]
    E --> E1["Time: O(N log N)"]
    F --> F1["Avg Time: O(N log N)"]
    G --> G1["Time: O(N log N)"]
    
```

---

## 8. Number of Comparisons over Input Size

This diagram illustrates the relationship between input size and the total number of comparisons.

```mermaid
graph LR
    N[Input Size N] --> C["Total Comparisons C(N)"]
    C --> Formula["C(N) = (N² - N) / 2"]
    Formula --> Complexity["Time Complexity O(N²)"]
    
```


---

## 9. Step-by-Step Operation Flow

Visual representation of operations in each iteration.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    subgraph "For Each i from 0 to N - 2"
        direction TB
        A[Set minIndex = i]
        A --> B[For j = i + 1 to N - 1]
        B --> C{"Is arr[j] < arr[minIndex]?"}
        C -- Yes --> D[Set minIndex = j]
        C -- No --> E[No Change]
        D --> F[Continue j loop]
        E --> F
        F --> B
        B --> G["After j loop, Swap arr[i] and arr[minIndex]"]
    end
    
```



---

## 10. Algorithm's Inefficiency for Large N

A diagram emphasizing Selection Sort's impracticality for large datasets due to its quadratic time complexity.

```mermaid
flowchart TD
    A[Large Input Size N] --> B["Total Comparisons: C(N) = O(N²)"]
    B --> C[Execution Time Increases Quadratically]
    C --> D[Impractical for Large N]
    
```


---

