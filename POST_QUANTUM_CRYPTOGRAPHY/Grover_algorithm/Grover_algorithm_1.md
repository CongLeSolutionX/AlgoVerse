---
created: 2025-06-11 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY-SA 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---


> ⚠️🏗️🚧🦺🧱🪵🪨🪚🛠️👷
> 
> This is a working draft in progress
> 
> ![Loading...](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzd4ZDB4YW9lc3E2cnlnM2c0MnI3N2UzczdjNnI3ZHZod283N3FpMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3fZLMbuCOqJ82gec/giphy.gif)
> 
> ⚠️🏗️🚧🦺🧱🪵🪨🪚🛠️👷


----

# Grover's Algorithm: A Quantum Leap in Search
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---

## 1. Introduction: The Needle in a Haystack, Quantum Style

Grover's algorithm, developed by Lov Grover in 1996 [1, 2], is a cornerstone of quantum computation, offering a significant speedup for a ubiquitous problem: **unstructured search**. Imagine trying to find a specific item (the "needle") in a vast, unsorted collection (the "haystack"). Classically, you might have to check each item one by one, leading to an average search time proportional to the size of the collection. Grover's algorithm leverages the principles of quantum mechanics—superposition and interference—to find the marked item with high probability in a time proportional to the square root of the collection's size. This quadratic speedup, while not exponential, is substantial for large datasets and has profound implications for various computational problems [3].

For those looking for comprehensive details on quantum algorithms, foundational texts like Nielsen and Chuang's "Quantum Computation and Quantum Information" [4] provide extensive coverage.

```mermaid
%%{ init: { 'theme': 'dark', 'fontFamily': 'monospace' } }%%
mindmap
  root((Grover's Algorithm))
    ::icon(fa fa-search)
    Definition
      :Quantum algorithm for unstructured search [1, 2];
      :Finds a "marked" item in a database;
    Key Inventor
      :Lov Grover (1996);
    Core Quantum Principles Utilized
      :Superposition (explore all items at once);
      :Interference (amplify desired item's probability);
      :Amplitude Amplification (the core mechanism) [4, Ch. 6];
    Primary Advantage
      :Quadratic speedup over classical search;
      :$O(\sqrt{N})$ vs $O(N)$ [3];
    Significance
      :One of the primary quantum algorithms demonstrating speedup;
      :Broad applicability to search-related problems;
```

----

## 2. The Problem: Unstructured Search

Consider a database or search space containing $N$ items. One or more of these items are "marked" or "target" items we wish to find. There is no exploitable structure or order in this database that could help us locate the marked item(s) more efficiently (e.g., it's not sorted). Such problems are common, for instance, when searching through large public datasets like those found on `data.gov` (US) or the `EU Open Data Portal` if no indexing related to the search query is available.

*   **Classical Approach:** In the worst-case scenario, a classical algorithm would need to examine up to $N$ items to find the marked one. On average, it would take $N/2$ queries. The complexity is thus $O(N)$.
*   **The Oracle:** We assume the existence of a "black box" function, called an **oracle**, $f(x)$, which can identify whether an item $x$ is marked or not.
	*   $f(x) = 1$ if $x$ is a marked item (the "solution" or "winner", denoted $\omega$).
	*   $f(x) = 0$ if $x$ is not a marked item.

The goal is to find an $x$ such that $f(x)=1$, using the minimum number of queries to the oracle.

----

## 3. Quantum Approach: Superposition and Interference

Grover's algorithm employs $n$ qubits to represent the $N=2^n$ items in the search space. The core quantum mechanical principles are detailed in many quantum computing textbooks [4, 5].

### 3.1. Initial Superposition
The algorithm begins by preparing the qubits in an equal superposition of all possible states (all $N$ items):
$$
\ket{s} = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} \ket{x}
$$
This state $\ket{s}$ represents a state where each item $\ket{x}$ has an equal probability amplitude of $1/\sqrt{N}$. Measuring this state would yield any item with equal probability $1/N$.

