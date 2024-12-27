---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
---

Below are diagrams in Mermaid syntax that explain the complexities of the sorting algorithms.


---


## 1. Classification of Sorting Algorithms

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    A[Sorting Algorithms]
    A --> B[Comparison-Based Sorts]
    A --> C[Non-Comparison-Based Sorts]
    
    %% Comparison-Based Sorts
    B --> D[Simple Sorts]
    D --> E[Bubble Sort]
    D --> F[Selection Sort]
    D --> G[Insertion Sort]
    
    B --> H[Efficient Sorts]
    H --> I[Merge Sort]
    H --> J[Quick Sort]
    H --> K[Heap Sort]
    
    %% Non-Comparison-Based Sorts
    C --> L[Counting Sort]
    C --> M[Radix Sort]
    C --> N[Bucket Sort]
    
```


**Explanation:**
- This diagram classifies sorting algorithms into **Comparison-Based Sorts** and **Non-Comparison-Based Sorts**.
- **Comparison-Based Sorts** are further divided into **Simple Sorts** and **Efficient Sorts**.

---

## 2. Time Complexity Comparison

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    O[Time Complexity of Sorting Algorithms]
    O --> P["O(n<sup>2</sup>) Algorithms"]
    O --> Q["O(n log n) Algorithms"]
    O --> R[Linear Time Algorithms]

    %% O(n^2) Algorithms
    P --> E[Bubble Sort]
    P --> F[Selection Sort]
    P --> G["Insertion Sort (Average/Worst Cases)"]

    %% O(n log n) Algorithms
    Q --> I[Merge Sort]
    Q --> J["Quick Sort (Average Case)"]
    Q --> K[Heap Sort]

    %% Linear Time Algorithms
    R --> L[Counting Sort]
    R --> M[Radix Sort]
    R --> N[Bucket Sort]
    
```


**Explanation:**
- This diagram groups sorting algorithms based on their time complexities.
- **O(n²) Algorithms** include Bubble Sort, Selection Sort, and Insertion Sort.
- **O(n log n) Algorithms** include Merge Sort, Quick Sort (average case), and Heap Sort.
- **Linear Time Algorithms** include Counting Sort, Radix Sort, and Bucket Sort.

---

## 3. Detailed Complexities of Key Sorting Algorithms

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    A[Sorting Algorithms]

    subgraph Comparison-Based Sorts
        direction TB
        A --> B1[Bubble Sort]
        A --> B2[Selection Sort]
        A --> B3[Insertion Sort]
        A --> B4[Merge Sort]
        A --> B5[Quick Sort]
        A --> B6[Heap Sort]
    end

    subgraph Non-Comparison-Based Sorts
        direction TB
        A --> C1[Counting Sort]
        A --> C2[Radix Sort]
        A --> C3[Bucket Sort]
    end

    %% Bubble Sort
    B1 --> BS1["**Best Case:** O(n)"]
    B1 --> BS2["**Average Case:** O(n²)"]
    B1 --> BS3["**Worst Case:** O(n²)"]
    B1 --> BS4["**Space:** O(1)"]
    B1 --> BS5[**Stable:** Yes]
    B1 --> BS6[**In-Place:** Yes]

    %% Selection Sort
    B2 --> SS1["**Best Case:** O(n²)"]
    B2 --> SS2["**Average Case:** O(n²)"]
    B2 --> SS3["**Worst Case:** O(n²)"]
    B2 --> SS4["**Space:** O(1)"]
    B2 --> SS5[**Stable:** No]
    B2 --> SS6[**In-Place:** Yes]

    %% Insertion Sort
    B3 --> IS1["**Best Case:** O(n)"]
    B3 --> IS2["**Average Case:** O(n²)"]
    B3 --> IS3["**Worst Case:** O(n²)"]
    B3 --> IS4["**Space:** O(1)"]
    B3 --> IS5[**Stable:** Yes]
    B3 --> IS6[**In-Place:** Yes]

    %% Merge Sort
    B4 --> MS1["**Best Case:** O(n log n)"]
    B4 --> MS2["**Average Case:** O(n log n)"]
    B4 --> MS3["**Worst Case:** O(n log n)"]
    B4 --> MS4["**Space:** O(n)"]
    B4 --> MS5[**Stable:** Yes]
    B4 --> MS6[**In-Place:** No]

    %% Quick Sort
    B5 --> QS1["**Best Case:** O(n log n)"]
    B5 --> QS2["**Average Case:** O(n log n)"]
    B5 --> QS3["**Worst Case:** O(n²)"]
    B5 --> QS4["**Space:** O(log n)"]
    B5 --> QS5[**Stable:** No]
    B5 --> QS6[**In-Place:** Yes]

    %% Heap Sort
    B6 --> HS1["**Best Case:** O(n log n)"]
    B6 --> HS2["**Average Case:** O(n log n)"]
    B6 --> HS3["**Worst Case:** O(n log n)"]
    B6 --> HS4["**Space:** O(1)"]
    B6 --> HS5[**Stable:** No]
    B6 --> HS6[**In-Place:** Yes]

    %% Counting Sort
    C1 --> CS1["**Time:** O(n + k)"]
    C1 --> CS2["**Space:** O(n + k)"]
    C1 --> CS3[**Stable:** Yes]
    C1 --> CS4[**In-Place:** No]

    %% Radix Sort
    C2 --> RS1["**Time:** O(n × d)"]
    C2 --> RS2["**Space:** O(n + k)"]
    C2 --> RS3[**Stable:** Yes]
    C2 --> RS4[**In-Place:** No]

    %% Bucket Sort
    C3 --> BK1["**Time:** O(n + k)"]
    C3 --> BK2["**Space:** O(n × k)"]
    C3 --> BK3["**Stable:** Yes (Depends on Inner Sort)"]
    C3 --> BK4[**In-Place:** No]
    
