---
created: 2025-06-13 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY-SA 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
main source: https://mitpress.mit.edu/9780262533058/introduction-to-algorithms/
other source: https://enos.itcollege.ee/~japoia/algorithms/GT/Introduction_to_algorithms-3rd%20Edition.pdf
---


> ⚠️🏗️🚧🦺🧱🪵🪨🪚🛠️👷
> 
> This is a working draft in progress
> 
> ![Loading...](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNhajI0cmJheTFsZ2g1ajQ0aHd0MHVkNHB6bGI5dWVuMWN3YTZ2aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y4PkFXkfTeEKqGBBsC/giphy.gif)
> 
> ⚠️🏗️🚧🦺🧱🪵🪨🪚🛠️👷


----


# Introduction to Algorithms - Third Edition
> by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein

> <ins>📢 **Disclaimer** 🚨</ins>
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## Visualizing "Introduction to Algorithms, Third Edition" 📖

The structure of this seminal textbook is vast and covers a wide range of topics in algorithms. The following mind map aims to capture its organization, key concepts, and the mathematical notations where appropriate.

```mermaid
---
title: "Introduction to Algorithms, Third Edition, An Overview"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'fontFamily': 'Andale Mono, monospace',
    'mindmap': {
	    'nodeAlign': 'center',
	    'padding': 5
    },
    'themeVariables': {
      'primaryColor': '#FC82',
      'primaryTextColor': '#F8B229',
      'primaryBorderColor': '#27AE60',
      'secondaryColor': '#EBF3',
      'secondaryTextColor': '#6C3483',
      'secondaryBorderColor': '#A569BD',
      'fontSize': '15px'
    }
  }
}%%
mindmap
  root)"Introduction to Algorithms, Third Edition 📚<br/>(Cormen, Leiserson, Rivest, Stein)"(
    Authors("Authors:<br/>Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein")

    Part_I))"Part I:<br/>Foundations ✨"((
      Ch1{{"Chapter 1:<br/>The Role of Algorithms in Computing"}}
        Sec1_1("Section 1.1<br/>Algorithms")
        Sec1_2("Section 1.2<br/>Algorithms as a technology")
      Ch2{{"Chapter 2:<br/> Getting Started 🚀"}}
        Sec2_1["Section 2.1<br/>Insertion sort"]
        Sec2_2["Section 2.2<br/>Analyzing algorithms"]
        Sec2_3["Section 2.3<br/>Designing algorithms"]
      Ch3{{"Chapter 3:<br/>Growth of Functions 📈<br/>($\Theta, O, \Omega$)"}}
        Sec3_1["Section 3.1<br/>Asymptotic notation ($\Theta(n^2)$, $O(n \log n)$)"]
        Sec3_2["Section 3.2<br/>Standard notations and common functions"]
      Ch4{{"Chapter 4:<br/>Divide-and-Conquer ➗👑<br/>($T(n) = aT(n/b) + f(n)$)"}}
        Sec4_1["Section 4.1<br/>The maximum-subarray problem"]
        Sec4_2["Section 4.2<br/>Strassen's algorithm for matrix multiplication"]
        Sec4_3["Section 4.3<br/>The substitution method for solving recurrences"]
        Sec4_4["Section 4.4<br/>The recursion-tree method for solving recurrences"]
        Sec4_5["Section 4.5<br/>The master method for solving recurrences"]
        Sec4_6["? Section 4.6<br/>Proof of the master theorem"]
      Ch5{{"Chapter 5:<br/> Probabilistic Analysis and Randomized Algorithms 🎲<br/>($E[X]$)"}}
        Sec5_1["Section 5.1<br/>The hiring problem"]
        Sec5_2["Section 5.2<br/>Indicator random variables ($I\{A\}$)"]
        Sec5_3["Section 5.3<br/>Randomized algorithms"]
        Sec5_4["? Section 5.4<br/>Probabilistic analysis and further uses of indicator random variables"]

    Part_II))"Part II<br/>Sorting and Order Statistics 📊"((
      Intro_II["Introduction"]
      Ch6{{"Chapter 6:<br/>Heapsort"}}
        Sec6_1["Section 6.1<br/>Heaps"]
        Sec6_2["Section 6.2<br/>Maintaining the heap property"]
        Sec6_3["Section 6.3<br/>Building a heap"]
        Sec6_4["Section 6.4<br/>The heapsort algorithm"]
        Sec6_5["Section 6.5<br/>Priority queues"]
      Ch7{{"Chapter 7:<br/>Quicksort"}}
        Sec7_1["Section 7.1<br/>Description of quicksort"]
        Sec7_2["Section 7.2<br/>Performance of quicksort"]
        Sec7_3["Section 7.3<br/>A randomized version of quicksort"]
        Sec7_4["Section 7.4<br/>Analysis of quicksort"]
      Ch8{{"Chapter 8:<br/>Sorting in Linear Time<br/> ($O(n)$)"}}
        Sec8_1["Section 8.1<br/>Lower bounds for sorting ($\Omega(n \log n)$ for comparisons)"]
        Sec8_2["Section 8.2<br/>Counting sort"]
        Sec8_3["Section 8.3<br/>Radix sort"]
        Sec8_4["Section 8.4<br/>Bucket sort"]
      Ch9{{"Chapter 9:<br/>Medians and Order Statistics"}}
        Sec9_1["Section 9.1<br/>Minimum and maximum"]
        Sec9_2["Section 9.2<br/>Selection in expected linear time"]
        Sec9_3["Section 9.3<br/>Selection in worst-case linear time"]

    Part_III))"Part III<br/>Data Structures 🗂️"((
      Intro_III["Introduction"]
      Ch10{{"Chapter 10:<br/>Elementary Data Structures<br/>(Stacks, Queues, Lists, Trees)"}}
        Sec10_1["Section 10.1<br/>Stacks and queues"]
        Sec10_2["Section 10.2<br/>Linked lists"]
        Sec10_3["Section 10.3<br/>Implementing pointers and objects"]
        Sec10_4["Section 10.4<br/>Representing rooted trees"]
      Ch11{{"Chapter 11:<br/>Hash Tables<br/>($h(k)$)"}}
        Sec11_1["Section 11.1<br/>Direct-address tables"]
        Sec11_2["Section 11.2<br/>Hash tables"]
        Sec11_3["Section 11.3<br/>Hash functions"]
        Sec11_4["Section 11.4<br/>Open addressing"]
        Sec11_5["? Section 11.5<br/>Perfect hashing"]
      Ch12{{"Chapter 12:<br/>Binary Search Trees"}}
        Sec12_1["Section 12.1<br/>What is a binary search tree?"]
        Sec12_2["Section 12.2<br/>Querying a binary search tree"]
        Sec12_3["Section 12.3<br/>Insertion and deletion"]
        Sec12_4["? Section 12.4<br/>Randomly built binary search trees"]
      Ch13{{"Chapter 13:<br/>Red-Black Trees ❤️🖤"}}
        Sec13_1["Section 13.1<br/>Properties of red-black trees"]
        Sec13_2["Section 13.2<br/>Rotations"]
        Sec13_3["Section 13.3<br/>Insertion"]
        Sec13_4["Section 13.4<br/>Deletion"]
      Ch14{{"Chapter 14:<br/>Augmenting Data Structures"}}
        Sec14_1["Section 14.1<br/>Dynamic order statistics"]
        Sec14_2["Section 14.2<br/>How to augment a data structure"]
        Sec14_3["Section 14.3<br/>Interval trees"]

    Part_IV))"Part IV<br/>Advanced Design and Analysis Techniques 🛠️"((
      Intro_IV["Introduction"]
      Ch15{{"Chapter 15:<br/>Dynamic Programming"}}
        Sec15_1["Section 15.1<br/>Rod cutting"]
        Sec15_2["Section 15.2<br/>Matrix-chain multiplication"]
        Sec15_3["Section 15.3<br/>Elements of dynamic programming<br/>(Opt. Substructure, Overlapping Subproblems)"]
        Sec15_4["Section 15.4<br/>Longest common subsequence"]
        Sec15_5["Section 15.5<br/>Optimal binary search trees"]
      Ch16{{"Chapter 16:<br/>Greedy Algorithms 💰"}}
        Sec16_1["Section 16.1<br/>An activity-selection problem"]
        Sec16_2["Section 16.2<br/>Elements of the greedy strategy"]
        Sec16_3["Section 16.3<br/>Huffman codes"]
        Sec16_4["? Section 16.4<br/>Matroids and greedy methods"]
        Sec16_5["? Section 16.5<br/>A task-scheduling problem as a matroid"]
      Ch17{{"Chapter 17:<br/>Amortized Analysis<br/>(Aggregate, Accounting, Potential)"}}
        Sec17_1["Section 17.1<br/>Aggregate analysis"]
        Sec17_2["Section 17.2<br/>The accounting method"]
        Sec17_3["Section 17.3<br/>The potential method"]
        Sec17_4["Section 17.4<br/>Dynamic tables"]

    Part_V))"Part V<br/>Advanced Data Structures 🧱"((
      Intro_V["Introduction"]
      Ch18{{"Chapter 18:<br/>B-Trees<br/>(Disk-based)"}}
        Sec18_1["Section 18.1<br/>Definition of B-trees"]
        Sec18_2["Section 18.2<br/>Basic operations on B-trees"]
        Sec18_3["Section 18.3<br/>Deleting a key from a B-tree"]
      Ch19{{"Chapter 19:<br/>Fibonacci Heaps ($O(1)$ amortized INSERT)<br/>($O(\log n)$ amortized EXTRACT-MIN)"}}
        Sec19_1["Section 19.1<br/>Structure of Fibonacci heaps"]
        Sec19_2["Section 19.2<br/>Mergeable-heap operations"]
        Sec19_3["Section 19.3<br/>Decreasing a key and deleting a node"]
        Sec19_4["Section 19.4<br/>Bounding the maximum degree"]
      Ch20{{"Chapter 20:<br/>van Emde Boas Trees ($O(\log\log u)$)"}}
        Sec20_1["Section 20.1<br/>Preliminary approaches"]
        Sec20_2["Section 20.2<br/>A recursive structure"]
        Sec20_3["Section 20.3<br/>The van Emde Boas tree"]
      Ch21{{"Chapter 21:<br/>Data Structures for Disjoint Sets (Union-Find)"}}
        Sec21_1["Section 21.1<br/>Disjoint-set operations"]
        Sec21_2["Section 21.2<br/>Linked-list representation of disjoint sets"]
        Sec21_3["Section 21.3<br/>Disjoint-set forests"]
        Sec21_4["? Section 21.4<br/>Analysis of union by rank with path compression"]

    Part_VI))"Part VI<br/>Graph Algorithms 🕸️ ($G=(V,E)$)"((
      Intro_VI["Introduction"]
      Ch22{{"Chapter 22:<br/>Elementary Graph Algorithms"}}
        Sec22_1["Section 22.1<br/>Representations of graphs"]
        Sec22_2["Section 22.2<br/>Breadth-ﬁrst search<br/>(BFS)"]
        Sec22_3["Section 22.3<br/>Depth-ﬁrst search<br/>(DFS)"]
        Sec22_4["Section 22.4<br/>Topological sort"]
        Sec22_5["Section 22.5<br/>Strongly connected components"]
      Ch23{{"Chapter 23:<br/>Minimum Spanning Trees<br/>(Kruskal, Prim)"}}
        Sec23_1["Section 23.1<br/>Growing a minimum spanning tree"]
        Sec23_2["Section 23.2<br/>The algorithms of Kruskal and Prim"]
      Ch24{{"Chapter 24:<br/>Single-Source Shortest Paths"}}
        Sec24_1["Section 24.1<br/>The Bellman-Ford algorithm<br/>($\delta(s,v)$)"]
        Sec24_2["Section 24.2<br/>Single-source shortest paths in directed acyclic graphs"]
        Sec24_3["Section 24.3<br/>Dijkstra's algorithm"]
        Sec24_4["Section 24.4<br/>Difference constraints and shortest paths"]
        Sec24_5["Section 24.5<br/>Proofs of shortest-paths properties"]
      Ch25{{"Chapter 25:<br/>All-Pairs Shortest Paths"}}
        Sec25_1["Section 25.1<br/>Shortest paths and matrix multiplication"]
        Sec25_2["Section 25.2<br/>The Floyd-Warshall algorithm<br/>($d_{ij}^{(k)}$)"]
        Sec25_3["Section 25.3<br/>Johnson's algorithm for sparse graphs"]
      Ch26{{"Chapter 26:<br/>Maximum Flow<br/>(Ford-Fulkerson, Push-Relabel)"}}
        Sec26_1["Section 26.1<br/>Flow networks<br/>($f(u,v), c(u,v)$)"]
        Sec26_2["Section 26.2<br/>The Ford-Fulkerson method"]
        Sec26_3["Section 26.3<br/>Maximum bipartite matching"]
        Sec26_4["? Section 26.4<br/>Push-relabel algorithms"]
        Sec26_5["? Section 26.5<br/>The relabel-to-front algorithm"]

    Part_VII))"Part VII<br/>Selected Topics 🌟"((
      Intro_VII["Introduction"]
      Ch27{{"Chapter 27:<br/>Multithreaded Algorithms<br/>(Work, Span, Parallelism)"}}
        Sec27_1["Section 27.1<br/>The basics of dynamic multithreading"]
        Sec27_2["Section 27.2<br/>Multithreaded matrix multiplication"]
        Sec27_3["Section 27.3<br/>Multithreaded merge sort"]
      Ch28{{"Chapter 28:<br/>Matrix Operations<br/>($A=LU, PA=LUP, A^{-1}$)"}}
        Sec28_1["Section 28.1<br/>Solving systems of linear equations"]
        Sec28_2["Section 28.2<br/>Inverting matrices"]
        Sec28_3["Section 28.3<br/>Symmetric positive-deﬁnite matrices and least-squares approximation"]
      Ch29{{"Chapter 29:<br/>Linear Programming<br/>(Simplex)"}}
        Sec29_1["Section 29.1<br/>Standard and slack forms"]
        Sec29_2["Section 29.2<br/>Formulating problems as linear programs"]
        Sec29_3["Section 29.3<br/>The simplex algorithm"]
        Sec29_4["Section 29.4<br/>Duality"]
        Sec29_5["Section 29.5<br/>The initial basic feasible solution"]
      Ch30{{"Chapter 30:<br/>Polynomials and the FFT<br/>($Y_k = \sum_{j=0}^{N-1} x_j e^{-i2\pi jk/N}$)"}}
        Sec30_1["Section 30.1<br/>Representing polynomials"]
        Sec30_2["Section 30.2<br/>The DFT and FFT"]
        Sec30_3["Section 30.3<br/>Efﬁcient FFT implementations"]
      Ch31{{"Chapter 31:<br/>Number-Theoretic Algorithms<br/>($\gcd(a,b)$, RSA, Primality)"}}
        Sec31_1["Section 31.1<br/>Elementary number-theoretic notions"]
        Sec31_2["Section 31.2<br/>Greatest common divisor"]
        Sec31_3["Section 31.3<br/>Modular arithmetic"]
        Sec31_4["Section 31.4<br/>Solving modular linear equations"]
        Sec31_5["Section 31.5<br/>The Chinese remainder theorem"]
        Sec31_6["Section 31.6<br/>Powers of an element"]
        Sec31_7["Section 31.7<br/>The RSA public-key cryptosystem"]
        Sec31_8["? Section 31.8<br/>Primality testing"]
        Sec31_9["? Section 31.9<br/>Integer factorization"]
      Ch32{{"Chapter 32:<br/>String Matching<br/>(KMP, Rabin-Karp)"}}
        Sec32_1["Section 32.1<br/>The naive string-matching algorithm"]
        Sec32_2["Section 32.2<br/>The Rabin-Karp algorithm"]
        Sec32_3["Section 32.3<br/>String matching with ﬁnite automata"]
        Sec32_4["? Section 32.4<br/>The Knuth-Morris-Pratt algorithm"]
      Ch33{{"Chapter 33:<br/>Computational Geometry"}}
        Sec33_1["Section 33.1<br/>Line-segment properties"]
        Sec33_2["Section 33.2<br/>Determining whether any pair of segments intersects"]
        Sec33_3["Section 33.3<br/>Finding the convex hull"]
        Sec33_4["Section 33.4<br/>Finding the closest pair of points"]
      Ch34{{"Chapter 34:<br/>NP-Completeness<br/>(P, NP, NPC, Reductions)"}}
        Sec34_1["Section 34.1<br/>Polynomial time"]
        Sec34_2["Section 34.2<br/>Polynomial-time veriﬁcation"]
        Sec34_3["Section 34.3<br/>NP-completeness and reducibility"]
        Sec34_4["Section 34.4<br/>NP-completeness proofs"]
        Sec34_5["Section 34.5<br/>NP-complete problems"]
      Ch35{{"Chapter 35:<br/>Approximation Algorithms<br/>($C/C^* \le \rho(n)$)"}}
        Sec35_1["Section 35.1<br/>The vertex-cover problem"]
        Sec35_2["Section 35.2<br/>The traveling-salesman problem"]
        Sec35_3["Section 35.3<br/>The set-covering problem"]
        Sec35_4["Section 35.4<br/>Randomization and linear programming"]
        Sec35_5["Section 35.5<br/>The subset-sum problem"]

    Part_VIII))"Part VIII<br/>Appendix:<br/>Mathematical Background 📐"((
      Intro_VIII["Introduction"]
      AppA["Appendix A <br/>Summations<br/>($\sum$)"]
        SecA_1["Section A.1 <br/>Summation formulas and properties"]
        SecA_2["Section A.2 <br/>Bounding summations"]
      AppB["Appendix B<br/>Sets, Etc. ($\cup, \cap, \subseteq$)"]
        SecB_1["Section B.1 <br/>Sets"]
        SecB_2["Section B.2 <br/>Relations"]
        SecB_3["Section B.3 <br/>Functions"]
        SecB_4["Section B.4 <br/>Graphs"]
        SecB_5["Section B.5 <br/>Trees"]
      AppC["Appendix C<br/>Counting and Probability ($P(A), E[X]$)"]
        SecC_1["Section C.1 <br/>Counting"]
        SecC_2["Section C.2 <br/>Probability"]
        SecC_3["Section C.3 <br/>Discrete random variables"]
        SecC_4["Section C.4 <br/>The geometric and binomial distributions"]
        SecC_5["? Section C.5 <br/>The tails of the binomial distribution"]
      AppD["Appendix D<br/>Matrices<br/>($A^{-1}, \det(A)$)"]
        SecD_1["Section D.1<br/>Matrices and matrix operations"]
        SecD_2["Section D.2<br/>Basic matrix properties"]
    Bibliography))"Bibliography 📜"((
    Index))"Index 🔍"((
```

