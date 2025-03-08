---
created: 2025-03-07 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "DOI: １０．１１８９７／ＳＰ．Ｊ．１０１６．２０２４．０１０３０"
---



# Quantum Annealing Public Key Cryptographic Attack Algorithm Based on D-Wave Advantage
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## A Diagrammatic Guide 


Here's the Mermaid syntax for creating diagrams based on the conceptual structure outlined in the previous response. I've focused on providing a variety of diagram types to represent the different aspects of the research.

### 1. Overall Strategy Diagram (Combined Approaches)

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    "graph": { "htmlLabels": false, 'curve': 'linear' },
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
    A["Public-Key Cryptography Attack"] --> B{"Two Main Approaches"}
    style A fill:#a3a,stroke:#333,stroke-width:1px

    subgraph Approach_1["Pure Quantum<br>(D-Wave)"]
    style Approach_1 fill:#f2b2,stroke:#333,stroke-width:1px
        B --> C["Ising/QUBO Formulation"]
        C --> C1["High-Level Optimization Model"]
        C1 --> C2["Dimensionality Reduction"]
        C2 --> C3["Reduces Qubit Resources"]
        C --> C4["D-Wave Advantage"]
        C4 --> C5["Experimental Factorization<br>(22-bit)"]
    end

    subgraph Approach_2["Quantum-Classical Hybrid"]
    style Approach_2 fill:#a2fa,stroke:#333,stroke-width:1px
        B --> D["Lattice Reduction<br>(LLL + Babai)"]
        D --> D1["Approximate CVP Solution"]
        D1 --> E["Quantum Annealing Optimization"]
        E --> E1["Improved CVP Solution"]
        E1 --> E2["Factorized Integer<br>(50-bit)"]
    end

    B --> F["Evaluation of D-Wave's Potential"]
    F --> G["Avoids Barren Plateaus"]
    F --> H["Promising Attack Capability"]
    
```


**Explanation:**

*   Shows the two main approaches in parallel.
*   Highlights the key steps within each approach.
*   Emphasizes D-Wave's role and the final result (factorization).

---

### 2. Approach 1: Pure Quantum (D-Wave) Details

```mermaid
---
title: "Approach 1: Pure Quantum (D-Wave) Details"
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
    "graph": { "htmlLabels": false, 'curve': 'linear' },
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
    A["RSA Factorization"] --> B{"Mathematical Transformation"}
    style A fill:#a3ae,stroke:#333,stroke-width:1px
    B --> C["Ising/QUBO Model"]
    C --> D["D-Wave Advantage"]
    D --> E["Factorized Integer<br>(22-bit)"]
    
    subgraph Model_Optimization["Model Optimization"]
    style Model_Optimization fill:#f2aa,stroke:#333,stroke-width:1px
        E --> F["High-Level Optimization"]
        F --> G["Dimensionality Reduction"]
        G --> H["Coefficient Range Reduction"]
        H --> I["Improved Stability"]
    end
```

**Explanation:**

*   Focuses on the steps specific to the pure quantum approach.
*   Shows the transformation and optimization process.

---

### 3. Approach 2: Quantum-Classical Hybrid Details

```mermaid
---
title: "Approach 2: Quantum-Classical Hybrid Details"
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
    "graph": { "htmlLabels": false, 'curve': 'linear' },
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
    A["RSA Factorization"] --> B{"Classical Lattice Reduction<br>(LLL + Babai)"}
    style A fill:#a3ae,stroke:#333,stroke-width:1px
    B --> C["Approximate CVP Solution"]
    C --> D["Quantum Annealing Optimization"]
    D --> E["Improved CVP Solution"]
    E --> F["Factorized Integer<br>(50-bit)"]
    
    subgraph CVP_Improvement["CVP Improvement"]
    style CVP_Improvement fill:#a2fa,stroke:#333,stroke-width:1px;
        E --> G["Better Approximation of Target Vector"]
        G --> H["Enhanced Smooth Pair Search"]
    end
    
```

**Explanation:**

*   Details the steps involved in the hybrid approach.
*   Emphasizes the use of quantum annealing for CVP optimization.

---


### 4. Process Flowchart: Quantum Annealing Algorithm

```mermaid
---
title: "Process Flowchart: Quantum Annealing Algorithm"
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
    "graph": { "htmlLabels": false, 'curve': 'linear' },
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
    A["Start with Initial State"]
    B{"Apply Transverse Magnetic Field"}
    C{"Slowly Reduce Transverse Field"}
    D{"Increase Interaction Strength"}
    E{"System Evolves to Ground State"}
    F{"Read Qubit States"}
    G["Solution<br>(Factorization)"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    
```

**Explanation:**

*   A high-level view of the quantum annealing process.
*   Suitable for illustrating the core principle of quantum annealing.

----


### 5. Key Limitations (Caveats)

```mermaid
---
title: "Key Limitations (Caveats)"
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
    "graph": { "htmlLabels": false, 'curve': 'linear' },
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
    A["Limitations of Quantum Annealing"] --> B{"Parameter Sensitivity"}
    style A fill:#a3ae,stroke:#333,stroke-width:1px
    B --> C[Schedule, Initial State]
    A --> D{Low Temperature Requirements}
    D --> E[Requires Cryogenic Environment]
    A --> F{Hardware Constraints}
    F --> G[Coefficient Range of Ising Model]
```

**Explanation:**

*   Highlights the challenges associated with quantum annealing.

----


### 6. Comparison Table (Simplified - for illustration, adapt with actual data)

```mermaid
---
title: "Comparison Table (Simplified - for illustration, adapt with actual data)"
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
    "graph": { "htmlLabels": false, 'curve': 'linear' },
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
    A["Comparison of Approaches"] --> B{"Criteria"}
    style A fill:#a3ae,stroke:#333,stroke-width:1px
    
    B --> C["Qubit Count"]
    B --> D["Coefficient Range"]
    B --> E["Factorization Size"]
    B --> F["Stability"]

    subgraph Approach_1["Approach 1"]
    style Approach_1 fill:#f2b3,stroke:#333,stroke-width:1px
        C --> C1[Lower]
        D --> D1[High Optimization Required]
        E --> E1["Smaller<br>(e.g., 22-bit)"]
    end
    subgraph Approach_2["Approach 2"]
     style Approach_2 fill:#a2fa,stroke:#333,stroke-width:1px
        C --> C2["Higher<br>(Potential)"]
        D --> D2["Less Stringent"]
        E --> E2["Larger<br>(e.g., 50-bit)"]
    end
    
```

**Explanation:**

*   Provides a structured comparison of the two approaches.
*   Use actual numerical data from the paper to populate the table.


----

### Important Considerations

*   **Translations:** Ensure accurate translations of technical terms from Chinese to English.
*   **Data:** Replace the placeholder information with the *actual* data from the original research paper.
*   **Level of Detail:** Adapt the level of detail in each diagram to suit your specific needs.
*   **Context:** Use captions and annotations to provide context for each diagram.



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---