```


**Explanation:**
- This diagram provides detailed complexities for each key sorting algorithm.
- It includes best, average, and worst-case time complexities, space complexity, and whether the algorithm is stable and in-place.

---

## 4. Time Complexity Recurrences

```mermaid
flowchart TD
    A[Recursive Sorting Algorithms]
    A --> B[Merge Sort]
    A --> C[Quick Sort]

    %% Merge Sort
    B --> B1[Recurrence Relation]
    B1 --> B2["T(n) = 2 × T(n/2) + O(n)"]
    B2 --> B3["Solution: T(n) = O(n log n)"]

    %% Quick Sort
    C --> C1[Average Case Recurrence]
    C1 --> C2["T(n) = 2 × T(n/2) + O(n)"]
    C2 --> C3["Solution: T(n) = O(n log n)"]

    C --> D1[Worst Case Recurrence]
    D1 --> D2["T(n) = T(n - 1) + O(n)"]
    D2 --> D3["Solution: T(n) = O(n²)"]
```

**Explanation:**
- This diagram shows the recurrence relations for Merge Sort and Quick Sort.
- For Merge Sort, the recurrence relation is `T(n) = 2T(n/2) + O(n)`, leading to `O(n log n)` complexity.
- Quick Sort's average case has a similar recurrence, but the worst-case has `T(n) = T(n - 1) + O(n)`, leading to `O(n²)` complexity.

---

## 5. Master Theorem Application

```mermaid
flowchart TD
    A[Master Theorem Cases]

    A --> B[Case 1]
    B --> B1["If f(n) = O(n^{log_b a - ε})"]
    B1 --> B2[Example]
    B2 --> B3["T(n) = 2T(n/2) + n^{0.99}"]
    B3 --> B4["Solution: T(n) = Θ(n^{log_2 2}) = Θ(n)"]

    A --> C[Case 2]
    C --> C1["If f(n) = Θ(n^{log_b a} × log^k n)"]
    C1 --> C2[Example]
    C2 --> C3["T(n) = 2T(n/2) + n log n"]
    C3 --> C4["Solution: T(n) = Θ(n log² n)"]

    A --> D[Case 3]
    D --> D1["If f(n) = Ω(n^{log_b a + ε})"]
    D1 --> D2[Example]
    D2 --> D3["T(n) = T(n/2) + n"]
    D3 --> D4["Solution: T(n) = Θ(n)"]
```

**Explanation:**
- This diagram illustrates the three cases of the Master Theorem used to solve recurrence relations.
- It provides examples and solutions for each case.

---

## 6. Merge Sort Recurrence Tree

```mermaid
graph TD
    Start[Array of Size n]
    Start --> Left1[Size n/2]
    Start --> Right1[Size n/2]
    Left1 --> Left2[Size n/4]
    Left1 --> Right2[Size n/4]
    Right1 --> Left3[Size n/4]
    Right1 --> Right3[Size n/4]
    Left2 --> L["..."]
    Right2 --> R["..."]
    Left3 --> L2["..."]
    Right3 --> R2["..."]
    Note[Total Levels ≈ log n]

    style Note fill:#f9f,stroke:#333,stroke-width:2px
```

**Explanation:**
- This diagram represents the recurrence tree of Merge Sort.
- It shows how the array is recursively divided until individual elements are reached.
- The total number of levels is approximately `log n`, explaining the `O(n log n)` time complexity.

---

## 7. Quick Sort Worst-Case Partition

```mermaid
flowchart LR
    A[Array of Size n]
    A --> B["Choose Pivot (Smallest Element)"]
    B --> C[Partition Array]
    C --> D["Left Subarray (Size 0)"]
    C --> E["Right Subarray (Size n - 1)"]
    E --> F[Repeat Process]
    Note["Results in T(n) = T(n - 1) + O(n)"]
    
```


**Explanation:**
- This diagram illustrates the worst-case scenario in Quick Sort when the smallest element is always chosen as the pivot.
- This results in unbalanced partitions, leading to `O(n²)` time complexity.

---

## 8. Space Complexity Comparison

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    A[Sorting Algorithms]

    A --> B["In-Place Algorithms <br> O(1) Space"]
    B --> B1[Bubble Sort]
    B --> B2[Selection Sort]
    B --> B3[Insertion Sort]
    B --> B4[Heap Sort]
    B --> B5[Quick Sort]

    A --> C["Not In-Place Algorithms <br> O(n) Space"]
    C --> C1[Merge Sort]
    C --> C2[Counting Sort]
    C --> C3[Radix Sort]
    C --> C4[Bucket Sort]
    
```



**Explanation:**
- This diagram classifies sorting algorithms based on their space complexity.
- **In-Place Algorithms** require only constant extra space.
- **Not In-Place Algorithms** require additional space proportional to the size of the input.

---
