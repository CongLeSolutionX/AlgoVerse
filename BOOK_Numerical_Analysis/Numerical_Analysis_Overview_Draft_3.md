---
created: 2025-03-29 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
original source: "https://eclass.aueb.gr/modules/document/file.php/MISC249/Sauer%20-%20Numerical%20Analysis%202e.pdf"
---



# Numerical Analysis by Timothy Sauer - 2nd Edition
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


Below diagrams capture the hierarchical structure and key concepts presented in the textbook's table of contents and preface. They highlight the main algorithms, their properties (convergence, complexity, stability), the core principles emphasized by the author, and connections to applications via the Reality Checks.

The preface highlights five core unifying principles: **Convergence, Complexity, Conditioning, Compression, and Orthogonality**. These themes permeate the various methods discussed throughout the book. The book aims to cover fundamental algorithms for solving science and engineering problems, often using MATLAB for illustration.

Here is a collection of Mermaid diagrams illustrating the main concepts:

----

### Diagram 1: Overall Structure of the Textbook

This diagram provides a high-level overview of the book's chapters and their primary topics.

```mermaid
---
title: "Overall Structure of the Textbook"
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
  root(("Numerical Analysis (Sauer, 2nd Ed.)"))
    Fundamentals (Ch 0)
      ::icon(fa fa-calculator)
      Polynomial Evaluation (Horner's)
      Binary Numbers
      Floating Point Arithmetic
        ::icon(fa fa-microchip)
        IEEE 754 Standard
        Machine Epsilon
        Rounding Error
      Loss of Significance
      Calculus Review (IVT, MVT, Taylor)
    Solving Equations (Ch 1)
      ::icon(fa fa-equals)
      Bracketing Methods
        Bisection Method
      Fixed-Point Iteration
        Convergence Analysis (Linear)
      Limits of Accuracy
        Forward/Backward Error
        Sensitivity
      Newton's Method
        Quadratic Convergence
        Multiplicity
      Derivative-Free Methods
        Secant Method
        Brent's Method
      Reality Check: Stewart Platform Kinematics
    Systems of Equations (Ch 2)
      ::icon(fa fa-th-large)
      Linear Systems (Ax=b)
        Gaussian Elimination
          Operation Counts
          LU Factorization
          Pivoting (PA=LU)
        Error Analysis
          Condition Number
          Swamping
        Iterative Methods
          Jacobi
          Gauss-Seidel
          SOR
          Convergence
        Special Matrices
          Symmetric Positive-Definite (SPD)
            Cholesky Factorization
            Conjugate Gradient Method
            Preconditioning
          Sparse Matrices
      Nonlinear_Systems["Nonlinear Systems<br>(F(x)=0)"]
        Multivariate Newton's Method (Jacobian)
        Broyden's Method
      Reality Check: Euler-Bernoulli Beam
    Interpolation (Ch 3)
      ::icon(fa fa-chart-line)
      Polynomial Interpolation
        Lagrange Form
        Newton's Divided Differences
        Interpolation Error
        Runge Phenomenon
      Chebyshev Interpolation
        Chebyshev Polynomials
        Minimax Property
      Splines
        Cubic Splines (Natural, Clamped, etc.)
        Bézier Curves
      Reality Check: Fonts from Bézier curves
    Least Squares (Ch 4)
      ::icon(fa fa-chart-bar)
      Linear Least Squares
        Normal Equations
        Inconsistent Systems
        Model Fitting (Lines, Polynomials)
        Conditioning
      Models Survey
        Periodic Data
        Data Linearization (Exponential, Power Law)
      QR Factorization
        Gram-Schmidt Orthogonalization (Classical, Modified)
        Householder Reflectors
      Iterative Methods for Linear Systems
        GMRES (Krylov Methods)
        Preconditioning
      Nonlinear Least Squares
        Gauss-Newton Method
        Levenberg-Marquardt Method
      Reality Check: GPS Conditioning
    Numerical Differentiation & Integration (Ch 5)
      ::icon(fa fa-infinity)
      Numerical Differentiation
        Finite Difference Formulas (Forward, Centered, Backward)
        Rounding Error Analysis
        Extrapolation (Richardson)
        Symbolic Differentiation
      Numerical Integration (Quadrature)
        Newton-Cotes Formulas
          Trapezoid Rule (Composite)
          Simpson's Rule (Composite)
          Midpoint Rule (Composite)
          Open Formulas
        Romberg Integration
        Adaptive Quadrature
        Gaussian Quadrature (Legendre Polynomials)
      Reality Check: Motion Control (Arc Length)
    Ordinary_Differential_Equations["Ordinary Differential Equations (ODE) (Ch 6)"]
      ::icon(fa fa-wave-square)
      Initial Value Problems (IVP)
        Existence & Uniqueness (Lipschitz)
        Stability (Gronwall)
      One-Step Methods
        Euler's Method (Order 1)
        Explicit Trapezoid Method (Order 2)
        Midpoint Method (Order 2)
        Taylor Methods
        Runge-Kutta Methods (RK4, Embedded Pairs RK23/RKF45/Dormand-Prince)
      Analysis
        Local & Global Truncation Error
        Order of Method
      Systems of ODEs
        Higher-Order Conversion
        Applications (Pendulum, Orbital Mechanics)
      Variable Step-Size Methods
      Implicit Methods & Stiff Equations
        Backward Euler
      Multistep Methods
        Adams-Bashforth (Explicit)
        Adams-Moulton (Implicit)
        Predictor-Corrector
        Stability (Dahlquist)
      Reality Check: Tacoma Narrows Bridge
    Boundary_Value_Problems["Boundary Value Problems (BVP)<br>(Ch 7)"]
      ::icon(fa fa-arrows-alt-h)
      Shooting Method
      Finite Difference Methods
        Linear BVP
        Nonlinear BVP (Newton's Method)
      Collocation Method
      Finite Element Method (FEM)
        Weak Form (Galerkin)
        Basis Functions (B-Splines)
      Reality Check: Buckling of Circular Ring
    Partial_Differential_Equations["Partial Differential Equations (PDE) (Ch 8)"]
      ::icon(fa fa-table)
      Classification (Parabolic, Hyperbolic, Elliptic)
      Parabolic Equations (Heat Eq.)
        Finite Difference Methods
          Forward Difference (Stability, Von Neumann)
          Backward Difference (Implicit, Unconditional Stability)
          Crank-Nicolson (Implicit, Order 2)
        Reaction-Diffusion Equations (Fisher's)
      Hyperbolic Equations (Wave Eq.)
        Finite Difference Method
        CFL Condition
      Elliptic Equations (Poisson/Laplace Eq.)
        Finite Difference Method
        Finite Element Method
        Dirichlet/Neumann Conditions
      Nonlinear PDEs
        Implicit Newton Solver
        Burgers' Equation
        Brusselator (Pattern Formation)
      Reality Check: Heat Distribution on Cooling Fin
    Random Numbers & Applications (Ch 9)
      ::icon(fa fa-random)
      Random Number Generation
        Pseudo-random (LCG)
        Quasi-random (Halton, Low-discrepancy)
        Distributions (Uniform, Exponential, Normal - Box-Muller)
      Monte Carlo Simulation
        Type 1 (Function Average)
        Type 2 (Area/Volume Estimation)
        Convergence (Power Laws)
      Brownian Motion
        Discrete (Random Walk)
        Continuous
        Escape Times
      Stochastic Differential Equations (SDE)
        Ito Calculus (Ito Formula)
        Numerical Methods (Euler-Maruyama, Milstein, Stochastic RK)
        Geometric Brownian Motion
        Langevin Equation
        Brownian Bridge
      Reality Check: Black-Scholes Formula
    Trigonometric Interpolation & FFT (Ch 10)
      ::icon(fa fa-signal)
      Complex Arithmetic (Euler's Formula)
      Fourier Transform
        Discrete Fourier Transform (DFT)
        Fast_Fourier_Transform["Fast Fourier Transform (FFT)<br>(Complexity O(n log n))"]
        Inverse DFT
      Trigonometric Interpolation (DFT Theorem)
      Signal Processing
        Orthogonality
        Least Squares Fitting
        Filtering (Low-pass)
      Reality Check: Wiener Filter
    Compression (Ch 11)
      ::icon(fa fa-compress-alt)
      Discrete Cosine Transform (DCT)
        DCT1, DCT4
        Orthogonality
        Interpolation & Least Squares
      Image Compression (JPEG)
        2D-DCT
        Quantization
        Lossy vs. Lossless
      Huffman Coding
        Shannon Information/Entropy
        Run Length Encoding (RLE)
      Audio Compression (MP3, AAC)
        Modified DCT (MDCT)
        Overlapping Windows
        Bit Quantization
        Psychoacoustics
      Reality Check: Simple Audio Codec
    Eigenvalues & Singular Values (Ch 12)
      ::icon(fa fa-search)
      Eigenvalue Problems
        Characteristic Polynomial (Conditioning Issues)
        Power Iteration (Dominant Eigenvalue)
        Inverse Power Iteration (Smallest/Nearest Eigenvalue)
        Rayleigh Quotient Iteration (Faster Convergence)
        QR Algorithm (Unshifted, Shifted)
          Real Schur Form
          Upper Hessenberg Form
      Singular Value Decomposition (SVD)
        Singular Values/Vectors
        Relation to Eigenvalues (A^T A, AA^T)
        Properties (Rank, Determinant, Inverse)
        Low Rank Approximation
      Applications
        Dimension Reduction
        Compression
      Reality Check: Search Engine Page Rank
    Optimization (Ch 13)
      ::icon(fa fa-crosshairs)
      Unconstrained Optimization
      Methods without Derivatives
        Golden Section Search
        Successive Parabolic Interpolation
        Nelder-Mead Search (Downhill Simplex)
      Methods with Derivatives
        Newton's Method (Hessian)
        Steepest Descent (Gradient Search)
        Conjugate Gradient Search
      Reality Check: Molecular Conformation (Lennard-Jones)
    Appendices
      Matrix Algebra Review
      MATLAB Introduction
      
```

