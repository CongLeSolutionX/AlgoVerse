---
created: 2025-02-09 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: https://scottaaronson.blog/?p=762

---


# The First Law of Complexodynamics
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## 1. The Paradox: Entropy vs. Complexity

The blog post starts by highlighting a paradox related to the Second Law of Thermodynamics and our intuitive understanding of complexity.

### Diagram 1: Entropy and Complexity over Time

```mermaid
---
title: Entropy (Red) vs. Complexity (Blue) over Time
caption:  Entropy increases monotonically according to the Second Law, while Complexity peaks at an intermediate time, creating a curve.
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    subgraph Entropy
    style Entropy fill:#f392,stroke:#333,stroke-width:2px
        direction LR
        A["Initial State<br>(Low Entropy)"] --> B["Increasing Entropy Monotonically"] --> C["Final State<br>(High Entropy)"]
        B -- Second Law of Thermodynamics --> C
    end

    subgraph Complexity
    style Complexity fill:#c3c4,stroke:#333,stroke-width:2px
        direction LR
        D["Initial State<br>(Low Complexity)"] --> E["Increasing Complexity"] --> F["Peak Complexity<br>(Interesting Structures)"] --> G["Decreasing Complexity"] --> H["Final State<br>(Low Complexity)"]
        E --> F --> G -- "Complexity Curve" --> H
    end

    I["Time Evolution"]
    I --> A & D
    I --> B & E
    I --> C & H

    linkStyle 0,3,6,9  stroke-width:2px,stroke:red,color:red
    linkStyle 1,4,7,10 stroke-width:2px,stroke:blue,color:blue
    linkStyle 2,5,8,11 stroke-width:2px,stroke:green,color:green

    classDef entropy fill:#f399,stroke:#333,stroke-width:2px
    classDef complexity fill:#c3c4,stroke:#333,stroke-width:2px
    class Entropy entropy
    class Complexity complexity

    subgraph Key_Question["Key Question"]
        style Key_Question fill:#e339,stroke:#333,stroke-dasharray: 5 5
        K["Why does complexity follow this curve, unlike entropy?"]
    end
    K --> F

```

#### Explanation

*   **Entropy (Red Line):** Starts low and increases continuously over time, as dictated by the Second Law of Thermodynamics.
*   **Complexity (Blue Line):** Starts low, increases to a peak at an intermediate stage (where "interesting structures" emerge), and then decreases back to a low level in the final, equilibrium state.
*   **Key Question:** The central puzzle is to explain this non-monotonic behavior of complexity in contrast to entropy.

---

## 2. The Coffee Cup Analogy

Sean Carroll illustrated this concept with the coffee cup example, showing milk mixing into coffee over time.

### Diagram 2: Coffee Cup Complexity Evolution

```mermaid
---
title: Coffee Cup Complexity Over Time
caption: Visual representation of the coffee cup example, showing complexity peaking in the intermediate stage during mixing
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart LR
    TS1["Stage 1: Initial<br>(Ordered)"];
    TS2["Stage 2: Intermediate<br>(Complex)"];
    TS3["Stage 3: Final<br>(Mixed/Disordered)"];

    S1A["Coffee & Milk Separated"];
    S1B["Low Entropy"];
    S1C["Low Complexity"];

    S2A["Milk Tendrils Mixing"];
    S2B["Increasing Entropy"];
    S2C["High Complexity"];

    S3A["Uniform Mixture"];
    S3B["High Entropy"];
    S3C["Low Complexity"];


    subgraph Time_Stages
    style Time_Stages fill:#f3f3,stroke:#333,stroke-width:1px
        TS1 --> TS2 --> TS3
    end

    subgraph Stage_1["Stage 1: Initial<br>(Ordered)"]
    style Stage_1 fill:#f3f3,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3
        S1A --> S1B & S1C
    end

    subgraph Stage_2 ["Stage 2: Intermediate<br>(Complex)"]
    style Stage_2 fill:#f3f3,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3
        S2A --> S2B & S2C
    end

    subgraph Stage_3 ["Stage 3: Final<br>(Mixed/Disordered)"]
    style Stage_3 fill:#f3f3,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3
        S3A --> S3B & S3C
    end

    Time_Stages --> Stage_1
    Time_Stages --> Stage_2
    Time_Stages --> Stage_3

    linkStyle 0 stroke-width:2px,stroke:black
    linkStyle 1 stroke-width:2px,stroke:black
    linkStyle 2 stroke-width:2px,stroke:black 
```

