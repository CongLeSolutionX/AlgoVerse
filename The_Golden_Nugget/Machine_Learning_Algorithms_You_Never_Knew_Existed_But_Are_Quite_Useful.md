---
created: 2025-02-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original_source: "https://medium.com/pythoneers/machine-learning-algorithms-you-never-knew-existed-but-are-quite-useful-2bb083401c51?"
---



# Machine Learning Algorithms You Never Knew Existed, But Are Quite Useful
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---



The diagrams below aim to provide clearer visual intuition for the core ideas behind each algorithm discussed in the article.


---

## 1. Symbolic Regression (Genetic Programming Core)

Symbolic Regression uses genetic programming to *discover* the underlying mathematical expression. This diagram illustrates the iterative evolutionary process.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
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
flowchart TD
    A["Start:<br/>Initialize Population of Random Expressions"] --> B{"Evaluate Fitness<br/>(How well expressions fit data?)"}
    B --> C{"Stopping Criteria Met?<br/>(e.g., good fit, max generations)"}
    C -- No --> D["Selection<br/>(Choose fitter expressions)"]
    D --> E["Genetic Operations"]
    
    subgraph Genetic Operations
        direction LR
        E1["Crossover<br/>(Combine parts of expressions)"]
        E2["Mutation<br/>(Randomly change parts of expressions)"]
    end
    E --> F["Create New Generation of Expressions"]
    F --> B
    C -- Yes --> G["Output: Best Discovered Expression"]
    
```

**Explanation:** The algorithm starts with random mathematical expressions. It iteratively evaluates them, selects the best ones, and applies genetic operations (like combining parts of different expressions or randomly changing them) to create a new generation, mimicking natural selection until a satisfactory expression is found.

-----

## 2. Isolation Forest (Anomaly Detection Mechanism)

Isolation Forests identify outliers by how easily they can be separated from the rest of the data. Outliers require fewer random partitions to be isolated.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'fontFamily': 'Monospace',
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
    subgraph Data_Space["Data Space"]
        direction LR
        N1(Normal Point)
        N2(Normal Point)
        O1(Outlier) -- Easily Isolated --> P1["Shallow Path in Tree"]
        N1 -- Harder to Isolate --> P2["Deeper Path in Tree"]
        N2 -- Harder to Isolate --> P2
    end

    subgraph Isolation_Tree_Building["Isolation Tree Building"]
        %% direction TD
        R["Root Node<br/>(Full Dataset)"] --> S1{"Randomly Select Feature & Split Value"}
        S1 --> L1["Left Partition"] & R1["Right Partition"]
        L1 --> S2{"Random Feature/Split"}
        R1 --> S3{"Random Feature/Split"}
        S2 --> ...
        S3 --> ...

        EndCondition["Stop when node has 1 point or max depth reached"]
        S2 --> EndCondition
        S3 --> EndCondition
    end

    O1 --> R
    N1 --> R
    N2 --> R

    P1 & P2 --> Decision{"Average Path Length Across Forest"}
    Decision --> Result["Shorter Average Path => Anomaly"]

```

**Explanation:** The algorithm builds multiple trees. In each tree, data is randomly partitioned. Outliers, being far from dense regions, tend to be isolated in fewer steps (shallower paths). Averaging path lengths across many trees identifies anomalies.

----

## 3. Tsetlin Machine (Conceptual Learning Loop)

Tsetlin Machines use Tsetlin Automata (TA) and propositional logic. They learn through a reward/penalty system applied to the states of the TAs based on the correctness of their contribution to the overall prediction.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
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

flowchart TD
    A["Input Features<br/>(Booleanized)"] --> B["Tsetlin Automata<br/>(TAs)"]
    B --> C["Form Clauses<br/>(Conjunctions of TA Literals)"]
    C --> D{"Clause Voting & Summation"}
    D --> E["Output Prediction<br/>(e.g., based on sum threshold)"]
    E --> F{"Compare Prediction to True Label"}
    F -- Correct --> G["Reward Contributing TAs<br/>(Strengthen states)"]
    F -- Incorrect --> H["Penalize Contributing TAs<br/>(Weaken states)"]
    G --> I["Update TA States"]
    H --> I
    I --> B
    
