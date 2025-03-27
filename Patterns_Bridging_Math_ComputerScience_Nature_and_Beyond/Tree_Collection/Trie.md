---
created: 2025-03-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Trie (Prefix Tree) - A Diagrammatic Guide 
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


Below is a multi-pronged approach, combining diagrams, step-by-step instructions, complexity analysis, comparisons, and a keyword mind map, provides a thorough explanation of the Trie data structure.


---


## 1. Core Trie Representation

A Trie is a tree-like data structure used to store a dynamic set of strings, where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated. All the descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empty string.

Here's a Mermaid flowchart representing a Trie containing the words "cat", "car", "can", "dog", and "do":

```mermaid
---
title: "Core Trie Representation"
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
    subgraph Trie["Trie<br>(Prefix Tree)"]
        style Trie fill:#eef3,stroke:#333,stroke-width:2px
        Root[(' ' - Root"")] --> C["c"]
        
        C --> A["a"]
        A --> T{"t" - End}
        A --> R{"r" - End}
        A --> N{"n" - End}
        
        Root --> D["d"]
        D --> O["o"]
        O --> G{"g" - End}
	    O --> EndDO{"do" - End}
	    
	    T --> EndCAT{"cat" - End}
	    R --> EndCAR{"car" - End}
	    N --> EndCAN{"can" - End}
	    
    end
```

**Explanation of the Core Mermaid Diagram:**

*   **`Root`**:  The Trie always starts with an empty root node (represented here as `""`).  This node doesn't represent any character.
*   **Nodes (Letters):** Each node, except the root, represents a single character of a word.
*   **Edges (Connections):** The edges represent transitions from one character to the next.
*   **`End` Nodes (Words):** Nodes marked with "End" (e.g., `{"t" - End}`) signify the end of a valid word.  This is crucial because a prefix of a valid word might also be a valid word itself (e.g., "do" and "dog").  The `End` marker distinguishes them.
*   **Shared Prefixes:**  Notice how "cat", "car", and "can" all share the prefix "ca".  They branch out from the same 'c' and 'a' nodes. This prefix sharing is the core efficiency of the Trie.

---

## 2. Trie Operations and Examples (Step-by-Step)

Let's illustrate the primary Trie operations: insertion, search, and deletion (although deletion is less commonly visualized).

### 2.a Insertion

```mermaid
---
title: "Trie Operations (Step-by-Step) - Insertion"
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
    subgraph Insert["Insert 'bat' into Trie"]
    style Insert fill:#eef,stroke:#333,stroke-width:1px
   direction TB
        I1["Start at Root (' ')"] --> I2{Does Root have 'b' child?}
        I2 -- No --> I3[Create 'b' node]
        I3 --> I4{Does 'b' have 'a' child?}
        I4 -- No --> I5[Create 'a' node]
        I5 --> I6{Does 'a' have 't' child?}
        I6 -- No --> I7[Create 't' node]
        I7 --> I8[Mark 't' as End of Word]
    end
    
```

**Explanation of Insertion:**

1.  **Start at Root:** Always begin at the empty root node.
2.  **Check for Child:** For each character in the word to be inserted, check if the current node has a child representing that character.
3.  **Create if Needed:** If a child doesn't exist, create a new node for that character.
4.  **Move to Child:** Move to the child node corresponding to the current character.
5.  **Mark End:** After processing all characters, mark the final node as an "End of Word" node.

### 2.b Search

```mermaid
---
title: "Trie Operations (Step-by-Step) - Search"
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
    subgraph Search["Search for 'car' in Trie"]
     style Search fill:#eef3,stroke:#333,stroke-width:1px
        S1["Start at Root (' ')"] --> S2{"Does Root have 'c' child?"}
        S2 -- Yes --> S3{"Does 'c' have 'a' child?"}
        S3 -- Yes --> S4{"Does 'a' have 'r' child?"}
        S4 -- Yes --> S5{"Is 'r' marked as End?"}
        S5 -- Yes --> S6["Found 'car'"]
        S4 -- No --> S7["Not Found"]
        S2 -- No --> S7
		S3 -- No --> S7
    end
```

**Explanation of Search:**

1.  **Start at Root:** Begin at the empty root node.
2.  **Check for Child:** For each character in the word being searched for, check if the current node has a child representing that character.
3.  **Not Found:** If at any point a child doesn't exist, the word is not in the Trie.
4.  **Move to Child:** If the child exists, move to that child node.
5.  **Check End:** After processing all characters, check if the final node is marked as "End of Word."  If it is, the word is found; otherwise, it's not (it might be a prefix of another word, but not a complete word itself).

----

### 2.c Search for Prefix (Slight Variation)
Searching if a given string is a prefix, not exactly the entire word.

```mermaid
---
title: "Trie Operations (Step-by-Step) - Search for Prefix"
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
    subgraph Prefix_Search["Search for Prefix 'ca' in Trie"]
    style Prefix_Search fill:#ddf3,stroke:#333,stroke-width:1px
      direction TB
        SP1["Start at Root"] --> SP2{"Does Root have a 'c' child?"}
        SP2 -- "Yes" --> SP3{"Does 'c' have an 'a' child?"}
		SP3 -- "Yes" --> SP4["Prefix 'ca' found"]
		SP2 -- "No" --> SP5["Prefix 'ca' not found"]
		SP3 -- "No" --> SP5
    end
    
```
### 2.d Deletion (Conceptual)

