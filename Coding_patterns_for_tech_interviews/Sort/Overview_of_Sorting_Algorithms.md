---
created: 2025-01-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
---

# Overview of Sorting Algorithms

Below is a series of diagrams using Mermaid syntax to visually represent the core concepts of sorting algorithms in a way that enhances understanding and provides a clear reference.


## Diagram 1: Overview of Sorting Algorithms

```mermaid
graph LR
    A[Sorting Algorithms] --> B(Purpose);
    B --> B1[Arrange items in a specific order];
    A --> C(Order);
    C --> C1[Numerical];
    C --> C2[Lexicographical];
    A --> D(Direction);
    D --> D1[Ascending];
    D --> D2[Descending];
    A --> E(Importance);
    E --> E1[Reduces problem complexity];
    E --> E2[Applications in searching, databases, etc.];

    style A fill:#f29f,stroke:#333,stroke-width:2px
    style B fill:#c2cf,stroke:#333
     style C fill:#c2cf,stroke:#333
      style D fill:#c2cf,stroke:#333
       style E fill:#c2cf,stroke:#333
```

---

## Diagram 2: Algorithm Trade-offs

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Algorithm Trade-offs] --> B{Questions to Ask};
    B --> B1[How big is the collection?];
    B --> B2[How much memory is available?];
    B --> B3[Does the collection need to grow?];
    
    A--> C{Implications};
    C-->C1[Determines best algorithm];
    C-->C2[Space requirements];
    C-->C3[Resource limitations];
    
    style A fill:#F277,stroke:#333;
    
```


----

## Diagram 3: Classification Parameters of Sorting Algoritms

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A["Sorting Algorithm Classification"] --> B{"Based on Swaps or Inversions"};
    B --> B1["Number of times elements are swapped"];
    B --> B2["Selection Sort has minimum swaps"];

    A --> C{"Based on Comparisons"};
    C -->C1["Number of times elements are compared"];
    C-->C2["Most algos: O(nlogn) best, O(n^2) worst cases"];

    A --> D{"Based on Recursion or Non-Recursion"};
    D-->D1["Quick Sort, Merge Sort - recursive"];
    D-->D2["Selection Sort, Insertion Sort - Non-recursive"];
        
    A --> E{"Based on Stability"};
    E-->E1["Stable algos maintain order of equal keys"];
    E-->E2["Insertion, Merge, Bubble - stable"];
    E-->E3["Heap, Quick Sort - Not stable"];
    
    A --> F{"Based on Extra Space Requirement"};
    F --> F1["In-place algos require constant O(1) space"];
    F --> F2["Insertion, Quick Sort - in place"];
    F --> F3["Merge Sort - out of place (extra memory needed)"];

    style A fill:#72F7,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    style D fill:#c2cf,stroke:#333
    style E fill:#c2cf,stroke:#333
    style F fill:#c2cf,stroke:#333
    
```

----

## Diagram 4: Bucket Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Bucket Sort] --> B{Concept};
    B --> B1[Divides elements into buckets];
    B --> B2[Sorts buckets individually];
    B --> B3[Useful for uniformly distributed inputs];

    B --> C{Pseudo Code};
    C --> C1["Insert elements into buckets based on properties"];
    C --> C2["Sort each bucket (e.g. Insertion Sort)"];
    
    A --> D{"Time Complexity"};
    D-->D1["Best Case: O(N)"];
    
    style A fill:#A21A,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    style D fill:#c2cf,stroke:#333
    
```

------

## Diagram 5: Counting Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Counting Sort] --> B{Mechanism};
    B --> B1[Counts occurrences of each element];
    B --> B2[Modifies count array to indicate positions];
    B --> B3[Outputs elements based on the modified count array];
    
    A --> C{"Properties"};
    C --> C1["Space Complexity: O(K)"];
    C --> C2["Time Complexity: O(n+K)"];
    C --> C3["Stable: Yes"];
    
    style A fill:#E28E,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    
```



-----