```

**Explanation:** Boolean inputs activate Tsetlin Automata. These form logical clauses that vote on the output. Based on whether the prediction is correct or incorrect, the states within the TAs that formed the active clauses are reinforced or weakened, refining the logical patterns over time.

----

## 4. Random Kitchen Sinks (Kernel Approximation)

RKS approximates complex kernel functions (like those in SVMs) by mapping data to a higher-dimensional space using random Fourier features, allowing a *linear* model in that new space to mimic the *non-linear* behavior of the kernel.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'fontFamily': 'Monospace',
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
    A["Input Data (Low-Dim, X)"] -- "Non-Linear Kernel Function (e.g., RBF)" --> B("Implicit High-Dim Feature Space")
    B -- "Kernel Method<br/>(e.g., SVM)" --> C["Non-Linear Decision Boundary"]

    A -- RKS Transformation --> D["Random Fourier Features Projection"]
    D --> E("Explicit Approx. High-Dim Space, Z")
    E -- "Linear Model<br/>(e.g., Linear SVM)" --> F["Approx. Non-Linear Decision Boundary"]

    style A fill:#f9f3,stroke:#333,stroke-width:2px
    style E fill:#ccf3,stroke:#333,stroke-width:2px
    style C fill:#9cf3,stroke:#333,stroke-width:2px
    style F fill:#9cf3,stroke:#333,stroke-width:2px

    G[Expensive Computation]:::note --- B
    H[Efficient Computation]:::note --- E

    classDef note fill:#eee3,stroke:#ccc
    
```


**Explanation:** Instead of the computationally expensive step of working implicitly in a high-dimensional space via a kernel function (A->B->C), RKS explicitly maps the data to a (different but related) high-dimensional space using random functions (A->D->E). A simple linear model in this new space (E->F) can then approximate the original non-linear decision boundary, but much more efficiently.

----

## 5. Bayesian Optimization (Iterative Search Process)

Bayesian Optimization intelligently searches for the best parameters of an expensive function by building a probabilistic model of it and using an acquisition function to decide where to sample next.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
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
flowchart TD
    A["Start:<br/>Define Objective Function & Parameter Bounds"] --> B["Initial Samples<br/>(Random or Grid)"]
    B --> C{"Evaluate Objective Function at Sampled Points"}
    C --> D["Build Probabilistic Model (e.g., Gaussian Process) of Objective Function"]
    D --> E["Use Acquisition Function (e.g., Expected Improvement) to Find Most Promising Next Sample Point"]
    E --> F{"Evaluate Objective Function at New Point"}
    F --> G["Update Probabilistic Model with New Data Point"]
    G --> H{"Stopping Criteria Met?<br/>(e.g., max iterations, convergence)"}
    H -- No --> E
    H -- Yes --> I[Output: Best Parameters Found]
```

**Explanation:** The process starts with a few initial guesses. It builds a statistical model (surrogate) of the function being optimized. An acquisition function then uses this model to balance exploring uncertain regions and exploiting promising regions, guiding the selection of the next point to evaluate. This cycle repeats until a stopping condition is met.

----

## 6. Hopfield Networks (Pattern Storage and Retrieval)

Hopfield Networks act as associative memory, storing patterns and retrieving the closest stored pattern when presented with a noisy or incomplete version.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
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
flowchart TD
    subgraph Storage_Phase["Storage Phase"]
        P1["Pattern 1<br/>(Binary Vector)"] --> S{"Calculate Weight Matrix<br/>(Hebbian Rule or similar)"}
        P2["Pattern 2<br/>(Binary Vector)"] --> S
        P3[...] --> S
    end

    subgraph Retrieval_Phase["Retrieval Phase"]
        I["Input<br/>(Noisy/Incomplete Pattern)"] --> R{"Initialize Network State with Input"}
        R --> U{"Iteratively Update Neuron States"}
        U -- "Update Rule<br/>(Based on Weights & Other Neuron States)" --> U
        U --> C{"Check for Convergence<br/>(State Stabilizes)"}
        C -- No --> U
        C -- Yes --> O["Output:<br/>Stable State<br/>(Closest Stored Pattern)"]
    end

    S --> R
    
```

**Explanation:** During storage, patterns are encoded into the network's weight matrix. During retrieval, an input pattern sets the initial state. Neurons then update their states based on the weights and the states of other neurons asynchronously or synchronously until the network converges to a stable state, which ideally corresponds to one of the stored patterns.

----

## 7. Self-Organizing Maps (SOM) (Competitive Learning & Topology Preservation)

SOMs map high-dimensional data onto a low-dimensional grid, preserving the topological relationships of the input data through competitive learning and neighborhood updates.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'flowchart': { 'htmlLabels': false, 'curve': 'linear' },
    'fontFamily': 'Monospace',
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
flowchart TD
    A["Initialize Map Grid<br/>(Neurons with Random Weight Vectors)"] --> B["Select Input Data Vector"]
    B --> C{"Find Best Matching Unit (BMU) - Neuron with Closest Weight Vector (Competition)"}
    C --> D{"Update Weight Vector of BMU and its Neighbors"}
    
    subgraph Update_Rule["Update Rule"]
        direction LR
        U1["BMU update:<br/>Move weights closer to input vector"]
        U2["Neighbor update:<br/>Move weights closer, less strongly with distance"]
        U3["Neighborhood size may shrink over time"]
    end
    D --> E{"Repeat with Next Input Vector"}
    E --> B
    Finished["Training Complete"] --> F["Result:<br/>Low-Dim Map reflecting Input Data Topology"]
    E -- Max Iterations Reached --> Finished
    
