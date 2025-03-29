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


## Numerical Analysis - Main Concepts


This detailed breakdown covers the core concepts presented in the Table of Contents and Preface of the "Numerical Analysis" textbook.

1.  **Fundamentals (Chapter 0)**
    *   Polynomial Evaluation (incl. Horner's Method/Nested Multiplication)
    *   Binary Number System
        *   Decimal-to-Binary Conversion
        *   Binary-to-Decimal Conversion
    *   Floating Point Representation
        *   Formats (Single, Double, Long-Double Precision)
        *   Machine Representation (Sign, Exponent, Mantissa, IEEE 754)
        *   Floating Point Arithmetic (Addition, Rounding)
        *   Machine Epsilon
    *   Loss of Significance (Cancellation Error)
    *   Calculus Review
        *   Intermediate Value Theorem
        *   Mean Value Theorem
        *   Taylor's Theorem with Remainder

2.  **Solving Equations (Chapter 1)**
    *   The Bisection Method
        *   Root Bracketing
        *   Accuracy and Convergence Speed
    *   Fixed-Point Iteration (FPI)
        *   Fixed Points
        *   Geometry of FPI (Cobweb Diagrams)
        *   Linear Convergence
        *   Stopping Criteria
    *   Limits of Accuracy in Root-Finding
        *   Forward and Backward Error
        *   Wilkinson Polynomial Example
        *   Sensitivity and Conditioning
    *   Newton's Method (Newton-Raphson)
        *   Quadratic Convergence
        *   Linear Convergence (Multiple Roots)
    *   Root-Finding without Derivatives
        *   Secant Method (and variants)
        *   Brent's Method
    *   Application: Kinematics of the Stewart Platform (Reality Check 1)

3.  **Systems of Equations (Chapter 2)**
    *   Gaussian Elimination
        *   Naive Gaussian Elimination
        *   Operation Counts (Complexity)
    *   LU Factorization
        *   Matrix Form of Gaussian Elimination
        *   Back Substitution with LU
        *   Complexity of LU Factorization
    *   Sources of Error in Linear Systems
        *   Error Magnification and Condition Number
        *   Swamping
    *   PA = LU Factorization
        *   Partial Pivoting
        *   Permutation Matrices
    *   Application: Euler–Bernoulli Beam (Reality Check 2)
    *   Iterative Methods for Linear Systems
        *   Jacobi Method
        *   Gauss–Seidel Method & SOR (Successive Over-Relaxation)
        *   Convergence of Iterative Methods
        *   Sparse Matrix Computations
    *   Methods for Symmetric Positive-Definite (SPD) Matrices
        *   Properties of SPD Matrices
        *   Cholesky Factorization
        *   Conjugate Gradient Method
        *   Preconditioning
    *   Nonlinear Systems of Equations
        *   Multivariate Newton's Method
        *   Broyden's Method

4.  **Interpolation (Chapter 3)**
    *   Data and Interpolating Functions
        *   Lagrange Interpolation Polynomial
        *   Newton's Divided Differences
        *   Uniqueness of Interpolating Polynomials
    *   Interpolation Error
        *   Error Formula
        *   Runge Phenomenon
    *   Chebyshev Interpolation
        *   Minimax Property (Chebyshev's Theorem)
        *   Chebyshev Polynomials
        *   Change of Interval
    *   Cubic Splines
        *   Properties (Smoothness Conditions)
        *   Endpoint Conditions (Natural, Clamped, etc.)
    *   Bézier Curves
    *   Application: Fonts from Bézier Curves (Reality Check 3)

5.  **Least Squares (Chapter 4)**
    *   Least Squares Problem and Normal Equations
        *   Inconsistent Systems of Equations
        *   Fitting Models to Data
        *   Conditioning of Least Squares
    *   Survey of Models
        *   Fitting Periodic Data
        *   Data Linearization (for exponential, power laws)
    *   QR Factorization
        *   Gram–Schmidt Orthogonalization
        *   Modified Gram–Schmidt
        *   Householder Reflectors
    *   Generalized Minimum Residual (GMRES) Method
        *   Krylov Subspace Methods
        *   Preconditioned GMRES
    *   Nonlinear Least Squares
        *   Gauss–Newton Method
        *   Models with Nonlinear Parameters
        *   Levenberg–Marquardt Method
    *   Application: GPS, Conditioning, and Nonlinear Least Squares (Reality Check 4)

6.  **Numerical Differentiation and Integration (Chapter 5)**
    *   Numerical Differentiation
        *   Finite Difference Formulas (Forward, Centered)
        *   Rounding Error Analysis
        *   Richardson Extrapolation
        *   Symbolic Differentiation
    *   Newton–Cotes Formulas for Numerical Integration
        *   Trapezoid Rule
        *   Simpson's Rule
        *   Composite Formulas
        *   Open Newton-Cotes Methods (Midpoint Rule)
    *   Romberg Integration
    *   Adaptive Quadrature
    *   Gaussian Quadrature
    *   Application: Motion Control in Computer-Aided Modeling (Reality Check 5)

7.  **Ordinary Differential Equations (ODEs) (Chapter 6)**
    *   Initial Value Problems (IVPs)
        *   Euler's Method
        *   Existence, Uniqueness, and Continuity of Solutions (Lipschitz Condition)
        *   First-Order Linear Equations
    *   Analysis of IVP Solvers
        *   Local and Global Truncation Error
        *   Order of a Method
        *   Explicit Trapezoid Method (Heun's Method)
        *   Taylor Methods
    *   Systems of ODEs
        *   Conversion of Higher-Order Equations
        *   Computer Simulation: Pendulum, Orbital Mechanics
    *   Runge–Kutta Methods
        *   RK Family (Midpoint Method, RK4)
        *   Computer Simulation: Hodgkin–Huxley Neuron, Lorenz Equations
    *   Application: Tacoma Narrows Bridge (Reality Check 6)
    *   Variable Step-Size Methods
        *   Embedded Runge–Kutta Pairs (RK2/3, RKF45, Dormand-Prince/ode45)
        *   Local Extrapolation
    *   Implicit Methods and Stiff Equations
        *   Stiffness
        *   Backward Euler Method
    *   Multistep Methods
        *   Generating Methods (Adams-Bashforth, Adams-Moulton)
        *   Explicit vs. Implicit Methods
        *   Stability (Dahlquist Criterion)
        *   Predictor-Corrector Methods

8.  **Boundary Value Problems (BVPs) (Chapter 7)**
    *   Shooting Method
        *   Converting BVP to IVP sequence
        *   Implementation using Root-Finding
    *   Application: Buckling of a Circular Ring (Reality Check 7)
    *   Finite Difference Methods for BVPs
        *   Discretization of Linear BVPs
        *   Discretization of Nonlinear BVPs (using Newton's Method)
    *   Collocation Method
    *   Finite Element Method (FEM)
        *   Galerkin Method
        *   Weak Form
        *   Basis Functions (Piecewise-Linear B-Splines)

9.  **Partial Differential Equations (PDEs) (Chapter 8)**
    *   Classification (Parabolic, Hyperbolic, Elliptic)
    *   Parabolic Equations (e.g., Heat Equation)
        *   Forward Difference Method (Stability Analysis, Conditional Stability)
        *   Backward Difference Method (Unconditional Stability)
        *   Crank–Nicolson Method (Unconditional Stability, Higher Order)
    *   Hyperbolic Equations (e.g., Wave Equation)
        *   Finite Difference Method
        *   CFL Condition (Courant-Friedrichs-Lewy)
    *   Elliptic Equations (e.g., Poisson/Laplace Equation)
        *   Finite Difference Method (Dirichlet/Neumann Boundary Conditions)
        *   Finite Element Method
    *   Application: Heat Distribution on a Cooling Fin (Reality Check 8)
    *   Nonlinear PDEs
        *   Implicit Newton Solver (e.g., for Burgers' Equation)
        *   Reaction-Diffusion Equations (e.g., Fisher's Equation, Brusselator)
        *   Pattern Formation (Turing Instability)

10. **Random Numbers and Applications (Chapter 9)**
    *   Random Number Generation
        *   Pseudo-Random Numbers (Linear Congruential Generators - LCGs)
        *   Generating Exponential and Normal Random Numbers (Box-Muller)
    *   Monte Carlo Simulation
        *   Convergence Rates (Power Laws)
        *   Quasi-Random Numbers (Low-Discrepancy Sequences, Halton Sequence)
    *   Brownian Motion
        *   Discrete Random Walks (First Passage Time)
        *   Continuous Brownian Motion (Properties)
    *   Stochastic Differential Equations (SDEs)
        *   Modeling with Noise
        *   Ito Calculus (Ito Formula)
        *   Numerical Methods for SDEs (Euler-Maruyama, Milstein Method)
    *   Application: Black–Scholes Formula (Reality Check 9)

11. **Trigonometric Interpolation and the FFT (Chapter 10)**
    *   The Fourier Transform
        *   Complex Arithmetic (Euler's Formula, Roots of Unity)
        *   Discrete Fourier Transform (DFT)
        *   Fast Fourier Transform (FFT) Algorithm (Complexity O(n log n))
    *   Trigonometric Interpolation
        *   DFT Interpolation Theorem
        *   Efficient Evaluation using FFT/IFFT
    *   FFT and Signal Processing
        *   Orthogonality of Trigonometric Basis
        *   Least Squares Fitting with Trigonometric Functions
        *   Sound, Noise, and Filtering (Low-Pass Filter)
    *   Application: Wiener Filter (Reality Check 10)

12. **Compression (Chapter 11)**
    *   The Discrete Cosine Transform (DCT)
        *   One-Dimensional DCT (Orthogonality, Interpolation)
        *   DCT and Least Squares Approximation
    *   Two-Dimensional DCT and Image Compression
        *   2D-DCT Definition
        *   Application to Image Blocks (Pixels)
        *   Quantization (Lossy Compression Trade-off)
    *   Huffman Coding
        *   Information Theory (Shannon Entropy)
        *   Huffman Trees for Lossless Coding
        *   Application in JPEG (DPCM, RLE, Zigzag Scan)
    *   Modified DCT (MDCT) and Audio Compression
        *   MDCT Definition (Overlapping Windows)
        *   Time Domain Aliasing Cancellation (TDAC) - Implicit
        *   Bit Quantization for Audio
    *   Application: Simple Audio Codec (Reality Check 11)

13. **Eigenvalues and Singular Values (Chapter 12)**
    *   Power Iteration Methods
        *   Power Iteration (Dominant Eigenvalue/Eigenvector)
        *   Convergence Analysis
        *   Inverse Power Iteration (Smallest Eigenvalue)
        *   Rayleigh Quotient Iteration (Faster Convergence)
    *   QR Algorithm
        *   Simultaneous Iteration / Normalized Simultaneous Iteration
        *   Real Schur Form
        *   Reduction to Upper Hessenberg Form
        *   Shifted QR Algorithm
    *   Application: Search Engine Page Ranking (Reality Check 12)
    *   Singular Value Decomposition (SVD)
        *   Definition (Singular Values, Left/Right Singular Vectors)
        *   Geometric Interpretation (Mapping Unit Sphere to Ellipsoid)
        *   Calculating the SVD (via AT A or symmetric embedding)
        *   SVD for Symmetric Matrices
    *   Applications of SVD
        *   Properties (Rank, Determinant, Inverse)
        *   Low-Rank Approximation
        *   Dimension Reduction
        *   Compression

14. **Optimization (Chapter 13)**
    *   Unconstrained Optimization without Derivatives
        *   Golden Section Search (for unimodal functions)
        *   Successive Parabolic Interpolation (SPI)
        *   Nelder–Mead Search (Downhill Simplex)
    *   Unconstrained Optimization with Derivatives
        *   Newton's Method (using Hessian)
        *   Steepest Descent (Gradient Search)
        *   Conjugate Gradient Search
    *   Application: Molecular Conformation (Lennard-Jones Potential) (Reality Check 13)

15. **Overarching Themes (from Preface)**
    *   Convergence
    *   Complexity
    *   Conditioning
    *   Compression
    *   Orthogonality

16. **Computational Tool (from Preface & Appendix B)**
    *   MATLAB (Environment, Graphics, Programming)

---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---