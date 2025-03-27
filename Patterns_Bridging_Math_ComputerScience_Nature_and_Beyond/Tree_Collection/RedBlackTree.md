---
created: 2025-03-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Red Black Tree - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


Below is a comprehensive breakdown provides a solid understanding of Red-Black Trees, covering their properties, operations, rebalancing strategies, and complexities. The combination of visual diagrams, step-by-step examples, and conceptual explanations makes the information accessible to various learning styles. Remember that the specific implementation details of insertion and deletion can be quite intricate, but understanding the core principles and properties is crucial.


----


## 1. What is a Red-Black Tree?

A Red-Black Tree is a type of self-balancing binary search tree.  This means it automatically keeps its height small (logarithmic in the number of nodes) even as elements are inserted and deleted. This balancing is crucial for maintaining good performance for operations like search, insertion, and deletion, which all take O(log n) time in a balanced tree, compared to O(n) in the worst case for an unbalanced tree.

---

## 2. Properties of Red-Black Trees

A Red-Black Tree must satisfy these five properties:

1.  **Node Color:** Each node is either red or black.
2.  **Root Property:** The root node is always black.
3.  **Leaf Property (NIL Property):** All leaves (NIL nodes – representing the absence of a child) are considered black.
4.  **Red Property (No Double Red):**  If a node is red, both its children must be black.  This means no two red nodes can be adjacent on any path.
5.  **Black Height Property:** Every path from a given node to any of its descendant NIL nodes must contain the same number of black nodes.  This number is called the node's *black-height*.

```mermaid
---
title: "Properties of Red-Black Trees"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph LR
    subgraph RedBlackTreeProperties["Red-Black Tree Properties"]
    style RedBlackTreeProperties fill:#fdd3,stroke:#333,stroke-width:2px
    direction TB
        A["Property 1: Node Color"] --> A1["Each node is either red or black"]
        B["Property 2: Root Property"] --> B1["The root is black"]
        C["Property 3: Leaf Property"] --> C1["All leaves (NIL) are black"]
        D["Property 4: Red Property"] --> D1["No two adjacent red nodes"]
        D1 --> D2["If a node is red, both children are black"]
        E["Property 5: Black Height Property"] --> E1["Every path from a node to its descendant NIL nodes has the same number of black nodes"]

    end
```

---

## 3. Example Red-Black Tree (Visual Representation)

```mermaid
---
title: "Example Red-Black Tree (Visual Representation)"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TB
    subgraph RedBlackTreeExample["Example Red-Black Tree"]
      style RedBlackTreeExample fill:#dfd3,stroke:#333,stroke-width:2px
        A((13)):::black --> B((8)):::black
        A --> C((17)):::red
        B --> D((1)):::black
        B --> E((11)):::red
        C --> F((15)):::black
        C --> G((25)):::black
        D --> H(( )):::NIL
        D --> I(( )):::NIL
        E --> J(( )):::NIL
        E --> K(( )):::NIL
        F --> L(( )):::NIL
        F --> M(( )):::NIL
        G --> N((22)):::red
        G --> O((27)):::red
        N --> P(( )):::NIL
        N --> Q(( )):::NIL
        O --> R(( )):::NIL
        O --> S(( )):::NIL
    end
      classDef black fill:#000,color:#fff
      classDef red fill:#f00,color:#fff
      classDef NIL fill:#333,color:#fff
    
```

**Explanation:**

*   **Nodes:** Circles represent nodes, with the key value inside. Double circles in the above diagram represent `NIL` node, which is the child leaf.
*   **Colors:**  Black nodes are represented by black fill, red nodes by red fill. and `NIL` node with dark fill according to the standard representation.
*   **Root:** Node 13 is the root and is black.
*   **Leaves:** All NIL nodes (represented by empty circles) are considered black.
*   **Red Property:** No red node has a red child.
*   **Black Height:**  For example, all paths from node 13 to any NIL descendant have a black-height of 2 (excluding the NIL node itself, but consistent among all paths).

---

## 4. Operations on a Red-Black Tree