#### Explanation

*   **Stage 1 (Initial):** Coffee and milk are separate - ordered, low entropy, low complexity.
*   **Stage 2 (Intermediate):** Milk starts mixing, forming intricate tendrils - increasing entropy, high complexity (visually interesting).
*   **Stage 3 (Final):** Uniform mixture of coffee and milk - high entropy, low complexity (homogeneous, less interesting).


## 3. Kolmogorov Complexity and Entropy

The blog post discusses using Kolmogorov Complexity to formalize these ideas.

### Diagram 3: Kolmogorov Complexity (KC) as Entropy?

```mermaid
---
title: Kolmogorov Complexity and Entropy Challenges
caption: Illustrates the concept of Kolmogorov Complexity and the issue of using it directly to model entropy increase in deterministic systems, highlighting possible solutions
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    KC_Def["Shortest program to output string x"];
    KC_Measure["Measures program length"];
    KC_Universal["Independent of Universal TM<br>(mostly)"];

    IA_State["System State"];
    IA_KC["KC of System State = Entropy?"];

    PD_System["Deterministic System Evolution"];
    PD_State("State at time t is determined by initial state and t");
    PD_KC("KC(State at time t) ~ log(t) + C");

    PD_Critique["KC increases only logarithmically,<br>not as expected for entropy"];

    Sol_Probabilistic["Consider Probabilistic Systems<br>(KC increases polynomially)"]
    Sol_Resource_Bounded["Resource-Bounded KC<br>(Short program within time/resource limit)"]

    subgraph Kolmogorov_Complexity["Kolmogorov Complexity<br>(KC)"]
    style Kolmogorov_Complexity fill:#e3f4,stroke:#333,stroke-width:1px
        KC_Def --> KC_Measure & KC_Universal
    end

    subgraph Initial_Attempt["Initial Attempt:<br>KC as Entropy"]
    style Initial_Attempt fill:#e3e4,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5
        IA_State --> IA_KC
    end

    Kolmogorov_Complexity --> Initial_Attempt

    subgraph Problem_Deterministic["Problem with Deterministic Systems"]
    style Problem_Deterministic fill:#f3e4,stroke:#333,stroke-width:1px
        PD_System
        PD_State --> PD_KC
        PD_KC --> PD_Critique
    end
    Initial_Attempt --> Problem_Deterministic

    subgraph Solutions
    style Solutions fill:#e3f4,stroke:#333,stroke-width:1px
        Sol_Probabilistic
        Sol_Resource_Bounded
    end
    Problem_Deterministic --> Solutions

    linkStyle 0 stroke-width:2px,stroke:blue
    linkStyle 1 stroke-width:2px,stroke:blue
    linkStyle 2 stroke-width:2px,stroke:blue
    linkStyle 3 stroke-width:2px,stroke:red
    linkStyle 4 stroke-width:2px,stroke:red
    linkStyle 5 stroke-width:2px,stroke:red
    linkStyle 6 stroke-width:2px,stroke:green
    linkStyle 7 stroke-width:2px,stroke:green
```

#### Explanation

*   **Kolmogorov Complexity (KC):** Defined as the length of the shortest program to describe a string.  It’s considered a measure of randomness and information content.
*   **Initial Thought:**  Could KC be used as a formal measure of entropy?
*   **Problem with Deterministic Systems:** In deterministic systems, the state at time `t` can be described by the initial state and `t`. This means KC only increases logarithmically with time (`log(t)`), which is too slow to represent the expected linear/polynomial increase in entropy.
*   **Solutions:**
    *   **Probabilistic Systems:** KC can increase more rapidly in probabilistic systems.
    *   **Resource-Bounded KC:**  Limit the computational resources (e.g., time) for the program. This forces program size to increase more significantly with time, better reflecting entropy.


## 4. Sophistication: Capturing "Interesting" Complexity

To capture the "interesting" complexity, the blog post introduces the concept of "sophistication."

### Diagram 4: Definition of Sophistication

