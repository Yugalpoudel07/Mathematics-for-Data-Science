[⏮️ **Previous: Chapter 06 — The Determinant: Scaling Space**](06-determinant.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 08 — Nonsquare Matrices & Dimensionality** ⏭️](08-nonsquare-matrices-dimension-transformations.md)

---

# Chapter 07: Inverse Matrices, Column Space, and Null Space
**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> Solving a linear system of equations $A\vec{\mathbf{x}} = \vec{\mathbf{v}}$ is not about performing algebraic tricks on paper. Geometrically, the matrix $A$ represents a linear transformation (a way of stretching or squishing space), the vector $\vec{\mathbf{v}}$ is a target landing spot, and the vector $\vec{\mathbf{x}}$ is our "mystery starting location". Solving the equation means finding which starting vector $\vec{\mathbf{x}}$ lands exactly on our target $\vec{\mathbf{v}}$.

---

### 1. Linear Systems of Equations as Spatial Transformations
Usually, we are introduced to systems of linear equations as algebraic grids of constants and variables:
$$
\begin{aligned}
2x + 2y &= -4 \\
1x + 3y &= -1
\end{aligned}
$$

We can package this system into a single matrix-vector equation:
$$
\underbrace{\begin{bmatrix} 2 & 2 \\ 1 & 3 \end{bmatrix}}_{\text{Matrix } A} \underbrace{\begin{bmatrix} x \\ y \end{bmatrix}}_{\text{Variable } \vec{\mathbf{x}}} = \underbrace{\begin{bmatrix} -4 \\ -1 \end{bmatrix}}_{\text{Target } \vec{\mathbf{v}}}
$$

Rather than thinking about variables intermingling, we can interpret this geometrically:
* **The Matrix $A$** is a machine that morphs space.
* **The Vector $\vec{\mathbf{x}}$** is some mystery input vector in our starting space.
* **The Vector $\vec{\mathbf{v}}$** is a known target vector in the transformed space.
* **The Equation $A\vec{\mathbf{x}} = \vec{\mathbf{v}}$** asks: *"Which vector $\vec{\mathbf{x}}$ lands on $\vec{\mathbf{v}}$ after we play the transformation $A$?"*

```text
       Starting Space (x)                 Transformed Space (v)
            y                                    y
            ^                                    ^
            |  ? [Mystery x]                     |       * [Target v]
            | /                                  |      /
            |/                                   |     / 
     -------+-------> x                   -------+-------> x
           /|   (Where did it                      /|
          / |    come from?)                      / |
            |                                       |
```

The behavior of our solutions depends entirely on whether $A$ collapses space into a lower dimension (i.e., whether its determinant is zero).

---

### 2. The Non-Zero Determinant Case: Inverse Matrices ($A^{-1}$)
If the determinant of $A$ is **not zero** ($\det(A) \neq 0$), space does not collapse. Every unique point in our starting space lands on a unique point in our ending space. 

In this case, there will always be **one and only one** vector $\vec{\mathbf{x}}$ that lands on our target $\vec{\mathbf{v}}$. We find it by **playing the transformation in reverse** (rewinding the tape):

```text
Playing the Tape Forward (A):
  [Mystery Vector x]  ======(Apply Transformation A)======>  [Target Vector v]

Rewinding the Tape (A⁻¹):
  [Mystery Vector x]  <=====(Apply Inverse Transform)=====  [Target Vector v]
```

This reverse transformation is called the **Inverse of $A$**, denoted as $A^{-1}$.
* If $A$ is a **$90^\circ$ counterclockwise rotation**, its inverse $A^{-1}$ is a **$90^\circ$ clockwise rotation**.
* If $A$ is a **rightward shear** that moves $\hat{\jmath}$ one unit right, its inverse $A^{-1}$ is a **leftward shear** that moves $\hat{\jmath}$ one unit left.

#### The Algebraic Definition of Inverse
If you play a transformation ($A$) and then immediately play its inverse ($A^{-1}$), you end up exactly where you started. Algebraically, this means multiplying a matrix by its inverse yields the **Identity Matrix ($I$)**, representing the "do-nothing" transformation:
$$ A^{-1}A = I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} $$

To solve our system of equations, we multiply both sides by the inverse:
$$
\begin{aligned}
A\vec{\mathbf{x}} &= \vec{\mathbf{v}} \\
A^{-1}A\vec{\mathbf{x}} &= A^{-1}\vec{\mathbf{v}} \\
\vec{\mathbf{x}} &= A^{-1}\vec{\mathbf{v}}
\end{aligned}
$$
Geometrically, this means we take our target vector $\vec{\mathbf{v}}$, apply the reverse transformation $A^{-1}$, and find exactly where our mystery vector $\vec{\mathbf{x}}$ started.

---

### 3. The Zero Determinant Case: Irreversibility
If the determinant of $A$ is **zero** ($\det(A) = 0$), the transformation squishes space into a lower dimension (such as a 2D plane collapsing onto a 1D line or a 3D space flattening into a 2D plane).

In this case, **no inverse matrix $A^{-1}$ exists**. 
* **The Reason:** You cannot "unsquish" a line to recreate a plane. A single point cannot be unmapped into a whole line of points, because mathematical functions can only map a single input to a single output. If you've lost an entire dimension of information, you cannot reconstruct it out of nothing.

