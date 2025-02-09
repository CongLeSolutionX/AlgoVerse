---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---


# Merge Sort Algorithm Framework  - Mermaid diagrams

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


### **1. Merge Sort Recursion Tree Diagram**

This diagram illustrates how the Merge Sort algorithm recursively divides the array until it reaches the base case.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TD
    A[Array of size n]
    A -->|Divide| B[Left Half<br>Size: n/2]
    A -->|Divide| C[Right Half<br>Size: n/2]

    B -->|Divide| D[Left Quarter<br>Size: n/4]
    B -->|Divide| E[Right Quarter<br>Size: n/4]
    C -->|Divide| F[Left Quarter<br>Size: n/4]
    C -->|Divide| G[Right Quarter<br>Size: n/4]

    D -->|Recursive Calls| H[...]
    E -->|Recursive Calls| I[...]
    F -->|Recursive Calls| J[...]
    G -->|Recursive Calls| K[...]

    H -->|Base Case<br>Size ≤ 1| L[Single Element]
    I -->|Base Case<br>Size ≤ 1| M[Single Element]
    J -->|Base Case<br>Size ≤ 1| N[Single Element]
    K -->|Base Case<br>Size ≤ 1| O[Single Element]
```

- **Explanation:**
  - The array is divided into halves recursively.
  - The depth of the recursion tree is **log₂ n** since the array size reduces by half each time.
  - At the leaves, we reach arrays of size 1, which are inherently sorted.

---

### **2. Time Complexity Breakdown Diagram**

This diagram shows how the total time complexity of **O(n log n)** arises from the work done at each level of recursion.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Level1[Level 1<br>n elements] --> Level2[Level 2<br>n elements]
    Level2 --> Level3[Level 3<br>n elements]
    Level3 --> Level4[...]
    Level4 --> LevelLogN[Level log n<br>n elements]

    subgraph Total Work at Each Level
        Level1 ---|Work = cn| Level2
        Level2 ---|Work = cn| Level3
        Level3 ---|Work = cn| Level4
        Level4 ---|...| LevelLogN
    end
```

- **Explanation:**
  - At each level, the total amount of data processed during merging is **n**.
  - With **log n** levels, the total time complexity is **O(n log n)**.

---

### **3. Merge Sort Algorithm Flowchart**

This flowchart depicts the steps involved in the Merge Sort algorithm.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start[Start] --> CheckSize{Is array size ≤ 1?}
    CheckSize -- Yes --> Return[Return array]
    CheckSize -- No --> Divide[Divide array into two halves]
    Divide --> Recursion1[Recursively sort left half]
    Divide --> Recursion2[Recursively sort right half]
    Recursion1 --> Merge[Merge sorted halves]
    Recursion2 --> Merge
    Merge --> ReturnSorted[Return merged array]
```

- **Explanation:**
  - The algorithm checks if the array can be divided.
  - It recursively sorts both halves and then merges them.

---

### **4. Space Complexity Diagram**

This diagram explains the space requirements of Merge Sort.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    A["Total Space Complexity S(n)"]
    A -- "Auxiliary Space<br>for merging" --> B["O(n)"]
    A -- "Call Stack Space<br>due to recursion" --> C["O(log n)"]
    B & C --> D["Combined Space Complexity<br>S(n) = O(n)"]
    
```


- **Explanation:**
  - **Auxiliary Space:** Temporary arrays used during the merge step require **O(n)** space.
  - **Call Stack Space:** The recursion depth is **log n**, so the stack space is **O(log n)**.
  - The dominant term is **O(n)**.

---

### **5. Comparison Table of Sorting Algorithms**

This class diagram compares Merge Sort with other sorting algorithms.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
classDiagram
    class SortingAlgorithm {
        +Name: String
        +BestCase: String
        +AverageCase: String
        +WorstCase: String
        +SpaceComplexity: String
        +IsStable: Boolean
    }

    class MergeSort {
        +Name = "Merge Sort"
        +BestCase = "O(n log n)"
        +AverageCase = "O(n log n)"
        +WorstCase = "O(n log n)"
        +SpaceComplexity = "O(n)"
        +IsStable = true
    }

    class QuickSort {
        +Name = "Quick Sort"
        +BestCase = "O(n log n)"
        +AverageCase = "O(n log n)"
        +WorstCase = "O(n²)"
        +SpaceComplexity = "O(log n)"
        +IsStable = false
    }

    class HeapSort {
        +Name = "Heap Sort"
        +BestCase = "O(n log n)"
        +AverageCase = "O(n log n)"
        +WorstCase = "O(n log n)"
        +SpaceComplexity = "O(1)"
        +IsStable = false
    }

    SortingAlgorithm <|-- MergeSort
    SortingAlgorithm <|-- QuickSort
    SortingAlgorithm <|-- HeapSort
