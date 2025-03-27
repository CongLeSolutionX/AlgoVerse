---
created: 2025-03-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# AVL Trees - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## 1. Introduction: What are AVL Trees?

An AVL Tree, named after its inventors **A**delson-**V**elsky and **L**andis, is a self-balancing Binary Search Tree (BST). In an AVL tree, the heights of the two child subtrees of any node differ by at most one. This height-balancing property ensures that the tree remains relatively balanced, preventing scenarios where the tree degenerates into a linked list (which would lead to O(n) performance for operations). This balance guarantees that major operations like search, insertion, and deletion have a worst-case time complexity of O(log n), where n is the number of nodes in the tree.

```mermaid
---
title: AVL Trees - High-Level Concept
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
  root((AVL Tree))
    Definition["Self-Balancing Binary Search Tree (BST)"]
    Inventors["Adelson-Velsky & Landis (1962)"]
    Core_Property["Height-Balanced:<br>Height difference between left/right subtrees ≤ 1 for every node"]
    Purpose["Avoids BST degeneration into a linked list"]
    Benefit["Guarantees O(log n) worst-case time complexity for major operations"]
    Operations
        Search
        Insertion
        Deletion
    Mechanism["Maintains balance using Rotations"]
    
```


---

## 2. Mathematical Definition: The Balance Factor

The core of an AVL tree's self-balancing property lies in the **Balance Factor (BF)**. For any node in the tree, the balance factor is defined as:

$$
\text{BalanceFactor}(node) = \text{Height}(node.\text{rightSubtree}) - \text{Height}(node.\text{leftSubtree})
$$

*Note: Sometimes the definition is swapped (Left Height - Right Height). The key is consistency.*

For a tree to be considered an AVL tree, the balance factor of **every** node must be within the set {-1, 0, 1}.

*   **BF = -1:** The left subtree is one level deeper than the right subtree.
*   **BF = 0:** The left and right subtrees have the same height.
*   **BF = +1:** The right subtree is one level deeper than the left subtree.

If any node has a balance factor outside this range (e.g., -2 or +2), the tree is unbalanced, and rotations must be performed to restore the AVL property. The height of an empty subtree is typically defined as -1 or 0 (consistency is key). If using -1 for empty trees: `Height(null) = -1`.

```mermaid
---
title: AVL Tree - Balance Factor Definition
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
%%{
  init: {
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    A["Node 'X' in AVL Tree"] --> B["Calculate Heights of Subtrees"]
    B --> BL["Left Subtree Height<br>h<SUB>L</SUB> = Height(X.left)"]
    B --> BR["Right Subtree Height<br>h<SUB>R</SUB> = Height(X.right)"]
    BL --> C["Balance Factor Formula<br><b>BF(X) = h<SUB>R</SUB> - h<SUB>L</SUB></b>"]
    BR --> C
    C --> D{"Is BF(X) in {-1, 0, 1}?"}
    D -- Yes --> E["Node 'X' is Balanced"]
    D -- No --> F["Node 'X' is Unbalanced<br>(BF = -2 or BF = +2)"]
    F --> G["Rotations Required!"]

    style A fill:#eef3,stroke:#333,stroke-width:1px
    style C fill:#dde3,stroke:#333,stroke-width:2px
    style F fill:#fcc3,stroke:#a00,stroke-width:1px
    style G fill:#faa3,stroke:#a00,stroke-width:2px
    style E fill:#cfc3,stroke:#0a0,stroke-width:1px
    
```

---

## 3. Rotations: Maintaining Balance

When an insertion or deletion causes a node's balance factor to become -2 or +2, the tree must be rebalanced using **rotations**. Rotations are local transformations that change the structure of the tree to restore the height balance while preserving the Binary Search Tree property. There are four types of imbalances that require specific rotations:

1.  **Left-Left (LL) Case (BF = -2):** An insertion into the left subtree of the left child causes the imbalance. A **Single Right Rotation** is performed.
2.  **Right-Right (RR) Case (BF = +2):** An insertion into the right subtree of the right child causes the imbalance. A **Single Left Rotation** is performed.
3.  **Left-Right (LR) Case (BF = -2):** An insertion into the right subtree of the left child causes the imbalance. A **Double Rotation (Left rotation followed by Right rotation)** is performed.
4.  **Right-Left (RL) Case (BF = +2):** An insertion into the left subtree of the right child causes the imbalance. A **Double Rotation (Right rotation followed by Left rotation)** is performed.