----

### Diagram 2: Core Numerical Analysis Principles

This diagram highlights the five key principles mentioned in the preface and links them to relevant areas covered in the book.

```mermaid
---
title: "Core Numerical Analysis Principles"
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
    subgraph CorePrinciples["Core Principles"]
        style CorePrinciples fill:#f9f3,stroke:#333,stroke-width:2px
        P1(Convergence):::principle --> EqSol("Equation Solving<br>(Iterative Methods)")
        P1 --> DESolvers("ODE/PDE Solvers<br>(Order, Stability)")
        P1 --> Opt("Optimization Algorithms")
        P1 --> MC("Monte Carlo<br>(n -> inf)")

        P2(Complexity):::principle --> GE("Gaussian Elim<br>(O(n³))")
        P2 --> FFT("FFT<br>(O(n log n))")
        P2 --> BackSub("Back Substitution<br>(O(n²))")
        P2 --> IterMethodCost("Iterative Methods<br>(Cost per step)")

        P3(Conditioning):::principle --> RootFind("Root Finding<br>(Sensitivity)")
        P3 --> LinSys("Linear Systems<br>(Condition Number)")
        P3 --> LSError("Least Squares<br>(Normal Eq. vs QR/SVD)")
        P3 --> PolyInterp("Polynomial Interpolation<br>(Runge)")
        P3 --> Eigen("Eigenvalue Problems")
        P3 --> ODEStab("ODE Stability<br>(Stiffness)")

        P4(Compression):::principle --> InterpApprox("Interpolation/Approximation")
        P4 --> LSFitting("Least Squares Model Fitting")
        P4 --> FFTBased("FFT/DCT/MDCT<br>(Signal/Image/Audio)")
        P4 --> SVDApprox("SVD<br>(Low Rank Approximation)")

        P5(Orthogonality):::principle --> GS("Gram-Schmidt")
        P5 --> QR("QR Factorization<br>(Householder)")
        P5 --> CG("Conjugate Gradient")
        P5 --> GMRES("GMRES")
        P5 --> OrthoPoly("Orthogonal Polynomials<br>(Legendre)")
        P5 --> FourierCos("Fourier/Cosine Transforms")
        P5 --> SVDOrtho("SVD<br>(Orthonormal Bases)")
        P5 --> FEM("Finite Element Method")
    end

classDef principle fill:#ccf3,stroke:#000,stroke-width:2px;

```