```mermaid
---
title: Understanding Sophistication
caption:  Diagram explains the definition and key properties of Sophistication, a measure intended to capture "interesting" complexity.
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    Soph_Goal["Formalize 'interesting' complexity"];
    Soph_Start("Kolmogorov's Observation:<br>Random strings are high KC but not 'complex'");
    Soph_Def["Min K(S) over all sets S such that:"];
    Soph_Cond1["Condition 1:<br>x ∈ S"];
    Soph_Cond2["Condition 2:<br>K(x|S) >= log<sub>2</sub>(|S|) - c"];
    Soph_Intuit["Shortest description of a set S where x is a 'generic' member"];

    Prop_LowKC["Low for strings with low KC<br>(S={x})"];
    Prop_Random["Low for Uniformly Random Strings<br>(S={0,1}^n})"];
    Prop_High_Potential["Potentially high for 'neither simple nor random' strings"];

    subgraph Sophistication["Sophistication<br>(Soph(x))"]
    style Sophistication fill:#f5f5,stroke:#333,stroke-width:1px
        Soph_Start --> Soph_Goal
        Soph_Goal --> Soph_Def
        Soph_Def --> Soph_Cond1
        Soph_Def --> Soph_Cond2
        Soph_Cond2 --> Soph_Intuit
    end

    subgraph Properties
    style Properties fill:#e5f2,stroke:#333,stroke-width:1px
        Sophistication --> Prop_LowKC
        Sophistication --> Prop_Random
        Sophistication --> Prop_High_Potential
    end

    linkStyle 0 stroke-width:2px,stroke:blue
    linkStyle 1 stroke-width:2px,stroke:blue
    linkStyle 2 stroke-width:2px,stroke:blue
    linkStyle 3 stroke-width:2px,stroke:blue
    linkStyle 4 stroke-width:2px,stroke:blue
    linkStyle 5 stroke-width:2px,stroke:green
    linkStyle 6 stroke-width:2px,stroke:green
    linkStyle 7 stroke-width:2px,stroke:green

```

#### Explanation

*   **Sophistication (Soph(x)) Goal:** To formalize a measure of "interesting" complexity, differentiating it from simple randomness.
*   **Definition:**  Find the smallest program size `K(S)` for a set `S` that satisfies two conditions:
    1.  `x` must be a member of `S`.
    2.  The conditional Kolmogorov Complexity of `x` given `S` (`K(x|S)`) must be close to the information content expected for a random element of `S` (at least `log<sub>2</sub>(|S|) - c`). This means knowing `S` essentially captures all the "non-random" information about `x`.
*   **Intuition:** Sophistication is the length of the shortest description of a set where `x` appears to be a typical, "random" member.
*   **Properties:**
    *   Low for strings with simply describable structures (low KC).
    *   Low for uniformly random strings (describable as "random n-bit string").
    *   Potentially high for strings that are neither simple nor completely random – the "interesting" cases.


---

## 5. Resource-Bounded Complextropy: Addressing Time Evolution

Sophistication, as initially defined, still has issues when applied to systems evolving over time.  The solution proposed is **Resource-Bounded Complextropy**.

### Diagram 5: Resource-Bounded Complextropy

```mermaid
---
title: Resource-Bounded Complextropy Definition
caption: Diagram defining Resource-Bounded Complextropy and highlighting the importance of dual efficiency constraints
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    PST_Similar_Issue["Similar issue as KC with deterministic systems"];
    PST_Soph_Limited("Soph(state at time t) <= log(t) + C");
    PST_Need_Resource_Bound["Need to incorporate computational resource bounds again"];

    Comp_Def["Shortest program<br>(within resource bound,<br>e.g., n log(n) time)<br>that:"];
    Comp_Sample("Condition 1:<br>Outputs nearly-uniform sample from set S");
    Comp_Cond1("Condition 2:<br>x ∈ S");
    Comp_Cond2("Condition 3:<br>Reconstructing x efficiently from S sample is hard:<br>K_resource(x|S) >= log<sub>2</sub>(|S|) - c");
    
    KI_Eff_Sample["Efficient Sampling Algorithm"];
    KI_Eff_Reconstruct["Efficient Reconstruction Algorithm Constraint"];
    KI_Essential["Both constraints are essential for Complextropy to work as intended"];

    
    subgraph Problem_Sophistication_Time["Problem:<br>Sophistication and Time"]
    style Problem_Sophistication_Time fill:#f3e5,stroke:#333,stroke-width:1px
        PST_Soph_Limited --> PST_Similar_Issue
        PST_Similar_Issue --> PST_Need_Resource_Bound
    end

    subgraph Resource_Bounded_Complextropy["Resource-Bounded Complextropy<br>(Complextropy(x))"]
    style Resource_Bounded_Complextropy fill:#f3f5,stroke:#333,stroke-width:1px
        Comp_Def --> Comp_Sample & Comp_Cond1 & Comp_Cond2
    end
    Problem_Sophistication_Time --> Resource_Bounded_Complextropy

    subgraph Key_Innovation["Key Innovation:<br>Dual Efficiency Constraints"]
    style Key_Innovation fill:#e3f5,stroke:#333,stroke-width:1px
        Resource_Bounded_Complextropy --> KI_Eff_Sample
        Resource_Bounded_Complextropy --> KI_Eff_Reconstruct
        KI_Eff_Sample & KI_Eff_Reconstruct --> KI_Essential
    end


    linkStyle 0 stroke-width:2px,stroke:red
    linkStyle 1 stroke-width:2px,stroke:red
    linkStyle 2 stroke-width:2px,stroke:red
    linkStyle 3 stroke-width:2px,stroke:blue
    linkStyle 4 stroke-width:2px,stroke:blue
    linkStyle 5 stroke-width:2px,stroke:blue
    linkStyle 6 stroke-width:2px,stroke:green
    linkStyle 7 stroke-width:2px,stroke:green
    linkStyle 8 stroke-width:2px,stroke:green  
```

