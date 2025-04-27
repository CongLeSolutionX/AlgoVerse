---
created: 2025-04-26 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# The Journey Recap - A Diagrammatic Guide
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


## 1. Overall Problem-Solving Progression

This flowchart shows the journey from initial attempts to the final successful strategy.

```mermaid
---
title: "Overall Problem-Solving Progression"
config:
  layout: elk
  look: handDrawn
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
    'themeVariables': {
      'primaryColor': '#BB28',
      'primaryTextColor': '#000',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
flowchart TD
    A["Start:<br/>Missing Mail Problem Defined"] --> B{"Attempt 1:<br/>Simple Greedy"}
    B -- Fail --> C{"Why?<br/>Ignores Risk (S) & Future Value"}
    C --> D{"Attempt 2:<br/> C/S Threshold Greedy"}
    D -- "Partial Success<br/>(e.g., 8/24)" --> E{"Why Limited?<br/>Local Optimum Trap"}
    E -- "Sample Case #4 Analysis" --> F{"Insight:<br/>Need Future Value Modeling"}
    F --> G{"Attempt 3:<br/>DP Conceptualization"}
    G --> H["State:<br/> f(i, E) = Max Profit from day i with value E"]
    G --> I["Challenge:<br/> Continuous State 'E' makes direct tabulation/memoization hard"]
    I --> J{"Attempt 4:<br/> DP - Backward Threshold Calculation"}
    J --> K["Key Idea:<br/> Calculate optimal decision threshold T[i] backward"]
    K --> L["Method:<br/> Binary Search + Future Profit Simulation Helper"]
    J --> M["Complexity:<br/> O(N^2 log(Range))"]
    M --> N[/"Success! Solved All Cases"/]

    style N fill:#9f9,stroke:#333,stroke-width:2px
    
```

---


## 2. Approach 2: C/S Threshold Greedy Logic

This flowchart details the decision process within the `C/S` threshold strategy.

```mermaid
---
title: "Approach 2: C/S Threshold Greedy Logic"
config:
  layout: elk
  look: handDrawn
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
    'themeVariables': {
      'primaryColor': '#BB28',
      'primaryTextColor': '#000',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
flowchart TD
    subgraph C_S_Threshold_Logic["C/S Threshold Logic"]
        A["Start Day i"] --> B["Current Expected Value:<br/> 'E'"]
        B --> C["Package Arrives:<br/> 'V[i]'"]
        C --> D["Calculate Potential:<br/> 'P = E + V[i]'"]
        D --> E{"Handle S=0?"}
            E -- Yes --> F["Threshold T = Infinity<br/>(Effectively never collect based on S)"]
            E -- No --> G["Calculate Threshold:<br/> 'T = C / S'"]
        F --> H{"Decision"}
        G --> H
        H -- "'P >= T - ε' AND 'P > C + ε'" --> I["Collect"]
        H -- Otherwise --> J["Don't Collect"]
        I --> K["Profit += P - C"]
        I --> L["E_next = 0"]
        J --> M["E_next = (1 - S) * P"]
        K --> N["End Day i"]
        L --> N
        M --> N
    end
    
    Note["Note:<br/>Fails because T only considers immediate loss avoidance (S*P vs C),<br/>not the lost potential of (1-S)*P for future days."] --> C_S_Threshold_Logic

```

---


## 3. Approach 4: DP - Backward Threshold Calculation Algorithm

This describes the core loop of the successful backward calculation.