-----


### Diagram 3: Methods for Solving Equations (Chapters 1 & 2)

Focuses on the methods for single equations and systems (linear and nonlinear).

```mermaid
---
title: "Methods for Solving Equations (Chapters 1 & 2)"
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
  root((Solving Equations))
    Single_Nonlinear_Equation["Single Nonlinear Equation<br>(f(x)=0)"]
      Bracketing Methods
        Bisection Method
          ::icon(fa fa-compress)
          Guaranteed Convergence (Linear, S=0.5)
      Iterative Methods (Require Good Initial Guess)
        Fixed_Point_Iteration["Fixed-Point Iteration<br>(x=g(x))"]
          ::icon(fa fa-sync-alt)
          Convergence_Condition["Convergence Condition<br>(|g'(r)| < 1)"]
          Linear Convergence
        Newton's Method
          ::icon(fa fa-lightbulb)
          Requires f'(x)
          Quadratic Convergence (Simple Roots)
          Linear Convergence (Multiple Roots)
          Modified Newton (for Multiplicity)
        Secant Method
          ::icon(fa fa-cut)
          Derivative-Free Approx. of Newton's
          Superlinear Convergence
        Brent's Method (Hybrid)
          ::icon(fa fa-shield-alt)
          Combines Bisection/Secant/IQI
          Robust and Fast
      Accuracy & Error
        Forward vs. Backward Error
        Loss of Significance
        Sensitivity & Conditioning
        Root Multiplicity
    Systems of Linear Equations (Ax=b)
      Direct Methods
        Gaussian Elimination
          ::icon(fa fa-calculator)
          Naive vs. Pivoting
          Operation_Counts["Operation Counts<br>(O(n³))"]
          Swamping Issue
        LU Factorization
          ::icon(fa fa- GripLinesVertical)
          Storing multipliers
          Solving Lc=b, Ux=c
          Efficiency for multiple RHS
        PA=LU Factorization
          ::icon(fa fa-random)
          Partial Pivoting
          Permutation Matrices
        Cholesky Factorization (A=RᵀR)
          ::icon(fa fa-check-circle)
          For_Symmetric_Positive_Definite_Matrices["For Symmetric Positive-Definite (SPD) Matrices"]
          Complexity O(n³/3)
      Iterative Methods (Good for Large/Sparse Systems)
        Jacobi Method
        Gauss-Seidel Method
        Successive Over-Relaxation (SOR)
        Convergence (Diagonal Dominance)
        Conjugate Gradient Method
          ::icon(fa fa-angle-double-down)
          For SPD Matrices
          Based on A-conjugacy
        Generalized Minimum Residual (GMRES)
          ::icon(fa fa-angle-double-right)
          For Non-symmetric Matrices
          Krylov Subspaces
        Preconditioning
          ::icon(fa fa-filter)
          Improves Convergence Rate (Reduces Condition Number)
      Error & Conditioning
        Vector/Matrix Norms (Infinity Norm)
        Residual
        Condition_Number["Condition Number (cond(A))"]
    Systems_of_Nonlinear_Equations["Systems of Nonlinear Equations<br>(F(x)=0)"]
      Multivariate Newton's Method
        ::icon(fa fa-sitemap)
        Requires Jacobian Matrix (DF)
        Solving DF*s = -F
        Quadratic Convergence (typically)
      Broyden's Method (Quasi-Newton)
        ::icon(fa fa-wrench)
        Approximates Jacobian or its Inverse
        Derivative-Free (after initial guess)
        Superlinear Convergence
        
```


