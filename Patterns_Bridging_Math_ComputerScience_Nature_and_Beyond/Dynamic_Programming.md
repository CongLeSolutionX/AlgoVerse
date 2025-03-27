---
created: 2025-03-26 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Dynamic Programming - A Diagrammatic Guide
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


Below is a comprehensive explanation, using diagrams, code examples, and a step-by-step approach, should provide a solid understanding of Dynamic Programming. It covers the core concept, the two main approaches (memoization and tabulation), a detailed example with the Fibonacci sequence, how to identify DP problems, and a list of common DP problem examples.



## 1. Core Concept (High-Level Overview)

Dynamic Programming is an optimization technique for solving problems that can be broken down into overlapping subproblems. Instead of recomputing the solutions to these subproblems multiple times, DP stores the results of subproblems (usually in a table or array – often called memoization) and reuses them when needed. This dramatically reduces computation time, often from exponential to polynomial.

```mermaid
---
title: "Dynamic Programming - Core Concept (High-Level Overview)"
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
    A[Complex Problem] --> B(Divide into Subproblems);
    B --> C{"Are Subproblems Overlapping?"}
    C -- Yes --> D["Solve Each Subproblem Once"]
    D --> E["Store Subproblem Solutions<br>(Memoization/Tabulation)"]
    E --> F["Reuse Solutions to Build Final Solution"]
    F --> G["Optimal Solution"]
    C -- No --> H["Solve Independently<br>(e.g., Divide and Conquer)"]
    H --> G
    
    style A fill:#fef2,stroke:#333,stroke-width:1px
    style G fill:#fef3,stroke:#333,stroke-width:1px
    
```

**Explanation of the Core Concept Diagram:**

*   **`Complex Problem`:** The starting point – a problem that can potentially be solved with DP.
*   **`Divide into Subproblems`:** The problem is broken down into smaller, self-similar subproblems.
*   **`Are Subproblems Overlapping?`:**  This is the *crucial* question.  If the same subproblems are encountered multiple times during the recursive solution, DP is likely beneficial.
*   **`Solve Each Subproblem Once`:**  Avoid redundant computation.
*   **`Store Subproblem Solutions (Memoization/Tabulation)`:** This is the heart of DP.  We use a data structure (often a table/array) to store the results.
*   **`Reuse Solutions to Build Final Solution`:**  The stored solutions are used to efficiently construct the solution to the original problem.
*   **`Optimal Solution`:**  DP is often used for optimization problems (finding the *best* solution, e.g., shortest path, maximum value).
*   **`Solve Independently (e.g., Divide and Conquer)`:** If subproblems are *not* overlapping, a technique like Divide and Conquer is more appropriate.

----

## 2. Two Main Approaches: Memoization and Tabulation

There are two primary ways to implement Dynamic Programming:

*   **Memoization (Top-Down):**  This is a recursive approach. You start with the original problem and recursively break it down.  You "memoize" (store) the result of each subproblem as you solve it. Before solving a subproblem, you check if it's already been solved; if so, you reuse the stored result.

*   **Tabulation (Bottom-Up):**  This is an iterative approach. You start with the smallest subproblems and build up solutions to larger and larger subproblems, storing the results in a table (hence "tabulation").  You systematically fill the table until you reach the solution to the original problem.

```mermaid
---
title: "Two Main Approaches of Dynamic Programming: Memoization and Tabulation"
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
    subgraph Memoization["Memoization<br>(Top-Down)"]
    style Memoization fill:#ccf3,stroke:#333,stroke-width:2px
        A["Start with Original Problem"] --> B["Recursive Calls"]
        B --> C{"Subproblem Solved Before?"}
        C -- Yes --> D["Return Stored Result"]
        C -- No --> E["Solve Subproblem"]
        E --> F["Store Result"]
        F --> D
        
        style A fill:#ccf3,stroke:#333,stroke-width:1px
        style D fill:#ccf3,stroke:#333,stroke-width:1px
    end

    subgraph Tabulation["Tabulation<br>(Bottom-Up)"]
    style Tabulation fill:#fcc3,stroke:#333,stroke-width:2px
        G["Start with Smallest Subproblems"] --> H["Iteratively Fill Table"]
        H --> I["Build Solutions to Larger Subproblems"]
        I --> J["Solution to Original Problem"]
        
         style G fill:#fcc3,stroke:#333,stroke-width:1px
         style J fill:#fcc3,stroke:#333,stroke-width:1px
    end

    Memoization -- "Recursive" --> DP["Dynamic Programming"]
    Tabulation -- "Iterative" --> DP
    
```

**Explanation of Approaches Diagram:**

*   **Memoization:**  Shows the recursive flow, with the check for previously solved subproblems.
*   **Tabulation:**  Shows the iterative, bottom-up construction of the solution table.
*   **`DP` Node:**  Both approaches are forms of Dynamic Programming.

---

## 3. Example: Fibonacci Sequence (with both approaches)