This mind map provides a high-level view of the book's structure, highlighting the different parts and the chapters contained within each. Key mathematical concepts and chapter themes are indicated with emojis and LaTeX notations for quick reference. Chapters and sections marked with '?' are those identified as more advanced in the original Table of Contents.

---

## Preface Highlights ✨

The preface of CLRS provides context for different readers and outlines the key changes in the third edition. Here's a summary:

```mermaid
---
title: "Preface Highlights"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY-SA 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  layout: elk
  theme: base
  look: handDrawn
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': { 'htmlLabels': true, 'curve': 'basis' },
    'fontFamily': 'American Typewriter, monospace',
    'logLevel': 'fatal',
    'themeVariables': {
      'primaryColor': '#22BB',
      'primaryTextColor': '#F8B229',
      'lineColor': '#F8B229',
      'primaryBorderColor': '#27AE60',
      'secondaryColor': '#E2F1',
      'secondaryTextColor': '#6C3483',
      'secondaryBorderColor': '#A569BD',
      'fontSize': '20px'
    }
  }
}%%
flowchart LR
    subgraph Preface_CLRS["Preface Insights"]
    style Preface_CLRS fill:#f9f3,stroke:#333,stroke-width:2px, color: #FFF
    direction LR

        Audience["🎯 Target Audiences"]
        Audience --> Teacher["To the Teacher 👨‍🏫<br/>- Versatile & complete for various courses<br/>- Self-contained chapters<br/>- 957 exercises & 158 problems<br/>- Solutions to some problems/exercises on website<br/>- Starred sections/exercises for graduate level"]
        Audience --> Student["To the Student 🧑‍🎓<br/>- Accessible and interesting algorithms<br/>- Step-by-step descriptions<br/>- Careful math explanations<br/>- Useful as textbook and future reference"]
        Audience --> Professional["To the Professional 👩‍💻<br/>- Excellent handbook on algorithms<br/>- Self-contained chapters for focused study<br/>- Addresses implementation concerns & engineering issues<br/>- Pseudocode designed for clarity and easy translation"]

        Prereqs["Prerequisites 🔑"]
        Prereqs --> ProgExp["Programming Experience<br/> (recursion, simple data structures like arrays & linked lists)"]
        Prereqs --> MathProofs["Facility with Mathematical Proofs<br/>(especially induction)"]
        Prereqs --> Calculus["Elementary Calculus<br/>(for some portions)"]
        Prereqs --> MathInBook["Parts I & VIII teach all necessary mathematical techniques"]

        Changes3rdEd["Key Changes in 3rd Edition 🔄"]
        Changes3rdEd --> NewContent["<b>New Chapters:</b> <br/>van Emde Boas trees, Multithreaded algorithms, Appendix on Matrix Basics"]
        Changes3rdEd --> Revisions["Chapter on recurrences revised<br/>(more on divide-and-conquer, Strassen's moved here)"]
        Changes3rdEd --> Removals["<b>Removed Chapters:</b><br/> Binomial heaps, Sorting networks<br/>(0-1 principle moved to a problem)"]
        Changes3rdEd --> DPGreedyRevisions["Revised treatment of Dynamic Programming (rod cutting example) and<br/> Greedy Algorithms (activity selection)"]
        Changes3rdEd --> BSTDeletionLogic["Revised BST deletion<br/>(node requested is the one deleted)"]
        Changes3rdEd --> FlowNetworkLogic["Flow networks based entirely on edges"]
        Changes3rdEd --> StringMatching["Modified Knuth-Morris-Pratt string-matching algorithm"]
        Changes3rdEd --> PseudocodeUpdate["<b>Revised Pseudocode:</b> <br/>Uses <code>:=</code> for assignment, <code>==</code> for equality tests, <code>//</code> for comments, dot-notation for attributes<br/>(still procedural)"]
        Changes3rdEd --> MorePractice["100 new exercises, 28 new problems, updated bibliography"]
        Changes3rdEd --> WritingEnhancements["Improved writing style:<br/>clearer and more active"]

        WebResources["🌐 Website<br/> (mitpress.mit.edu/algorithms/)"]
        WebResources --> ErrataList["List of known errors"]
        WebResources --> PartialSolutions["Solutions to selected exercises and problems"]
        WebResources --> Jokes["Explanation of 'corny professor jokes' 😉"]
        WebResources --> Feedback["How to report errors or make suggestions"]

        Production["Book Production Notes 🖨️"]
        Production --> LaTeX["Produced in LaTeX 2ε"]
        Production --> Fonts["Times font with MathTime Pro 2 for math"]
        Production --> Illustrations["Illustrations drawn using MacDraw Pro"]
    end
```