```mermaid
---
title: "AVL Tree Rotations Overview"
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
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    A[Imbalance Detected at Node 'Z'] --> B{"What is BF(Z)?"}

    B -- "BF(Z) = -2 (Left Heavy)" --> C{Check BF of Left Child 'Y'};
    C -- "BF(Y) ≤ 0 (Left or Balanced)" --> D["LL Case:<br><b>Single Right Rotation</b> at Z"]
    C -- "BF(Y) = +1 (Right Heavy)" --> E["LR Case:<br><b>Left Rotation</b> at Y,<br>then <b>Right Rotation</b> at Z"]

    B -- "BF(Z) = +2 (Right Heavy)" --> F{Check BF of Right Child 'Y'};
    F -- "BF(Y) ≥ 0 (Right or Balanced)" --> G["RR Case:<br><b>Single Left Rotation</b> at Z"]
    F -- "BF(Y) = -1 (Left Heavy)" --> H["RL Case:<br><b>Right Rotation</b> at Y,<br>then <b>Left Rotation</b> at Z"]

    subgraph Rotations["Rotation Types"]
        style Rotations fill:#eee3,stroke:#555,stroke-width:1px
        D --- R1(Single Right)
        G --- R2(Single Left)
        E --- R3(Double LR)
        H --- R4(Double RL)
    end
```

*(Detailed diagrams of each rotation would typically follow here, showing the node movements, but are omitted for brevity in this overview structure).*

---

## 4. Operations

AVL trees support the standard BST operations, but with modifications to maintain balance after insertions and deletions.

*   **Search:** Identical to standard BST search. Since the tree is balanced, the height is logarithmic, guaranteeing **O(log n)** time complexity.
*   **Insertion:**
    1.  Insert the new node as in a standard BST.
    2.  Travel back up the tree from the newly inserted node towards the root.
    3.  For each node on the path, update its height.
    4.  Check the balance factor of each node on the path.
    5.  If an imbalance is found (BF = -2 or +2), perform the appropriate rotation (LL, RR, LR, or RL) based on the case. Note that only *one* rotation (single or double) is needed to fix the entire imbalance caused by an insertion.
    6.  The overall time complexity is **O(log n)** (BST insertion + height updates + at most one rotation).
*   **Deletion:**
    1.  Delete the node as in a standard BST (handling cases with 0, 1, or 2 children). If a node with two children is deleted, it's typically replaced by its inorder successor or predecessor.
    2.  Travel back up the tree from the *parent* of the physically removed node (or the replacement node) towards the root.
    3.  For each node on the path, update its height.
    4.  Check the balance factor of each node on the path.
    5.  If an imbalance is found, perform the appropriate rotation. Unlike insertion, deletion might require *multiple* rotations along the path back to the root to restore balance.
    6.  The overall time complexity is **O(log n)** (BST deletion + height updates + potentially multiple rotations up the path).

```mermaid
---
title: "AVL Tree Operations Flow"
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
    'graph': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#ffff',
      'primaryTextColor': '#55ff',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
graph TD
    subgraph Search_Op["Search(key)"]
     style Search_Op fill:#cce3, stroke:#00a
        S1[Start at Root] --> S2{Node == null?}
        S2 -- Yes --> S3[Not Found]
        S2 -- No --> S4{key == Node.key?}
        S4 -- Yes --> S5[Found!]
        S4 -- No --> S6{key < Node.key?}
        S6 -- Yes --> S7[Search Left Subtree]
        S6 -- No --> S8[Search Right Subtree]
        S7 --> S2
        S8 --> S2
    end

    subgraph Insert_Op["Insert(key)"]
	style Insert_Op fill:#cfc3, stroke:#0a0
        I1[Perform Standard BST Insert] --> I2[Trace Path Back to Root];
        I2 --> I3[Update Heights on Path];
        I3 --> I4{"Node Unbalanced?<br>(BF=-2 or +2)"}
        I4 -- No --> I5["Continue Up Path / Done"]
        I4 -- Yes --> I6["Perform Appropriate Rotation(s)"]
        I6 --> I7[Balance]
    end
    
```


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---