----


### Diagram 4: Interpolation, Approximation, and Transforms (Chapters 3, 4, 10, 11, 12)

Covers methods for fitting functions to data and transforming data representations.

```mermaid
---
title: "Interpolation, Approximation, and Transforms (Chapters 3, 4, 10, 11, 12)"
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
  root((Data Fitting & Transforms))
    Interpolation (Exact Fit Through Points)
      ::icon(fa fa-chart-line)
      Polynomial Interpolation
        Existence & Uniqueness Theorem
        Lagrange Polynomial
        Newton's Divided Differences
          ::icon(fa fa-table)
          Efficient calculation & updates
          Nested form
        Interpolation Error Formula
        Runge Phenomenon (High-degree wiggle)
      Chebyshev Interpolation
        ::icon(fa fa-star)
        Minimizes max error on [-1, 1]
        Chebyshev Polynomials & Nodes
        Mitigates Runge Phenomenon
      Spline Interpolation (Piecewise Polynomials)
        Linear Splines (Connect-the-dots)
        Cubic Splines
          ::icon(fa fa-pencil-ruler)
          Smoothness conditions (C², C¹)
          End Conditions (Natural, Clamped, Not-a-Knot, Parabolic)
          Solving for coefficients (Tridiagonal System)
        Bézier Curves
          ::icon(fa fa-signature)
          Parametric curves
          Control Points
          Applications (Fonts, CAD)
    Least Squares Approximation (Best Fit)
      ::icon(fa fa-bullseye)
      Linear Least Squares (Ax=b, m>n)
        Normal Equations (AᵀAx = Aᵀb)
          ::icon(fa fa-balance-scale)
          Conditioning_issues["Conditioning issues<br>(cond(AᵀA) ≈ cond(A)²)"]
        QR Factorization Approach
          ::icon(fa fa-qrcode)
          Gram-Schmidt (Classical, Modified)
          Householder Reflectors
          More stable than Normal Equations
        Model Fitting
          Lines, Polynomials
          Periodic Models (Sines/Cosines)
          Data Linearization (Exponential, Power Law)
      Nonlinear_Least_Squares["Nonlinear Least Squares<br>(min ||r(c)||²)"]
        Gauss-Newton Method
          ::icon(fa fa-crosshairs)
          Uses Jacobian of residual (Dr)
          Can converge to local minima/maxima
        Levenberg-Marquardt Method
          ::icon(fa fa-life-ring)
          Regularization term (λ)
          Improves conditioning, robustness
    Transforms (Change of Basis/Representation)
      ::icon(fa fa-retweet)
      Fourier Transform (Complex Basis)
        Discrete Fourier Transform (DFT)
          ::icon(fa fa-wave-square)
          Unitary Matrix (Fn)
          DFT Interpolation Theorem
        Fast Fourier Transform (FFT)
          ::icon(fa fa-fighter-jet)
          Complexity O(n log n)
          Cooley-Tukey Algorithm
        Applications: Signal Processing, Filtering
      Cosine Transform (Real Basis)
        Discrete Cosine Transform (DCT)
          ::icon(fa fa-camera)
          DCT1, DCT4
          Orthogonal Matrix (C)
          DCT Interpolation/Least Squares
          Applications: Image Compression (JPEG)
        Modified DCT (MDCT)
          ::icon(fa fa-headphones)
          Rectangular Matrix (n x 2n)
          Overlapping Windows for Inversion
          Applications: Audio Compression (MP3, AAC)
      Singular_Value_Decomposition["Singular Value Decomposition (SVD)<br>(A = USVᵀ)"]
        ::icon(fa fa-search-plus)
        Singular_Values["Singular Values<br>(si)"]
        Singular_Vectors["Singular Vectors (ui, vi)<br>(Orthonormal Bases)"]
        Relationship to Eigenvalues (AᵀA, AAᵀ)
        Properties (Rank, Determinant, Inverse)
        Low Rank Approximation (Best LS Approx)
        Applications: Dimension Reduction, Compression, Conditioning
        
```