### 3.2. The Quantum Oracle ($U_\omega$)
The classical oracle $f(x)$ is transformed into a quantum operator $U_\omega$. This oracle doesn't reveal the marked item directly but applies a conditional phase shift to it. Specifically, if $\ket{x}$ is the marked state (solution $\omega$), its phase is flipped. For all other states, the phase is unchanged.
$$
U_\omega \ket{x} = (-1)^{f(x)} \ket{x}
$$
So,
*   If $x = \omega$ (marked item): $U_\omega \ket{\omega} = -\ket{\omega}$
*   If $x \neq \omega$ (unmarked item): $U_\omega \ket{x} = \ket{x}$

Geometrically, this operation can be viewed as a reflection of the state vector about the hyperplane orthogonal to the marked state $\ket{\omega}$ [4, Sec. 6.1].

### 3.3. The Grover Diffusion Operator ($U_s$) - Inversion About the Mean
After the oracle marks the solution(s) by flipping their phase, the second crucial step is the **Grover diffusion operator**, also known as "inversion about the mean" or "amplitude amplification." This operator, denoted $U_s$, amplifies the amplitude of the marked state(s) and dampens the amplitudes of the unmarked states.
It is defined as:
$$
U_s = 2\ket{s}\bra{s} - I
$$
Where:
*   $\ket{s}$ is the initial equal superposition state.
*   $\bra{s}$ is its conjugate transpose.
*   $I$ is the identity operator.

This operator $U_s$ can be implemented using Hadamard gates and a conditional phase shift: $U_s = H^{\otimes n} U_0 H^{\otimes n}$, where $U_0$ flips the phase of the $\ket{0…0}$ state and leaves others unchanged ($U_0 \ket{0} = -\ket{0}$, $U_0 \ket{x} = \ket{x}$ for $x \neq 0$). The process of amplitude amplification is a general quantum technique described extensively in the literature [e.g., 6].

Geometrically, $U_s$ reflects the current state vector about the initial superposition state $\ket{s}$. The combined effect of $U_\omega$ and $U_s$ is a rotation in the 2D space spanned by $\ket{s}$ and $\ket{\omega}$ (assuming a single marked item for simplicity).

```mermaid
%%{ init: { 'theme': 'dark', 'fontFamily': 'monospace' } }%%
graph TD
    subgraph GroverIteration ["Grover Iteration Block (G)"]
        style GroverIteration fill:#223,stroke:#09f,stroke-width:2px
        direction LR
        U_omega["<b>Oracle</b><br>(Phase Flip Marked Item(s))<br>$U_\\omega$"]
        U_s["<b>Grover Diffusion / Inversion About Mean</b><br>(Amplify Marked, Dampen Unmarked)<br>$U_s = 2|s⟩⟨s| - I$"]
        U_omega --> U_s
    end

    U_omega_desc>"Marks solution(s) by<br>flipping their phase. [4, Sec. 6.1.2]"
    U_s_desc>"Amplifies amplitude of marked state(s)<br>by reflecting about the mean <br>amplitude (|s⟩). [4, Sec. 6.1.3]"

    U_omega_desc -.-> U_omega
    U_s_desc -.-> U_s

    classDef operator fill:#05a,stroke:#fff,stroke-width:1px,color:#fff;
    class U_omega,U_s operator;
```

----

## 4. The Algorithm Steps

The Grover algorithm proceeds as follows [1, 4]:

1.  **Initialization:** Prepare an $n$-qubit register (where $N=2^n$) in the state $\ket{0…0}$. Apply Hadamard gates to each qubit to create the uniform superposition state:
	$$
    \ket{\psi_0} = \ket{s} = H^{\otimes n} \ket{0}^{\otimes n} = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} \ket{x}
    $$
2.  **Iterative Amplification (Grover Iterations):** Repeat the following "Grover operator" $G = U_s U_\omega$ approximately $R$ times:
	a. Apply the quantum oracle $U_\omega$.
		$$ \ket{\psi_{t_a}} = U_\omega \ket{\psi_t} $$
	b. Apply the Grover diffusion operator $U_s$.
		$$ \ket{\psi_{t+1}} = U_s \ket{\psi_{t_a}} $$
	The number of iterations $R$ is crucial and is approximately $\frac{\pi}{4}\sqrt{N/M}$, where $M$ is the number of marked items (if $M=1$, $R \approx \frac{\pi}{4}\sqrt{N}$).
