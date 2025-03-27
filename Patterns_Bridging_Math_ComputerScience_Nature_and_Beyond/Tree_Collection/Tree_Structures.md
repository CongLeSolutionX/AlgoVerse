---
created: 2025-03-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Tree Structures (in Computer Science) - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


Below is a comprehensive overview covers the fundamental concepts of tree structures, different types of trees, their properties, operations, complexities, and applications.  The combination of Mermaid diagrams, code examples, and textual explanations provides a multi-faceted learning experience.


---


## 1. Basic Tree Structure

A tree is a hierarchical data structure. Unlike arrays, linked lists, stacks, and queues, which are linear, trees organize data in a non-linear, branching fashion. Here's a basic representation:

```mermaid
---
title: "Basic Tree Structure"
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
graph TD
    subgraph Tree_Structure["Basic Tree Structure"]
        style Tree_Structure fill:#eef3,stroke:#333,stroke-width:2px
        A[Root] --> B(Node B)
        A --> C(Node C)
        B --> D(Node D)
        B --> E(Node E)
        C --> F(Node F)
    end
```

**Explanation:**

*   **Root:**  The topmost node in the tree (Node A in this case).  Every tree has exactly one root.
*   **Nodes:** The elements of the tree (A, B, C, D, E, F).  Each node contains data and may have links to other nodes.
*   **Edges/Links:** The connections between nodes (represented by the arrows).  They show the hierarchical relationships.
*   **Parent:**  A node that has child nodes.  In the diagram, A is the parent of B and C.  B is the parent of D and E.
*   **Child:** A node that has a parent.  B and C are children of A.  D and E are children of B.
*   **Leaf:**  A node with no children (D, E, and F in this example).  Leaves are the "end points" of the tree's branches.
*   **Subtree:**  A node and all its descendants.  For instance, B and its children (D and E) form a subtree.
*   **Height**: Height of a node is the longest downward path to a leaf from that node.
*   **Depth**: Depth of a node is the length of the path from the root to the node.

----

## 2. Types of Trees

There are many specialized types of tree structures, each with its own properties and use cases. Let's illustrate some common ones with a class diagram:

```mermaid
---
title: "Types of Trees"
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
    'classDiagram': { 'htmlLabels': true },
    'fontFamily': 'Fantasy',
    'themeVariables': {
      'primaryColor': '#B528',
      'primaryTextColor': '#2cf',
      'primaryBorderColor': '#7C33',
      'lineColor': '#F8B229'
    }
  }
}%%
classDiagram
    class Tree{
        +data
        +children[]
        +insert()
        +delete()
        +search()
    }

    class BinaryTree{
        +left
        +right
    }
    Tree <|-- BinaryTree

    class BinarySearchTree{
        +insert(value)
        +delete(value)
        +search(value)
        +findMin()
        +findMax()
    }
    BinaryTree <|-- BinarySearchTree

    class AVLTree{
        +height
        +rotateLeft()
        +rotateRight()
        +rebalance()
    }
    BinarySearchTree <|-- AVLTree
    
    class RedBlackTree{
        +color
        +rotateLeft()
        +rotateRight()
        +rebalance()    
	}
	BinarySearchTree <|-- RedBlackTree

    class BTree{
        +m (order)
        +keys[]
        +children[]
        +insertNonFull()
        +splitChild()
    }
    Tree <|-- BTree

    class Trie{
      +isEndOfWord
      +children[ALPHABET_SIZE]
    }
    Tree <|-- Trie

    class Heap{
        +heapify()
        +insert()
        +extractMax()/extractMin()
    }
    Tree <|-- Heap
    
```

**Explanation:**

*   **`Tree` (General):**  The base class, representing the fundamental concept.  It has `data` (the value stored in the node) and `children` (a list of references to child nodes).  Basic operations like `insert`, `delete`, and `search` are defined.
*   **`BinaryTree`:**  A tree where each node has at most *two* children, typically referred to as `left` and `right`.
*   **`BinarySearchTree` (BST):**  A special type of binary tree where the values in the nodes are ordered.  For any node:
    *   All values in the left subtree are *less than* the node's value.
    *   All values in the right subtree are *greater than* the node's value.
    *   This ordering allows for efficient searching (hence the name).
      $$
      \text{Left Subtree Values} < \text{Node Value} < \text{Right Subtree Values}
      $$
*   **`AVLTree`:**  A self-balancing BST.  It maintains a balanced structure by performing rotations (`rotateLeft`, `rotateRight`) to ensure the height difference between the left and right subtrees of any node is at most 1.  This guarantees logarithmic time complexity for operations.
*   **`RedBlackTree`:** Another self-balancing BST.  It uses "colors" (red and black) assigned to nodes to maintain balance.  Rotations and color flips keep the tree relatively balanced.  Slightly less strict balancing than AVL trees, but often faster in practice for insertions and deletions.
*   **`BTree`:**  Designed for disk-based data storage (databases and file systems).  A B-tree node can have many children (determined by the "order," *m*).  It keeps keys sorted within each node and uses a multi-level index to efficiently locate data.
* **`Trie` (Prefix Tree):** Used for storing strings or sequences.  Each edge represents a character, and paths from the root to a node spell out a word or prefix.  Efficient for prefix-based searches (like autocomplete).

