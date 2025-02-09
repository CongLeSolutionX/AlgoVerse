---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---

# Bubble Sort Algorithm Framework - Mermaid diagrams

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## **1. Bubble Sort Algorithm Flowchart**

This flowchart demonstrates the step-by-step process of the Bubble Sort algorithm.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> Initialization
    Initialization[Set n = length of array] --> OuterLoop
    OuterLoop[For i from 0 to n-1] --> InnerLoop
    InnerLoop[For j from 0 to n-i-1] --> Compare{"Is arr[j] > arr[j+1]?"}
    Compare -- Yes --> Swap["Swap arr[j] and arr[j+1]"]
    Swap --> InnerLoop
    Compare -- No --> InnerLoop
    InnerLoop --> CheckSwapped{Was any swap made?}
    CheckSwapped -- No --> End([Array is sorted])
    CheckSwapped -- Yes --> OuterLoop
    
```


**Explanation:**

- **Initialization:** Sets the initial parameters for the algorithm.
- **Outer Loop:** Iterates through the entire array.
- **Inner Loop:** Compares adjacent elements and performs swaps if necessary.
- **Swap Condition:** Determines if a swap is needed based on the comparison.
- **Early Exit Optimization:** Checks if any swaps were made; if not, the array is already sorted.

---

## **2. Comparison and Swapping Mechanism**

This sequence diagram illustrates how adjacent elements are compared and swapped during each iteration.

```mermaid
sequenceDiagram
    participant A as arr[j]
    participant B as arr[j+1]
    Note over A,B: Compare arr[j] and arr[j+1]
    A-->>B: Is arr[j] > arr[j+1]?
    alt Yes
        A->>B: Swap values
        Note over A,B: arr[j] and arr[j+1] are swapped
    else No
        Note over A,B: No action needed
    end
```

**Explanation:**

- **Participants:** Represent the two adjacent array elements being compared.
- **Condition:** Determines whether a swap is required.
- **Actions:** Swap or retain the positions based on the comparison result.

---

## **3. Time Complexity Analysis**

### **a. Worst-Case Time Complexity**

In the worst-case scenario (reverse sorted array), the number of comparisons and swaps is maximized.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TB
    subgraph WorstCase["Worst-Case Time Complexity <br> O(n^2)"]
        direction LR
        N1["Total Comparisons:<br> C = n(n - 1)/2"]
        N2["Total Swaps:<br> S = n(n - 1)/2"]
    end
    
```


### **b. Best-Case Time Complexity**

In the best-case scenario (already sorted array with optimization), the algorithm completes in linear time.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph TB
    subgraph BestCase["Best-Case Time Complexity <br> O(n)"]
        direction LR
        M1[Total Comparisons:<br> C = n - 1]
        M2[Total Swaps:<br> S = 0]
        M3[Early Exit after first pass]
    end
    
```


**Explanation:**

- **Worst Case:**
  - The number of comparisons and swaps reaches the maximum.
  - Time complexity is \( O(n^2) \).
- **Best Case:**
  - The array is already sorted; swaps are not needed.
  - Early exit optimization reduces time complexity to \( O(n) \).

---

## **4. Number of Comparisons Visualization**

This bar chart represents the number of comparisons for different array sizes in the worst-case scenario.

```mermaid
%% Note: Mermaid currently does not support bar charts directly.
%% This is a conceptual representation.

graph LR
    A[Array Size n] --> B{Total Comparisons}
    B --> C[Comparisons = n(n - 1)/2]
    subgraph ComparisonsGraph[Comparisons Increase Quadratically]
        direction TB
        for n from 1 to N do
            CompN[At n=N:<br> C = N(N - 1)/2]
        end
    end
```

**Note:** Mermaid does not support plotting actual graphs or bar charts with data points. The above is a conceptual illustration.

---

## **5. Comparison with Other Sorting Algorithms**

This flowchart compares the time complexities of Bubble Sort with Insertion Sort and Merge Sort.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    StartComparison([Start Comparison]) --> BubbleSort
    BubbleSort["Bubble Sort<br>O(n^2)"] --> InsertionSort
    InsertionSort["Insertion Sort<br>O(n^2)"] --> MergeSort
    MergeSort["Merge Sort<br>O(n log n)"] --> EndComparison([End Comparison])
    
```

**Explanation:**

