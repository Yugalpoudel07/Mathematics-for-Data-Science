# 📐 Mathematics for Data Science & Machine Learning

A structured, rigorous, and visually intuitive journey through the core mathematical pillars underpinning modern Data Science, Machine Learning, and Deep Learning engineering.

[![Completed Modules](https://img.shields.io/badge/Completed_Modules-3%20of%206-brightgreen?style=flat-square)](#-learning-roadmap--curriculum-status)
[![Essence of Linear Algebra](https://img.shields.io/badge/3Blue1Brown_Linear_Algebra-16%20of%2016%20(100%25)-blue?style=flat-square)](3Blue1Brown%20-%20Essence%20of%20Linear%20Algebra/README.md)
[![Essence of Calculus](https://img.shields.io/badge/3Blue1Brown_Calculus-12%20of%2012%20(100%25)-blue?style=flat-square)](3Blue1Brown%20-%20Essence%20of%20Calculus/README.md)
[![StatQuest](https://img.shields.io/badge/StatQuest-23%20of%2023%20(100%25)-blue?style=flat-square)](StatQuest%20with%20Josh%20Starmer/README.md)
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
| **[3Blue1Brown — Essence of Calculus](3Blue1Brown%20-%20Essence%20of%20Calculus/README.md)** | Grant Sanderson (3b1b) | Visual derivatives, integrals, chain rule, curvature, Taylor series | ✅ **Completed** | **12 / 12 (100%)** |
| **Khan Academy — Linear Algebra** | Sal Khan | Vector spaces, formal proofs, matrix row operations, null space | ⏳ Upcoming | Planned |
| **Khan Academy — Multivariable Calculus** | Khan Academy | Partial derivatives, gradients, Jacobians, Hessians, directional derivatives | ⏳ Upcoming | Planned |
| **Khan Academy — Statistics & Probability** | Khan Academy | Distributions, Bayes theorem, expected value, hypothesis testing | ⏳ Upcoming | Planned |
| **[StatQuest with Josh Starmer](StatQuest%20with%20Josh%20Starmer/README.md)** | Josh Starmer | Probability, distributions, CLT, confidence intervals, bootstrapping, maximum likelihood | ✅ **Completed** | **23 / 23 (100%)** |
| **[Month 1 — Build Tasks](Month%201%20-%20Build%20Tasks/README.md)** | Roadmap "What you build" (Weeks 1–4) | From-scratch NumPy code + tested notebooks: matmul, projection, gradient checker, gradient descent, distributions, CLT, Monty Hall, naive Bayes, bootstrap, CI coverage | ✅ **Completed** | **10 / 10 tasks** |

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

## 🌟 Spotlight: 3Blue1Brown — Essence of Calculus (Completed)

> [!TIP]
> **Complete Notes Available:** All 12 chapters include geometric derivations, ASCII diagrams, KaTeX formulas, a dedicated **Connection to Machine Learning & Data Science** section, and self-check questions with full worked solutions.  
> 👉 **[Explore the Essence of Calculus Module Directory](3Blue1Brown%20-%20Essence%20of%20Calculus/README.md)**

### 📚 Chapter Breakdown

The 12 chapters are chronologically numbered and structured into four major themes:

#### Part I: The Core Idea & The Derivative

* [**Chapter 01: The Essence of Calculus**](3Blue1Brown%20-%20Essence%20of%20Calculus/01-essence-of-calculus.md) — Deriving $\pi R^2$ by slicing a disc into rings; how integrals, derivatives, and the Fundamental Theorem all fall out of one concrete problem; what $dx$ actually means.
* [**Chapter 02: The Paradox of the Derivative**](3Blue1Brown%20-%20Essence%20of%20Calculus/02-paradox-of-the-derivative.md) — Why "instantaneous rate of change" is a contradiction in terms; secant lines converging to the tangent; where derivatives fail to exist.
* [**Chapter 03: Derivative Formulas Through Geometry**](3Blue1Brown%20-%20Essence%20of%20Calculus/03-derivative-formulas-geometry.md) — The power rule as a growing hypercube; $1/x$ as a fixed-area rectangle; $\sin$ and $\cos$ from a point sliding on the unit circle.

#### Part II: Combining & Composing Functions

* [**Chapter 04: Visualizing the Chain Rule & Product Rule**](3Blue1Brown%20-%20Essence%20of%20Calculus/04-chain-rule-product-rule.md) — Products as rectangles gaining two strips; composition as a pipeline where sensitivities multiply; the direct line to backpropagation.
* [**Chapter 05: What's So Special About Euler's Number $e$?**](3Blue1Brown%20-%20Essence%20of%20Calculus/05-derivatives-exponentials.md) — Why $\frac{d}{dt}a^t = \ln(a)a^t$; $e$ defined by being its own derivative; rate proportional to amount; the natural logarithm.
* [**Chapter 06: Implicit Differentiation**](3Blue1Brown%20-%20Essence%20of%20Calculus/06-implicit-differentiation.md) — Curves as constraints rather than functions; the sliding ladder; related rates; level sets, gradients, and a preview of multivariable calculus.

#### Part III: Rigor, Accumulation & Averages

* [**Chapter 07: Limits, L'Hôpital's Rule & Epsilon-Delta**](3Blue1Brown%20-%20Essence%20of%20Calculus/07-limits.md) — The $\epsilon$-$\delta$ definition as a challenge-response game; turning $\frac{0}{0}$ into a ratio of derivatives; continuity and differentiability.
* [**Chapter 08: Integration & the Fundamental Theorem**](3Blue1Brown%20-%20Essence%20of%20Calculus/08-integration-fundamental-theorem.md) — Distance from velocity; Riemann sums and signed area; antiderivatives collapsing an infinite sum into one subtraction; why $\int e^{-x^2}dx$ has no elementary form.
* [**Chapter 09: What Does Area Have to Do With Slope?**](3Blue1Brown%20-%20Essence%20of%20Calculus/09-area-and-slope.md) — Average value of a continuous function; the $\frac{1}{n} \to \frac{\Delta x}{b-a}$ trick; why average value equals the secant slope of the antiderivative; the Mean Value Theorem.

#### Part IV: Local Structure & The Bigger Picture

* [**Chapter 10: Higher Order Derivatives**](3Blue1Brown%20-%20Essence%20of%20Calculus/10-higher-order-derivatives.md) — Curvature and concavity; the second derivative test; inflection points; the Hessian matrix and why its eigenvalues govern optimization.
* [**Chapter 11: Taylor Series**](3Blue1Brown%20-%20Essence%20of%20Calculus/11-taylor-series.md) — Rebuilding a function from its derivatives at one point; where the factorials come from; radius of convergence; every optimizer as a truncated Taylor model.
* [**Chapter 12: What They Won't Teach You in Calculus**](3Blue1Brown%20-%20Essence%20of%20Calculus/12-what-they-wont-teach-you.md) — Three independent derivations of $\pi R^2$; proving $\sin' = \cos$ with pure geometry; how mathematics is actually invented.

---

## 🌟 Spotlight: StatQuest with Josh Starmer (Completed)

> [!TIP]
> **Complete Notes Available:** All 23 topics are fully completed, formatted, and cross-linked, each carrying a **Core Intuition** callout, worked formulas, an ASCII diagram, and a dedicated **Connection to Machine Learning & Data Science** angle — the same treatment as the other completed modules above.  
> 👉 **[Explore the StatQuest Module Directory](StatQuest%20with%20Josh%20Starmer/README.md)**

### 📚 Topic Breakdown

All 23 topics are chronologically numbered and build progressively across four themes, from "what is randomness" to "how do I fit a model to it":

#### Part I: Foundations of Probability

* [**Topic 01: The Main Ideas behind Probability Distributions**](StatQuest%20with%20Josh%20Starmer/01-probability-distributions.md) — A distribution as the smooth, idealized version of a histogram.
* [**Topic 02: What Does It Mean to "Sample from a Distribution"?**](StatQuest%20with%20Josh%20Starmer/02-sampling-from-a-distribution.md) — Generating random values that respect a distribution's shape.
* [**Topic 03: Conditional Probability**](StatQuest%20with%20Josh%20Starmer/03-conditional-probability.md) — Shrinking the world to the cases that match a condition.
* [**Topic 04: Bayes' Theorem**](StatQuest%20with%20Josh%20Starmer/04-bayes-theorem.md) — Updating a prior belief into a posterior given new evidence.

#### Part II: Distributions, Expectation & Relationships

* [**Topic 05: The Binomial Distribution and Test**](StatQuest%20with%20Josh%20Starmer/05-binomial-distribution.md) — Exactly $k$ successes in $n$ independent yes/no trials.
* [**Topic 06: The Normal Distribution**](StatQuest%20with%20Josh%20Starmer/06-normal-distribution.md) — The bell curve, fully described by a mean and standard deviation.
* [**Topic 07: Expected Values, Part 1 (Discrete)**](StatQuest%20with%20Josh%20Starmer/07-expected-values-discrete.md) — The long-run, probability-weighted average.
* [**Topic 08: Expected Values, Part 2 (Continuous)**](StatQuest%20with%20Josh%20Starmer/08-expected-values-continuous.md) — The same weighted average as an integral over a density.
* [**Topic 09: Covariance**](StatQuest%20with%20Josh%20Starmer/09-covariance.md) — Whether two variables move together, oppositely, or without pattern.
* [**Topic 10: Pearson's Correlation**](StatQuest%20with%20Josh%20Starmer/10-pearsons-correlation.md) — Covariance with the units stripped off, bounded between −1 and +1.

#### Part III: Samples, Estimation & Inference

* [**Topic 11: The Central Limit Theorem**](StatQuest%20with%20Josh%20Starmer/11-central-limit-theorem.md) — Sample means from any distribution converge toward a normal distribution.
* [**Topic 12: Naive Bayes**](StatQuest%20with%20Josh%20Starmer/12-naive-bayes.md) — Classifying by which class makes the observed features most likely.
* [**Topic 13: Population and Estimated Parameters**](StatQuest%20with%20Josh%20Starmer/13-population-estimated-parameters.md) — Using a sample to estimate the population's true parameters.
* [**Topic 14: Estimating the Mean, Variance and Standard Deviation**](StatQuest%20with%20Josh%20Starmer/14-estimating-mean-variance-sd.md) — Why sample variance divides by $n-1$, not $n$.
* [**Topic 15: Standard Deviation vs Standard Error**](StatQuest%20with%20Josh%20Starmer/15-sd-vs-standard-error.md) — Spread of the data vs. spread of the estimate.
* [**Topic 16: The Standard Error**](StatQuest%20with%20Josh%20Starmer/16-standard-error.md) — The size of an estimate's wobble across repeated experiments.
* [**Topic 17: Confidence Intervals**](StatQuest%20with%20Josh%20Starmer/17-confidence-intervals.md) — A range built by a method that captures the true value a known fraction of the time.
* [**Topic 18: Bootstrapping, Part 1 — Main Ideas**](StatQuest%20with%20Josh%20Starmer/18-bootstrapping-main-ideas.md) — Resampling with replacement to approximate sampling variability.

#### Part IV: Likelihood & Maximum Likelihood Estimation

* [**Topic 19: Probability vs Likelihood**](StatQuest%20with%20Josh%20Starmer/19-probability-vs-likelihood.md) — Fixed distribution, ask about the data vs. fixed data, ask about the distribution.
* [**Topic 20: Maximum Likelihood**](StatQuest%20with%20Josh%20Starmer/20-maximum-likelihood.md) — Choosing parameters that make the observed data as likely as possible.
* [**Topic 21: MLE for the Normal Distribution**](StatQuest%20with%20Josh%20Starmer/21-mle-normal-distribution.md) — MLE recovers the sample mean and average squared deviation.
* [**Topic 22: MLE for the Binomial Distribution**](StatQuest%20with%20Josh%20Starmer/22-mle-binomial-distribution.md) *(Optional)* — MLE recovers $\hat{p} = k/n$ and derives binary cross-entropy.
* [**Topic 23: MLE for the Exponential Distribution**](StatQuest%20with%20Josh%20Starmer/23-mle-exponential-distribution.md) *(Optional)* — MLE gives the rate as one over the average waiting time.

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

## 💡 How Calculus Powers Machine Learning

| Mathematical Concept | Machine Learning / Data Science Role | Concrete Application |
| :--- | :--- | :--- |
| **Derivatives & Gradients** | Direction of steepest change on a loss surface | Gradient descent ($\theta \leftarrow \theta - \eta\nabla_\theta L$), learning rate selection |
| **Chain Rule** | Propagating error through composed layers | **Backpropagation**, reverse-mode automatic differentiation |
| **Product Rule** | Gradients of gated and multiplicative architectures | LSTM gates, attention $\text{softmax}(QK^T)V$, adapter layers |
| **Exponentials & Logarithms** | Probability, likelihood, and normalization | Softmax, sigmoid, cross-entropy, log-likelihood, weight decay |
| **Integration** | Expectations over continuous distributions | Expected risk, ROC-AUC, Bayesian evidence, partition functions |
| **Average Value of a Function** | The definition of every empirical loss | $\frac{1}{N}\sum_i \ell_i \to \mathbb{E}_p[\ell]$; why mini-batching is valid |
| **Second Derivatives & the Hessian** | Curvature of the loss landscape | Newton's method, L-BFGS, K-FAC, saddle-point analysis |
| **Taylor Series** | Local polynomial models of the objective | Trust regions, Neural Tangent Kernel, numerically stable softmax |
| **Implicit Differentiation** | Differentiating through constraints and fixed points | Deep Equilibrium Models, Neural ODEs, Lagrange multipliers in SVMs |
| **Limits & Continuity** | Requirements for gradient-based learning | Gradient checking, straight-through estimators, Gumbel-Softmax |

---

## 💡 How StatQuest Powers Machine Learning

| Statistical Concept | Machine Learning / Data Science Role | Concrete Application |
| :--- | :--- | :--- |
| **Bayes' Theorem** | Updating beliefs given evidence | Naive Bayes classifiers, spam filtering, Bayesian A/B testing |
| **Binomial & Normal Distributions** | Modeling binary outcomes and Gaussian noise | A/B test significance; MSE loss as a Gaussian noise assumption |
| **Covariance & Correlation** | Quantifying relationships between features | Covariance matrices feeding PCA; multicollinearity checks |
| **Central Limit Theorem** | Why averaged quantities behave predictably | Confidence intervals on batch losses and averaged metrics |
| **Standard Error & Confidence Intervals** | Quantifying uncertainty in an estimate | Honest reporting of model metrics; A/B test decisions |
| **Bootstrapping** | Resampling-based uncertainty for any statistic | Random Forests / bagging; confidence intervals on AUC, F1 |
| **Maximum Likelihood Estimation** | Fitting parameters by maximizing data probability | Derives MSE (Gaussian MLE) and binary cross-entropy (Bernoulli MLE) directly |

---

## 🔗 How the Modules Fit Together

```text
   ESSENCE OF LINEAR ALGEBRA          ESSENCE OF CALCULUS               STATQUEST
   (the STRUCTURE of space)           (how things CHANGE in it)     (uncertainty & inference)

      vectors, matrices                  derivatives, integrals        distributions, Bayes
      transformations                    rates and accumulation        expectation, covariance
      determinants, rank                 curvature, optimization       sampling, estimation
      eigenvalues                        Taylor approximation          likelihood, MLE
              \                                   /                          |
               \                                 /                          |
                +-------------------------------+                           |
                |     MULTIVARIABLE CALCULUS    |                           |
                |  gradients, Jacobians,        | <-------------------------+
                |  and the HESSIAN MATRIX       |     MLE optimization is
                +-------------------------------+     differentiation applied
                                |                      to a likelihood function
                                v
                   MACHINE LEARNING OPTIMIZATION
```

The Linear Algebra and Calculus modules meet at the **Hessian matrix**: calculus builds it out of second derivatives, and linear algebra tells you what its **eigenvalues** mean. StatQuest supplies the third leg — it is where a covariance matrix (Topic 09) becomes the input to an eigendecomposition (PCA), and where maximum likelihood (Topics 19–23) turns a probability assumption into the loss function that calculus then minimizes.

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
├── 3Blue1Brown - Essence of Calculus/        # [Completed: 12/12 Chapters]
│   ├── README.md                             # Module syllabus, index & ML concepts
│   ├── 01-essence-of-calculus.md             # Chapter 01
│   ├── 02-paradox-of-the-derivative.md       # Chapter 02
│   ├── ...                                   # Chapters 03 - 11
│   └── 12-what-they-wont-teach-you.md        # Chapter 12
├── Khan Academy - Linear Algebra/            # [Upcoming]
├── Khan Academy - Multivariable Calculus/    # [Upcoming]
├── Khan Academy - Statistics and Probability/# [Upcoming]
├── StatQuest with Josh Starmer/              # [Completed: 23/23 Topics]
│   ├── README.md                             # Topic index, ML concepts & syllabus
│   ├── 01-probability-distributions.md       # Topic 01
│   ├── ...                                   # Topics 02 - 22
│   └── 23-mle-exponential-distribution.md    # Topic 23
├── Month 1 - Build Tasks/                    # [Completed: 10/10 roadmap build tasks]
│   ├── README.md                             # Task map, results, how to run
│   ├── mathkit/                              # From-scratch implementations (NumPy)
│   ├── tests/                                # 36 tests vs NumPy / SciPy / scikit-learn
│   └── Week 1 … Week 4/                      # One notebook per task + figures
├── LICENSE                                   # MIT License
└── README.md                                 # Main repository index (You are here)
```

---

## 🚀 Navigation & Study Guide

* Every chapter/topic file includes **top and bottom navigation breadcrumbs** for seamless reading without navigating back to the folder.
* Look for the **`[!TIP]` Core Intuition** callout at the beginning of each chapter/topic for a high-level summary before diving into the details.
* Each Calculus chapter and StatQuest topic ends with a **Connection to Machine Learning & Data Science** table mapping the theory to concrete ML practice.
* Try answering each chapter's **Check Your Understanding** questions — or filling in each StatQuest topic's **"My one line"** callout — before revealing the derivations!

---

*Authored as part of the Data Science Journey. Continuously updated as new mathematical tracks are completed!*
