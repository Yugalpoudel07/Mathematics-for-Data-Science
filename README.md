# 📐 Mathematics for Data Science & Machine Learning

A structured, rigorous, and visually intuitive journey through the core mathematical pillars underpinning modern Data Science, Machine Learning, and Deep Learning engineering.

[![Completed Modules](https://img.shields.io/badge/Completed_Modules-1%20of%206-brightgreen?style=flat-square)](#-learning-roadmap--curriculum-status)
[![Essence of Linear Algebra](https://img.shields.io/badge/3Blue1Brown_Linear_Algebra-16%20of%2016%20(100%25)-blue?style=flat-square)](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Focus](https://img.shields.io/badge/Focus-Theory%20%2B%20Geometric%20Intuition%20%2B%20ML-purple?style=flat-square)](#)

---

## 🎯 Vision & Philosophy

Modern machine learning libraries (like PyTorch, Scikit-Learn, and TensorFlow) make calling algorithms effortless with single-line APIs. However, **true mastery in data science comes from understanding the underlying geometry, calculus, and probability**:

1. **Geometric Intuition First:** Visualizing high-dimensional transformations before memorizing matrix formulas.
2. **Algebraic & Analytical Rigor:** Understanding how formulas derive, when assumptions break down, and how proofs work.
3. **Machine Learning Connection:** Mapping theoretical concepts directly to modern ML architectures (e.g., embeddings, attention mechanisms, loss surfaces, PCA, and gradient descent).

---

## 🗺️ Learning Roadmap & Curriculum Status

| Track / Module | Primary Source | Core Mathematical Focus | Status | Progress |
| :--- | :--- | :--- | :---: | :---: |
| **[3Blue1Brown — Essence of Linear Algebra](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/README.md)** | Grant Sanderson (3b1b) | Geometric & visual vector spaces, matrices, determinants, eigenvalues | ✅ **Completed** | **16 / 16 (100%)** |
| **3Blue1Brown — Essence of Calculus** | Grant Sanderson (3b1b) | Visual derivatives, integrals, chain rule, Taylor series | ⏳ Upcoming | 0 / 12 (0%) |
| **Khan Academy — Linear Algebra** | Sal Khan | Vector spaces, formal proofs, matrix row operations, null space | ⏳ Upcoming | Planned |
| **Khan Academy — Multivariable Calculus** | Khan Academy | Partial derivatives, gradients, Jacobians, Hessians, directional derivatives | ⏳ Upcoming | Planned |
| **Khan Academy — Statistics & Probability** | Khan Academy | Distributions, Bayes theorem, expected value, hypothesis testing | ⏳ Upcoming | Planned |
| **StatQuest with Josh Starmer** | Josh Starmer | Clear algorithmic intuitions for PCA, trees, regressions, and neural nets | ⏳ Upcoming | Planned |

---

## 🌟 Spotlight: 3Blue1Brown — Essence of Linear Algebra (Completed)

> [!TIP]
> **Complete Notes Available:** All 16 chapters are written with detailed explanations, ASCII diagrams, KaTeX formulas, and self-check comprehension questions.  
> 👉 **[Explore the Essence of Linear Algebra Module Directory](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/README.md)**

### 📚 Chapter Breakdown

The 16 chapters are chronologically numbered and structured into five major mathematical themes:

#### Part I: Vectors & Coordinate Foundations
* [**Chapter 01: Vectors — What Even Are They?**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/01-vectors.md) — The physics arrow, computer science number list, and mathematician's axiomatic perspective; anchoring vectors at the origin; vector addition and scalar multiplication.
* [**Chapter 02: Linear Combinations, Span, and Basis Vectors**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/02-linear-combinations-span.md) — Scaling basis vectors $\hat{\imath}$ and $\hat{\jmath}$; spanning lines, planes, and hyperspaces; linear independence vs. redundancy.

#### Part II: Transformations & Matrix Machines
* [**Chapter 03: Linear Transformations and Matrices**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/03-linear-transformations-matrices.md) — What keeps grid lines parallel and origin fixed; tracking landing spots of basis vectors as matrix columns; computing $A\vec{x}$.
* [**Chapter 04: Matrix Multiplication as Composition**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/04-matrix-multiplication-composition.md) — Chaining spatial transformations in sequence; non-commutativity ($AB \neq BA$); geometric proof of associativity.
* [**Chapter 05: Three-Dimensional Linear Transformations**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/05-three-dimensional-transformations.md) — Tracking $\hat{\imath}, \hat{\jmath}, \hat{k}$ in $3 \times 3$ matrices; 3D rotations, shears, and spatial compositions.

#### Part III: Determinants, Inverses & Dimensional Collapse
* [**Chapter 06: The Determinant: Scaling Space**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/06-determinant.md) — Measuring area/volume scaling factor; negative determinant as spatial inversion/orientation flip; determinant zero as dimension collapse.
* [**Chapter 07: Inverse Matrices, Column Space, and Null Space**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/07-inverse-matrices-column-null-space.md) — Playing transformations in reverse ($A^{-1}$); Rank as output dimensionality; Column Space (all reachable outputs); Null Space (vectors collapsed into the origin).
* [**Chapter 08: Nonsquare Matrices as Transformations Between Dimensions**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/08-nonsquare-matrices-dimension-transformations.md) — Geometric meaning of $2 \times 3$ and $3 \times 2$ matrices; transforming space between different dimensionalities.

#### Part IV: Products, Duality & Geometric Solvers
* [**Chapter 09: Dot Products and Duality**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/09-dot-products-duality.md) — Projection onto a line; the duality theorem explaining why numerical dot products match geometric projections.
* [**Chapter 10: Cross Products**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/10-cross-products.md) — Perpendicular vectors in 3D; parallelogram area scaling; right-hand rule convention.
* [**Chapter 11: Cross Products in the Light of Linear Transformations**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/11-cross-products-extended.md) — Connecting 3D volume scaling (determinants) with duality to prove why the cross product algebraic formula works.
* [**Chapter 12: Cramer's Rule, Explained Geometrically**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/12-cramers-rule.md) — Solving linear systems through ratios of transformed areas/volumes via determinants.

#### Part V: Coordinate Changes, Eigen-theory & Abstract Spaces
* [**Chapter 13: Change of Basis**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/13-change-of-basis.md) — Alternate coordinate languages; transition matrices $P$; similarity transformations $P^{-1}AP$.
* [**Chapter 14: Eigenvectors and Eigenvalues**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/14-eigenvectors-eigenvalues.md) — Vectors that remain on their original span during a transformation; eigenvalues $\lambda$; diagonalizing matrices via eigenbases.
* [**Chapter 15: A Quick Trick for Computing Eigenvalues**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/15-quick-eigenvalues.md) — Rapid calculation of $2 \times 2$ eigenvalues using diagonal mean $m$ and determinant $p$ ($m \pm \sqrt{m^2 - p}$).
* [**Chapter 16: Abstract Vector Spaces**](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/16-abstract-vector-spaces.md) — Generalizing vectors to functions, polynomials, audio signals, and quantum states; linear operators and derivatives as matrices.

---

## 💡 How Linear Algebra Powers Machine Learning

| Mathematical Concept | Machine Learning / Data Science Role | Concrete Application |
| :--- | :--- | :--- |
| **Vectors & Dot Products** | Feature embeddings & similarity scoring | Word2Vec, Transformer Query-Key Attention ($Q K^T$), Cosine Similarity |
| **Matrix-Vector Multiplication** | Feed-forward neural network layers | Dense / Linear layer forward pass ($W\vec{x} + \vec{b}$) |
| **Matrix Composition** | Deep layered feature representations | Multi-layer Perceptrons ($W_L \dots W_2 W_1 \vec{x}$) |
| **Nonsquare Matrices** | Dimensionality expansion and compression | Autoencoders, bottleneck layers, latent embeddings |
| **Determinant & Inverses** | Probability density transformations | Normalizing Flows, Gaussian Mixture Models, change-of-variables |
| **Column Space & Rank** | Solvability of linear systems | Ordinary Least Squares regression ($(X^T X)^{-1} X^T y$), multicollinearity |
| **Eigenvalues & Eigenvectors** | Directions of maximum variance | Principal Component Analysis (PCA), Spectral Clustering, PageRank |
| **Change of Basis** | Coordinate transformation to decorrelate data | Whitening transforms, diagonal covariance representations |
| **Abstract Vector Spaces** | Continuous representations & kernel tricks | Support Vector Machines (SVMs with RBF kernels), Fourier Neural Operators |

---

## 📂 Repository Organization

```text
Mathematics-for-Data-Science/
├── 3Blue1Brown - Essence of Linear Algebra/  # [Completed: 16/16 Chapters]
│   ├── README.md                             # Module syllabus, index & ML concepts
│   ├── 01-vectors.md                         # Chapter 01
│   ├── 02-linear-combinations-span.md        # Chapter 02
│   ├── ...                                   # Chapters 03 - 15
│   └── 16-abstract-vector-spaces.md          # Chapter 16
├── 3Blue1Brown - Essence of Calculus/        # [Upcoming]
├── Khan Academy - Linear Algebra/            # [Upcoming]
├── Khan Academy - Multivariable Calculus/    # [Upcoming]
├── Khan Academy - Statistics and Probability/# [Upcoming]
├── StatQuest with Josh Starmer/              # [Upcoming]
├── LICENSE                                   # MIT License
└── README.md                                 # Main repository index (You are here)
```

---

## 🚀 Navigation & Study Guide
* Every chapter file includes **top and bottom navigation breadcrumbs** for seamless reading without navigating back to the folder.
* Look for the **`[!TIP]` Core Intuition** callout at the beginning of each chapter for a high-level summary before diving into the details.
* Try answering each chapter's **Check Your Understanding** questions before revealing the derivations!

---

*Authored as part of the Data Science Journey. Continuously updated as new mathematical tracks are completed!*