```

- **Explanation:**
  - **Merge Sort** is stable and has consistent time complexity but requires extra space.
  - **Quick Sort** is faster on average but has a worse-case time of **O(n²)**.
  - **Heap Sort** has good time complexity and minimal space usage but is not stable.

---

### **6. Master Theorem Application Diagram**

This flowchart demonstrates how the Master Theorem is applied to determine the time complexity.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start["Start with Recurrence<br>T(n) = 2T(n⁄2) + cn"]
    Identify[Identify Parameters]
    Identify --> a[A = 2]
    Identify --> b[B = 2]
    Identify --> f["f(n) = cn"]
    Compute[Compute log_b A]
    Compute --> logValue[log₂ 2 = 1]
    Compare["Compare f(n) with n^log_b A"]
    Compare --> Case2["Since f(n) = Θ(n^{log_b A}), use Case 2"]
    Conclude["Conclude T(n) = Θ(n log n)"]
    Start --> Identify --> Compute --> Compare --> Case2 --> Conclude
    
```


- **Explanation:**
  - **Parameters:** The recurrence fits the form for applying the Master Theorem.
  - **Result:** The time complexity is **Θ(n log n)**.

---

### **7. Execution Time vs. Input Size Illustration**

While Mermaid doesn't support graph plotting, we can represent the relationship between input size and execution time textually.

```mermaid
graph LR
    A[Input Size n]
    A -->|Time Complexity<br>T(n) = O(n log n)| B[Execution Time]

    note right of B
      - Execution time increases proportionally to n log n.
      - Doubling n increases T(n) by more than double.
    end
```

- **Explanation:**
  - The execution time grows logarithmically due to the **log n** factor.

---

### **8. Space-Time Trade-off Diagram**

This diagram illustrates the trade-off between time and space complexities.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    MergeSort[Merge Sort]
    MergeSort -- "Time Complexity<br>O(n log n)" --> TimeComplexity
    MergeSort -- "Space Complexity<br>O(n)" --> SpaceComplexity

    Alternative[Alternative Algorithms]
    Alternative -->|Less Space| InPlaceMergeSort["In-place Merge Sort<br>Space: O(1)"]
    InPlaceMergeSort -->|Potentially Higher Time| HigherTimeComplexity

    MergeSort --- Alternative
    
```


- **Explanation:**
  - **Merge Sort** has optimal time complexity but requires extra space.
  - **In-place Merge Sort** reduces space but may increase time complexity due to overhead.

---

### **9. Merge Operation Illustration**

This diagram shows how two sorted subarrays are merged into a single sorted array.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TB
    subgraph LeftSubarray
        A1[Left Subarray]
        A1 -->|Elements| L1[1]:::sorted --> L2[3]:::sorted --> L3[5]:::sorted
    end

    subgraph RightSubarray
        B1[Right Subarray]
        B1 -->|Elements| R1[2]:::sorted --> R2[4]:::sorted --> R3[6]:::sorted
    end

    LeftSubarray -->|Merge| MergeProcess[Merge Process]
    RightSubarray -->|Merge| MergeProcess
    MergeProcess --> MergedArray[Merged Array]
    MergedArray -->|Elements| M1[1]:::merged --> M2[2]:::merged --> M3[3]:::merged --> M4[4]:::merged --> M5[5]:::merged --> M6[6]:::merged

    classDef sorted fill:#79F7,stroke:#036,stroke-width:1px;
    classDef merged fill:#E3EC,stroke:#C21,stroke-width:1px;

    class L1,L2,L3 sorted
    class R1,R2,R3 sorted
    class M1,M2,M3,M4,M5,M6 merged
    
```


- **Explanation:**
  - Elements from both subarrays are compared and merged in order.
  - This operation takes **O(n)** time where **n** is the total number of elements being merged.

---

### **10. Recursion Depth Visualization**

This diagram shows how the depth of recursion contributes to the **log n** factor in time complexity.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Level0["Level 0<br>Array Size: n"]
    Level0 --> Level1["Level 1<br>Array Size: n⁄2"]
    Level1 --> Level2["Level 2<br>Array Size: n⁄4"]
    Level2 --> Level3["Level 3<br>Array Size: n⁄8"]
    Level3 --> LevelDot[...] 
    LevelDot --> LevelLogN["Level log n<br>Array Size: 1"]

    %% Note right of LevelLogN: Total levels is log₂ n
    
```


- **Explanation:**
  - The number of recursion levels is **log n**, contributing to the overall time complexity.

---

You can use the Mermaid Live Editor or any compatible tool to render these diagrams by copying the code snippets.

---

### **Note on Viewing Mermaid Diagrams**

To render and view the diagrams:

1. **Copy** the Mermaid code snippet for the diagram.
2. **Paste** the code into [Mermaid Live Editor](https://mermaid.live/).
3. **Render** the diagram to visualize it.
4. **Export** or **save** the diagram if needed.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---