Deletion is a bit more complex, especially if you need to maintain the Trie's integrity (removing nodes that are no longer needed). Here's the general idea:

1.  **Find the Word:** Perform a search for the word to be deleted.
2.  **Unmark End:** If found, unmark the "End of Word" status of the final node.
3.  **Check for Children:** If the final node has *no* children, you can delete it.
4.  **Recursive Deletion:**  Move back up the Trie. If a parent node has no other children *and* is not marked as "End of Word," you can delete it too. Continue this process recursively until you reach a node that either has other children or marks the end of another word. This step prevents accidental removal of prefixes that are part of other valid words.

----

## 3. Time and Space Complexity

A key advantage of Tries is their efficiency in terms of time complexity for certain operations.

```mermaid
---
title: "Trie - Time and Space Complexity"
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
    subgraph Complexity["Time and Space Complexity"]
    style Complexity fill:#ddf3,stroke:#333,stroke-width:2px
        direction TB
        Insert["Insert: O(L)"]
        Search["Search: O(L)"]
        SearchPrefix["SearchPrefix: O(L)"]
        Delete["Delete: O(L)"]
        Space["Space: O(N * L) - Worst Case"]

        Insert --> WhereL["Where L = Length of Word"]
        Search --> WhereL
        SearchPrefix --> WhereL
        Delete --> WhereL
        Space --> WhereNL["Where N = Number of Words, L = Average Word Length"]
    end
    
```

**Explanation:**

*   **Insert, Search, SearchPrefix, Delete:** All have a time complexity of O(L), where L is the length of the word being inserted, searched for, or deleted.  This is because, in the worst case, you traverse a path from the root to a leaf, and the length of this path is proportional to the word's length.  This is significantly faster than searching in an unsorted list (O(N)) or even a balanced binary search tree (O(log N) average, O(N) worst case), especially when dealing with many short strings.
*   **Space Complexity:**  The space complexity is where Tries can be less efficient. In the *worst case*, where no prefixes are shared, the space complexity is O(N * L), where N is the number of words and L is the average length of the words.  If you have many words with little prefix overlap, this can be significant. However, in many practical applications, there *is* significant prefix sharing, and the actual space used is much less.

---

## 4. Trie vs. Other Data Structures

```mermaid
---
title: "Trie vs. Other Data Structures"
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
    subgraph Comparison["Trie vs. Other Data Structures"]
        style Comparison fill:#eef3,stroke:#333,stroke-width:2px
      direction TB
        Trie --> TrieAdvantage["Efficient Prefix Search (Autocomplete)"]
        Trie --> TrieDisadvantage["Can be space-inefficient if little prefix sharing"]
        HashTable["Hash Table"] --> HashAdvantage["O(1) average case for insert/search/delete (single word)"]
        HashTable --> HashDisadvantage["Poor for prefix searches"]
        BalancedBST["Balanced Binary Search Tree"] --> BSTAdvantage["O(log N) average for insert/search/delete"]
         BalancedBST --> BSTAdvantage2["Good for sorted data"]
        BalancedBST --> BSTDisadvantage["Not optimized for prefix searches"]

    end
```

**Explanation:**

*   **Trie:**
    *   **Advantage:**  Excels at prefix searches (e.g., autocomplete suggestions).  This is its primary strength.
    *   **Disadvantage:** Can use a lot of memory if there's not much prefix sharing among the stored strings.
*   **Hash Table:**
    *   **Advantage:** Very fast (average O(1)) for inserting, searching, and deleting *individual* words, assuming a good hash function and few collisions.
    *   **Disadvantage:** Very poor for prefix searches.  You'd have to iterate through all keys and check each one.
*   **Balanced Binary Search Tree:**
    *   **Advantage:**  Provides good average-case performance (O(log N)) for insertion, search, and deletion.  Also keeps the data sorted, which can be useful for other operations.
    *   **Disadvantage:** Not specifically optimized for prefix searches. While you could find prefixes, it wouldn't be as efficient as a Trie.

----

## 5. Key Terms and Concepts

```mermaid
---
title: "Trie - Key Terms and Concepts"
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
    root(("Trie<br>(Prefix Tree)"))
      Definition[A tree-like data structure used to store a dynamic set of strings, optimized for prefix-based operations]
      Structure
        Root[Special node representing the empty string]
        Nodes[Each node represents a single character]
        Edges[Connections between nodes, representing character transitions]
        End_Markers[Nodes marking the end of valid words]
      Operations
        Insert[Add a new word to the Trie]
        Search[Check if a word exists in the Trie]
        SearchPrefix[Check if a string is a prefix of any word in the Trie]
        Delete[Remove a word from the Trie]
      Properties
        Prefix_Sharing[Descendants of a node share a common prefix]
        Time_Complexity["O(L) for insert, search, delete, where L is the length of the word"]
        Space_Complexity["O(N * L) worst case, where N is the number of words and L is the average word length"]
      Use_Cases
        Autocomplete[Suggesting words as the user types]
        Spell_Checkers[Identifying misspelled words]
        IP_Routing[Used in routers for longest prefix matching]
        Contact_Search[Finding contacts based on partial names]
      Variations
        Compressed_Trie["Reduces space usage by combining nodes with single children"]
        Suffix_Tree["A Trie-like structure that stores all suffixes of a string"]
```



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---