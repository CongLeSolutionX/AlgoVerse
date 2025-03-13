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



This document is an expansion of the initial version [here](./Advanced_Data_Structures_Draft_1.md), providing a comprehensive overview of advanced data structures and their implementations in Python, along with relevant algorithms and their complexities.  It covers stacks, queues, linked lists, trees, graphs, deques, hashing, and symbol tables, with a focus on practical applications and performance analysis.


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
        A1 --> A5("Applications:<br>Call Stack, Expression Evaluation, Undo/Redo Functionality, Backtracking Algorithms")
        A --> B["Queues"]
        B --> B1["FIFO<br>(First In, First Out)"]
        B1 --> B2("Enqueue:<br>O(1) or O(n)")
        B1 --> B3("Dequeue:<br>O(1) or O(n)")
        B1 --> B4("Applications:<br>Task Scheduling, Media Player, Print Queue, Asynchronous Data Transfer")
        B --> C["Linked Lists"]
        C --> C1["Nodes & Pointers"]
        C1 --> C2("Singly Linked")
        C2 --> C2a("Insert/Delete at Head: O(1)")
        C2 --> C2b("Insert/Delete at Tail: O(n)")
        C2 --> C2c("Search: O(n)")
        C1 --> C3("Doubly Linked")
        C3 --> C3a("Insert/Delete at Head/Tail: O(1)")
        C3 --> C3b("Search: O(n)")
        C1 --> C4("Circular Linked")
        C4 --> C4a("Traversal loops back to head")
    C4 --> C4b("Applications: Round Robin Scheduling")
        C1 --> C5("O(1) append in doubly linked list")
        C --> D["Trees"]
        D --> D1["Hierarchical Data"]
        D1 --> D2("Binary Trees:<br>O(log n) search (balanced)")
        D1 --> D3("BSTs:<br>Binary Search Trees -<br> O(log n) best,<br> O(n) worst")
        D3 --> D3a("Search, Insert, Delete:<br>O(log n) average, O(n) worst")
        D1 --> D4("Self-Balancing Trees:<br>AVL, Red-Black - O(log n)")
        D4 --> D4a("Guaranteed O(log n) for all operations")
        D1 --> D5("Heaps:<br> O(log n) insert/delete")
        D5 --> D5a("Priority Queues")
        D5 --> D5b("Binary Heap: Min-Heap, Max-Heap")
        D5 --> D5c("Heapify: O(n)")
    D5 --> D5d("Heapsort: O(n log n)")
        D --> E["Graphs"]
        E --> E1["Vertices & Edges"]
        E1 --> E2("Directed Graphs (Digraphs)")
        E2 --> E2a("One-way connections")
        E1 --> E3("Undirected Graphs")
        E3 --> E3a("Two-way connections")
        E1 --> E4("Weighted Graphs")
        E4 --> E4a("Edges have associated costs")
        E1 --> E5("Adjacency List, Adjacency Matrix")
        E5 --> E5a("Adjacency List: Space efficient for sparse graphs")
    E5 --> E5b("Adjacency Matrix: Space efficient for dense graphs, fast edge lookup")
        E1 --> E6("BFS - Breadth First Search:<br>O(V+E)")
        E6 --> E6a("Shortest Path (Unweighted)")
        E6 --> E6b("Uses a Queue")
        E1 --> E7("DFS - Depth First Search:<br>O(V+E)")
        E7 --> E7a("Uses a Stack (or recursion)")
    E7 --> E7b("Topological Sorting (Directed Acyclic Graphs)")
    E7 --> E7c("Finding Connected Components")
    end
    
    subgraph Deque["Deque<br>(Double-Ended Queue)"]
    style Deque fill:#ccf3,stroke:#333,stroke-width:1px
        DQ["Deque"] --> DA["List-like with efficient appends/pops"]
        DA --> DA1("Append/Pop Left: O(1)")
        DA --> DA2("Append/Pop Right: O(1)")
        DA --> DA3("Rotate: O(k) where k is the number of rotations")
        DA --> DA4("maxlen parameter for circular buffer")
        DA --> DA5("Applications:<br>Sliding Window Problems, Task Scheduling")
    end

    subgraph Hashing_and_Symbol_Tables["Hashing & Symbol Tables"]
    style Hashing_and_Symbol_Tables fill:#cff3,stroke:#333,stroke-width:1px
        HS["Hash Tables"] --> HSa["Key-Value Storage"]
        HSa --> HSb("Average O(1) access, insert, delete")
        HSa --> HSc("Collisions:<br>Chaining, Open Addressing")
        HSc --> HSc1("Chaining: Linked List at each index")
        HSc --> HSc2("Open Addressing: Linear Probing, Quadratic Probing, Double Hashing")
        HS --> HSm["Symbol Tables"]
        HSm --> HSd("Compiler/Interpreter Use")
        HSm --> HSe("Symbol Lookup: O(1) average, O(n) worst")
        HSm --> HSf("Scope Management")
    end
    
    A --> DQ
    B --> DQ
    
    subgraph Tree_Traversal["Tree Traversal"]
        style Tree_Traversal fill:#bfc3,stroke:#333,stroke-width:1px
        D -- Depth First Traversal --> TT1["Pre-order (Root, Left, Right)"]
        D -- Depth First Traversal --> TT2["In-order (Left, Root, Right) - BST only"]
        D -- Depth First Traversal --> TT3["Post-order (Left, Right, Root)"]
        D -- Breadth First Traversal --> TT4["Level-order (Uses a Queue)"]
    end

    subgraph Graph_Algorithms["Graph Algorithms"]
        style Graph_Algorithms fill:#bbf3,stroke:#333,stroke-width:1px
         E -- Shortest Path Algorithms --> GA1["Dijkstra's Algorithm (Weighted, Non-negative)"]
         GA1 --> GA1a("O(V^2) with Adjacency Matrix")
     GA1 --> GA1b("O((V + E) log V) with Adjacency List and Min-Heap")
         E -- Shortest Path Algorithms --> GA2["Bellman-Ford Algorithm (Weighted, Negative Edges)"]
         GA2 --> GA2a("O(VE)")
         E -- Shortest Path Algorithms --> GA3["Floyd-Warshall Algorithm (All Pairs Shortest Paths)"]
     GA3 --> GA3a("O(V^3)")
         E -- Minimum Spanning Tree --> GA4["Prim's Algorithm"]
     GA4 --> GA4a("O(E log V) with Min-Heap")
         E -- Minimum Spanning Tree --> GA5["Kruskal's Algorithm"]
     GA5 --> GA5a("O(E log E) or O(E log V)")
    end
    