#### Explanation

*   **Problem with Sophistication over Time:** Similar to the issue with Kolmogorov Complexity and deterministic systems, sophistication alone might not capture the complexity changes in evolving systems effectively. Sophistication might also be limited by `log(t) + C`.
*   **Resource-Bounded Complextropy Definition:** Define complextropy using resource-bounded computation in two key places:
    1.  **Efficient Sampling:** The program to describe `S` must run within a given time limit (e.g., `n log(n)`). It outputs a near-uniform sample from `S`.
    2.  **Inefficient Reconstruction (given S sample):**  Any program that tries to reconstruct `x` within the same resource bound, given access to samples from `S`, must still be complex (at least  `log<sub>2</sub>(|S|) - c` bits).
*   **Dual Efficiency Constraints:**  It's crucial to have efficiency constraints on *both* the sampling algorithm (for defining S) and the reconstruction algorithm (for recovering x from S). This dual constraint is the key innovation to capture the desired "complextropy" behavior.

---



## 6. Conjecture and Proposed Experiment: "First Law of Complexodynamics"

The blog post conjectures that this Resource-Bounded Complextropy will exhibit the desired "small-large-small" behavior over time.

### Diagram 6: "First Law of Complexodynamics" Conjecture

```mermaid
---
title: Conjecture and Experiment for Complextropy
caption: Diagram outlines the core conjecture about complextropy's behavior and the proposed experiment using a discrete coffee cup simulation
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TB
    Conj_Complextropy_Behavior[Resource-Bounded Complextropy exhibits Sean's desired behavior];
    Conj_Initial(Small at initial state);
    Conj_Intermediate(Large at intermediate states);
    Conj_Final("Small at final (equilibrium) state");

    Exp_System["2D array of black/white pixels<br>(coffee/milk)"];
    Exp_Initial("Initially separated regions");
    Exp_Dynamics["Random Nearest-Neighbor Mixing<br>(swap adjacent pixels)"];
    Exp_Measure("Plot Complextropy over time");
    Exp_Expected_Outcome["Complextropy curve:<br>small -> large -> small"];

    Chal_Computation["Complextropy is likely intractable to compute exactly"];
    Chal_Approximation["Use approximations<br>(e.g., gzip compression size)"];
    Chal_Empirical_Approach["Empirical validation through simulation and plotting"];
    
    subgraph Conjecture["Conjecture:<br>'First Law of Complexodynamics'"]
    style Conjecture fill:#f3f4,stroke:#333,stroke-width:1px
        Conj_Complextropy_Behavior --> Conj_Initial & Conj_Intermediate & Conj_Final
    end

    subgraph Proposed_Experiment["Proposed Experiment:<br>Discrete 'Coffee Cup'"]
    style Proposed_Experiment fill:#e336,stroke:#333,stroke-width:1px
        Exp_System --> Exp_Initial & Exp_Dynamics
        Exp_Dynamics --> Exp_Measure
        Exp_Measure --> Exp_Expected_Outcome
    end
    Conjecture --> Proposed_Experiment

    subgraph Challenges
    style Challenges fill:#f3e4,stroke:#333,stroke-width:1px
        Proposed_Experiment --> Chal_Computation
        Chal_Computation --> Chal_Approximation
        Chal_Approximation --> Chal_Empirical_Approach

    end

    linkStyle 0 stroke-width:2px,stroke:blue
    linkStyle 1 stroke-width:2px,stroke:blue
    linkStyle 2 stroke-width:2px,stroke:blue
    linkStyle 3 stroke-width:2px,stroke:green
    linkStyle 4 stroke-width:2px,stroke:green
    linkStyle 5 stroke-width:2px,stroke:green
    linkStyle 6 stroke-width:2px,stroke:red
    linkStyle 7 stroke-width:2px,stroke:red
    linkStyle 8 stroke-width:2px,stroke:red
    
```