3.  **Measurement:** Measure the $n$-qubit register in the computational basis. The outcome will be one of the marked items $\omega$ with high probability.

```mermaid
%%{ init: { 'theme': 'dark', 'fontFamily': 'monospace', 'flowchart': {'curve': 'basis'} } }%%
flowchart TD
    A[Start] --> B(1. Initialize Qubits<br>$\ket{\psi_0} = H^{\otimes n} \ket{0...0} = \frac{1}{\sqrt{N}}\sum \ket{x}$);
    B --> C{Repeat R times<br>$R \approx \frac{\pi}{4}\sqrt{N/M}$};
    C -- Yes --> D(2a. Apply Oracle $U_\omega$);
    D --> E(2b. Apply Grover Diffusion $U_s$);
    E --> C;
    C -- No (After R iterations) --> F(3. Measure Qubits);
    F --> G[Output: Marked Item $\omega$<br>with high probability];
    G --> H[End];

    classDef step fill:#333,stroke:#0af,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    classDef io fill:#063,stroke:#0c6,stroke-width:2px,color:#fff,rx:15px,ry:15px;
    classDef decision fill:#502,stroke:#a04,stroke-width:2px,color:#fff,rx:5px,ry:5px;
    class B,D,E,F step;
    class A,G,H io;
    class C decision;
```

----

## 5. Mathematical Analysis: The Geometry of Search

For simplicity, let's assume there is exactly one marked item $\ket{\omega}$. The state of the system can always be expressed as a linear combination of $\ket{\omega}$ and a state $\ket{\alpha}$ which is the normalized superposition of all unmarked states:
$$ \ket{s} = \sin\theta \ket{\omega} + \cos\theta \ket{\alpha} $$
where $\sin\theta = \langle s | \omega \rangle = 1/\sqrt{N}$ (the initial amplitude of $\ket{\omega}$).
The Grover iteration $G = U_s U_\omega$ can be understood as a rotation in the 2D plane spanned by $\ket{\omega}$ and $\ket{\alpha}$ [4, Sec. 6.1.4].

*   The oracle $U_\omega$ reflects the state vector about $\ket{\alpha}$. It flips the component along $\ket{\omega}$.
*   The diffusion $U_s$ reflects the state vector about $\ket{s}$.

The combined operation $G = U_s U_\omega$ is a rotation by an angle of $2\theta$ in the $\ket{\alpha}$-$\ket{\omega}$ plane, towards $\ket{\omega}$.
After $k$ iterations, the state is:
$$ \ket{\psi_k} = \sin((2k+1)\theta)\ket{\omega} + \cos((2k+1)\theta)\ket{\alpha} $$
The probability of measuring the marked state $\ket{\omega}$ after $k$ iterations is $P_k(\omega) = |\langle \omega | \psi_k \rangle|^2 = \sin^2((2k+1)\theta)$.

### 5.1. Optimal Number of Iterations
We want $(2R+1)\theta \approx \pi/2$ to maximize $\sin^2((2R+1)\theta)$.
So, $2R+1 \approx \frac{\pi}{2\theta}$.
Since $\theta$ is small for large $N$, $\sin\theta \approx \theta$. Thus, $\theta \approx 1/\sqrt{N}$.
$$ 2R+1 \approx \frac{\pi}{2 (1/\sqrt{N})} = \frac{\pi\sqrt{N}}{2} $$
$$ R \approx \frac{\pi\sqrt{N}}{4} - \frac{1}{2} \approx \frac{\pi}{4}\sqrt{N} $$
The optimal number of iterations is $R = \text{round}\left(\frac{\pi}{4\theta} - \frac{1}{2}\right) = \text{round}\left(\frac{\arccos(1/\sqrt{N})}{2\arcsin(1/\sqrt{N})} - \frac{1}{2}\right) \approx \lfloor \frac{\pi}{4}\sqrt{N} \rfloor$.

