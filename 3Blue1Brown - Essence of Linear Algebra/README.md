[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [**Start Reading: Chapter 01 — Vectors** ⏭️](01-vectors.md)

---

# 🎬 3Blue1Brown — Essence of Linear Algebra

### *Visual Geometric Foundations for Data Science & Machine Learning*

[![Status: Completed](https://img.shields.io/badge/Status-100%25_Completed-brightgreen?style=flat-square)](#)
[![Playlist](https://img.shields.io/badge/3Blue1Brown-Essence_of_Linear_Algebra-red?style=flat-square&logo=youtube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
[![Chapters](https://img.shields.io/badge/Chapters-16%20of%2016-blue?style=flat-square)](#-chapter-directory--syllabus)
[![Focus](https://img.shields.io/badge/Focus-Geometric_Intuition-purple?style=flat-square)](#)

> [!NOTE]
> **About this Series:**  
> Traditional linear algebra courses often dive straight into symbolic calculations, row reductions, and tedious matrix manipulation without providing an intuitive mental model. This module follows Grant Sanderson's renowned **3Blue1Brown "Essence of Linear Algebra"** series, capturing the visual and geometric intuition behind every major concept. 
> 
> When you truly visualize what matrices and vectors do in space, high-dimensional machine learning concepts like **embeddings, linear layers, PCA, coordinate changes, and attention mechanisms** become instantly intuitive.

---

## 🗺️ Chapter Directory & Syllabus

All 16 chapters are fully completed, formatted, and cross-linked. Click any chapter title below to jump straight to its notes, formulas, visual diagrams, and self-check questions:

| # | Chapter Title | Core Geometric Concept | Machine Learning & Data Science Application |
| :-: | :--- | :--- | :--- |
| **01** | [**Vectors: What Even Are They?**](01-vectors.md) | Arrow vs. list of numbers; anchoring vectors at the origin; addition and scaling. | Feature vectors, data sample representations, high-dimensional word/item embeddings. |
| **02** | [**Linear Combinations, Span & Basis**](02-linear-combinations-span.md) | Scaling and adding basis vectors; sweeping out space; linear independence vs. redundancy. | Feature redundancy, multicollinearity, vector subspaces, identifying independent features. |
| **03** | [**Linear Transformations & Matrices**](03-linear-transformations-matrices.md) | Matrices as space-transforming machines; tracking $\hat{\imath}$ and $\hat{\jmath}$ landing columns. | Linear layers in deep learning ($W\vec{x} + \vec{b}$), affine transformations, computer graphics. |
| **04** | [**Matrix Multiplication as Composition**](04-matrix-multiplication-composition.md) | Chaining transformations in sequence; non-commutativity ($AB \neq BA$); associativity. | Feed-forward networks (sequential matrix operations $W_2 W_1 \vec{x}$), composite feature extractors. |
| **05** | [**Three-Dimensional Transformations**](05-three-dimensional-transformations.md) | Tracking $\hat{\imath}, \hat{\jmath}, \hat{k}$ landing spots in $3 \times 3$ matrices; 3D rotations and shears. | 3D computer vision, point cloud processing, camera projection pipelines, robotics. |
| **06** | [**The Determinant: Scaling Space**](06-determinant.md) | Measuring area/volume scaling factors; negative orientation flips; zero determinant collapse. | Normalizing flows, Jacobian determinants in continuous probability, invertible ML models. |
| **07** | [**Inverse Matrices, Column Space & Null Space**](07-inverse-matrices-column-null-space.md) | Playing transformations in reverse ($A^{-1}$); rank; span of outputs; kernel collapse to origin. | Ordinary Least Squares regression ($(X^T X)^{-1} X^T y$), solvability, rank deficiencies. |
| **08** | [**Nonsquare Matrices Between Dimensions**](08-nonsquare-matrices-dimension-transformations.md) | Transformations between different spaces ($2\text{D} \to 3\text{D}$ or $3\text{D} \to 2\text{D}$); row/column geometry. | Autoencoders (bottleneck dimensionality reduction), projection matrices, latent space mapping. |
| **09** | [**Dot Products and Duality**](09-dot-products-duality.md) | Geometric projection onto 1D lines; duality translating 1D transformations into vectors. | Cosine similarity, query-key attention scores ($Q K^T$), projection in SVMs and perceptrons. |
| **10** | [**Cross Products**](10-cross-products.md) | Generating perpendicular vectors; parallelogram area scaling; right-hand orientation. | Surface normal estimation in 3D data, robotics kinematics, angular momentum modeling. |
| **11** | [**Cross Products & Transformations**](11-cross-products-extended.md) | 3D volume scaling connection; proving the cross product trick via linear duality. | Rigorous multilinear algebraic proofs, understanding tensor transformations. |
| **12** | [**Cramer's Rule Geometrically**](12-cramers-rule.md) | Solving systems via area/volume ratios of transformed parallelograms using determinants. | Analytical closed-form solutions, theoretical sensitivity analysis in optimization. |
| **13** | [**Change of Basis**](13-change-of-basis.md) | Translating coordinate languages; similarity transformations ($P^{-1} A P$); alternate grids. | Principal Component Analysis (PCA coordinate shifts), diagonalizing matrices, feature rotation. |
| **14** | [**Eigenvectors and Eigenvalues**](14-eigenvectors-eigenvalues.md) | Vectors that stay on their span; scaling factor $\lambda$; eigenbasis diagonal representations. | PCA dominant components, Google PageRank, spectral graph theory, Markov stability. |
| **15** | [**Quick Trick for Computing Eigenvalues**](15-quick-eigenvalues.md) | Instant $2 \times 2$ eigenvalues using the mean diagonal $m$ and determinant $p$ ($m \pm \sqrt{m^2 - p}$). | Rapid manual checks, 2D continuous dynamical systems, Hessian eigenvalue tests. |
| **16** | [**Abstract Vector Spaces**](16-abstract-vector-spaces.md) | Generalizing vectors beyond arrows: polynomials, audio signals, functions, and linear operators. | Kernel methods, Reproducing Kernel Hilbert Spaces (RKHS), Fourier analysis, functional data analysis. |

---

## 🧠 Key Conceptual Pillars

Throughout these 16 chapters, linear algebra is synthesized into four universal geometric principles:

```text
               ┌─────────────────────────────────────────────────┐
               │         VECTORS AS SPATIAL LOCATIONS            │
               │  Anchored at origin; scaled and combined (Span) │
               └────────────────────────┬────────────────────────┘
                                        │
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │         MATRICES AS SPATIAL OPERATORS           │
               │  Columns are the landing spots of basis vectors │
               └────────────────────────┬────────────────────────┘
                                        │
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │         DETERMINANTS & DIMENSIONALITY           │
               │  Scale factor of space; det = 0 collapses info  │
               └────────────────────────┬────────────────────────┘
                                        │
                                        ▼
               ┌─────────────────────────────────────────────────┐
               │         EIGENVECTORS & CHANGE OF BASIS          │
               │  The invariant coordinate system of a matrix    │
               └─────────────────────────────────────────────────┘
```

1. **Space & Coordinates are Distinct:** Space exists independently of coordinate systems. Coordinate grids are just arbitrary human choices of basis vectors. Changing the basis translates descriptions between coordinate systems via $P^{-1}AP$.
2. **Every Matrix is an Action:** A matrix is not a static grid of numbers—it is a continuous transformation that distorts, shears, stretches, or rotates space while keeping grid lines parallel and evenly spaced.
3. **Determinants Measure Spatial Scaling:** The determinant is the volume scaling factor of a transformation. When $\det(A) = 0$, space is compressed into a lower dimension, causing information loss (meaning no inverse matrix exists).
4. **Eigenvectors Reveal the Transformation's Axis:** Most vectors rotate away from their initial direction when transformed. Eigenvectors are the rare, privileged vectors that remain on their original span, simply scaling by an eigenvalue $\lambda$.

---

## 📌 Study Tips

* Read each chapter in order from **01** to **16**.
* Follow along with the ASCII visual diagrams to train your mind to "see" transformations.
* Before expanding each chapter's **Check Your Understanding** dropdown, attempt the derivation on paper!

---

[🏠 **Back to Main Repository**](../README.md) &nbsp;•&nbsp; [**Start with Chapter 01: Vectors** ⏭️](01-vectors.md)