----


### Diagram 5: Numerical Calculus & Differential Equations (Chapters 5, 6, 7, 8)

Covers differentiation, integration, and the solution of ODEs and PDEs.

```mermaid
---
title: "Numerical Calculus & Differential Equations (Chapters 5, 6, 7, 8)"
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
  root((Numerical Calculus & Differential Equations))
    Numerical Differentiation
      ::icon(fa fa-calculator)
      Finite Difference Formulas
        Forward, Backward, Centered Differences
        Higher-Order Derivatives
        Truncation Error (Order of Accuracy)
      Rounding Error Analysis
        Loss of Significance for small h
        Optimal h trade-off
      Extrapolation (Richardson)
        ::icon(fa fa-angle-double-up)
        Increases order of accuracy
    Numerical Integration (Quadrature)
      ::icon(fa fa-infinity)
      Newton-Cotes Formulas (Equally Spaced Points)
        Trapezoid_Rule["Trapezoid Rule (Order 1 precision, O(h³) error)"]
        Simpson_Rule["Simpson's Rule (Order 3 precision, O(h⁵) error)"]
        Composite Rules
        Open vs. Closed Formulas
        Midpoint Rule
        Degree of Precision
      Romberg Integration
        ::icon(fa fa-fast-forward)
        Extrapolation applied to Trapezoid Rule
        Higher order accuracy
      Adaptive Quadrature
        ::icon(fa fa-tachometer-alt)
        Variable step size based on error estimate
        Efficient for functions with varying behavior
      Gaussian Quadrature
        ::icon(fa fa-star-of-life)
        Optimal nodes (Legendre Polynomial roots)
        High degree of precision (2n-1 for n points)
    Ordinary Differential Equations (ODE)
      ::icon(fa fa-project-diagram)
      Initial_Value_Problems["Initial Value Problems (IVP: y'=f(t,y), y(a)=ya)"]
        Existence & Uniqueness (Lipschitz Condition)
        Stability (Sensitivity to Initial Conditions, Gronwall)
      Methods
        One-Step Methods
          Euler's Method (Order 1)
          Explicit Trapezoid (Order 2)
          Midpoint Method (Order 2)
          Runge-Kutta Methods (RK4, Embedded Pairs)
            ::icon(fa fa-running)
          Taylor Methods (Require higher derivatives of f)
        Multistep Methods (Use past values)
          Adams-Bashforth (Explicit)
          Adams-Moulton (Implicit)
          Predictor-Corrector Methods
          Stability (Root Condition, Dahlquist Theorem)
        Implicit vs. Explicit
        Variable Step-Size Methods
        Stiff Equations (Require Implicit Methods)
          ::icon(fa fa-exclamation-triangle)
          Backward Euler
      Systems of ODEs & Higher Order
        Conversion to First-Order Systems
        Applications (Pendulum, Orbital Mechanics)
    Boundary_Value_Problems["Boundary Value Problems<br>(BVP: y''=f, y(a)=ya, y(b)=yb)"]
      ::icon(fa fa-ruler-horizontal)
      Shooting Method
        ::icon(fa fa-bullseye)
        Convert BVP to IVP, iterate on initial slope
        Uses root-finding (Bisection, Newton)
      Finite Difference Method
        ::icon(fa fa-border-all)
        Discretize derivatives -> System of equations
        Linear BVP -> Linear System
        Nonlinear BVP -> Nonlinear System (Newton)
      Collocation Method
        Approximate solution as sum of basis functions
        Satisfy DE at specific points -> System of equations
      Finite Element Method (FEM)
        ::icon(fa fa-cubes)
        Weak Formulation (Galerkin Method, Orthogonality)
        Piecewise Basis Functions (B-Splines)
        Reduces to system of equations
    Partial Differential Equations (PDE)
      ::icon(fa fa-th)
      Classification
        Parabolic (e.g., Heat Equation)
          ::icon(fa fa-thermometer-half)
        Hyperbolic (e.g., Wave Equation)
          ::icon(fa fa-water)
        Elliptic (e.g., Laplace/Poisson Equation)
          ::icon(fa fa-bolt)
      Methods
        Finite Difference Methods
          Forward Difference (Conditionally Stable)
          Backward Difference (Implicit, Unconditionally Stable)
          Crank-Nicolson (Implicit, Order 2, Unconditionally Stable)
          Stability Analysis (Von Neumann, CFL Condition)
        Finite Element Method (for Elliptic)
      Boundary Conditions (Dirichlet, Neumann)
      Nonlinear PDEs
        Burgers' Equation
        Reaction-Diffusion (Fisher's Eq., Brusselator)
        Implicit Newton Solver
        Pattern Formation (Turing Instability)
        
```

