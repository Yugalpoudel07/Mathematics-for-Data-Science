[⏮️ **Previous: Chapter 13 — Change of Basis**](13-change-of-basis.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 15 — Quick Eigenvalues Trick** ⏭️](15-quick-eigenvalues.md)

---

# Chapter 14: Eigenvectors and Eigenvalues

**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> When a linear transformation acts on space, most vectors get rotated away from the line they started on. **Eigenvectors** are those special vectors that stay on their own span (line passing through the origin and their tip)—they are only stretched, squished, or flipped. The factor by which an eigenvector is scaled is called its **eigenvalue ($\lambda$)**. Choosing eigenvectors as your basis (an **eigenbasis**) makes complex operations—like matrix exponentiation—effortless.

---

### 1. Geometric Intuition: Vectors That Stay on Their Line

When a matrix $\mathbf{A}$ transforms space, it generally rotates, stretches, or shears vectors. 

* **Generic Vector:** Most vectors get knocked off the line passing through their tail and tip.
* **Eigenvector:** Stays strictly on its original span line. The transformation acts on it like simple scalar multiplication:
  $$ \mathbf{A}\vec{\mathbf{v}} = \lambda \vec{\mathbf{v}} $$

#### Concrete 2D Example

Consider the linear transformation represented by $\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$:

```text
Eigenvectors of A = [[3, 1], [0, 2]]:

                              y
                              ^
                              |
      eigenvector [1, -1]     |      eigenvector [1, 0]
      (stretched by 2)        |      (stretched by 3)
             \                |
              \               |
               \              |
   -------------+-------------o=============>=========> x
                 \            |             i-hat   3 * i-hat
                  \           |
                   v          |

  Every other vector gets knocked OFF its original line by A.
  These two lines are the only ones that survive the transformation
  intact - each is merely scaled by its eigenvalue.
```

1. **The $x$-axis ($\hat{\imath}$):** $\mathbf{A}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \end{bmatrix} = 3\begin{bmatrix} 1 \\ 0 \end{bmatrix}$. 
   * The $x$-axis stays fixed on its line and is stretched by a factor of $3$. 
   * **Eigenvector:** $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$, **Eigenvalue ($\lambda_1$):** $3$.
2. **The Diagonal Line ($\begin{bmatrix} 1 \\ -1 \end{bmatrix}$):** $\mathbf{A}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix} = 2\begin{bmatrix} 1 \\ -1 \end{bmatrix}$. 
   * All vectors on this diagonal line remain on the line and stretch by a factor of $2$.
   * **Eigenvector:** $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$, **Eigenvalue ($\lambda_2$):** $2$.

---

### 2. Physical & High-Dimensional Value

Why look for eigenvectors?

* **3D Rotations:** The eigenvector of a 3D rotation matrix is its **axis of rotation** (with eigenvalue $\lambda = 1$, since rotations preserve lengths). Finding the axis and angle of rotation gives far deeper insight than staring at a $3 \times 3$ grid of 9 numbers.
* **Coordinate-Independent Understanding:** Columns of a matrix tell you where basis vectors land in a *specific* coordinate system. Eigenvectors and eigenvalues describe what the transformation actually *does* independent of coordinate choices.

---

### 3. The Algebraic Framework: Deriving the Characteristic Equation

We want to find non-zero vectors $\vec{\mathbf{v}}$ and scalars $\lambda$ satisfying:
$$ \mathbf{A}\vec{\mathbf{v}} = \lambda \vec{\mathbf{v}} $$

#### Step-by-Step Derivation

1. **Express scalar multiplication as matrix multiplication:**
   Using the identity matrix $\mathbf{I}$, we write $\lambda \vec{\mathbf{v}} = (\lambda \mathbf{I})\vec{\mathbf{v}}$:
   $$ \mathbf{A}\vec{\mathbf{v}} = (\lambda \mathbf{I})\vec{\mathbf{v}} $$

2. **Subtract right-hand side and factor out $\vec{\mathbf{v}}$:**
   $$ (\mathbf{A} - \lambda \mathbf{I})\vec{\mathbf{v}} = \vec{\mathbf{0}} $$

3. **Apply the zero determinant condition:**
   For a **non-zero** vector $\vec{\mathbf{v}}$ to be compressed into the zero vector $\vec{\mathbf{0}}$, the transformation $(\mathbf{A} - \lambda \mathbf{I})$ must squish space into a lower dimension (it must have a non-trivial null space).
   This happens if and only if its **determinant is zero**:
   $$ \det(\mathbf{A} - \lambda \mathbf{I}) = 0 $$

This equation is called the **characteristic equation**.

---

### 4. Step-by-Step Computational Process

#### Example: Finding Eigenvalues & Eigenvectors for $\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$

1. **Form the matrix $(\mathbf{A} - \lambda \mathbf{I})$:**
   $$ \mathbf{A} - \lambda \mathbf{I} = \begin{bmatrix} 3 - \lambda & 1 \\ 0 & 2 - \lambda \end{bmatrix} $$

