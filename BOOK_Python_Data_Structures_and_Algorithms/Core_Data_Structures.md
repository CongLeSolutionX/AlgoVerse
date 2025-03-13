---
created: 2025-03-12 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://www.packtpub.com/en-us/product/python-data-structures-and-algorithms-9781786467355"
---



# Core Data Structures
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


Here's an expanded Mermaid diagram for `Core Data Structures`, built from the information in the book extract, and drawing from more general knowledge of data structures:

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
    subgraph Core_Data_Structures["Core Data Structures"]
    style Core_Data_Structures fill:#f9f3,stroke:#333,stroke-width:1px
        A[Lists] --> A1[Sequential, Mutable]
        A1 --> A2{Implementation}
        A2 --> A21[Dynamic Arrays]
        A2 --> A22[Linked Lists]
        A1 --> A3{Characteristics}
        A3 --> A31[Ordered]
        A3 --> A32[Allow Duplicates]
        A3 --> A33[Variable Size]
        A --> A4{Operations}
        A4 --> A41[Append]
        A4 --> A42[Insert]
        A4 --> A43[Delete]
        A4 --> A44[Search]
        A4 --> A45[Iterate]
        A4 --> A46[Slice]

        B["Tuples"] --> B1["Sequential, Immutable"]
        B1 --> B2{Characteristics}
        B2 --> B21[Ordered]
        B2 --> B22[Allow Duplicates]
        B2 --> B23[Fixed Size]
        B --> B3{Use Cases}
        B3 --> B31[Returning Multiple Values from Function]
        B3 --> B32[Record Representation]
        B --> B4{Operations}
        B4 --> B41[Index]
        B4 --> B42[Slice]
        B4 --> B43[Iterate]
        B4 --> B44[Count]
        B4 --> B45[Index]

        C[Dictionaries] --> C1[Key-Value Pairs]
        C1 --> C2{Implementation}
        C2 --> C21[Hash Tables]
        C1 --> C3{Characteristics}
        C3 --> C31[Unordered]
        C3 --> C32[Mutable]
        C3 --> C33[Keys Must Be Immutable]
        C --> C4{Use Cases}
        C4 --> C41[Symbol Tables]
        C4 --> C42[Caching]
        C4 --> C43[Configuration Settings]
        C --> C5{Operations}
        C5 --> C51[Insert]
        C5 --> C52[Delete]
        C5 --> C53["Lookup<br>(Get)"]
        C5 --> C54[Update]
        C5 --> C55["Iterate<br>(Keys, Values, Items)"]

        D[Sets] --> D1[Unordered, Unique Elements]
        D1 --> D2{Implementation}
        D2 --> D21[Hash Tables]
        D1 --> D3{Characteristics}
        D3 --> D31["Mutable<br>(set)"]
        D3 --> D32["Immutable<br>(frozenset)"]
        D3 --> D33[No Duplicates]
        D --> D4{Use Cases}
        D4 --> D41[Membership Testing]
        D4 --> D42[Removing Duplicates]
        D4 --> D43["Set Operations<br>(Union, Intersection, Difference)"]
        D --> D5{Operations}
        D5 --> D51[Add]
        D5 --> D52[Remove]
        D5 --> D53[Membership Test]
        D5 --> D54[Union]
        D5 --> D55[Intersection]
        D5 --> D56[Difference]
    end
    
```

----


**Key Additions and Expansions:**

*   **Lists (A):** Added implementation details (dynamic arrays, linked lists) and characteristics (ordered, duplicates allowed, variable size) to provide a more complete picture. Also added common operations.
*   **Tuples (B):**  Included characteristics and use cases to highlight their advantages (returning multiple values, representing records). Added Operations.
*   **Dictionaries (C):** Added "Use Cases" (symbol tables, caching, configuration settings) to show practical applications. Added Operations.
*   **Sets (D):** Expanded on the operations sets support (union, intersection, difference, etc.) and different types of sets.


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---