* **`Heap`:** A specialized tree-based data structure optimized for maintaining the minimum or maximum element. Heaps are commonly implemented using an underlying array to minimize memory overhead and enhance access speed.

----

## 3. Binary Search Tree (BST) Example with Operations

Let's visualize a BST and demonstrate insertion and search.

```mermaid
---
title: "Binary Search Tree (BST) Example with Operations"
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
graph TD
    subgraph BST_Example["Binary Search Tree"]
    style BST_Example fill:#def3,stroke:#333,stroke-width:2px
        A[50] --> B(30)
        A --> C(70)
        B --> D(20)
        B --> E(40)
        C --> F(60)
        C --> G(80)
    end

    subgraph Insert_25["Insert 25"]
    style Insert_25 fill:#fed3,stroke:#333,stroke-width:2px
       IN["Start at Root (50)"] --> INB{"25 < 50?"}
       INB -- "Yes" --> INC["Go Left (30)"]
       INC --> IND{"25 < 30?"}
       IND -- "Yes" --> INE["Go Left (20)"]
       INE --> INF{"25 < 20?"}
       INF -- "No" --> ING["Insert as Right Child of 20"]
    end

    subgraph Search_60["Search for 60"]
    style Search_60 fill:#fed3,stroke:#333,stroke-width:2px
       SE["Start at Root (50)"] --> SEB{"60 = 50?"}
       SEB -- "No" --> SEC{"60 < 50?"}
       SEC -- "No" --> SED["Go Right (70)"]
       SED --> SEE{"60 = 70?"}
       SEE -- "No" --> SEF{"60 < 70?"}
       SEF -- "Yes" --> SEG["Go Left (60)"]
       SEG --> SEH{"60 = 60?"}
       SEH -- "Yes" --> SEI["Found!"]
    end

    BST_Example -.-> Insert_25
    BST_Example -.-> Search_60

```


**Explanation:**

*   **`BST_Example`:** A simple BST with some initial values.
*   **`Insert_25`:**  Demonstrates the process of inserting a new value (25) into the BST:
    *   Start at the root (50).
    *   Compare the new value (25) with the current node's value.
    *   If it's less, go left; if it's greater, go right.
    *   Repeat until you find an empty spot (a `null` child) and insert the new node there.
