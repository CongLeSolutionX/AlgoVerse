---
created: 2025-03-22 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://doi.org/10.1007/978-3-662-70107-2"
---


# Graduate Texts in Mathematics - Graph Theory
> **Disclaimer:**
>
> This document contains my personal notes on the topic,
> compiled from publicly available documentation and various cited sources.
> The materials are intended for educational purposes, personal study, and reference.
> The content is dual-licensed:
> 1. **MIT License:** Applies to all code implementations (Swift, Mermaid, and other programming languages).
> 2. **Creative Commons Attribution 4.0 International License (CC BY 4.0):** Applies to all non-code content, including text, explanations, diagrams, and illustrations.
---


The diagrams below provide a visual representation of the major topics and their relationships within the original document.  They are structured hierarchically, which helps in understanding the flow of concepts. The use of subgraphs groups related ideas, making the overall structure clearer. 



## 1. Fundamental Graph Concepts (Chapter 1)

```mermaid
---
title: "Fundamental Graph Concepts (Chapter 1)"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Graph_Structure["Graph Structure"]
        A["Graph G=(V,E)"] --> B("Vertices V")
        A --> C(Edges E)
        C --> D{"Edge:<br>Pair of Vertices"}
    end

    subgraph Graph_Properties["Graph Properties"]
        A --> E(Properties)
        E --> F("Order: |G|")
        E --> G("Size: Number of Edges")
        E --> H(Degree)
        H --> I("Minimum Degree: δ(G)")
        H --> J("Maximum Degree: Δ(G)")
        H --> K("Average Degree: d(G)")
        E --> L(Connectivity)
        L --> M(k-connected)
        M --> N(Cutvertex)
        M --> O(Bridge)
        M --> P(Block)
        E --> Q(Paths)
        Q --> R(Path Length)
        Q --> S(Shortest Path)
        E --> T(Cycles)
        E --> U(Bipartite)
    end

    subgraph Special_Graphs["Special Graphs"]
        A --> V(Special Graphs)
        V --> W("Complete Graph:<br>K<sup>n</sup>")
        V --> X(Tree)
        X --> Y(Rooted Tree)
        X --> Z(Normal Spanning Tree)
        V --> AA(Forest)
        V --> BB(Cycle: C<sup>n</sup>)
        V --> CC(Bipartite Graph)
        CC --> DD("Complete Bipartite:<br>K<sup>m,n</sup>")
        V --> EE(Planar Graph)
    end

    subgraph Graph_Operations["Graph Operations"]
        A --> FF(Graph Operations)
        FF --> GG(Edge Contraction)
        FF --> HH(Vertex/Edge Deletion)
    end
    
style A fill:#ccf3,stroke:#333,stroke-width:2px
style E fill:#ccf3,stroke:#333,stroke-width:2px
style V fill:#ccf3,stroke:#333,stroke-width:2px

```

---


## 2. Probability and Graphical Models (Sections 1.2 & 1.3)

```mermaid
---
title: "Probability and Graphical Models"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Probability
        A[Probability] --> B("Probability Density Function:<br> p(x)")
        B --> C("Integral[Integral of p(x) dx = 1]")
        A --> D(Rules);
        D --> E("Sum Rule:<br> p(x) = ∫p(x,y)dy")
        D --> F("Product Rule:<br> p(x,y) = p(y|x)p(x)")
        D --> G("Bayes' Theorem:<br> p(x|y) = p(y|x)p(x)/p(y)")
        A --> H(Moments)
        H --> I("Mean:<br> E[x]")
        H --> J("Variance:<br> V[x]")
        H --> K("Covariance:<br> Cov[x,y]")
        A --> L("Statistical Independence")
        A --> M(Distributions)
        M --> N(Uniform)
        M --> O(Bernoulli)
        M --> P(Binomial)
        M --> Q(Beta)
        M --> R(Gaussian)
        M --> S(Gamma)
        M --> T(Wishart)
        A --> U(Conjugacy)
    end

    subgraph Graphical_Models["Graphical Models"]
        A1["Graphical Models"] --> B1("Directed:<br>Bayesian Networks")
        A1 --> C1("Undirected:<br>Markov Random Fields")
        A1 --> D1("Factor Graphs")
    end

    style A fill:#ccf3,stroke:#333,stroke-width:2px
    style A1 fill:#ccf3,stroke:#333,stroke-width:2px
    
```

---


## 3. Vector Calculus and Parameter Estimation (Sections 1.4 & 1.5)

```mermaid
---
title: "Vector Calculus and Parameter Estimation"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Vector_Calculus
        A[Vector Calculus] --> B(Gradient: ∇f);
        A --> C(Partial Derivative: ∂f/∂x);
        A --> D(Jacobian);
        A --> E(Linearization);
        A --> F(Taylor Series);
        A --> G(Chain Rule);
    end

    subgraph Parameter_Estimation
        H[Parameter Estimation] --> I(Maximum Likelihood Estimation: MLE);
        I --> J(Loss Function);
        J --> K(Negative Log-Likelihood);
        I --> L(Optimization Algorithm);
        L --> M(Gradient Descent);
        L --> N(Closed-Form Solution);
        H --> O(Regularization);
        H --> P(Maximum A-Posteriori: MAP);
        H --> R(Overfitting);
    end
    style A fill:#ccf3,stroke:#333,stroke-width:2px
    style H fill:#ccf3,stroke:#333,stroke-width:2px
```