```mermaid
---
title: "Approach 4: DP - Backward Threshold Calculation Algorithm"
config:
  layout: elk
  look: handDrawn
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
    'themeVariables': {
      'primaryColor': '#BB28',
      'primaryTextColor': '#000',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
flowchart TD
    A["Start Backward Pass:<br/>i = N-1 down to 0"] --> B["Get Future Thresholds 'T[i+1...N-1]'"]
    B --> C["Calculate 'f0_next = calculateFutureProfit(i+1, 0, T_future)'"]
    C --> D["Define 'Balance(v) = ((v-C) + f0_next) - calculateFutureProfit(i+1, (1-S)v, T_future)'"]
    D --> E{"Binary Search for 'v'"}
        subgraph BinarySearch["Find smallest v where Balance(v) >= 0"]
            direction TB
            E1["Init lowV=C, highV=Large"] --> E2["Loop 100 times"]
            E2 --> E3["midV = lowV + (highV-lowV)/2"]
            E3 --> E4["Evaluate 'Balance(midV)'"]
            E4 --> E5{"Balance >= 0?"}
            E5 -- Yes --> E6["Threshold <= midV,<br/> highV = midV"]
            E5 -- No --> E7["Threshold > midV,<br/> lowV = midV"]
            E6 --> E8["End Loop Iteration"]
            E7 --> E8
            E8 --> E2
        end
        
    E --> F["Result:<br/> 'v = highV'<br/>(converged threshold)"]
    F --> G["Store Optimal Threshold:<br/> 'thresholds[i] = v'"]
    G --> H{"i > 0?"}
    H -- Yes --> A
    H -- No --> I["End Backward Pass:<br/> All T[i] computed"]
    
```

----


## 4. Approach 4: Helper - `calculateFutureProfit` Simulation

This illustrates the logic inside the helper function used during the backward pass.

```mermaid
---
title: "Approach 4: Helper - `calculateFutureProfit` Simulation"
config:
  layout: elk
  look: handDrawn
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
    'themeVariables': {
      'primaryColor': '#BB28',
      'primaryTextColor': '#000',
      'primaryBorderColor': '#7c2',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%
flowchart TD
    subgraph CalculateFutureProfit["Func:<br/> calculateFutureProfit(startDay, startE, T_computed)"]
        A["Init:<br/> currentE = startE, profit = 0"] --> B{"Loop:<br/> day = startDay to N-1"}
        B --> C["Potential 'P = currentE + V[day]'"]
        C --> D["Lookup 'threshold = T_computed[day]'"]
        D --> E{"'P >= threshold - ε' AND 'P > C + ε'?"}
        E -- Yes --> F["Collect"]
        E -- No --> G["Don't Collect"]
        F --> H["profit += P - C"]
        F --> I["currentE = 0"]
        G --> J["currentE = (1 - S) * P"]
        H --> K{"End day loop"}
        I --> K
        J --> K
        K --> B
        B -- Loop Complete --> L["Final Check:<br/> profit += max(0, currentE - C)"]
        L --> M["Return total accumulated profit"]
    end
```

---


## 5. Approach 4: Final Forward Pass

This flowchart shows the final step using the computed thresholds.

```mermaid
---
title: "Approach 4: Final Forward Pass"
author: "Cong Le"
version: "1.0"
license(s): "MIT, CC BY 4.0"
copyright: "Copyright (c) 2025 Cong Le. All Rights Reserved."
config:
  look: handDrawn
  theme: base
---
%%%%%%%% Mermaid version v11.4.1-b.14
%%%%%%%% Toggle theme value to `base` to activate the initilization below for the customized theme version.
%%%%%%%% Available curve styles include the following keywords:
%% basis, bumpX, bumpY, cardinal, catmullRom, linear, monotoneX, monotoneY, natural, step, stepAfter, stepBefore.
%%{
  init: {
    'flowchart': {'htmlLabels': true, 'curve': 'basis' },
    'fontFamily': 'Monospace',
    'themeVariables': {
      'lineColor': '#F8B229'
    }
  }
}%%
flowchart TD
    A["Start Forward Pass:<br/>i = 0 to N-1"] --> B["Load All Computed 'thresholds[0...N-1]'"]
    B --> C["Init:<br/> 'totalProfit = 0', 'currentE = 0'"]
    C --> D{"Loop Day 'i'"}
    D --> E["Potential 'P = currentE + V[i]'"]
    E --> F["Lookup 'T = thresholds[i]'"]
    F --> G{"'P >= T - ε' AND 'P > C + ε'?"}
    G -- Yes --> H["Collect:<br/> 'totalProfit += P - C', 'currentE = 0'"]
    G -- No --> I["Don't Collect:<br/> 'currentE = (1 - S) * P'"]
    H --> J{"End Day 'i' Loop"}
    I --> J
    J --> D
    D -- Loop Complete --> K["Final 'totalProfit' is Max Expected Profit"]
    K --> L[End]


```

These diagrams visually map out the different stages and logic flows we explored. They should serve as a helpful reference for understanding how we navigated the complexities of the "Missing Mail" problem!


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---