- **Bubble Sort and Insertion Sort:**
  - Both have quadratic time complexities.
  - Less efficient for large datasets.
- **Merge Sort:**
  - Has a logarithmic time complexity.
  - More efficient for larger datasets.

---

## **6. Algorithm Performance Summary Table**

While Mermaid does not natively support detailed tables, we can represent a simple comparison.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
classDiagram
    class SortingAlgorithm {
        +AlgorithmName
        +TimeComplexity
        +SpaceComplexity
    }
    class BubbleSort {
        +AlgorithmName: Bubble Sort
        +TimeComplexity: O(n^2)
        +SpaceComplexity: O(1)
    }
    class InsertionSort {
        +AlgorithmName: Insertion Sort
        +TimeComplexity: O(n^2)
        +SpaceComplexity: O(1)
    }
    class MergeSort {
        +AlgorithmName: Merge Sort
        +TimeComplexity: O(n log n)
        +SpaceComplexity: O(n)
    }
    SortingAlgorithm <|-- BubbleSort
    SortingAlgorithm <|-- InsertionSort
    SortingAlgorithm <|-- MergeSort
    
```


**Explanation:**

- **Inheritance Hierarchy:**
  - `SortingAlgorithm` is a general class.
  - `BubbleSort`, `InsertionSort`, and `MergeSort` inherit properties.
- **Attributes:**
  - **AlgorithmName**
  - **TimeComplexity**
  - **SpaceComplexity**

---

## **7. Pseudocode Representation**

A flowchart representing the pseudocode steps of the optimized Bubble Sort algorithm with an early exit.

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Start([Start]) --> SetVariables[Set n = length of array<br>swapped = true]
    SetVariables --> CheckSwapped{Is swapped == true?}
    CheckSwapped -- Yes --> SetSwappedFalse[Set swapped = false]
    SetSwappedFalse --> ForJ[For j from 0 to n - 1]
    ForJ --> Compare{"Is arr[j] > arr[j+1]?"}
    Compare -- Yes --> SwapElements["Swap arr[j] and arr[j+1]<br>Set swapped = true"]
    SwapElements --> ForJ
    Compare -- No --> ForJ
    ForJ --> DecrementN["n = n - 1"]
    DecrementN --> CheckSwapped
    CheckSwapped -- No --> End([Array is sorted])
    
```


**Explanation:**

- **Variable Initialization:** Prepare variables before sorting.
- **Swapped Flag:** Determines if another pass is needed.
- **Inner Loop:** Performs comparisons and swaps.
- **Optimization:** Early exit when no swaps occur.

---

## **8. Algorithm Complexity Summary**

A mind map summarizing the complexities of Bubble Sort.

```mermaid
mindmap
  root((Bubble Sort Complexities))
    Time_Complexity
      Worst_Case
        O(n^2)
        Reverse_Sorted_Array
      Average_Case
        O(n^2)
        Random_Array
      Best_Case
        O(n)
        Already_Sorted_Array
        With_Early_Exit_Optimization
    Space_Complexity
      In-Place_Sorting
        O(1)
    Characteristics
      Stable_Sort
      Comparison_Based
      Simple_Implementation
    Optimizations
      Early_Exit_Flag
      Cocktail_Shaker_Sort
      
```


**Explanation:**

- **Time Complexity Branch:**
  - Details different cases and their complexities.
- **Space Complexity Branch:**
  - Notes the in-place nature of the algorithm.
- **Characteristics Branch:**
  - Summarizes key features.
- **Optimizations Branch:**
  - Lists common optimizations applied to Bubble Sort.

---

## **Notes on Diagram Limitations**

- **Graphical Plots:**
  - Mermaid does not support plotting graphs with axes to show \( T(n) \) vs. \( n \) or \( n^2 \).
  - For detailed graphs, consider using external tools or programming libraries (e.g., Matplotlib in Python).

- **Tables:**
  - Mermaid's support for detailed tables is limited.
  - The class diagram is used here to represent comparative data.

---

## **Conclusion**

These diagrams provide a visual representation of the Bubble Sort algorithm and its complexities. By illustrating the algorithm's flow, comparison mechanism, and time complexities, we can better understand its behavior and performance characteristics. Visual tools like Mermaid help in conceptualizing these aspects, aiding in both learning and teaching the fundamentals of algorithm analysis.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---