----

## 4. Gradient Descent and Model Selection (Sections 1.6 & 1.7)

```mermaid
---
title: "Gradient Descent and Model Selection"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Gradient_Descent
        A[Gradient Descent] --> B(Stepsize);
        A --> C(Momentum);
        A --> D(Stochastic Gradient Descent: SGD);
    end

    subgraph Model_Selection
        E[Model Selection] --> F(Cross-Validation);
        E --> G(Bayesian Model Selection);
        E -->H(Marginal Likelihood)
    end
     style A fill:#ccf3,stroke:#333,stroke-width:2px
     style E fill:#ccf3,stroke:#333,stroke-width:2px

```

----

## 5. Bayesian Linear Regression (Section 1.8)

```mermaid
---
title: "Bayesian Linear Regression"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
   subgraph Bayesian_Linear_Regression["Bayesian Linear Regression"]
    A["Bayesian Linear Regression"] --> B(Model)
    B --> C("y = Φ<sup>T</sup>(x)θ + ε")
    C --> D("ε ~ N(0, σ<sup>2</sup>)")
    A --> E("Parameter Posterior")
     E --> F("p(θ|X, y) = N(θ|m<sub>N</sub>, S<sub>N</sub>)")
    A --> G("Prediction and Inference")
    G --> H("p(y<sup>*</sup>|X, y, x<sup>*</sup>)")
   end
    style A fill:#ccf3,stroke:#333,stroke-width:2px
    
```

----


## 6. Feature Extraction (Chapter 2)

```mermaid
---
title: "Feature Extraction"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Feature_Extraction["Feature Extraction"]
        A[Feature Extraction] --> B(Decompositions)
        B --> C(Eigen-decomposition)
        C --> D(Symmetric Matrices)
        B --> E(QR Decomposition)
        E --> F(Gram-Schmidt Process)
        B --> G(Singular Value Decomposition: SVD)
        G --> H(Thin SVD)
        G --> I(Dimensionality Reduction)
        A --> J(Principal Component Analysis: PCA)
        J --> K(Statistical Perspective)
        J --> L(Reconstruction Perspective)
        J --> M(Probabilistic PCA)
        A --> N(Linear Discriminant Analysis: LDA)
        N --> O(Two-Class Case)
        N --> P(Multi-Class Case)
         A --> Q(Kernel Methods)
        Q --> R(Kernel PCA)
        Q --> S(Kernel LDA)
    end
    
    style A fill:#ccf3,stroke:#333,stroke-width:2px
    
```

----

## 7. Support Vector Machines (Chapter 3)

```mermaid
---
title: "Support Vector Machines"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Support_Vector_Machines["Support Vector Machines"]
        A[Support Vector Machines] --> B(Support Vector Classification: SVC)
        B --> C(Linear Separating Hyperplane)
        C --> D(Maximal Margin)
        C --> E(Lagrangian Duality)
        E --> F(Karush-Kuhn-Tucker Conditions)
        E --> G(SVM Dual Problem)
        B --> H(Mapping Data to Higher Dimensions)
        H --> I(Kernel Trick)
        B --> J(The Dual Problem)

        A --> K(Support Vector Regression: SVR)
        K --> L(Linear Regression)
        K --> M(Support Vector Regression)
    end
    
    style A fill:#ccf3,stroke:#333,stroke-width:2px
    
```

----

## 8. Matrix Preliminaries

```mermaid
---
title: "Matrix Preliminaries"
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
    "flowchart": { "htmlLabels": false, 'curve': 'natural' },
    'fontFamily': 'Fantasy',
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
graph LR
    subgraph Vectors_and_Matrices["Vectors and Matrices"]
	    A[Vectors and Matrices] --> B(Vectors)
        B --> C(Vector Operators)
        C --> D(Inner Product)
        C --> E(Norm)
        A --> F(Matrices)
        F --> G(Matrix Operators)
        G --> H(Matrix Norms)
        G --> I(Matrix Multiplications)
        G --> J(Matrix Transposition)
        G --> K(Trace Operator)
        G --> L(Matrix Determinant)
        G --> M(Matrix Inverse)
        G --> N(Matrix Pseudo-Inverse)
        G --> O(Range, Null Space, Rank)
        G --> P(Eigenvalues and Eigenvectors)
        G --> Q(Positive and Negative Definite Matrices)
        G --> R(Triangular Matrices)
        G --> S(QR Decomposition)
        A --> T(Scalar Products)
        T --> U(Lengths, Distances, Orthogonality)
        A --> V(Useful Matrix Identities)
    end

style A fill:#ccf3,stroke:#333,stroke-width:2px

```


---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---