If there are $M$ marked items, $\sin\theta = \sqrt{M/N}$, and the optimal number of iterations becomes $R \approx \frac{\pi}{4}\sqrt{N/M}$ [7].

### 5.2. Success Probability
With $R \approx \frac{\pi}{4}\sqrt{N/M}$ iterations, the success probability is very high, approaching 1 for large $N$.
It's important to note that over-iterating (i.e., performing significantly more than $R$ iterations) will rotate the state vector *past* $\ket{\omega}$, decreasing the success probability [4, Sec. 6.1.5].

----

## 6. Complexity and Advantages

*   **Query Complexity:** Grover's algorithm requires $O(\sqrt{N/M})$ queries to the oracle. For a single marked item ($M=1$), this is $O(\sqrt{N})$ [1, 2].
*   **Time Complexity:** Assuming the oracle $U_\omega$ and diffusion operator $U_s$ can be implemented efficiently (e.g., in polylogarithmic time in $N$, $O(\text{poly}(\log N))$), the overall time complexity is also $O(\sqrt{N/M})$. This is a quadratic speedup compared to the classical $O(N/M)$ average-case complexity.
*   **Provably Optimal:** It has been proven that for unstructured search, any quantum algorithm must make at least $\Omega(\sqrt{N/M})$ queries to the oracle. Thus, Grover's algorithm is asymptotically optimal [8, 9].

```mermaid
%%{ init: { 'theme': 'dark', 'fontFamily': 'monospace' } }%%
graph LR
    title["Grover's vs. Classical Search Complexity"]
    subgraph ClassicalSearch["Classical Unstructured Search"]
        style ClassicalSearch fill:#511,stroke:#f33,stroke-width:2px
        C_Avg["Average Case: <br><b>O(N/M)</b> queries"]
        C_Worst["Worst Case: <br><b>O(N)</b> queries (for M=1)"]
    end

    subgraph GroverAlgorithm["Grover's Quantum Search"]
        style GroverAlgorithm fill:#115,stroke:#33f,stroke-width:2px
        Q_Queries["Oracle Queries: <br><b>O(√(N/M))</b> [1, 2]"]
        Q_Optimal["Provably Optimal<br>for quantum search [8, 9]"]
    end

    SpeedupInfo((Quadratic Speedup<br>Significant for large N))

    ClassicalSearch --- SpeedupInfo
    GroverAlgorithm --- SpeedupInfo

    note right of Q_Queries
      Where:
      N = Number of items in database
      M = Number of marked items
    endnote

    classDef complexityBox fill:#222,stroke:#ccc,stroke-width:1px,color:#fff,padding:10px,rx:5,ry:5;
    class C_Avg,C_Worst,Q_Queries,Q_Optimal complexityBox;
```

----

## 7. Quantum Circuit Representation (Conceptual)

A typical quantum circuit for Grover's algorithm involves:
1.  A layer of Hadamard gates ($H^{\otimes n}$) on $n$ qubits initialized to $\ket{0…0}$.
2.  Repeated blocks of:
	a. The Oracle ($U_\omega$) implementation.
	b. The Grover Diffusion Operator ($U_s$). $U_s$ itself is often implemented as $H^{\otimes n} \rightarrow \text{PhaseShift}(\ket{0..0}) \rightarrow H^{\otimes n}$. The phase shift targeting $\ket{0..0}$ can be built using multi-controlled Z gates or X gates, a multi-controlled Z (or Toffoli if an ancilla qubit is used), and X gates again [4, Appendix A4].
3.  Final measurement.

Many quantum computing platforms and research institutions, such as those listed by the US National Quantum Initiative (quantum.gov) or EU's Quantum Flagship (qt.eu), provide tools and simulators for constructing and testing such circuits.