The Fibonacci sequence is a classic (though not always the *best*) example to illustrate DP because it clearly demonstrates the overlapping subproblems issue.

### 3.a. Naive Recursive Fibonacci (without DP)

```python
def fib_naive(n):
  if n <= 1:
    return n
  return fib_naive(n-1) + fib_naive(n-2)

# Example calls
print(fib_naive(5))
print(fib_naive(6))
```

```mermaid
---
title: "Naive Recursive Fibonacci (without DP)"
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
    A["fib(5)"] --> B["fib(4)"]
    A --> C["fib(3)"]
    B --> D["fib(3)"]
    B --> E["fib(2)"]
    C --> E
    C --> F["fib(1)"]
    D --> G["fib(2)"]
    D --> H["fib(1)"]
    E --> I["fib(1)"]
    E --> J["fib(0)"]
    G --> I
    G --> J

```

**Explanation of Naive Recursion:**

*   The code is a direct implementation of the recursive definition of Fibonacci.
*   The diagram shows the *massive* redundancy. `fib(3)` is calculated twice, `fib(2)` three times, and so on. This leads to exponential time complexity, O(2^n), which is very inefficient.

### 3.b. Fibonacci with Memoization (Top-Down DP)

```python
def fib_memo(n, memo={}):
  if n in memo:
    return memo[n]
  if n <= 1:
    return n
  memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
  return memo[n]

# Example
print(fib_memo(5))
print(fib_memo(6))
print(fib_memo(100)) # This would take forever with fib_naive!

```

```mermaid
---
title: "Fibonacci with Memoization (Top-Down Dynamic Programming)"
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
    A["fib(5)"] --> B["fib(4)"]
    A --> C["fib(3)"]
    B --> D["fib(3)"]
    B --> E["fib(2)"]
    C --> E
    C --> F["fib(1)"]
    D --> G["fib(2)"]
    D --> H["fib(1)"]
    E --> I["fib(1)"]
    E --> J["fib(0)"]
    G --> I
    G --> J

	%% Dotted line: Result reused from memo
    A -.-> C
    B -.-> D
    B -.-> E
    C -.-> E
    C -.-> F
    D -.-> G
    D -.-> H
    E -.-> I
    E -.-> J
    G -.-> I
    G -.-> J

    style A fill:#ccf3,stroke:#333,stroke-width:1px
    style B fill:#ccf3,stroke:#333,stroke-width:1px
    
```


**Explanation of Memoization:**

*   We use a dictionary `memo` to store results.
*   Before computing `fib(n)`, we check if it's already in `memo`.
*   The diagram shows how redundant calculations are avoided (dotted lines indicate reused values).  The time complexity improves to O(n) because each subproblem is solved only once.

### 3.c. Fibonacci with Tabulation (Bottom-Up DP)

```python
def fib_tab(n):
  if n <= 1:
    return n
  table = [0] * (n + 1)
  table[1] = 1
  for i in range(2, n + 1):
    table[i] = table[i-1] + table[i-2]
  return table[n]

#Example
print(fib_tab(5))
print(fib_tab(6))
print(fib_tab(100))

```


```mermaid
---
title: "Fibonacci with Tabulation (Bottom-Up Dynamic Programming)"
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
    A["table[0] = 0"] --> B["table[1] = 1"]
    B --> C["table[2] = 1"]
    C --> D["table[3] = 2"]
    D --> E["table[4] = 3"]
    E --> F["table[5] = 5"]
    F --> G[...]
    
    style A fill:#fcc3,stroke:#333,stroke-width:1px
    style F fill:#fcc3,stroke:#333,stroke-width:1px

```

**Explanation of Tabulation:**

*   We create a `table` (list) to store results.
*   We initialize `table[0]` and `table[1]` (base cases).
*   We iteratively fill the table, using previously computed values.
*   The diagram shows the table being built up. The time complexity is also O(n), and the space complexity is O(n) as well (for both memoization and tabulation in this specific Fibonacci example).

----

## 4. Identifying DP Problems: Key Characteristics

*   **Optimal Substructure:**  An optimal solution to the problem can be constructed from optimal solutions to its subproblems. This means the problem can be broken down recursively.

*   **Overlapping Subproblems:** The recursive solution would solve the same subproblems repeatedly.  This is where DP's efficiency gain comes from.

---

## 5. Steps to Solve a DP Problem

1.  **Identify Optimal Substructure:**  Can you define the solution to the problem in terms of solutions to smaller instances of the same problem?

2.  **Identify Overlapping Subproblems:**  Draw the recursion tree (like we did for the naive Fibonacci). Are the same subproblems appearing multiple times?

3.  **Choose Memoization or Tabulation:**
    *   **Memoization:**  Often easier to implement if you already have a recursive solution.  Can be less efficient if you end up solving subproblems you don't need.
    *   **Tabulation:**  Often more efficient in terms of constant factors (no recursion overhead).  Requires careful planning to determine the correct order to fill the table.