```text
Collapsing 2D Space to a 1D Line (det = 0):
      y                                          y
      ^                                          ^    [All of space squished]
      |   /                                      |  /
      |  /  (v₁, v₂, v₃)                         | /  L(v₁)
      | /                                        |/   L(v₂) = L(v₃)
 -----+-----> x          ======== A =======> ----+-----> x
     /|                                         /|
    / |                                        / |
   /  |                                       /  |
   
  You cannot "unsquish" L(v₂) back to its original unique vector because we 
  no longer know if it started as v₂ or v₃. Information has been permanently lost.
```

Even without an inverse, a solution to $A\vec{\mathbf{x}} = \vec{\mathbf{v}}$ can still exist. However, you have to be **lucky** enough for your target vector $\vec{\mathbf{v}}$ to land exactly on the line or plane where space was squished.

---

### 4. Column Space and Rank
To describe these collapsed spaces with precision, we use the terms **Rank** and **Column Space**.

#### A. Rank: The Number of Output Dimensions
The **Rank** of a matrix is simply the **number of dimensions in the output of the transformation**:
* **Rank 1:** Space is squished down onto a **1D line**.
* **Rank 2:** Space is squished down onto a **2D plane**.
* **Rank 3:** The output spans a full **3D volume**.

When the rank of a matrix is as high as it can possibly be (equal to the number of columns), we say the matrix is **Full Rank**. This means no dimensions were lost during the transformation.

#### B. Column Space: The Reachable Span
The set of all possible output vectors we can reach after applying a transformation is called the **Column Space** of the matrix.
* **Why "Column" Space?** The columns of a matrix tell us exactly where our basis vectors ($\hat{\imath}$, $\hat{\jmath}$, etc.) land after the transformation. Because every vector in space is a linear combination of these basis vectors, the set of all possible outputs is simply the **span of the columns** of the matrix.
* **Rank Redefined:** A more formal definition of Rank is the **number of dimensions in the Column Space** of a matrix.

Therefore, a system $A\vec{\mathbf{x}} = \vec{\mathbf{v}}$ has a solution if and only if the target vector $\vec{\mathbf{v}}$ lies within the **Column Space** of $A$.

---

### 5. Null Space (The Kernel)
When a transformation collapses space onto a lower dimension, many non-zero vectors are flattened directly into the origin $(0,0)$. 

The set of all vectors that land **exactly on the origin (the zero vector $\vec{\mathbf{0}}$)** after the transformation is called the **Null Space** or the **Kernel** of the matrix.

```text
Visualizing Null Space:
      y                                          y
      ^   / [Null Space Line]                    ^   
      |  /                                       |   
      | /  v₁ (non-zero vector)                  | 
 -----+-----> x          ======== A =======> ----+-----> x
     /|                                         /| \
    / |  v₂ (non-zero vector)                  / |  A(v₁) = A(v₂) = (0,0)
   /  |                                       /  |
   
   An entire line of non-zero vectors collapses down to a single point 
   at the origin. This line of collapsed vectors is the Null Space.
```

* **In 2D:** If a transformation squishes 2D space onto a 1D line, there is a separate 1D line of vectors (the Null Space) that get flattened onto the origin.
* **In 3D:**
  * If space squishes onto a **2D plane**, there is a **1D line** of vectors that land on the origin.
  * If space squishes onto a **1D line**, there is a **2D plane** of vectors that land on the origin.

#### Null Space and Equations
In terms of linear systems of equations, if we are trying to solve:
$$ A\vec{\mathbf{x}} = \vec{\mathbf{0}} $$

The **Null Space** gives us the **set of all possible solutions** to this equation. If the matrix is full-rank, the null space consists *only* of the zero vector $\vec{\mathbf{0}}$ itself.

---

### 6. Check Your Understanding

**Q1: Suppose you have a $3 \times 3$ matrix with a rank of 2. What does its Null Space look like geometrically?**
<details>
<summary><b>Reveal Answer & Intuition</b></summary>

* **Rank of 2** means the 3D space collapses onto a 2D plane.
* Because we have collapsed 3 dimensions down to 2, we have lost exactly **1 dimension** of space.
* This lost dimension is flattened into the origin. Therefore, the **Null Space is a 1D line** passing through the origin.
</details>

**Q2: Does the matrix $A = \begin{bmatrix} 1 & -2 \\ -3 & 6 \end{bmatrix}$ have an inverse? Explain geometrically.**
<details>
<summary><b>Reveal Answer</b></summary>

* Let's look at the columns of $A$, which represent the landing spots of our basis vectors:
  $$ \hat{\imath} \to \begin{bmatrix} 1 \\ -3 \end{bmatrix}, \quad \hat{\jmath} \to \begin{bmatrix} -2 \\ 6 \end{bmatrix} $$
* Notice that the landing spot of $\hat{\jmath}$ is a direct scalar multiple of $\hat{\imath}$'s landing spot:
  $$ \begin{bmatrix} -2 \\ 6 \end{bmatrix} = -2 \cdot \begin{bmatrix} 1 \\ -3 \end{bmatrix} $$
* Because these landing spots are **linearly dependent**, they span only a 1D line, meaning the 2D space is collapsed onto a line.
* The determinant is zero: $\det(A) = (1)(6) - (-2)(-3) = 6 - 6 = 0$.
* Since space collapses into a lower dimension, **no inverse matrix $A^{-1}$ exists** because you cannot "unsquish" a line back into a plane.
</details>

---

[⏮️ **Previous: Chapter 06 — The Determinant: Scaling Space**](06-determinant.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 08 — Nonsquare Matrices & Dimensionality** ⏭️](08-nonsquare-matrices-dimension-transformations.md)