#### Explanation

*   **Conjecture:**  Resource-Bounded Complextropy is conjectured to behave as Sean Carroll described for complexity – low initially, high at intermediate stages, and low again in equilibrium. This is termed the "First Law of Complexodynamics."
*   **Proposed Experiment: Discrete Coffee Cup:** Simulate a 2D grid representing coffee and milk. Start with separated regions and apply random mixing over time.
*   **Expected Outcome:** Plot the complextropy (or an approximation like gzip compression size) over time.  Expect to see the "small-large-small" curve, supporting the conjecture.
*   **Challenges:**
    *   Complextropy is likely computationally intractable.
    *   Use approximations (like gzip compression) as a practical substitute for empirical investigation.
    *   Focus on empirical validation by plotting the approximate complextropy in simulations.

---

## 7. Summary Diagram: The Flow of Ideas

### Diagram 7:  Overall Conceptual Flow

```mermaid
---
title: Conceptual Flow of Ideas in the Blog Post
caption:  A high-level diagram summarizing the logical progression of ideas presented in Scott Aaronson's blog post
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TB
    Start[Sean Carroll's Question: Complexity vs. Entropy] --> Paradox[Paradox: Entropy Monotonic, Complexity Not]
    Paradox --> CoffeeCup[Coffee Cup Example]
    CoffeeCup --> KC_Entropy[Kolmogorov Complexity to define Entropy?]
    KC_Entropy --> Problem_KC[Problem: KC too slow for Deterministic Entropy]
    Problem_KC --> ResourceBoundKC[Resource-Bounded KC for Entropy]
    ResourceBoundKC --> Sophistication["Sophistication for 'Interesting' Complexity"]
    Sophistication --> Problem_Soph[Problem: Sophistication and Time Evolution]
    Problem_Soph --> Complextropy[Resource-Bounded Complextropy proposed]
    Complextropy --> Conjecture_Law["'First Law of Complexodynamics' Conjecture"]
    Conjecture_Law --> Experiment[Proposed Experiment: Discrete Coffee Cup]
    Experiment --> Expected_Result[Expected 'Small-Large-Small' Complextropy Curve]
    Expected_Result --> Open_Problem[Open Problem: Rigorous Proof & Further Research]

    style Start fill:#a3c3,stroke:#333,stroke-width:2px
    style Paradox fill:#f33b,stroke:#333,stroke-width:2px
    style CoffeeCup fill:#dd3fd,stroke:#333,stroke-width:2px
    style KC_Entropy fill:#d449,stroke:#333,stroke-width:2px
    style Problem_KC fill:#f31e,stroke:#333,stroke-width:2px
    style ResourceBoundKC fill:#d3ef,stroke:#333,stroke-width:2px
    style Sophistication fill:#d3d2,stroke:#333,stroke-width:2px
    style Problem_Soph fill:#f325,stroke:#333,stroke-width:2px
    style Complextropy fill:#d3d,stroke:#333,stroke-width:2px
    style Conjecture_Law fill:#a3aa,stroke:#333,stroke-width:2px
    style Experiment fill:#d3e3,stroke:#333,stroke-width:2px
    style Expected_Result fill:#a2fa,stroke:#333,stroke-width:2px
     style Open_Problem fill:#ff29d,stroke:#333,stroke-width:2px

```

#### Explanation

*   This diagram provides a bird's-eye view of the entire blog post's argument, showing the logical flow and connections between different concepts.
*   It starts with the initial question, moves through the challenges and proposed solutions, and ends with the conjecture and open problems.


---



**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---