[⏮️ **Previous: Chapter 15 — Quick Eigenvalues Trick**](15-quick-eigenvalues.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [🏠 **Repository Home**](../README.md)

---

# Chapter 16: Abstract Vector Spaces
**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> A vector is not fundamentally an arrow, nor is it strictly a list of numbers. In modern mathematics, a **vector can be anything**—arrows, lists of numbers, polynomial functions, audio signals, or quantum states—as long as there is a sensible rule for **adding** two of them and **scaling** them by a number. Linear algebra is the study of these universal rules of addition and scaling.

---

### 1. What Are Vectors, Really?
Throughout this series, we have moved between two primary viewpoints:
1. **The Physics View:** Vectors are arrows pointing in space with magnitude and direction.
2. **The Computer Science View:** Vectors are ordered lists of numbers (e.g., feature arrays).

As you study deeper linear algebra (e.g., changing coordinate systems, computing determinants, or finding eigenvectors), you realize that geometric space exists **independently of coordinates**. Determinants measure area scaling, and eigenvectors stay on their own span—regardless of which coordinate system you choose. 

This raises the fundamental question: **Is a vector the coordinate list, the arrow, or something deeper?**

---

### 2. Functions as Vectors
To see how general vectors can be, consider **functions**. Functions behave just like vectors because they satisfy the two fundamental operations:

#### A. Function Addition
Adding two functions $f$ and $g$ creates a new function $(f+g)$:
$$ (f + g)(x) = f(x) + g(x) $$
* **Analogy:** This is completely analogous to adding vectors coordinate-by-coordinate, except that a function has **infinitely many coordinates** (one for every real number $x$).

#### B. Scalar Multiplication
Scaling a function $f$ by a number $c$ scales all of its outputs:
$$ (c \cdot f)(x) = c \cdot f(x) $$
* **Analogy:** Just like multiplying a 2D vector $\begin{bmatrix}x \\ y\end{bmatrix}$ by $2$ doubles every coordinate $\begin{bmatrix}2x \\ 2y\end{bmatrix}$, scaling a function doubles its output at every single point $x$.

---

### 3. The True Definition of Linearity
In Chapter 3, we defined a linear transformation visually: *grid lines stay parallel and evenly spaced, and the origin remains fixed*. But for functions or abstract spaces, grid lines aren't visible. 

The formal, universal definition of a **linear transformation (or operator)** $L$ relies on preserving two algebraic rules for any vectors $\vec{\mathbf{v}}, \vec{\mathbf{w}}$ and scalar $c$:

1. **Additivity:** 
   $$ L(\vec{\mathbf{v}} + \vec{\mathbf{w}}) = L(\vec{\mathbf{v}}) + L(\vec{\mathbf{w}}) $$
2. **Homogeneity (Scaling Property):** 
   $$ L(c \cdot \vec{\mathbf{v}}) = c \cdot L(\vec{\mathbf{v}}) $$

---

### 4. The Derivative as a Linear Transformation
Calculus provides a classic example of a linear operator on functions: **the derivative operator** $\frac{d}{dx}$.

* **Additivity:** $\frac{d}{dx}(f(x) + g(x)) = \frac{d}{dx}f(x) + \frac{d}{dx}g(x)$
* **Scaling:** $\frac{d}{dx}(c \cdot f(x)) = c \cdot \frac{d}{dx}f(x)$

#### Representing the Derivative as a Matrix
If we restrict our function space to **polynomials**, we can pick a natural basis:
$$ b_0(x) = 1, \quad b_1(x) = x, \quad b_2(x) = x^2, \quad b_3(x) = x^3, \quad \dots $$

Any polynomial, such as $P(x) = 5 + 4x + 5x^2 + x^3$, can be written as a coordinate vector in this infinite basis:
$$ \vec{\mathbf{p}} = \begin{bmatrix} 5 \\ 4 \\ 5 \\ 1 \\ 0 \\ \vdots \end{bmatrix} $$

Taking the derivative transforms this vector:
* $\frac{d}{dx}(1) = 0$
* $\frac{d}{dx}(x) = 1$
* $\frac{d}{dx}(x^2) = 2x$
* $\frac{d}{dx}(x^3) = 3x^2$

We can construct an **infinite matrix** where each column records the derivative of a basis function:

$$ \mathbf{D} = \begin{bmatrix} 0 & 1 & 0 & 0 & 0 & \dots \\ 0 & 0 & 2 & 0 & 0 & \dots \\ 0 & 0 & 0 & 3 & 0 & \dots \\ 0 & 0 & 0 & 0 & 4 & \dots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} $$