```mermaid
%%{ init: { 'theme': 'dark', 'look': 'handDrawn', 'fontFamily': 'monospace' } }%%
sequenceDiagram
    participant Qubits as Qubits<br>$\ket{0...0}$
    participant H_Layer as H<sup>&otimes;n</sup> Gates
    participant Oracle_U_omega as Oracle $U_\omega$
    participant Diffusion_U_s as Diffusion $U_s$
    participant Measurement as Measurement

    Qubits->>H_Layer: Apply Hadamards
    Note over H_Layer, Oracle_U_omega: Initial State: $\ket{s} = \frac{1}{\sqrt{N}}\sum\ket{x}$
    loop R ≈ (π/4)√N Iterations
        H_Layer->>Oracle_U_omega: Apply Oracle
        Oracle_U_omega->>Diffusion_U_s: Apply Diffusion Operator
        Diffusion_U_s->>H_Layer: Output for next iteration (conceptually)
    end
    Diffusion_U_s->>Measurement: Measure Qubits
    Measurement->>Qubits: Result (Marked Item $\omega$)

    Note left of Qubits: Start
    Note right of Measurement: End
```

*Note: The sequence diagram above is a high-level conceptual flow. Actual quantum circuit diagrams depict qubits as horizontal lines and gates as blocks operating on them.*

----

## 8. Applications

Grover's algorithm and its core idea of amplitude amplification have implications beyond simple database search [3, 4]:

*   **Solving NP-Complete Problems:** While not providing a general polynomial-time solution for NP-Complete problems, Grover's algorithm can offer a quadratic speedup for problems that can be cast as a search. For example, for 3-SAT, if one can verify a solution in polynomial time, Grover can find a solution in $O(\sqrt{2^n} \cdot \text{poly}(n))$ time, compared to classical $O(2^n \cdot \text{poly}(n))$.
*   **Element Distinctness:** Finding if all elements in a list are unique.
*   **Collision Finding:** Finding two inputs to a function that produce the same output, relevant in cryptography.
*   **Approximating the Mean and Median:** Quantum algorithms for these statistical tasks can leverage Grover-like amplitude amplification.
*   **Quantum Counting:** Estimating the number of marked items ($M$) in $O(\sqrt{N/M})$ or $O(\sqrt{N})$ time [10].
*   **Speeding up Heuristics:** Can be used as a subroutine in larger classical or quantum algorithms to accelerate search components.

----

## 9. Limitations and Considerations

*   **Oracle Construction:** The efficiency of Grover's algorithm depends on the ability to construct an efficient quantum oracle $U_\omega$ for the specific problem [4]. Devising this oracle can be non-trivial and might require significant quantum resources. The US National Institute of Standards and Technology (NIST) often discusses challenges in quantum oracle construction in its quantum computing program literature.
*   **Quadratic, Not Exponential:** The speedup is quadratic, not exponential like Shor's algorithm for factoring. This means for many NP-Complete problems, the complexity remains exponential, albeit with a smaller exponent relative to classical brute force.
*   **Parallelism is Key:** The power comes from quantum parallelism (superposition) and interference, not from running many classical searches in parallel.
*   **Error Correction:** Like all quantum algorithms, practical implementation requires robust quantum error correction due to decoherence and gate inaccuracies [4, Ch. 10].
*   **Number of Iterations:** The precise optimal number of iterations must be known (or well-estimated). Over-iterating reduces the probability of success. If $M$ (number of solutions) is unknown, Quantum Counting can be used first [10], or techniques for unknown $M$ can be applied [7].
*   **Not a Magic Bullet for AI Search:** While it speeds up *unstructured* search, many AI search problems involve heuristics and structured state spaces where classical algorithms like A\* are already very effective. Grover's algorithm is best suited where little to no structural information can be exploited.

----

## 10. Summary: The Grover's Algorithm Landscape

Grover's algorithm stands as a testament to the power of quantum computation for accelerating search tasks [1, 2]. Its quadratic speedup, achieved through clever manipulation of quantum amplitudes via an oracle and diffusion operations, has opened new avenues for tackling computationally intensive problems. While not a universal solution, its principles are fundamental to the field of quantum algorithms and continue to inspire research into further quantum advantages, as often highlighted in roadmap documents by national quantum initiatives [e.g., 11].

