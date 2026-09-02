# Matrix Multiplication as Composition
## Essence of Linear Algebra — Chapter 4

> **In simple words:** Matrix multiplication is usually taught in high school as a confusing ritual of shuffling numbers around (dotting rows of the first with columns of the second). In linear algebra, **multiplying two matrices means chaining (composing) two spatial transformations together.** You apply the first transformation, then the second. The resulting "product matrix" is just a single machine that does the work of both in one single step.

---

### 1. The Core Intuition: Chaining Transformations
Imagine you have two separate spatial operations you want to perform in order on a 2D grid:
1. **First,** you rotate all of space by $90^\circ$ counterclockwise. Let's call this transformation $R$ (represented by matrix $M_1$).
2. **Second,** you apply a horizontal shear. Let's call this transformation $S$ (represented by matrix $M_2$).

If you take any vector and apply $R$, then apply $S$ to the result, the overall movement from start to finish is itself a new linear transformation. This combined action is called the **composition** of the two transformations.

```text
       [Input Vector v]
              │
              ▼
   ┌──────────────────────┐
   │    Transformation 1  │  (e.g., Rotate 90° CCW)
   │      (Matrix M1)     │
   └──────────┬───────────┘
              │ [Intermediate Vector]
              ▼
   ┌──────────────────────┐
   │    Transformation 2  │  (e.g., Horizontal Shear)
   │      (Matrix M2)     │
   └──────────┬───────────┘
              │
              ▼
       [Output Vector]
```

We can represent this entire multi-step process with a **single, new 2x2 matrix**—the product of the shear matrix and the rotation matrix.

---

### 2. The Notation Quirk: Reading Right-to-Left
In math notation, we write functions on the left of their inputs (like $f(x)$). When nesting functions—applying $g(x)$ first, then applying $f$ to the result—we write it as:
$$ f(g(x)) $$

Because matrix-vector multiplication behaves like a function, matrix composition inherits this same **right-to-left order**:
$$ M_2 \cdot M_1 \cdot \vec{\mathbf{v}} $$

* **Read it as:** "Apply $M_1$ first, then apply $M_2$ to the output."
* This means when multiplying two matrices $M_2 M_1$, **the matrix on the right represents the first transformation applied, and the matrix on the left represents the second.**

```text
       M2      *      M1      *   v
   └───────┘       └───────┘
    Second          First
  Transformation  Transformation
```

---

### 3. Computing the Product Matrix (The Visual Way)
Instead of memorizing algorithmic row-by-column calculations, we can find the product matrix by applying our golden rule from Chapter 3: **Track where the unit basis vectors $\hat{\imath}$ and $\hat{\jmath}$ ultimately land.**

Let’s find the product of applying a **Rotation $90^\circ$ CCW** first, then a **Horizontal Shear**:
* Rotation Matrix ($M_1$): $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$
* Shear Matrix ($M_2$): $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$

#### Step 1: Follow $\hat{\imath}$
1. **Transformation 1 (Rotation):** $\hat{\imath}$ starts at $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and lands at $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ (this is the first column of $M_1$).
2. **Transformation 2 (Shear):** Now, apply the shear matrix $M_2$ to that intermediate landing spot:
   $$ M_2 \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = 0\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 1\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} $$
* Thus, the final landing spot of $\hat{\imath}$ is $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$. This becomes the **first column** of our product matrix.

#### Step 2: Follow $\hat{\jmath}$
1. **Transformation 1 (Rotation):** $\hat{\jmath}$ starts at $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ and lands at $\begin{bmatrix} -1 \\ 0 \end{bmatrix}$ (the second column of $M_1$).
2. **Transformation 2 (Shear):** Apply the shear matrix $M_2$ to that intermediate spot:
   $$ M_2 \cdot \begin{bmatrix} -1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} -1 \\ 0 \end{bmatrix} = -1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 0\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 0 \end{bmatrix} $$
* Thus, the final landing spot of $\hat{\jmath}$ is $\begin{bmatrix} -1 \\ 0 \end{bmatrix}$. This becomes the **second column** of our product matrix.

#### The Result:
$$ \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ 1 & 0 \end{bmatrix} $$

---

### 4. General Algebraic Form
If we generalize this process for any two matrices $M_2$ and $M_1$:
$$ M_2 = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \quad M_1 = \begin{bmatrix} e & f \\ g & h \end{bmatrix} $$

To compute $M_2 M_1$:
1. **First Column:** Find where $\hat{\imath}$ lands by multiplying $M_2$ by the first column of $M_1$:
   $$ \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} e \\ g \end{bmatrix} = \begin{bmatrix} ae + bg \\ ce + dg \end{bmatrix} $$
