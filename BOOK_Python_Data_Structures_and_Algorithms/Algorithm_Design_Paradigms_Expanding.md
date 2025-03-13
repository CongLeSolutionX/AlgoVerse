---
created: 2025-03-12 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://www.packtpub.com/en-us/product/python-data-structures-and-algorithms-9781786467355"
---


# Algorithm Design Paradigms
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


This document is an expansion of the initial version [here](./Algorithm_Design_Paradigms.md), exploring fundamental algorithm design paradigms, providing a comprehensive overview of Divide and Conquer, Dynamic Programming, and Greedy Algorithms, with examples implemented in Python.  These paradigms form the cornerstone of efficient problem-solving in computer science.

---

## Algorithm Design Paradigms

Algorithm design paradigms are general approaches or strategies for constructing algorithms to solve various types of problems. They provide a framework for thinking about problem decomposition and solution construction.  We will examine three major paradigms:

### 1. Divide and Conquer

The Divide and Conquer paradigm involves breaking down a problem into smaller, independent subproblems, solving these subproblems recursively, and then combining their solutions to solve the original problem.

**Key Concepts:**

*   **Problem Decomposition:**  The original problem is divided into smaller instances of the same problem.
*   **Recursion:**  The subproblems are solved recursively, meaning the same algorithm is applied to each subproblem.
*   **Smaller Subproblems:** The subproblems must be smaller than the original problem and eventually reach a base case.
*   **Base Case:**  A simple case that can be solved directly without further recursion.
*   **Recursive Step:**  The part of the algorithm that divides the problem and calls itself recursively.
*   **Merge Solutions:**  The solutions to the subproblems are combined to produce the solution to the original problem.

**Examples:**

*   **Merge Sort:**  A sorting algorithm that divides the input array into two halves, recursively sorts each half, and then merges the sorted halves.

    ```python
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
    ```

*   **Quick Sort:**  Another sorting algorithm that selects a 'pivot' element and partitions the array around the pivot, recursively sorting the sub-arrays.

    ```python
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    ```

*   **Binary Search:**  An efficient algorithm for finding a target value within a sorted array.  It repeatedly divides the search interval in half.

    ```python
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # Target not found
    ```

*   **Strassen's Matrix Multiplication:**  An algorithm for matrix multiplication that is asymptotically faster than the standard algorithm for large matrices.

**Time Complexity:**  The time complexity of Divide and Conquer algorithms is often expressed using the Master Theorem, which provides a way to determine the complexity based on the recurrence relation.  For example, Merge Sort has a time complexity of  O(n log n), where n is the number of elements.

---

### 2. Dynamic Programming

Dynamic Programming (DP) is a technique for solving problems with overlapping subproblems.  Instead of solving the same subproblems repeatedly (as in recursion), DP stores the solutions to subproblems in a table (or memoizes them) so that they can be reused later.

**Key Concepts:**

*   **Optimal Substructure:**  A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
*   **Overlapping Subproblems:**  The problem can be broken down into subproblems that are reused multiple times.
*   **Memoization (Top-Down):**  Storing the results of expensive function calls and returning the cached result when the same inputs occur again.  This is a top-down, recursive approach.
*   **Tabulation (Bottom-Up):**  Building a table of solutions to subproblems in a bottom-up manner, starting with the smallest subproblems and using their solutions to solve larger ones.

**Examples:**

*   **Fibonacci Sequence:**  Calculating the nth Fibonacci number.

    ```python
    # Memoization (Top-Down)
    def fibonacci_memo(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        return memo[n]

    # Tabulation (Bottom-Up)
    def fibonacci_tab(n):
        fib_table = [0] * (n + 1)
        fib_table[1] = 1
        for i in range(2, n + 1):
            fib_table[i] = fib_table[i-1] + fib_table[i-2]
        return fib_table[n]
    ```

*   **Knapsack Problem:**  Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value.

*   **Shortest Path Algorithms (e.g., Floyd-Warshall):**  Finding the shortest paths between all pairs of vertices in a graph.

*   **Sequence Alignment (e.g., Needleman-Wunsch):**  Finding the optimal alignment between two sequences (e.g., DNA sequences).

**Time Complexity:** DP often reduces the time complexity from exponential (as in naive recursion) to polynomial. For example, the naive recursive Fibonacci implementation is O(2^n), while the DP versions are O(n).

----

### 3. Greedy Algorithms

Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum.  They are "short-sighted" in that they don't consider the long-term consequences of their choices.  Greedy algorithms are not always guaranteed to find the optimal solution, but they are often simple and efficient.

**Key Concepts:**

*   **Local Optimality:**  At each step, the algorithm chooses the best option available at that moment.
*   **Short-Sighted Decisions:**  The algorithm doesn't look ahead to see if a different choice might lead to a better overall solution.
*   **Feasible Solutions:**  The algorithm must always maintain a feasible solution (one that satisfies the problem's constraints).
*   **Locally Optimal Choice:** The choice made at each step must be the best among all available feasible choices.
*   **Irrevocable Decisions:**  Once a choice is made, it cannot be changed.

**Examples:**

*   **Coin Changing (Suboptimal):**  Making change for a given amount using the fewest number of coins.  The greedy approach (always choosing the largest denomination coin possible) works for some coin systems (like US currency) but not all.  This is a case where the greedy approach does *not* guarantee an optimal solution.

*   **Dijkstra's Algorithm (Shortest Path):**  Finding the shortest path from a source node to all other nodes in a graph with non-negative edge weights.

    ```python
    import heapq

    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    ```

*   **Prim's Algorithm (Minimum Spanning Tree):**  Finding a minimum spanning tree for a weighted, undirected graph.

* **Kruskal's Algorithm (Minimum Spanning Tree):** Another algorithm to find the minimum spanning tree.

    ```python
    def kruskal(graph):
        # graph is represented as a list of edges: (weight, node1, node2)
        edges = sorted(graph)  # Sort edges by weight
        parent = {node: node for node in set(sum([(u, v) for w, u, v in edges], ()))}
        mst = []

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        for weight, u, v in edges:
            if union(u, v):
                mst.append((weight, u, v))

        return mst
    ```

*   **Huffman Coding:**  A lossless data compression algorithm that assigns variable-length codes to characters based on their frequency.

**Time Complexity:** Greedy algorithms often have a time complexity of O(n log n) or O(n), where n is the size of the input. Dijkstra's algorithm, for example, has a time complexity of O(E log V) using a binary heap, where E is the number of edges and V is the number of vertices.

---

### Choosing the Right Paradigm
Deciding which algorithmic paradigm is best for a particular problem is essential.

- **Divide and Conquer:** Suitable for problems easily broken into independent subproblems (sorting, searching).
- **Dynamic Programming:** Suitable for problems with overlapping subproblems and optimal substructure (optimization, sequence alignment).
- **Greedy Algorithms:** Suitable for problems where a locally optimal choice leads to a globally optimal solution (or a good approximation). Always consider if a greedy approach will yield the *correct* answer; proof of correctness is important.

This overview provides a foundation for understanding and applying these fundamental algorithm design paradigms. Each paradigm offers a powerful approach to problem-solving, and mastering them is crucial for any aspiring computer scientist or software engineer.




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---