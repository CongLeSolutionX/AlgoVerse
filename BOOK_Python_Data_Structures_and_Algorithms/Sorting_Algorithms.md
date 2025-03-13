---
created: 2025-03-12 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://www.packtpub.com/en-us/product/python-data-structures-and-algorithms-9781786467355"
---



# Sorting Algorithms
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## A Diagrammatic Guide 


Here's a more detailed and expanded Mermaid diagram for Sorting Algorithms, incorporating the content from the original document and relating it to relevant sub-topics and considerations:

```mermaid
---
title: "Python Data Structures and Algorithms"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    "graph": { "htmlLabels": false, 'curve': 'linear' },
    'themeVariables': {
        'fontFamily': 'Comic Sans MS',
        'fontSize': '20px',
        'primaryColor': '#ffff',
        'primaryTextColor': '#55ff',
        'primaryBorderColor': '#7c2',
        'lineColor': '#F8B229',
        'secondaryColor': '#006100',
        'tertiaryColor': '#fff'
    }
  }
}%%
graph LR
    subgraph Sorting_Algorithms["Sorting Algorithms"]
    style Sorting_Algorithms fill:#aaf3,stroke:#333,stroke-width:1px

        A[Comparison-Based Sorting] --> B{Comparison Mechanism}
        B --> C[Bubble Sort]:::detail
        C --> CA[Simple, Inefficient]
        C --> CB["O(n^2) Worst,<br>O(n) Best"]
        C --> CC[In-place, Stable]

        B --> D[Insertion Sort]:::detail
        D --> DA[Efficient for small datasets]
        D --> DB["O(n^2) Worst,<br>O(n) Best"]
        D --> DC[In-place, Stable]

        B --> E[Selection Sort]:::detail
        E --> EA[Simple Implementation]
        E --> EB["O(n^2) Always"]
        E --> EC[In-place, Unstable]

        B --> F[Quick Sort]:::detail
        F --> FA[Divide & Conquer]
        F --> FB[Pivot Selection]
        F --> FC[Partitioning]
        F --> FD["O(n^2) Worst,<br>O(n log n) Avg"]
        F --> FE["In-place (usually), Unstable"]

        B --> G[Heap Sort]:::detail;
        G --> GA[Uses Heap Data Structure]
        G --> GB["O(n log n) Always"]
        G --> GC[In-place, Unstable]

        A --> H[Key Factors]
        H --> HA[Time Complexity]
        H --> HB[Space Complexity]
        H --> HC[Stability]
        H --> HD[Ease of Implementation]

    A --> I[Merge Sort]
    I --> IA[Divide & Conquer]
        I --> IB[Recursion]
        I --> IC["O(n log n) Always"]
        I --> ID[Stable]
        I --> IE["Not In-place (requires O(n) extra space)"]

    subgraph Non_Comparison_Based["Non-Comparison-Based Sorting"]
    style Non_Comparison_Based fill:#ddf3,stroke:#333,stroke-width:1px

       J[Bucket Sort] --> J1[Good for uniformly distributed data]
       J --> K[Radix Sort]
       K --> K1[Sorts integers by digits]
    end

    end

    classDef detail fill:#f9c3,stroke:#333,stroke-width:1px
    
```

---


**Explanation of Additions and Refinements:**

*   **Comparison-Based vs. Non-Comparison-Based Sorting:** Added a top-level split to distinguish between these two broad categories. The original document focused primarily on comparison-based sorts.
*   **Merge Sort Added:**  Since it was mentioned in the text, but not detailed as one of the main algorithms, I've included a basic entry for Merge Sort and made it a separate entry instead of "Comaparison-Based"
*    **More Details:** The comments and notes are provided so you can get a better understanding.
*   **Clarification of Properties:**  The properties (e.g., "In-place," "Stable") are now listed directly under each algorithm for easy comparison.
*   **Key Factors Added:** To show the influence of those factors
*   **Emphasis on Trade-offs:** It shows how different algorithms have different trade-offs between time complexity, space complexity, stability, and ease of implementation.




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---