```

**Explanation:** For each input data point, the neuron on the map grid whose weights are most similar (the BMU) is found. The BMU's weights are adjusted to be even closer to the input. Crucially, the weights of neurons *near* the BMU on the grid are also adjusted similarly (but less strongly), ensuring that similar inputs map to nearby locations on the grid, thus preserving the data's structure.

----

## 8. Field-Aware Factorization Machines (FFM) vs. Factorization Machines (FM)

FFMs extend FMs by making the latent vectors used for feature interactions *field-aware*, allowing for more nuanced modeling, especially with categorical data grouped into fields.

```mermaid
graph TD
    subgraph FM["Factorization Machine"]
        direction LR
        F1["Feature i<br/>(e.g., User U1)"] --> V_i[("Latent Vector V_i")]
        F2["Feature j<br/>(e.g., Item I1)"] --> V_j[("Latent Vector V_j")]
        Interaction_FM(("Interaction i, j")) ~~~ V_i
        Interaction_FM ~~~ V_j
        Calc_FM["Calculate: <V_i, V_j>"]
        Interaction_FM --> Calc_FM
    end

    subgraph FFM["Field-Aware Factorization Machine"]
        direction LR
        FF1["Feature i<br/>(User U1, Field: User)"] --> V_i_fItem[("Latent Vector V_i for Field Item")]
        FF2["Feature j<br/>(Item I1, Field: Item")] --> V_j_fUser[("Latent Vector V_j for Field User")]
        Interaction_FFM(("Interaction i, j")) ~~~ V_i_fItem
        Interaction_FFM ~~~ V_j_fUser
        Calc_FFM["Calculate: <V_i_fItem, V_j_fUser>"]
        Interaction_FFM --> Calc_FFM
    end

    %% Note1["Feature 'i' has ONE vector V_i used for interactions with ALL other features j."]:::fmNote -- F1
    %% Note2["Feature 'i' has MULTIPLE vectors, one for interacting with each field (e.g., V_i_fItem for interacting with Item field features)."]:::ffmNote -- FF1

    %% classDef fmNote fill:#fdd3,stroke:#f00
    %% classDef ffmNote fill:#dfd3,stroke:#0f0
    
```


**Explanation:** In FMs, each feature has *one* latent vector used for all its interactions. In FFMs, features are grouped into 'fields' (e.g., User, Item, Publisher). A feature `i` has *multiple* latent vectors, one specific to interacting with features from each other field `f`. When feature `i` (from field `f_i`) interacts with feature `j` (from field `f_j`), FFM uses `i`'s vector specific to field `f_j` and `j`'s vector specific to field `f_i`.

----

## 9. Conditional Random Fields (CRF) (Structured Prediction for Sequences)

CRFs model the probability of a label sequence given an observation sequence, explicitly considering dependencies between adjacent labels, making them strong for tasks like Named Entity Recognition or Part-of-Speech tagging.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'fontFamily': 'Monospace',
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
    subgraph Observation_Sequence_Input["Observation Sequence<br/>(Input)"]
        X1[Word 1] --> X2[Word 2] --> X3[Word 3] --> X4[...]
    end

    subgraph Label_Sequence["Label Sequence<br/>(Output - Predicted Structure)"]
        Y1[Label 1] --> Y2[Label 2] --> Y3[Label 3] --> Y4[...]
    end

    subgraph Dependencies["Dependencies<br/>(P(Y|X))"]
        X1 --> Y1
        X2 --> Y2
        X3 --> Y3
        X4 --> Y4

        Y1 --> Y2
        Y2 --> Y3
        Y3 --> Y4

        X_Seq[Entire X Sequence] --> Y1
        X_Seq --> Y2
        X_Seq --> Y3
        X_Seq --> Y4
    end

    style Y1 fill:#ccf3,stroke:#333,stroke-width:2px
    style Y2 fill:#ccf3,stroke:#333,stroke-width:2px
    style Y3 fill:#ccf3,stroke:#333,stroke-width:2px
    style Y4 fill:#ccf3,stroke:#333,stroke-width:2px

    %% Note ["Label Y_i depends on:"\n " - Corresponding observation X_i"\n " - Previous Label Y_{i-1}"\n " - Potentially the entire X sequence"]:::crfNote
    %% Note --- Dependencies

    %% classDef crfNote fill:#eee,stroke:#999,max-width:250px
```