```

----


## Detailed Explanations


### 1. Stacks

*   **LIFO (Last In, First Out):**  The last element added to the stack is the first element removed.
*   **Operations:**
    *   `Push`: Adds an element to the top of the stack.  O(1) time complexity.
    *   `Pop`: Removes the top element from the stack. O(1) time complexity.
    *   `Peek`:  Returns the top element without removing it. O(1) time complexity.
    *   `isEmpty`: Checks if the stack is empty. O(1) time complexity.
*   **Applications:**
    *   **Call Stack:**  Managing function calls in program execution.
    *   **Expression Evaluation:**  Converting infix expressions to postfix and evaluating them.
    *   **Undo/Redo Functionality:**  Storing previous states for undo operations.
    * **Backtracking Algorithms:** Explore the options and revert back if a dead end is found.

---

### 2. Queues

*   **FIFO (First In, First Out):** The first element added to the queue is the first element removed.
*   **Operations:**
    *   `Enqueue`: Adds an element to the rear of the queue.  O(1) for most Python implementations (using `collections.deque`), but can be O(n) for list-based implementations if resizing is needed.
    *   `Dequeue`: Removes the front element from the queue. O(1) for `collections.deque`, O(n) for list-based implementations.
    *   `isEmpty`: Checks if the queue is empty.  O(1).
    *   `isFull`: Checks if the queue is full (relevant for fixed-size queues). O(1)
*   **Applications:**
    *   **Task Scheduling:**  Managing tasks in operating systems or applications.
    *   **Media Player Queues:**  Storing songs or videos to be played.
    *   **Print Queues:**  Managing print jobs.
    *   **Asynchronous Data Transfer:** Handling data streams between processes.

---


### 3. Linked Lists

*   **Nodes & Pointers:**  Data is stored in nodes, each containing a data element and a pointer (reference) to the next node.
*   **Types:**
    *   **Singly Linked List:**  Each node points to the next node.
        *   Insert/Delete at Head: O(1)
        *   Insert/Delete at Tail: O(n) (unless a tail pointer is maintained)
        *   Search: O(n)
    *   **Doubly Linked List:** Each node points to both the next and previous nodes.
        *   Insert/Delete at Head/Tail: O(1)
        *   Search: O(n)
    *   **Circular Linked List:**  The last node's pointer points back to the head.
        *   Useful for applications where continuous looping is required (e.g., Round Robin scheduling).
* **Advantages over Arrays**: Dynamic size. Efficient insertion/deletion in the middle (for doubly linked lists).
* **Disadvantages over Arrays**: No constant-time random access. Extra memory overhead for pointers.

---


### 4. Trees

*   **Hierarchical Data Structure:**  Data is organized in a hierarchy of nodes, with a root node and child nodes.
*   **Types:**
    *   **Binary Tree:**  Each node has at most two children (left and right).
    *   **Binary Search Tree (BST):**  A binary tree where the left child's value is less than the parent's value, and the right child's value is greater.
        *   Search, Insert, Delete: O(log n) average case (balanced tree), O(n) worst case (skewed tree).
    *   **Self-Balancing Trees (AVL, Red-Black):**  Trees that automatically adjust their structure to maintain balance, ensuring O(log n) performance for all operations.
    *   **Heaps:**  A complete binary tree (all levels are filled except possibly the last, which is filled from left to right) that satisfies the heap property (min-heap or max-heap).
        *   **Min-Heap:**  The value of each node is less than or equal to the value of its children.
        *   **Max-Heap:**  The value of each node is greater than or equal to the value of its children.
        *   Insert/Delete: O(log n)
        *   Heapify (build a heap from an array): O(n)
        *   Heapsort: O(n log n) sorting algorithm.  Uses a heap to efficiently sort an array.
*   **Tree Traversal:**
    *   **Depth-First Traversal:**
        *   **Pre-order:** Visit the root, then the left subtree, then the right subtree.
        *   **In-order:** Visit the left subtree, then the root, then the right subtree (BSTs only - produces sorted output).
        *   **Post-order:** Visit the left subtree, then the right subtree, then the root.
    *   **Breadth-First Traversal (Level-order):**  Visit nodes level by level, using a queue.

---

### 5. Graphs

*   **Vertices & Edges:**  Data is represented as a set of vertices (nodes) and edges (connections between vertices).
*   **Types:**
    *   **Directed Graphs (Digraphs):**  Edges have a direction (one-way).
    *   **Undirected Graphs:** Edges have no direction (two-way).
    *   **Weighted Graphs:**  Edges have associated weights (costs).
*   **Representations:**
    *   **Adjacency List:**  Each vertex stores a list of its adjacent vertices.  Space-efficient for sparse graphs (few edges).
    *   **Adjacency Matrix:**  A 2D array where `matrix[i][j]` indicates the presence (or weight) of an edge between vertex `i` and vertex `j`. Space-efficient for dense graphs (many edges), provides fast edge lookup.
*   **Graph Algorithms:**
    *   **Breadth-First Search (BFS):**  Explores the graph level by level, using a queue.  Finds the shortest path in unweighted graphs. O(V+E) time complexity.
    *   **Depth-First Search (DFS):**  Explores the graph by going as deep as possible along each branch before backtracking, using a stack (or recursion). O(V+E) time complexity.  Useful for topological sorting (directed acyclic graphs) and finding connected components.
    * **Shortest Path Algorithms**:
        *   **Dijkstra's Algorithm:**  Finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. O(V^2) with an adjacency matrix, O((V + E) log V) with an adjacency list and a min-heap.
        *   **Bellman-Ford Algorithm:**  Finds the shortest path in a weighted graph that may contain negative edge weights (but no negative cycles). O(VE) time complexity.
        *   **Floyd-Warshall Algorithm:**  Finds the shortest paths between all pairs of vertices in a weighted graph. O(V^3) time complexity.
    * **Minimum Spanning Tree**:
        *   **Prim's Algorithm:** Finds a minimum spanning tree (a tree that connects all vertices with the minimum total edge weight) for a weighted, undirected graph. O(E log V) with a min-heap.
        *   **Kruskal's Algorithm:**  Another algorithm for finding a minimum spanning tree. O(E log E) or O(E log V) time complexity.

---

### 6. Deque (Double-Ended Queue)

*   **List-like with Efficient Appends/Pops:**  Allows efficient addition and removal of elements from both ends.
*   **Operations:**
    *   `appendleft`: Adds an element to the left. O(1)
    *   `append`: Adds an element to the right. O(1)
    *   `popleft`: Removes an element from the left. O(1)
    *   `pop`: Removes an element from the right. O(1)
    *   `rotate`: Rotates the deque by a specified number of steps. O(k), where k is the number of rotations.
    * `maxlen`: Optional parameter to create a bounded deque (circular buffer).
*   **Applications:**
    *   **Sliding Window Problems:**  Maintaining a window of elements in a stream.
    *   **Task Scheduling:** Can be used for scheduling tasks with different priorities.
    * Implementing stacks and queues.


----


### 7. Hashing and Symbol Tables

*   **Hash Tables:**  Data structure that uses a hash function to map keys to indices in an array (or a list of buckets).
    *   **Key-Value Storage:**  Stores data in key-value pairs.
    *   **Average O(1) access, insert, delete:**  In the average case, hash tables provide very fast operations.
    *   **Collisions:**  When different keys map to the same index.
        *   **Chaining:**  Each index stores a linked list of elements that hash to that index.
        *   **Open Addressing:**  If a collision occurs, the algorithm probes for an empty slot using techniques like:
            *   **Linear Probing:**  Checks consecutive slots.
            *   **Quadratic Probing:**  Checks slots with increasing quadratic offsets.
            *   **Double Hashing:**  Uses a second hash function to determine the probing sequence.
*   **Symbol Tables:**  A data structure used by compilers and interpreters to store information about symbols (variables, functions, etc.) in a program.
    *   **Compiler/Interpreter Use:**  Used for symbol lookup, scope management, and type checking.
    *   **Symbol Lookup:**  Finding the information associated with a symbol. O(1) average case, O(n) worst case (for hash table implementations).
    * **Scope Management:** Keeping track of which symbols are visible in different parts of the code.

---

## Mathematical Notation (LaTeX)

*   **Time Complexity:**
    *   Big O Notation:  O(n), O(log n), O(n log n), O(n^2), etc.
    *   Example:  $O(n \log n)$ (for heapsort)
*   **Heap Property (Min-Heap):**
    $$
    \forall i, \text{parent}(i) \le \text{child}(i)
    $$
*  **Heap Property (Max-Heap):**

    $$
     \forall i,  parent(i) \ge child(i)
    $$
* **Adjacency Matrix:**

  $$
  A_{ij} =
  \begin{cases}
  1, & \text{if there is an edge from vertex } i \text{ to vertex } j \\
  0, & \text{otherwise}
  \end{cases}
  $$

  For weighted graphs, $A_{ij}$ would store the weight of the edge.

* **Dijkstra's Algorithm (Shortest Path):**

  $$
    d[v] = \min(d[v], d[u] + w(u, v))
  $$

Where:
* $d[v]$ is the shortest distance from the source vertex to vertex $v$.
* $d[u]$ is the shortest distance from the source vertex to vertex $u$.
* $w(u, v)$ is the weight of the edge between vertex $u$ and vertex $v$.

* **Hash Function:**
$$
h(k) = k \mod m
$$

Where:
* $h(k)$ is the hash value for key $k$.
* $k$ is the key.
* $m$ is the size of the hash table.
This is a simple example of a hash function (division method). Other, more sophisticated hash functions exist.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---