----


### Diagram 6: Stochastic Methods & Optimization (Chapters 9, 13)

Covers random number generation, simulation using randomness, and finding minima/maxima of functions.

```mermaid
---
title: "Stochastic Methods & Optimization (Chapters 9, 13)"
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
  root((Stochastic Methods & Optimization))
    Random Numbers & Simulation (Ch 9)
      ::icon(fa fa-dice)
      Random Number Generation
        Pseudo-random Numbers
          Linear Congruential Generators (LCG)
          Issues (randu, Periodicity, Correlations)
          Minimal Standard Generator
        Quasi-random Numbers
          Low-discrepancy sequences (Halton)
          Self-avoiding property
        Distributions
          Uniform [0, 1]
          Exponential (Inverse CDF method)
          Normal_N["Normal N(0,1)<br>(Box-Muller, Ziggurat)"]
      Monte Carlo Simulation
        ::icon(fa fa-chart-pie)
        Type 1: Function Averaging (Integration)
        Type 2: Probability/Area/Volume Estimation
        Convergence Rates
          Pseudo-random: O(n⁻⁰⁵)
          Quasi_random["Quasi-random:<br> O(n⁻¹) or better (Type 1),<br> O(n⁻⁰⁵⁻¹/(²ᵈ)) (Type 2)"]
      Stochastic Processes
        Brownian Motion (Wiener Process)
          Discrete (Random Walk)
          Continuous (Properties, Simulation)
          Escape Times
        Stochastic Differential Equations (SDEs)
          ::icon(fa fa-random)
          Ito Calculus (Ito Integral, Ito Formula)
          White Noise (dBt)
          Examples (Geometric Brownian Motion, Langevin Eq., Brownian Bridge)
        Numerical Methods for SDEs
          Euler-Maruyama (Order 0.5)
          Milstein Method (Order 1.0)
          Stochastic Runge-Kutta
      Applications
        Black-Scholes Formula (Option Pricing)
    Optimization (Ch 13)
      ::icon(fa fa-crosshairs)
      Unconstrained_Optimization["Unconstrained Optimization<br>(min f(x))"]
      Methods without Derivatives
        Golden Section Search
          ::icon(fa fa-search-minus)
          One dimension, requires unimodal function
          Linear convergence (Rate ≈ 0.618)
        Successive Parabolic Interpolation (SPI)
          ::icon(fa fa-chart-line)
          One dimension, uses function values
          Faster_convergence["Faster convergence (typically) but not guaranteed"]
        Nelder-Mead Search (Downhill Simplex)
          ::icon(fa fa-cubes)
          Multiple dimensions
          Uses simplex reflection, expansion, contraction, shrink
      Methods with Derivatives
        Newton's Method
          ::icon(fa fa-bolt)
          Requires_Gradient_and_Hessian["Requires Gradient (∇f) and Hessian (Hf)"]
          Solves ∇f = 0
          Quadratic convergence (typically)
        Steepest Descent (Gradient Search)
          ::icon(fa fa-arrow-down)
          Moves in direction -∇f
          Requires 1D line search
          Can be slow (zigzagging)
        Conjugate Gradient Search
          ::icon(fa fa-sync)
          Uses conjugate directions (related to CG for linear systems)
          Faster than Steepest Descent
      Applications
        Molecular Conformation (Lennard-Jones Potential)
        
```



---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---