Multiplying $\mathbf{D} \cdot \vec{\mathbf{p}}$ yields:
$$ \begin{bmatrix} 0 & 1 & 0 & 0 & \dots \\ 0 & 0 & 2 & 0 & \dots \\ 0 & 0 & 0 & 3 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \begin{bmatrix} 5 \\ 4 \\ 5 \\ 1 \\ \vdots \end{bmatrix} = \begin{bmatrix} 4 \\ 10 \\ 3 \\ 0 \\ \vdots \end{bmatrix} \implies 4 + 10x + 3x^2 $$

> **Key Insight:** Taking a derivative in calculus and multiplying a matrix by a vector in linear algebra are fundamentally **the exact same operation** expressed in different domains!

---

### 5. Abstract Vector Spaces & Axioms
A **vector space** is any collection of objects where addition and scalar multiplication are defined and satisfy **8 fundamental rules (Axioms)**:

| # | Axiom Name | Requirement for all vectors $\vec{\mathbf{u}}, \vec{\mathbf{v}}, \vec{\mathbf{w}}$ and scalars $a, b$ |
| :--- | :--- | :--- |
| 1 | **Associativity of Addition** | $\vec{\mathbf{u}} + (\vec{\mathbf{v}} + \vec{\mathbf{w}}) = (\vec{\mathbf{u}} + \vec{\mathbf{v}}) + \vec{\mathbf{w}}$ |
| 2 | **Commutativity of Addition** | $\vec{\mathbf{u}} + \vec{\mathbf{v}} = \vec{\mathbf{v}} + \vec{\mathbf{u}}$ |
| 3 | **Identity Element of Addition** | There exists a zero vector $\vec{\mathbf{0}}$ such that $\vec{\mathbf{v}} + \vec{\mathbf{0}} = \vec{\mathbf{v}}$ |
| 4 | **Inverse Elements of Addition** | For every $\vec{\mathbf{v}}$, there exists $-\vec{\mathbf{v}}$ such that $\vec{\mathbf{v}} + (-\vec{\mathbf{v}}) = \vec{\mathbf{0}}$ |
| 5 | **Compatibility of Scalar Multiplication** | $a(b\vec{\mathbf{v}}) = (ab)\vec{\mathbf{v}}$ |
| 6 | **Identity Element of Scalar Multiplication** | $1 \cdot \vec{\mathbf{v}} = \vec{\mathbf{v}}$ |
| 7 | **Distributivity over Vector Addition** | $a(\vec{\mathbf{u}} + \vec{\mathbf{v}}) = a\vec{\mathbf{u}} + a\vec{\mathbf{v}}$ |
| 8 | **Distributivity over Scalar Addition** | $(a + b)\vec{\mathbf{v}} = a\vec{\mathbf{v}} + b\vec{\mathbf{v}}$ |

#### The "Interface" Analogy
These 8 axioms act like a **software interface** or contract. Mathematicians prove theorems using *only* these 8 axioms. If you create a new mathematical object (like audio signals or quantum wavefunctions) and verify that it satisfies these 8 rules, **you automatically get access to all of linear algebra**—eigenvalues, projections, transformations, and basis changes—for free!

---

### 6. Summary of the Series
Linear algebra is powerful because it provides a unified language for manipulation:
* **Geometry** gives us visual intuition (arrows, grids, rotations).
* **Numerics** gives us computational tools (matrices, arrays, algorithms).
* **Abstraction** connects them all, allowing us to solve complex real-world problems in physics, machine learning, signal processing, and computer science using a single framework.

---

### 7. Check Your Understanding

**Q1: Why can functions be considered vectors in an infinite-dimensional space?**
<details>
<summary><b>Reveal Answer</b></summary>
Because functions can be added together $((f+g)(x) = f(x)+g(x))$ and scaled by numbers $((c\cdot f)(x) = c\cdot f(x))$ while satisfying all 8 vector space axioms. Evaluating a function at each input $x$ is analogous to reading off a coordinate value, and since there are infinitely many real numbers $x$, a continuous function has infinitely many coordinates.
</details>

**Q2: Is the operation $T(f(x)) = f(x) + 1$ a linear transformation on the space of functions?**
<details>
<summary><b>Reveal Answer & Proof</b></summary>
<b>No.</b> It fails both conditions:
1. <b>Additivity fails:</b> $T(f + g) = (f(x) + g(x)) + 1$, but $T(f) + T(g) = (f(x) + 1) + (g(x) + 1) = f(x) + g(x) + 2$. Since $f(x)+g(x)+1 \neq f(x)+g(x)+2$, it is not additive.
2. <b>Homogeneity fails:</b> $T(c\cdot f) = c\cdot f(x) + 1$, whereas $c \cdot T(f) = c(f(x) + 1) = c\cdot f(x) + c$.
3. <b>Origin check:</b> The zero function $f(x) = 0$ is mapped to $T(0) = 1$, not the zero function $0$.
</details>

---

[⏮️ **Previous: Chapter 15 — Quick Eigenvalues Trick**](15-quick-eigenvalues.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [🏠 **Repository Home**](../README.md)