## Diagram 6: Insertion Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Insertion Sort] --> B{Process};
    B --> B1[Compares key element with previous elements];
    B --> B2[Moves elements greater than the key to the right];
    B --> B3[Inserts the key into the correct position];

    A--> C{Properties};
    C --> C1["Space Complexity: O(1)"];
    C --> C2["Time Complexity : Best O(n) Average O(n*n) Worst O(n*n)"];
    C --> C3[Stable: Yes, <br> In-place: Yes];
    
    style A fill:#E27A,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333

```

----

## Diagram 7: Heap Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Heap Sort] --> B{Concept};
    B --> B1[Uses a max heap data structure];
    B --> B2[Leverages heap property to find max element];
    B --> B3[Repeatedly extracts the max element and places it in the sorted array];
    
    A--> C{Properties};
    C --> C1["Space Complexity: O(1)"];
    C --> C2["Time Complexity: O(nlogn) all cases"];
    C --> C3[Not Stable];
    
    style A fill:#A2BC,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    
```


-----

## Diagram 8: Radix Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Radix Sort] --> B{Mechanism};
    B --> B1[Sorts input based on digits from least to most significant];
    B --> B2[Uses Counting Sort as a subroutine];

    A--> C{Time Complexity};
    C-->C1["O(nk), k = number of digits"]
    
    style A fill:#A2CC,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    
```


----

## Diagram 9: Selection Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Selection Sort] --> B{Process};
    B --> B1["Finds the minimum element and swaps"];
    B --> B2["Repeats the process for remaining array"];

    A --> C{"Time Complexity"};
    C --> C1["O(n^2) all cases"];
    A --> D{Space Complexity};
    D --> D1["O(1)"];
    A --> E{Properties}
    E --> E1[Stable: No, In place: Yes]

    style A fill:#C2DE,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    style D fill:#c2cf,stroke:#333
    style E fill:#c2cf,stroke:#333
    
```



----

## Diagram 10: Bubble Sort


```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Bubble Sort] --> B{Process};
    B --> B1["Repeatedly compares adjacent elements"];
    B --> B2["Swaps if elements are in wrong order <br> (bubbling up the largest element)"];

    A --> C{"Time Complexity"};
    C --> C1["Best-O(n), <br> Average-O(n^2), <br> Worst-O(n^2)"];
    A --> D{Space Complexity};
    D-->D1["O(1)"];
    
    A--> E{Properties};
    E-->E1[Stable: Yes];
    
    style A fill:#D2DC,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    style D fill:#c2cf,stroke:#333
    style E fill:#c2cf,stroke:#333
    
```



----

## Diagram 11: Quick Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Quick Sort] --> B{Mechanism};
    B --> B1[chooses pivot element];
    B --> B2[Partitions the array around the pivot];
    B --> B3[Sorts subarrays recursively];
    
    A --> C{Properties};
    
    C-->C1["Stable: No, <br> In place: Yes"];
    C-->C2["Time Complexity: <br> Best: O(n log n), <br> Average: O(n log n), <br> Worst: O(n^2)"];

    style A fill:#E2EC,stroke:#333
    style B fill:#c2cf,stroke:#333
    style C fill:#c2cf,stroke:#333
    
```




----


## Diagram 12: Timsort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Tim Sort] --> B{Concept};
    B --> B1["Hybrid sorting algorithm - combine Insertion sort and Merge sort"];
    B --> B2["Effective with real-world data patterns"];

    A-->C{Properties};
    C-->C1["Stable: Yes"];
    C-->C2["Time Complexity: O(nlogn)"];
    
    style A fill:#D2DE,stroke:#333;
    style B fill:#c2cf,stroke:#333;
    style C fill:#c2cf,stroke:#333;
    
```


----

## Diagram 13: Merge Sort

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
graph LR
    A[Merge Sort] --> B{Algorithm};
    B --> B1[Divides array into two halves recursively];
    B --> B2[Merges the sorted halves];
    
    A-->C{Properties};
    C --> C1["Space Complexity: O(n)"];
    C --> C2["Time Complexity: O(n log n)"];
    C --> C3[Stable: Yes];
    C --> C4[Not In Place];

    style A fill:#E2CD,stroke:#333;
    style B fill:#c2cf,stroke:#333;
    style C fill:#c2cf,stroke:#333;
    
```


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---