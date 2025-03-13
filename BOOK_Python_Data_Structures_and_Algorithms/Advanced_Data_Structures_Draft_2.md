---
created: 2025-03-12 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://www.packtpub.com/en-us/product/python-data-structures-and-algorithms-9781786467355"
---



# Advanced Data Structures
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



Here's a more comprehensive Mermaid diagram for "Advanced Data Structures," drawing from the provided text and expanding on the concepts:

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
    subgraph Advanced_Data_Structures["Advanced Data Structures"]
    style Advanced_Data_Structures fill:#bfb3,stroke:#333,stroke-width:1px
        A["Stacks"] --> A1["LIFO<br>(Last In, First Out)"]
        A1 --> A2("Push: O(1)")
        A1 --> A3("Pop: O(1)")
        A1 --> A4("Peek: O(1)")
        A1 --> A5("Applications:<br>Call Stack, Expression Evaluation")
        A --> B["Queues"]
        B --> B1["FIFO<br>(First In, First Out)"]
        B1 --> B2("Enqueue:<br>O(1) or O(n)")
        B1 --> B3("Dequeue:<br>O(1) or O(n)")
        B1 --> B4("Applications:<br>Task Scheduling, Media Player")
        B --> C["Linked Lists"]
        C --> C1["Nodes & Pointers"]
        C1 --> C2("Singly Linked")
        C1 --> C3("Doubly Linked")
        C1 --> C4("Circular Linked")
        C1 --> C5("O(1) append in doubly linked list")
        C --> D["Trees"]
        D --> D1["Hierarchical Data"]
        D1 --> D2("Binary Trees:<br>O(log n) search")
        D1 --> D3("BSTs:<br>Binary Search Trees -<br> O(log n) best,<br> O(n) worst")
        D1 --> D4("Self-Balancing Trees:<br>AVL, Red-Black - O(log n)")
        D1 --> D5("Heaps:<br> O(log n) insert/delete")
        D --> E["Graphs"]
        E --> E1["Vertices & Edges"]
        E1 --> E2("Directed Graphs")
        E1 --> E3("Undirected Graphs")
        E1 --> E4("Weighted Graphs")
        E1 --> E5("Adjacency List, Adjacency Matrix")
        E1 --> E6("BFS - Breadth First Search:<br>O(V+E)")
        E1 --> E7("DFS - Depth First Search:<br>O(V+E)")
    end
    
    subgraph Deque["Deque<br>(Double-Ended Queue)"]
    style Deque fill:#ccf3,stroke:#333,stroke-width:1px
        DQ["Deque"] --> DA["List-like with efficient appends/pops"]
        DA --> DA1("Append/Pop Left: O(1)")
        DA --> DA2("Append/Pop Right: O(1)")
        DA --> DA3("Rotate")
        DA --> DA4("maxlen parameter for circular buffer")
    end

    subgraph Hashing_and_Symbol_Tables["Hashing & Symbol Tables"]
    style Hashing_and_Symbol_Tables fill:#cff3,stroke:#333,stroke-width:1px
        HS["Hash Tables"] --> HSa["Key-Value Storage"]
        HSa --> HSb("Average O(1) access")
        HSa --> HSc("Collisions:<br>Chaining, Open Addressing")
        HS --> HSm["Symbol Tables"]
        HSm --> HSd("Compiler/Interpreter Use")
        HSm --> HSe("Symbol Lookup")
    end
    
    A --> DQ
    B --> DQ
    
```


----

**Key Improvements and Expansions:**

*   **More Detail for Each Structure:** Each data structure now includes more specific operations and characteristics.
*   **Time Complexity:** Key operations (e.g., push, pop, enqueue, dequeue) are now annotated with their typical time complexities (Big O notation).  This is crucial for understanding performance.
*   **Applications:** Real-world use cases for each data structure are listed to give more context.
*   **Tree Specializations:**  The "Trees" section is expanded to include Binary Search Trees (BSTs) and Self-Balancing Trees.
*    **Heaps**: Added heaps to provide different ordering for elements and its time complexity.
*   **Graphs:** Graph representation techniques such as adjacency lists and adjacency matrices, plus the Breadth First Search (BFS) and Depth First Search (DFS) algorithms are listed.
*   **Deques and Circular Buffers:** Added `Deque` data structure with its utility to be a circular buffer.
*   **Hashing and Symbol Tables:** Added the `Hashing & Symbol Tables` from chapter 7 in original document and linked with its feature details.




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---