This diagram summarizes who the book is for, what background is helpful, the significant updates made in the third edition, and information about supplementary online resources.

### Mathematical Notations Highlighted

Several chapter sections imply specific mathematical notations or concepts central to their theme. Examples from the Table of Contents illustrated in the mindmap include:
-   **Chapter 3 (Growth of Functions):** $\Theta(n^2), O(n \log n), \Omega(n)$
-   **Chapter 4 (Divide-and-Conquer):** Recurrence relations like $T(n) = aT(n/b) + f(n)$
-   **Chapter 5 (Probabilistic Analysis):** Expected value $E[X]$, indicator random variables $I\{A\}$
-   **Chapter 8 (Sorting in Linear Time):** $O(n)$ complexity
-   **Chapter 11 (Hash Tables):** Hash function notation $h(k)$
-   **Chapter 13 (Red-Black Trees):** Use of colors ❤️🖤 (conceptual)
-   **Chapter 19 (Fibonacci Heaps):** Amortized $O(1)$ for INSERT, UNION, DECREASE-KEY; $O(\log n)$ for EXTRACT-MIN.
-   **Chapter 20 (van Emde Boas Trees):** $O(\log\log u)$ complexity.
-   **Chapter 24 (Single-Source Shortest Paths):** Shortest-path weight $\delta(s,v)$.
-   **Chapter 25 (All-Pairs Shortest Paths):** $d_{ij}^{(k)}$ notation for the Floyd-Warshall algorithm.
-   **Chapter 26 (Maximum Flow):** Flow $f(u,v)$, capacity $c(u,v)$.
-   **Chapter 28 (Matrix Operations):** $A=LU$, $PA=LUP$, $A^{-1}$, $\det(A)$.
-   **Chapter 30 (Polynomials and the FFT):** Discrete Fourier Transform $Y_k = \sum_{j=0}^{N-1} x_j e^{-i2\pi jk/N}$.
-   **Chapter 31 (Number-Theoretic Algorithms):** $\gcd(a,b)$, RSA, Primality related concepts.
-   **Chapter 35 (Approximation Algorithms):** Approximation ratio $C/C^* \le \rho(n)$.
-   **Appendices:** $\sum$ (Summations), $\cup, \cap, \subseteq$ (Sets), $P(A), E[X]$ (Probability), $A^{-1}, \det(A)$ (Matrices).