4.  **Define the Memo/Table:** What data structure will you use to store subproblem solutions? What are the dimensions of the table? What does each entry in the table represent?

5.  **Define the Recurrence Relation:**  This is the mathematical formula that defines how to compute a subproblem's solution based on the solutions to smaller subproblems. (For Fibonacci: `fib(n) = fib(n-1) + fib(n-2)`).

6.  **Implement (with Memoization or Tabulation):** Write the code!

7.  **Determine Time and Space Complexity:** Analyze the efficiency of your DP solution.

---

## 6. Examples of DP Problems (Beyond Fibonacci)

*   **0/1 Knapsack Problem:** Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value.
*   **Longest Common Subsequence (LCS):** Find the longest subsequence common to two sequences. Used in DNA sequence alignment, diff utilities, and more.
*   **Shortest Path Problems (e.g., Dijkstra's Algorithm with a min-priority queue, Floyd-Warshall Algorithm):** Find the shortest path between nodes in a graph.
*   **Edit Distance (Levenshtein Distance):** Find the minimum number of edits (insertions, deletions, substitutions) needed to transform one string into another.
*   **Matrix Chain Multiplication:** Find the most efficient way to multiply a chain of matrices.
*   **Coin Change Problem:** Given a set of coin denominations and a target amount, find the minimum number of coins needed to make up that amount.
*   **Rod Cutting** Given a rod with n length, we want to maximize the revenue.

For each of these more practical problems, the same process applies but you will have much better performance in terms of complexities:

```mermaid
---
title: "Dynamic Programming - Examples of DP Problems (Beyond Fibonacci)"
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
    subgraph Knapsack_Problem["0/1 Knapsack Problem"]
    style Knapsack_Problem fill:#aaf3,stroke:#333,stroke-width:2px
    direction TB
        KP["Items:<br>(weight, value)"] --> KCap[Knapsack Capacity]
        KCap --> KPSolve{"Optimal Subset?"}
        KPSolve --> KPResult["Maximized Value"]
        KPResult --> KPDetails["Items Included"]
        KPDetails --> KPComp["Time Complexity (DP): O(nW)"]
    end
    
    subgraph LCS["Longest Common Subsequence<br>(LCS)"]
    style LCS fill:#faa3,stroke:#333,stroke-width:2px
        direction TB
        LCS1[Sequence 1] --> LCMatch{"Common Subsequence?"}
        LCS2[Sequence 2] --> LCMatch
        LCMatch --> LCSResult["Longest Subsequence"]
        LCSResult --> LCSComp["Time Complexity (DP): O(mn)"]
    end
     
    
    subgraph Edit_Distance["Edit Distance<br>(Levenshtein)"]
      style Edit_Distance fill:#aff3,stroke:#333,stroke-width:2px
        direction TB
        ED1[String 1] --> EDMatch{Minimum Edits?}
        ED2[String 2] --> EDMatch
        EDMatch --> EDResult["Number of Edits"]
        EDResult --> EDComp["Time Complexity (DP): O(mn)"]
    end
   
```


---

## 7. Key Terms and Concepts

```mermaid
---
title: "Dynamic Programming - Key Terms and Concepts"
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
  root((Dynamic Programming))
    Definition[An algorithmic technique for solving optimization problems by breaking them down into overlapping subproblems and storing the results of subproblems to avoid redundant computation.]
    Approaches
      Memoization
        Description[Top-down approach using recursion and a memo table to store results.]
        Time_Complexity["Often O(n) or O(n*m) depending on the problem, but significantly better than exponential"]
        Space_Complexity[Depends on the size of the memo table]
      Tabulation
        Description["Bottom-up approach using iteration and a table to store results"]
        Time_Complexity["Often O(n) or O(n*m), similar to memoization"]
        Space_Complexity["Depends on the size of the table"]
    Key_Concepts
      Optimal_Substructure[An optimal solution to the problem can be constructed from optimal solutions to its subproblems.]
      Overlapping_Subproblems[The same subproblems are encountered multiple times during the recursive solution.]
      Recurrence_Relation[A mathematical formula that defines how to compute a subproblem's solution based on smaller subproblems.]
    Steps
      Step1[Identify Optimal Substructure]
      Step2[Identify Overlapping Subproblems]
      Step3[Choose Memoization or Tabulation]
      Step4[Define the Memo/Table]
      Step5[Define the Recurrence Relation]
      Step6[Implement]
      Step7[Analyze Time and Space Complexity]
    Example_Problems
      Fibonacci_Sequence[Illustrative example, but not the best practical application]
      Knapsack_Problem[Classic optimization problem]
      Longest_Common_Subsequence[Used in sequence alignment]
      Shortest_Path_Problems[Finding shortest paths in graphs]
      Edit_Distance[Measuring string similarity]
      Matrix_Chain_Multiplication[Optimizing matrix multiplication order]

```



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---