The main operations on a Red-Black Tree are:

*   **Search:** Identical to a regular Binary Search Tree (BST) search.  O(log n) time.
*   **Insertion:**  Insert the new node as in a BST, then rebalance the tree to maintain the Red-Black properties.  O(log n) time.
*   **Deletion:** Delete the node as in a BST, then rebalance. O(log n) time.

The rebalancing operations (rotations and recolorings) are the key to maintaining the tree's balance.

---

## 5. Rotations

Rotations are fundamental operations used to restructure the tree during insertion and deletion. There are two types:

*   **Left Rotation:**  Pivots the tree to the left around a given node.
*   **Right Rotation:** Pivots the tree to the right around a given node.

```mermaid
---
title: "Red Black Tree - Rotations"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph BT
    subgraph Left_Rotation["Left Rotation"]
       style Left_Rotation fill:#ddf3,stroke:#333,stroke-width:2px
       direction LR
        A[y] --> B[x]
        B --> C[α]
        B --> D[β]
        A --> E[γ]
        B1[x] --> C1[α]
        B1 --> A1[y]
        A1 --> D1[β]
        A1 --> E1[γ]
        LR["Left Rotate(y)"] --> B1
    end

    subgraph Right_Rotation["Right Rotation"]
    style Right_Rotation fill:#ddf3,stroke:#333,stroke-width:2px
    direction LR
        A[y] --> B[x]
        B --> C[α]
        B --> D[β]
        A --> E[γ]
        B2[x] --> C2[α]
        B2 --> A2[y]
        A2 --> D2[β]
        A2 --> E2[γ]
        RR["Right Rotate(x)"] --> A
    end
```
*   **Before Rotation:** The tree structure before the rotation.
*   **Left Rotate/Right Rotate:**  The action performed.
*   **After Rotation:** The resulting tree structure.
*   **Nodes:** x and y are the nodes involved in the rotation. α, β, and γ represent subtrees.

---

## 6. Insertion (Step-by-Step with Rebalancing)

Let's illustrate insertion with an example.  We'll insert the value 10 into a simplified Red-Black Tree.

**Initial Tree (Before Insertion):**

```mermaid
---
title: "Red Black Tree - Initial Tree (Before Insertion)"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TB
    A((13)):::black --> B((8)):::black
    A --> C((17)):::black
    B --> D((1)):::black
    B --> E((11)):::black
    C --> F((15)):::black
    C --> G((25)):::black

      classDef black fill:#000,color:#fff
      classDef red fill:#f00,color:#fff
```

**Step 1: BST Insertion**

Insert 10 as you would in a regular BST.  The new node is initially colored *red*.

```mermaid
---
title: "Red Black Tree - BST Insertion"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TB
    A((13)):::black --> B((8)):::black
    A --> C((17)):::black
    B --> D((1)):::black
    B --> E((11)):::black
    C --> F((15)):::black
    C --> G((25)):::black
    E --> H((10)):::red

  classDef black fill:#000,color:#fff
  classDef red fill:#f00,color:#fff
```

**Step 2: Check for Violations and Rebalance**

Now, we check for violations of the Red-Black properties. Node 10 (red) has a red parent (11), violating the Red Property.  We need to rebalance.  Here's where we use rotations and recoloring:

*   **Case Analysis:** The rebalancing strategy depends on the "uncle" of the newly inserted node (the sibling of the node's parent). In this case, node 10's uncle is node 1, which is **black**.
*   **Case 1: Uncle is Black**
(the uncle is RED)
    *   **Step 1 (Recolor):** Change the colors of the node's parent, and grandparent, and the uncle:


```mermaid
---
title: "Red Black Tree - Check for Violations and Rebalance - Recolor"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TB
    A((13)):::black --> B((8)):::red
    A --> C((17)):::black
    B --> D((1)):::black
    B --> E((11)):::black
    C --> F((15)):::black
    C --> G((25)):::black
    E --> H((10)):::red
    
classDef black fill:#000,color:#fff
classDef red fill:#f00,color:#fff

```

*   **Step 2 (Rotate):** Rotate around Node 8:


```mermaid
---
title: "Red Black Tree - Check for Violations and Rebalance - Rotate"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TB
    A((13)):::black --> B((8)):::red
    A --> C((17)):::black
    B --> D((1)):::black
    B --> E((10)):::black
    C --> F((15)):::black
    C --> G((25)):::black
    E --> H((11)):::red
    
classDef black fill:#000,color:#fff
classDef red fill:#f00,color:#fff

```

*   **Step 3 (Recolor):** Recolor the final tree:


```mermaid
---
title: "Red Black Tree - Check for Violations and Rebalance - Recolor"
config:
  layout: elk
  look: handDrawn
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#BB2528',
      'primaryTextColor': '#f529',
      'primaryBorderColor': '#7C0000',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TB
	A((13)):::black --> B((10)):::black
    A --> C((17)):::black
    B --> D((8)):::red
    D --> F((1)):::black
    D --> G(( )):::NIL
    B --> E((11)):::red
    E --> H(( )):::NIL
    E --> I(( )):::NIL
    
    C --> J((15)):::black
    C --> K((25)):::black
    
    J --> L(( )):::NIL
    J --> M(( )):::NIL
    
    K --> N(( )):::NIL
    K --> O(( )):::NIL
    
    F --> O1(( )):::NIL
    F --> P(( )):::NIL
    
    G --> Q(( )):::NIL
    G --> R(( )):::NIL
    
    H --> S(( )):::NIL
    H --> T(( )):::NIL
    
    I --> U(( )):::NIL
    I --> V(( )):::NIL

classDef black fill:#000,color:#fff
classDef red fill:#f00,color:#fff
classDef NIL fill:#333,color:#fff
    
```

----


## 7. Deletion (Conceptual Overview)

Deletion is more complex than insertion but follows a similar principle:

1.  **BST Deletion:** Delete the node as in a regular BST.
2.  **Rebalancing:**  If the deleted node or its replacement was black, this can violate the Black Height Property.  We use a series of rotations and recolorings, similar to insertion, to restore the Red-Black properties.  There are multiple cases to consider, depending on the colors of the replacement node, its sibling, and its nephews.

----

## 8. Time and Space Complexity

*   **Time Complexity:**
    *   Search: O(log n)
    *   Insertion: O(log n)
    *   Deletion: O(log n)
*   **Space Complexity:** O(n) - We need to store the nodes.

----

## 9. Key Terms and Concepts

```mermaid
---
title: "Red Black Tree - Key Terms and Concepts"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: dark
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'themeVariables': {
      'fontSize': '12px',
      'fontFamily': 'Fantasy'
    }
  }
}%%
mindmap
    root((Red-Black Tree))
        Definition
            ["A self-balancing binary search tree"]
            ["Guarantees O(log n) time for search, insertion, and deletion"]
        Properties
            ["Node Color:<br>Red or Black"]
            ["Root Property:<br>Root is Black"]
            ["Leaf Property:<br>NIL nodes are Black"]
            ["Red Property:<br>No adjacent red nodes"]
            ["Black Height Property:<br>Equal black nodes on all paths to NIL descendants"]
        Operations
            Search["O(log n) - Like BST search"]
            Insertion["O(log n) - BST insert + rebalancing"]
            Deletion["O(log n) - BST delete + rebalancing"]
        Rebalancing
            Rotations
                [Left Rotation]
                [Right Rotation]
            Recoloring[Changing node colors]
            ["Case Analysis based on uncle/sibling/nephew colors"]
        Complexity
            ["Time: O(log n) for core operations"]
            ["Space: O(n)"]
        Advantages
            ["Guaranteed logarithmic performance"]
            ["Efficient for frequent insertions/deletions"]
        Disadvantages
           ["More complex implementation than simpler trees"]
        Use_Cases
            ["Operating system schedulers"]
            ["Databases<br>(e.g., indexes)"]
            ["Language implementations<br>(e.g., standard library maps/sets)"]
            ["Anywhere balanced search trees are needed"]
            
```


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---