The selection of which chapters/sections are marked with '?' is directly from the provided Table of Contents.

----

<!-- 
```mermaid
%% Current Mermaid version
info
```  -->


```mermaid
---
title: "CongLeSolutionX"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY-SA 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%{
  init: {
    'flowchart': { 'htmlLabels': false },
    'fontFamily': 'Bradley Hand',
    'themeVariables': {
      'primaryColor': '#fc82',
      'primaryTextColor': '#F8B229',
      'primaryBorderColor': '#27AE60',
      'secondaryColor': '#81c784',
      'secondaryTextColor': '#6C3483',
      'lineColor': '#F8B229',
      'fontSize': '20px'
    }
  }
}%%
flowchart LR
  My_Meme@{ img: "https://raw.githubusercontent.com/CongLeSolutionX/MY_GRAPHIC_ASSETS/refs/heads/main/MY_MEME/My-meme-ideas.png", label: "Ăn uống gì chưa ngừi đẹp?", pos: "b", w: 200, h: 150, constraint: "off" }

  Closing_quote@{ shape: braces, label: "Math and code work together to bring interactive art to life!" }
    
  My_Meme ~~~ Closing_quote
    
  Link_to_my_profile{{"<a href='https://github.com/CongLeSolutionX/CongLeSolutionX' target='_blank'>Click here if you care about my profile</a>"}}

  Closing_quote ~~~ My_Meme
  My_Meme animatingEdge@--> Link_to_my_profile
  
  animatingEdge@{ animate: true }

```

---
>**Licenses:**
>
>- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
>- **Creative Commons Attribution-ShareAlike 4.0 International**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) [![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/) - Legal details in [LICENSE-CC-BY-SA-4.0](THE_PAST/LICENSE-CC-BY-SA-4.0) and at [Creative Commons official site](https://creativecommons.org/licenses/by-sa/4.0/).
>
---


## References

The primary reference for this document is the book itself:
*   Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

Additional references for specific concepts or algorithms mentioned within CLRS can be found in its extensive bibliography. For example, the text mentions:
*   Knuth, D. E. (1997). *The Art of Computer Programming, Volume 1: Fundamental Algorithms* (3rd ed.). Addison-Wesley. (For general algorithm study and history)
*   Aho, A. V., Hopcroft, J. E., & Ullman, J. D. (1974). *The Design and Analysis of Computer Algorithms*. Addison-Wesley. (For asymptotic analysis and recurrences)
*   And numerous other specific papers and books for individual topics.

---

