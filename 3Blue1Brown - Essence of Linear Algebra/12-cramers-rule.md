[⏮️ **Previous: Chapter 11 — Cross Products & Linear Transformations**](11-cross-products-extended.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 13 — Change of Basis** ⏭️](13-change-of-basis.md)

---

# Chapter 12: Cramer's Rule, Explained Geometrically

**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> Solving a linear system $A\vec{\mathbf{x}} = \vec{\mathbf{v}}$ is usually taught as a mechanical process of row reduction. Cramer's rule offers an alternative geometric view: each coordinate of the unknown vector $\vec{\mathbf{x}}$ can be understood as an **area (or volume) ratio**. By measuring how a linear transformation scales areas, we can isolate each unknown coordinate using determinants without ever explicitly computing the inverse matrix.

---

### 1. Motivation: Why Study Cramer's Rule?

In practical software engineering and machine learning, **Gaussian elimination** is preferred over Cramer's rule because it is vastly faster ($O(n^3)$ operations vs $O(n^4)$ or $O(n!)$ for naive determinant evaluation). 

So why study Cramer's rule?

1. **Geometric Intuition:** It connects linear systems, determinants, and spatial volume scaling into one elegant picture.
2. **Theoretical Value:** It provides an explicit symbolic formula for solutions, which is invaluable in analytical calculus and physics derivations.
3. **Conceptual Unification:** It deepens your understanding of how transformations morph fundamental coordinate shapes.

---

### 2. The Setup: A Linear System as a Spatial Puzzle

Consider a system of two linear equations with two unknowns ($x, y$):

$$ A \vec{\mathbf{x}} = \vec{\mathbf{v}} \implies \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} $$

* **Geometric Framing:** We have a known linear transformation $A$, and a known target output vector $\vec{\mathbf{v}}$. We want to find the mystery input vector $\vec{\mathbf{x}} = \begin{bmatrix} x \\ y \end{bmatrix}$ that lands directly on $\vec{\mathbf{v}}$ after $A$ is applied.
* **Assumption ($\det(A) \neq 0$):** We assume the determinant is non-zero so space does not collapse to a lower dimension. This guarantees that every output vector $\vec{\mathbf{v}}$ corresponds to a **single, unique** input vector $\vec{\mathbf{x}}$.

```text
       Input Space (Pre-Transform)                 Output Space (Post-Transform)
             y                                          y
             ^                                          ^         A(x) = v
             |   x = [x, y]                             |         /
             |   .                                      |        /
             |  /|                                      |       /
  -----------+---+-+---> x                  ------------+------+------> x
             |   |                                      |     /
             |   x                                      |    /  A(i_hat)
             |                                          |   v
```

---

### 3. A Failed Shortcut: Why Dot Products Don't Work

A natural first thought might be: *"In the input space, $x = \vec{\mathbf{x}} \cdot \hat{\imath}$ and $y = \vec{\mathbf{x}} \cdot \hat{\jmath}$. Can we just take the dot product of the output vector $\vec{\mathbf{v}}$ with the transformed basis vectors $A(\hat{\imath})$ and $A(\hat{\jmath})$?"*

**Why this fails for general matrices:**
Most linear transformations stretch space, warp grid lines, and alter angles between vectors. Two vectors that started out perpendicular ($\hat{\imath} \cdot \hat{\jmath} = 0$) will usually **not** remain perpendicular after transformation.

```text
Pre-Transform (Perpendicular):             Post-Transform (Angles Warped):
       j_hat                                       A(j_hat)
        ^                                           /
        |                                          /  Angle < 90°
        +---> i_hat                               +------> A(i_hat)
     (dot = 0)                                 (dot != 0)
```

> **The Special Exception (Orthonormal Transformations):**
> If $A$ is an **orthonormal matrix** (a rigid rotation or reflection with no stretching or squishing), dot products **are** preserved. In that rare case, $x = \vec{\mathbf{a}}_1 \cdot \vec{\mathbf{v}}$ and $y = \vec{\mathbf{a}}_2 \cdot \vec{\mathbf{v}}$. For all general matrices, we need a property that *does* transform predictably.

---

### 4. The Key Insight: Coordinates as Areas and Volumes

Instead of dot products, we look for a geometric quantity that transforms by a **constant scale factor**. That quantity is **area (in 2D)** or **volume (in 3D)**, and the constant scale factor is the **determinant** ($\det(A)$).

#### A. Expressing Coordinates as Areas in 2D

In the 2D xy-plane, consider the unit basis vectors $\hat{\imath} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\hat{\jmath} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$:

1. **Measuring the $y$-coordinate:** Form the parallelogram spanned by $\hat{\imath}$ and the mystery input vector $\vec{\mathbf{x}} = \begin{bmatrix} x \\ y \end{bmatrix}$.
   * $\text{Base} = 1$ (length of $\hat{\imath}$)
   * $\text{Height} = y$ ($y$-component of $\vec{\mathbf{x}}$)
   * $\text{Area} = \text{Base} \times \text{Height} = 1 \cdot y = y$

```text
The y-coordinate of x is the area of a parallelogram:

      y
      ^
      |            *-------------* x = [x, y]
      |           /             /
      |          /   Area = y  /   <- height is y, base is 1
      |         /             /
    0 -+-------*-------------*------> x
      |     (0,0)    i-hat
      |        |<----->|
      |         base = 1

  Area( i-hat , x ) = base x height = 1 * y = y

  So the second coordinate of x is literally a signed area.
```

2. **Measuring the $x$-coordinate:** Form the parallelogram spanned by $\vec{\mathbf{x}}$ and $\hat{\jmath}$.
   * $\text{Base} = 1$ (length of $\hat{\jmath}$)
   * $\text{Height} = x$ ($x$-component of $\vec{\mathbf{x}}$)
   * $\text{Area} = \text{Base} \times \text{Height} = 1 \cdot x = x$

> **Signed Area:** We use signed areas (orientations). If $y$ is negative, the orientation of the parallelogram $(\hat{\imath}, \vec{\mathbf{x}})$ is flipped, making its determinant negative. Thus, **Area = Coordinate** holds for negative values as well!

#### B. Expressing Coordinates as Volumes in 3D

In 3D space, the $z$-coordinate of $\vec{\mathbf{x}} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ is the signed volume of the **parallelepiped** spanned by $\hat{\imath}, \hat{\jmath}$, and $\vec{\mathbf{x}}$:
$$\text{Volume}(\hat{\imath}, \hat{\jmath}, \vec{\mathbf{x}}) = \text{Base Area}(\hat{\imath}, \hat{\jmath}) \times \text{Height} = 1 \cdot z = z$$

---

### 5. Following Areas into the Output Space

Now, apply the linear transformation $A$ to the entire space:

1. $\hat{\imath}$ transforms into the first column of $A$, denoted $\vec{\mathbf{a}}_1$.
2. $\hat{\jmath}$ transforms into the second column of $A$, denoted $\vec{\mathbf{a}}_2$.
3. The mystery input vector $\vec{\mathbf{x}}$ transforms into the known target vector $\vec{\mathbf{v}}$.

#### Deriving $y$:

* **Before Transformation:** $\text{Area}(\hat{\imath}, \vec{\mathbf{x}}) = y$
* **After Transformation:** The parallelogram $(\hat{\imath}, \vec{\mathbf{x}})$ becomes $(\vec{\mathbf{a}}_1, \vec{\mathbf{v}})$.
* **Determinant Property:** A linear transformation $A$ scales **all** areas in space by exactly $\det(A)$.
$$\text{Area}(\vec{\mathbf{a}}_1, \vec{\mathbf{v}}) = \det(A) \cdot \text{Area}(\hat{\imath}, \vec{\mathbf{x}}) = \det(A) \cdot y$$

Solving for $y$:
$$y = \frac{\text{Area}(\vec{\mathbf{a}}_1, \vec{\mathbf{v}})}{\det(A)} = \frac{\det \begin{bmatrix} | & | \\ \vec{\mathbf{a}}_1 & \vec{\mathbf{v}} \\ | & | \end{bmatrix}}{\det(A)}$$

#### Deriving $x$:

* **Before Transformation:** $\text{Area}(\vec{\mathbf{x}}, \hat{\jmath}) = x$
* **After Transformation:** The parallelogram $(\vec{\mathbf{x}}, \hat{\jmath})$ becomes $(\vec{\mathbf{v}}, \vec{\mathbf{a}}_2)$.
$$\text{Area}(\vec{\mathbf{v}}, \vec{\mathbf{a}}_2) = \det(A) \cdot \text{Area}(\vec{\mathbf{x}}, \hat{\jmath}) = \det(A) \cdot x$$

Solving for $x$:
$$x = \frac{\text{Area}(\vec{\mathbf{v}}, \vec{\mathbf{a}}_2)}{\det(A)} = \frac{\det \begin{bmatrix} | & | \\ \vec{\mathbf{v}} & \vec{\mathbf{a}}_2 \\ | & | \end{bmatrix}}{\det(A)}$$

---