2. **Compute the determinant and set to zero:**
   $$ \det(\mathbf{A} - \lambda \mathbf{I}) = (3 - \lambda)(2 - \lambda) - (1)(0) = (3 - \lambda)(2 - \lambda) = 0 $$
   * **Eigenvalues:** $\lambda_1 = 3$ and $\lambda_2 = 2$.

3. **Find the eigenvectors for $\lambda = 2$:**
   Plug $\lambda = 2$ back into $(\mathbf{A} - \lambda \mathbf{I})\vec{\mathbf{v}} = \vec{\mathbf{0}}$:
   $$ \begin{bmatrix} 3 - 2 & 1 \\ 0 & 2 - 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} $$
   This gives the equation $x + y = 0 \implies x = -y$.
   * **Eigenvector line:** All vectors proportional to $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$.

---

### 5. Geometric Edge Cases

| Transformation | Matrix Example | Eigenvalue / Eigenvector Behavior | Geometric Explanation |
| :--- | :--- | :--- | :--- |
| **90° Rotation** | $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | No real eigenvalues ($\lambda^2 + 1 = 0 \implies \lambda = \pm i$) | Every vector is rotated off its span; no line remains invariant. |
| **Shear** | $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ | Single eigenvalue $\lambda = 1$; single eigenvector line (x-axis) | Only the x-axis stays fixed; all other vectors tilt off their original span. |
| **Uniform Scale** | $\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ | Single eigenvalue $\lambda = 2$; **every** vector is an eigenvector | Every vector in the plane is stretched by 2 without changing direction. |

---

### 6. Working in an Eigenbasis (Diagonalization)

#### A. Diagonal Matrices

If a matrix $\mathbf{D}$ is diagonal, all its basis vectors are eigenvectors:
$$ \mathbf{D} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} $$
Computing powers of a diagonal matrix is computationally trivial:
$$ \mathbf{D}^{100} = \begin{bmatrix} \lambda_1^{100} & 0 \\ 0 & \lambda_2^{100} \end{bmatrix} $$

#### B. Diagonalizing via Change of Basis

If a matrix $\mathbf{A}$ has enough eigenvectors to span the space, we construct a **Change of Basis Matrix $\mathbf{S}$** whose columns are those eigenvectors.

1. **Transform into Eigenbasis:**
   $$ \mathbf{D} = \mathbf{S}^{-1} \mathbf{A} \mathbf{S} $$
2. **Compute Matrix Powers easily:**
   $$ \mathbf{A}^n = \mathbf{S} \mathbf{D}^n \mathbf{S}^{-1} = \mathbf{S} \begin{bmatrix} \lambda_1^n & 0 \\ 0 & \lambda_2^n \end{bmatrix} \mathbf{S}^{-1} $$

#### Real-World Case Study: Unlocking the Fibonacci Formula

The matrix $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$ advances Fibonacci state pairs $\begin{bmatrix} F_n \\ F_{n+1} \end{bmatrix}$.
By finding its eigenvalues $\lambda_1 = \frac{1 + \sqrt{5}}{2}$ (Golden Ratio $\phi$) and $\lambda_2 = \frac{1 - \sqrt{5}}{2}$, diagonalizing $\mathbf{A}^n = \mathbf{S} \mathbf{D}^n \mathbf{S}^{-1}$ directly derives Binet's closed-form formula for the $n$-th Fibonacci number:
$$ F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} = \frac{\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n}{\sqrt{5}} $$

---

### 7. Check Your Understanding

**Q1: What are the eigenvalues and eigenvectors of the 2D reflection matrix $\mathbf{A} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ across the x-axis?**
<details>
<summary><b>Reveal Answer & Geometric Explanation</b></summary>

1. **Geometric View:** 
   - Vectors along the x-axis stay unchanged ($\lambda_1 = 1$).
   - Vectors along the y-axis get flipped upside down ($\lambda_2 = -1$).
2. **Algebraic Calculation:**
   $$ \det(\mathbf{A} - \lambda \mathbf{I}) = (1 - \lambda)(-1 - \lambda) = 0 \implies \lambda_1 = 1, \lambda_2 = -1 $$
* **Eigenvectors:** $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ with $\lambda = 1$, and $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ with $\lambda = -1$.
</details>

**Q2: Why does a $3\times3$ rotation matrix always have at least one real eigenvalue equal to 1?**
<details>
<summary><b>Reveal Answer</b></summary>

Every 3D rotation has a line of points that stays fixed during the rotation—this line is the **axis of rotation**. Any vector lying on this axis is unchanged by the rotation, meaning $\mathbf{A}\vec{\mathbf{v}} = 1\vec{\mathbf{v}}$. Thus, $\vec{\mathbf{v}}$ is an eigenvector with eigenvalue $\lambda = 1$.
</details>

---

[⏮️ **Previous: Chapter 13 — Change of Basis**](13-change-of-basis.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 15 — Quick Eigenvalues Trick** ⏭️](15-quick-eigenvalues.md)