2. **Second Column:** Find where $\hat{\jmath}$ lands by multiplying $M_2$ by the second column of $M_1$:
   $$ \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} f \\ h \end{bmatrix} = \begin{bmatrix} af + bh \\ cf + dh \end{bmatrix} $$

Putting them together into a single matrix:
$$ M_2 M_1 = \begin{bmatrix} ae+bg & af+bh \\ ce+dg & cf+dh \end{bmatrix} $$

Rather than memorizing this grid of variables, think of each column of the product matrix as **the left matrix applied to the corresponding column of the right matrix**.

---

### 5. Critical Properties of Matrix Multiplication

#### A. Noncommutativity (Order Matters!)
In general arithmetic, $2 \cdot 3 = 3 \cdot 2$. However, in linear algebra, **matrix multiplication is noncommutative**:
$$ AB \neq BA $$

* **Geometric Intuition:** Think of the visual operations. If you shear space first, then rotate it $90^\circ$, space will look completely different than if you rotated it first, then sheared it.
* **Special Case (Commutative Matrices):** 
  * A matrix that scales both axes by the exact same amount $a$ (a scaling matrix) *does* commute with every other matrix.
  * This is because a uniform scaling matrix is just a scalar multiplier written in matrix form:
    $$ \begin{bmatrix} a & 0 \\ 0 & a \end{bmatrix} = a \cdot \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = aI $$
  * Since $I$ (the **identity matrix**, representing "do nothing") commutes with everything, uniform scaling matrices also commute.

---

#### B. Associativity (Parentheses Don't Matter)
If you are multiplying three matrices $A(BC)$ vs $(AB)C$, **matrix multiplication is associative**:
$$ A(BC) = (AB)C $$

* **Algebraic Proof:** Extremely tedious and symbol-heavy.
* **Geometric Intuition:** Associativity simply states: "If you have three transformations applied in sequence ($C$, then $B$, then $A$), it doesn't matter if you think of grouping the first two first ($BC$) or the last two first ($AB$). You are still just applying the same three operations in the exact same sequence." There is fundamentally nothing to prove because the sequential path of the vectors remains unchanged!

---

### 6. Check Your Understanding

**Q1: Find the product of the following two transformations: first rotate $90^\circ$ CCW, then scale space by a factor of 2 along both axes.**
$$ \text{Scaling Matrix } S = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}, \quad \text{Rotation Matrix } R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} $$
**Calculate both $SR$ and $RS$. Do they agree? Why?**

<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

**1. Calculate $SR$ (Rotation first, then Scaling):**
* **First Column ($\hat{\imath}$):** Apply $S$ to first column of $R$:
  $$ \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 2 \end{bmatrix} $$
* **Second Column ($\hat{\jmath}$):** Apply $S$ to second column of $R$:
  $$ \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} -1 \\ 0 \end{bmatrix} = \begin{bmatrix} -2 \\ 0 \end{bmatrix} $$
* **Result $SR$:** $\begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}$

**2. Calculate $RS$ (Scaling first, then Rotation):**
* **First Column ($\hat{\imath}$):** Apply $R$ to first column of $S$:
  $$ \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 2 \end{bmatrix} $$
* **Second Column ($\hat{\jmath}$):** Apply $R$ to second column of $S$:
  $$ \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 \\ 2 \end{bmatrix} = \begin{bmatrix} -2 \\ 0 \end{bmatrix} $$
* **Result $RS$:** $\begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}$

**Conclusion:** 
They agree perfectly ($SR = RS$). Since $S$ is a uniform scaling matrix, it acts as a scalar multiplier ($2I$), which commutes with any linear transformation. Geometrically, stretching space by 2 and then rotating is identical to rotating and then stretching by 2.
</details>

**Q2: Given $M_2 = \begin{bmatrix} 0 & 2 \\ 1 & 0 \end{bmatrix}$ and $M_1 = \begin{bmatrix} 1 & -2 \\ 1 & 0 \end{bmatrix}$, find the product matrix $M_2 M_1$.**

<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

We compute $M_2 M_1$:
* **First column of product:** Apply $M_2$ to the first column of $M_1$ ($\begin{bmatrix} 1 \\ 1 \end{bmatrix}$):
  $$ \begin{bmatrix} 0 & 2 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = 1\begin{bmatrix} 0 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix} $$
* **Second column of product:** Apply $M_2$ to the second column of $M_1$ ($\begin{bmatrix} -2 \\ 0 \end{bmatrix}$):
  $$ \begin{bmatrix} 0 & 2 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} -2 \\ 0 \end{bmatrix} = -2\begin{bmatrix} 0 \\ 1 \end{bmatrix} + 0\begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \end{bmatrix} $$

* **Resulting Product Matrix:**
  $$ M_2 M_1 = \begin{bmatrix} 2 & 0 \\ 1 & -2 \end{bmatrix} $$
</details>