### 6. General Formula for Cramer's Rule

For an $n \times n$ linear system $A \vec{\mathbf{x}} = \vec{\mathbf{v}}$, each coordinate $x_i$ of the solution vector $\vec{\mathbf{x}}$ is given by:

$$ x_i = \frac{\det(A_i)}{\det(A)} $$

where $A_i$ is the matrix formed by **replacing the $i$-th column of $A$ with the target vector $\vec{\mathbf{v}}$**:

$$ A_i = \begin{bmatrix} | & & | & | & | \\ \vec{\mathbf{a}}_1 & \dots & \vec{\mathbf{a}}_{i-1} & \mathbf{\vec{\mathbf{v}}} & \vec{\mathbf{a}}_{i+1} & \dots & \vec{\mathbf{a}}_n \\ | & & | & | & | \end{bmatrix} $$

---

### 7. Worked Numerical Example

Solve the following $2 \times 2$ linear system using Cramer's rule:

$$ \begin{bmatrix} 2 & -1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix} $$

#### Step 1: Compute $\det(A)$

$$ \det(A) = \det \begin{bmatrix} 2 & -1 \\ 0 & 1 \end{bmatrix} = (2)(1) - (-1)(0) = 2 $$

#### Step 2: Compute $x$ (Replace Column 1 with $\vec{\mathbf{v}} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$)

$$ A_x = \begin{bmatrix} 4 & -1 \\ 2 & 1 \end{bmatrix} $$
$$ \det(A_x) = (4)(1) - (-1)(2) = 4 + 2 = 6 $$
$$ x = \frac{\det(A_x)}{\det(A)} = \frac{6}{2} = 3 $$

#### Step 3: Compute $y$ (Replace Column 2 with $\vec{\mathbf{v}} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$)

$$ A_y = \begin{bmatrix} 2 & 4 \\ 0 & 2 \end{bmatrix} $$
$$ \det(A_y) = (2)(2) - (4)(0) = 4 - 0 = 4 $$
$$ y = \frac{\det(A_y)}{\det(A)} = \frac{4}{2} = 2 $$

#### Verification:

$$ \begin{bmatrix} 2 & -1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 2(3) - 1(2) \\ 0(3) + 1(2) \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix} \quad \checkmark $$

---

### 8. Summary Comparison: Gaussian Elimination vs. Cramer's Rule

| Feature | Gaussian Elimination | Cramer's Rule |
| :--- | :--- | :--- |
| **Computational Complexity** | $O(n^3)$ (Efficient) | $O(n \cdot n!) \to O(n^4)$ (Very Slow for large $n$) |
| **Primary Use Case** | Numerical computation in software & ML | Symbolic algebraic derivations & theory |
| **Geometric Intuition** | Step-by-step row reduction | Ratios of scaled areas and volumes |
| **Requires Matrix Inversion?** | No | No |

---

### 9. Check Your Understanding

**Q1: What is the $x$-coordinate solution for the system $\begin{bmatrix} 1 & 3 \\ -2 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 2 \end{bmatrix}$ using Cramer's rule?**

<details>
<summary><b>Reveal Answer & Step-by-Step Solution</b></summary>

1. **Compute $\det(A)$:**
   $$ \det(A) = \det \begin{bmatrix} 1 & 3 \\ -2 & 0 \end{bmatrix} = (1)(0) - (3)(-2) = 0 + 6 = 6 $$
2. **Compute $\det(A_x)$:** (Replace column 1 with $\begin{bmatrix} 5 \\ 2 \end{bmatrix}$)
   $$ \det(A_x) = \det \begin{bmatrix} 5 & 3 \\ 2 & 0 \end{bmatrix} = (5)(0) - (3)(2) = 0 - 6 = -6 $$
3. **Calculate $x$:**
   $$ x = \frac{\det(A_x)}{\det(A)} = \frac{-6}{6} = -1 $$
</details>

**Q2: Why does Cramer's rule fail if $\det(A) = 0$?**

<details>
<summary><b>Reveal Answer</b></summary>

If $\det(A) = 0$, the transformation squishes space into a lower dimension (a line or point in 2D, or a plane/line/point in 3D). The area scale factor is 0, making division by $\det(A)$ impossible ($\frac{\det(A_i)}{0}$). Geometrically, either no input lands on $\vec{\mathbf{v}}$ (no solution) or infinitely many inputs do (infinite solutions).
</details>

---

[⏮️ **Previous: Chapter 11 — Cross Products & Linear Transformations**](11-cross-products-extended.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 13 — Change of Basis** ⏭️](13-change-of-basis.md)