```mermaid
%%{ init: { 'theme': 'dark', 'fontFamily': 'monospace' } }%%
mindmap
  root((Grover's Algorithm Summary))
    ::icon(fa fa-量子)
    Core Concept
      :Quantum search in unstructured database [1, 2]
      :Amplitude Amplification [4, 6]
    Key Components
      :Initial Superposition ($\ket{s}$)
      :Quantum Oracle ($U_\omega$)
        :Flips phase of marked item(s)
        :$U_\omega \ket{x} = (-1)^{f(x)} \ket{x}$
      :Grover Diffusion Operator ($U_s$)
        :Inversion about the mean
        :$U_s = 2\ket{s}\bra{s} - I$
        :Amplifies marked state's amplitude
    Algorithm Flow
      :1. Initialize to $\ket{s}$
      :2. Repeat $G = U_s U_\omega$ for $R \approx \frac{\pi}{4}\sqrt{N/M}$ times
      :3. Measure state
    Mathematical Basis
      :Rotation in 2D space (spanned by $\ket{\omega}$ and $\ket{\alpha}$) [4]
      :Each iteration rotates state by $2\theta$ (where $\sin\theta = \sqrt{M/N}$)
      :Probability of success $P_k(\omega) = \sin^2((2k+1)\theta)$
    Complexity & Optimality
      :Query Complexity: $O(\sqrt{N/M})$ [1]
      :Provably optimal for quantum unstructured search [8, 9]
      :Quadratic speedup over classical $O(N/M)$
    Applications
      :Database search
      :Collision finding
      :Speeding up NP-problem heuristics (e.g., SAT solvers)
      :Quantum Counting [10]
    Limitations
      :Oracle construction complexity
      :Requires knowledge/estimate of $M$ for optimal iterations (or use Quantum Counting) [7, 10]
      :Quadratic, not exponential, speedup
      :Susceptible to over-iteration
    Impact
      :Demonstrates clear quantum advantage for a broad class of problems
      :Fundamental building block for other quantum algorithms [3]
```

---

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

  Closing_quote@{ shape: braces, label: "With the right context,<br/>theory become reality" }
    
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


### References

[1] Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *Proceedings of the twenty-eighth annual ACM symposium on Theory of computing*, 212-219. (Available via ACM Digital Library, often pre-prints on arXiv such as arXiv:quant-ph/9605043)

[2] Grover, L. K. (1997). Quantum mechanics helps in searching for a needle in a haystack. *Physical Review Letters*, 79(2), 325-328.

[3] Bernstein, D. J., Buchmann, J., & Dahmen, E. (Eds.). (2009). *Post-Quantum Cryptography*. Springer. (Section on Grover's impact on symmetric crypto).

[4] Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information: 10th Anniversary Edition*. Cambridge University Press.

[5] Kaye, P., Laflamme, R., & Mosca, M. (2007). *An Introduction to Quantum Computing*. Oxford University Press.

[6] Brassard, G., Høyer, P., Mosca, M., & Tapp, A. (2002). Quantum amplitude amplification and estimation. *Contemporary Mathematics*, 305, 53-74. (arXiv:quant-ph/0005055)

[7] Boyer, M., Brassard, G., Høyer, P., & Tapp, A. (1998). Tight bounds on quantum searching. *Fortschritte der Physik: Progress of Physics*, 46(4‐5), 493-505. (arXiv:quant-ph/9605034 - Discusses case of unknown M)

[8] Bennett, C. H., Bernstein, E., Brassard, G., & Vazirani, U. (1997). Strengths and weaknesses of quantum computing. *SIAM journal on Computing*, 26(5), 1510-1523. (arXiv:quant-ph/9701001)

[9] Zalka, C. (1999). Grover's quantum searching algorithm is optimal. *Physical Review A*, 60(4), 2746. (arXiv:quant-ph/9711070)

[10] Brassard, G., Hoyer, P., & Tapp, A. (1998). Quantum counting. *Automata, Languages and Programming*, 81-90. (ICALP '98, arXiv:quant-ph/9805082)

[11] National Quantum Initiative (US). (Various publications and roadmaps). Available at `quantum.gov`. *(Example of a public resource discussing quantum computing efforts generally, where Grover's algorithm is a known component of the field.)*

----