*   **`Search_60`:** Shows how to search for a value (60):
    *   Start at the root (50).
    *   Compare the target value (60) with the current node's value.
    *   If they're equal, you've found it.
    *   If the target is less, go left; if it's greater, go right.
    *   Repeat until you find the value or reach a `null` child (meaning the value isn't present).

----

## 4. Tree Traversals (Code and Visualization)

There are several ways to "visit" all the nodes in a tree.  Common traversal methods include:

*   **In-order Traversal (Left, Root, Right):**  Visits the left subtree, then the current node, then the right subtree.  For a BST, this produces the values in *sorted* order.
*   **Pre-order Traversal (Root, Left, Right):**  Visits the current node, then the left subtree, then the right subtree.  Useful for creating a copy of the tree.
*   **Post-order Traversal (Left, Right, Root):**  Visits the left subtree, then the right subtree, then the current node.  Useful for deleting a tree.
* **Breadth-First Traversal (Level order):** Visits the tree level by level.

```swift
// Swift code for tree traversals (using a Binary Tree)

class TreeNode {
    var data: Int
    var left: TreeNode?
    var right: TreeNode?

    init(_ data: Int) {
        self.data = data
    }
}

func inorderTraversal(node: TreeNode?) {
    guard let node = node else { return }
    inorderTraversal(node: node.left)
    print(node.data, terminator: " ") // Process the node
    inorderTraversal(node: node.right)
}

func preorderTraversal(node: TreeNode?) {
    guard let node = node else { return }
    print(node.data, terminator: " ") // Process the node
    preorderTraversal(node: node.left)
    preorderTraversal(node: node.right)
}

func postorderTraversal(node: TreeNode?) {
    guard let node = node else { return }
    postorderTraversal(node: node.left)
    postorderTraversal(node: node.right)
    print(node.data, terminator: " ") // Process the node
}
func breadthFirstTraversal(root: TreeNode?) {
        guard let root = root else { return }

        var queue: [TreeNode] = []
        queue.append(root)

        while !queue.isEmpty {
            let node = queue.removeFirst()
            print(node.data, terminator: " ")

            if let leftChild = node.left {
                queue.append(leftChild)
            }
            if let rightChild = node.right {
                queue.append(rightChild)
            }
        }
    }

// Example Usage (using the BST from the previous diagram):
let root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left?.left = TreeNode(20)
root.left?.right = TreeNode(40)
root.right?.left = TreeNode(60)
root.right?.right = TreeNode(80)

print("In-order:")
inorderTraversal(node: root) // Output: 20 30 40 50 60 70 80
print("\nPre-order:")
preorderTraversal(node: root) // Output: 50 30 20 40 70 60 80
print("\nPost-order:")
postorderTraversal(node: root) // Output: 20 40 30 60 80 70 50
print("\nBreadth-First Traversal:")
breadthFirstTraversal(root: root)

```

```mermaid
---
title: "Tree Traversals Visualization"
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
graph TD
    subgraph Traversal_Example["Traversal of BST"]
        style Traversal_Example fill:#def3,stroke:#333,stroke-width:2px
        A[50] --> B(30)
        A --> C(70)
        B --> D(20)
        B --> E(40)
        C --> F(60)
        C --> G(80)

        subgraph Inorder["In-order Traversal"]
            direction LR
            D --> B --> E --> A --> F --> C --> G
        end

        subgraph Preorder["Pre-order Traversal"]
            direction LR
            A --> B --> D --> E --> C --> F --> G
        end

        subgraph Postorder["Post-order Traversal"]
            direction LR
            D --> E --> B --> F --> G --> C --> A
        end
         subgraph BreadthFirst["Breadth-First Traversal"]
            direction LR
            A --> B --> C --> D --> E --> F --> G
        end
    end

```


---

## 5. Time and Space Complexity

A key consideration for any data structure is its efficiency.  Here's a summary of the time and space complexity for common tree operations (focusing on balanced binary search trees):

| Operation         | Average Time Complexity | Worst-Case Time Complexity (Unbalanced Tree) | Space Complexity |
| ----------------- | ----------------------- | ------------------------------------------- | ---------------- |
| Search            | O(log n)                | O(n)                                        | O(n)             |
| Insertion         | O(log n)                | O(n)                                        | O(n)             |
| Deletion          | O(log n)                | O(n)                                        | O(n)             |
| Find Min/Max      | O(log n)                | O(n)                                        | O(1)             |
| Traversal (all) | O(n)                    | O(n)                                        | O(n)             |

**Explanation:**

*   **`n`:** The number of nodes in the tree.
*   **`O(log n)` (Logarithmic):**  This is the ideal case for balanced BSTs.  Because you effectively eliminate half the remaining search space with each comparison, the operations are very efficient, even for large trees.
*   **`O(n)` (Linear):**  This is the worst-case scenario, occurring when the tree is highly *unbalanced* (essentially becoming a linked list).  In this degenerate case, you might have to traverse all nodes.
*    **Space complexity:**
    *  **O(n)**  Worst-case scenario for recursive traversals where each node creates its own space.

---

## 6. Use Cases and Applications

Tree structures are used extensively in computer science:

*   **File Systems:**  Directories and files are organized hierarchically.
*   **Databases:**  B-Trees and their variants are crucial for indexing and efficient data retrieval.
*   **Compilers:**  Parse trees represent the syntactic structure of code.
*   **Networking:**  Routing algorithms often use tree-like structures.
*   **Decision Trees (Machine Learning):** Used for classification and regression tasks.
*   **HTML/XML Parsing:**  The Document Object Model (DOM) represents web pages as trees.
*   **Game AI:**  Game trees represent possible moves and outcomes in games like chess.
*   **Autocomplete and Spell Checkers:**  Tries are used to store dictionaries and efficiently search for words.
*   **Priority Queues:** Heaps are commonly used to manage tasks or elements with priorities.

---

## 7. Key Terms and Concepts

```mermaid
---
title: "Key Terms and Concepts of Tree Structure"
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
  root((Tree Structures))
    General_Concepts
      Root[The top node of the tree]
      Node[An element in the tree, containing data]
      Edge[Connection between two nodes]
      Parent[A node with children]
      Child[A node connected to a parent]
      Leaf[A node with no children]
      Subtree[A node and all its descendants]
      Height[Longest downward path to leaf nodes]
      Depth[Length of the path to a leaf node]
    Types_of_Trees
      Binary_Tree[Each node has at most two children]
      Binary_Search_Tree_BST["Ordered binary tree for efficient searching"]
      AVL_Tree[Self-balancing BST]
      Red_Black_Tree[Self-balancing BST]
      B_Tree[Optimized for disk-based storage]
      Trie["Used for storing strings/sequences<br>(prefix tree)"]
      Heap[Optimized to maintain min/max elements]
    Operations
      Insertion[Adding a new node]
      Deletion[Removing a node]
      Search[Finding a node with a specific value]
      Traversal
        In_order["Left, Root, Right<br>(sorted for BSTs)"]
        Pre_order[Root, Left, Right]
        Post_order[Left, Right, Root]
        Breadth_First[Level by Level search]
    Complexity
      Time_Complexity
        Average["Often O(log n) for balanced trees"]
        Worst_Case["O(n) for unbalanced trees"]
      Space_Complexity["O(n)"]
    Applications
      File_Systems
      Databases
      Compilers
      Networking
      AI_and_Machine_Learning
      Web_Development
      Game_Development

```



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---