**Explanation:** Unlike models predicting each label independently, CRFs model the probability of the entire label sequence `Y` given the input sequence `X`. The prediction for label `Y_i` considers not only the corresponding input `X_i` (and potentially the whole input sequence) but also the *previously predicted label* `Y_{i-1}`, capturing the sequential structure.

---

## 10. Extreme Learning Machines (ELM) (Training Process)

ELMs simplify feedforward neural network training by fixing the input-to-hidden layer weights randomly and only learning the hidden-to-output layer weights, typically via a fast linear solver.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'fontFamily': 'Monospace',
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
    A["Input Layer (X)"] --> B("Hidden Layer")
    B -- "W_out<br/>(Learned)" --> C["Output Layer<br/>(Y)"]

    subgraph Weight Setting
        R["Random Initialization"] --> W_in(("Input->Hidden Weights W_in"))
        W_in -- Fixed --> B
        LS["Linear Solver<br/>(e.g., Moore-Penrose Pseudoinverse)"] --> W_out(("Hidden->Output Weights W_out"))
        H["Hidden Layer Activation H = g(X * W_in)"] --> LS
        T[Target Output T] --> LS
        LS -- "Solves H * W_out = T" --> W_out
    end

    A -- "W_in<br/>(Random & Fixed)" --> B

    style W_in fill:#f99,stroke:#f00,stroke-width:2px
    style W_out fill:#9f9,stroke:#0f0,stroke-width:2px

    %%Note["NO Backpropagation.<br/>Hidden weights (W_in) are set randomly ONCE and FIXED.<br/>Only Output weights (W_out) are learned, often analytically."]:::elmNote
    %%Note -- Weight Setting

    %% classDef elmNote fill:#eef3,stroke:#99f
    
```


**Explanation:** Data flows from input to hidden layer using randomly assigned and then *fixed* weights (`W_in`). The activations of the hidden layer (`H`) are calculated. The only part that is "learned" are the weights from the hidden layer to the output layer (`W_out`). This is often solved directly using linear algebra (finding `W_out` such that `H * W_out` approximates the target `T`), avoiding iterative backpropagation.

----

## Bonus: Variational Autoencoder (VAE) (Generative Process)

VAEs learn a probabilistic latent space. The encoder maps input data to parameters (mean μ, variance σ) of a distribution, and the decoder generates data from samples drawn from this distribution.

```mermaid
---
title: "CHANGE_ME_DADDY"
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
    'fontFamily': 'Monospace',
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
    subgraph Encoder["Encoder<br/>(q(z|x))"]
        direction LR
        X[Input Data] --> EncNN{"Encoder NN"}
        EncNN --> Mu[Mean μ]
        EncNN --> Sigma["Log-Variance log(σ²)"]
    end

    subgraph Latent_Space_and_Sampling["Latent Space & Sampling"]
        Mu --> Sample{"Sample z"}
        Sigma --> Sample
        Noise["ε ~ N(0, I)"] --> Sample
        Calc["z = μ + σ * ε"] --> Sample
        Sample --> Z["Latent Vector z"]
    end

    subgraph Decoder["Decoder<br/>(p(x|z))"]
        direction LR
        Z --> DecNN{Decoder NN}
        DecNN --> X_hat["Reconstructed/Generated Data"]
    end

    subgraph Training_Objective["Training Objective"]
        direction TB
        L_recon["Reconstruction Loss<br/>(e.g., MSE(X, X_hat))"]
        L_KL["KL Divergence D_KL(q(z|x) || p(z))"]
        NoteKL["Regularizer:<br/>Keeps latent space close to prior p(z), often N(0,I)"]
        L_KL --> NoteKL
        TotalLoss["Total Loss = L_recon + L_KL"]
        L_recon --> TotalLoss
        L_KL --> TotalLoss
    end

    X_hat --> L_recon
    Mu --> L_KL
    Sigma --> L_KL

    style Z fill:#ccf3,stroke:#333,stroke-width:2px
    
```


**Explanation:** An input `X` is encoded not to a single point, but to the parameters (mean `μ`, log-variance `log(σ²)`) of a probability distribution in the latent space. A latent vector `z` is then *sampled* from this distribution (specifically, from N(μ, σ²)). This sampled `z` is fed into the decoder network to generate an output `X_hat`. The training optimizes both reconstructing the input (Reconstruction Loss) and keeping the learned distributions close to a standard normal distribution (KL Divergence). This probabilistic sampling allows VAEs to generate novel data similar to the training set.





---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---