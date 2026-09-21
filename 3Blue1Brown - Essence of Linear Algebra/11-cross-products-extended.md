[⏮️ **Previous: Chapter 10 — Cross Products**](10-cross-products.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 12 — Cramer's Rule Geometrically** ⏭️](12-cramers-rule.md)

---

# Chapter 11: Cross Products in the Light of Linear Transformations

**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> In Chapter 10, computing a 3D cross product involved a strange "trick": putting the basis vectors $\hat{\imath}, \hat{\jmath}, \hat{k}$ into the first column of a $3 \times 3$ matrix and calculating its determinant. Chapter 11 proves that this is **not a random coincidence or cheap gimmick**. By connecting **3D volumes (determinants)** with **duality (translating transformations into vectors)**, we prove why the algebraic formula and the geometric arrow (perpendicular, length equal to area, right-hand rule) are fundamentally the exact same thing.

---

### 1. The Core Puzzle: Why Does the Trick Work?

Recall the standard formula for the 3D cross product of two vectors $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$:

$$ \vec{\mathbf{v}} \times \vec{\mathbf{w}} = \det\left(\begin{bmatrix} \hat{\imath} & v_1 & w_1 \\ \hat{\jmath} & v_2 & w_2 \\ \hat{k} & v_3 & w_3 \end{bmatrix}\right) $$

Normally, students are told: *"Just pretend $\hat{\imath}, \hat{\jmath}, \hat{k}$ are numbers, expand the determinant, and accept that the resulting vector is perpendicular to $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$, has length equal to the area of their parallelogram, and obeys the right-hand rule."*

To understand **why** this works without brute-force algebra, we bridge two previous concepts:

1. **Determinants as Volume (Chapter 6):** A $3 \times 3$ matrix determinant measures the signed volume of a 3D parallelepiped.
2. **Duality (Chapter 9):** Every linear transformation from 3D space to the 1D number line ($3\text{D} \to 1\text{D}$) corresponds to a unique 3D **dual vector** $\vec{\mathbf{p}}$, such that applying the transformation to any vector $\vec{\mathbf{u}}$ is identical to taking the dot product $\vec{\mathbf{p}} \cdot \vec{\mathbf{u}}$.

---

### 2. Step 1: Defining a $3\text{D} \to 1\text{D}$ Linear Transformation

Fix two constant 3D vectors $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$. Now define a function $T(\vec{\mathbf{u}})$ that takes any variable input vector $\vec{\mathbf{u}} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ and returns a single number:

$$ T(\vec{\mathbf{u}}) = \det\left(\begin{bmatrix} x & v_1 & w_1 \\ y & v_2 & w_2 \\ z & v_3 & w_3 \end{bmatrix}\right) $$

```text
               Volume of Parallelepiped
                      /
                     /   . u (variable input)
                    /   /|
                   /   / | (perpendicular height)
                  +---/--+
                 /   /  /
                /   .  /
               +------+  <- Base area spanned by v and w
```

* **Geometric Meaning:** $T(\vec{\mathbf{u}})$ calculates the **signed volume** of the 3D parallelepiped spanned by $\vec{\mathbf{u}}$, $\vec{\mathbf{v}}$, and $\vec{\mathbf{w}}$.
* **Linearity:** Because matrix determinants are linear with respect to their columns, $T(\vec{\mathbf{u}})$ is a valid **linear transformation from $3\text{D}$ to $1\text{D}$**.

---

### 3. Step 2: The Computational View of the Dual Vector

By the principle of **Duality**, because $T(\vec{\mathbf{u}})$ is a $3\text{D} \to 1\text{D}$ linear transformation, there must exist some special 3D vector $\vec{\mathbf{p}} = \begin{bmatrix} p_x \\ p_y \\ p_z \end{bmatrix}$ such that:

$$ T(\vec{\mathbf{u}}) = \vec{\mathbf{p}} \cdot \vec{\mathbf{u}} $$

Let's compute both sides algebraically:

1. **Dot product side:**
   $$ \vec{\mathbf{p}} \cdot \vec{\mathbf{u}} = p_x \cdot x + p_y \cdot y + p_z \cdot z $$

2. **Determinant side (expanding down the first column):**
   $$ \det\left(\begin{bmatrix} x & v_1 & w_1 \\ y & v_2 & w_2 \\ z & v_3 & w_3 \end{bmatrix}\right) = (v_2 w_3 - v_3 w_2) \cdot x + (v_3 w_1 - v_1 w_3) \cdot y + (v_1 w_2 - v_2 w_1) \cdot z $$

3. **Matching Coefficients:**
   For these two expressions to be equal for *every* possible $(x, y, z)$, the components of $\vec{\mathbf{p}}$ **must** be:
   $$ p_x = v_2 w_3 - v_3 w_2 $$
   $$ p_y = v_3 w_1 - v_1 w_3 $$
   $$ p_z = v_1 w_2 - v_2 w_1 $$

Plugging $\hat{\imath}, \hat{\jmath}, \hat{k}$ into the first column of the matrix is simply a compact notation to collect these exact coefficients into vector form!

---

### 4. Step 3: The Geometric View of the Dual Vector

Now, let's ask the exact same question geometrically: **What 3D vector $\vec{\mathbf{p}}$ satisfies $\vec{\mathbf{p}} \cdot \vec{\mathbf{u}} = \text{Volume}(\vec{\mathbf{u}}, \vec{\mathbf{v}}, \vec{\mathbf{w}})$ for all $\vec{\mathbf{u}}$?**

Recall two geometric formulas:

1. **Volume of a Parallelepiped:**
   $$ \text{Volume} = (\text{Base Area spanned by } \vec{\mathbf{v}} \text{ and } \vec{\mathbf{w}}) \times (\text{Perpendicular height of } \vec{\mathbf{u}}) $$

2. **Geometric Dot Product:**
   $$ \vec{\mathbf{p}} \cdot \vec{\mathbf{u}} = \|\vec{\mathbf{p}}\| \times (\text{Length of } \vec{\mathbf{u}} \text{ projected onto } \vec{\mathbf{p}}) $$

```text
                  p (Dual Vector / Cross Product)
                  ^
                  |
                  |  u_perp (height)
                  | /
     -------------+------------ <- Plane spanned by v and w
                 / \
                /   \  Base Area = ||v x w||
```

To make $\vec{\mathbf{p}} \cdot \vec{\mathbf{u}}$ equal to $\text{Volume}(\vec{\mathbf{u}}, \vec{\mathbf{v}}, \vec{\mathbf{w}})$ for *any* vector $\vec{\mathbf{u}}$:

1. **Direction of $\vec{\mathbf{p}}$:** $\vec{\mathbf{p}}$ must be **perpendicular** to the plane spanned by $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$. This ensures that projecting $\vec{\mathbf{u}}$ onto $\vec{\mathbf{p}}$ measures its exact perpendicular height above the base!
2. **Length of $\vec{\mathbf{p}}$:** $\|\vec{\mathbf{p}}\|$ must equal the **area of the parallelogram** spanned by $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$.
3. **Orientation:** $\vec{\mathbf{p}}$ must point in the direction specified by the **right-hand rule**, so that when the triple $(\vec{\mathbf{u}}, \vec{\mathbf{v}}, \vec{\mathbf{w}})$ forms a right-handed orientation, the dot product is positive (matching the positive determinant).

---

### 5. Step 4: The Unification (The Aha! Moment)

We asked one question: *"Which 3D vector $\vec{\mathbf{p}}$ satisfies $T(\vec{\mathbf{u}}) = \vec{\mathbf{p}} \cdot \vec{\mathbf{u}}$?"*

* **Computational Answer:** The vector obtained by expanding the determinant with $\hat{\imath}, \hat{\jmath}, \hat{k}$ in the first column.
* **Geometric Answer:** The vector perpendicular to $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$, with length equal to their spanned area, oriented by the right-hand rule.

Since both methods answer the **exact same duality question**, they MUST produce the **exact same vector**.

$$ \text{Algebraic Determinant Trick} \equiv \text{Geometric Cross Product Vector } (\vec{\mathbf{v}} \times \vec{\mathbf{w}}) $$

---

### 6. Summary Comparison

| Perspective | Computational View | Geometric View |
| :--- | :--- | :--- |
| **Operation** | Determinant expansion of $1 \times 3$ or $3 \times 3$ matrix. | Measuring parallelepiped volume via base area $\times$ height. |
| **Role of $\vec{\mathbf{u}}$** | Variables $(x, y, z)$ in the first column. | Input vector whose perpendicular component gives height. |
| **Dual Vector $\vec{\mathbf{p}}$** | Coefficients $[v_2 w_3 - v_3 w_2, \dots]^T$. | Arrow $\vec{\mathbf{v}} \times \vec{\mathbf{w}}$ perpendicular to base plane. |
| **Why they match** | Both represent the unique dual vector for $T(\vec{\mathbf{u}}) = \det([\vec{\mathbf{u}} \ \vec{\mathbf{v}} \ \vec{\mathbf{w}}])$. |

---

### 7. Check Your Understanding

**Q1: Why do we define $T(\vec{\mathbf{u}}) = \det([\vec{\mathbf{u}} \ \vec{\mathbf{v}} \ \vec{\mathbf{w}}])$ as a $3\text{D} \to 1\text{D}$ transformation rather than $3\text{D} \to 3\text{D}$?**
<details>
<summary><b>Reveal Answer</b></summary>
Because a determinant always outputs a single scalar (volume), taking a 3D input vector $\vec{\mathbf{u}}$ and returning a scalar makes it a transformation from $\mathbb{R}^3$ to $\mathbb{R}^1$. This allows us to invoke <b>Duality</b>, which states that every linear $\mathbb{R}^3 \to \mathbb{R}^1$ map corresponds to a dot product with a unique 3D dual vector.
</details>

**Q2: What happens to the dual vector $\vec{\mathbf{p}}$ if $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ are linearly dependent (pointing in the same line)?**
<details>
<summary><b>Reveal Answer</b></summary>
If $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ are linearly dependent, the parallelogram base area is $0$. Therefore, the parallelepiped volume is $0$ for all inputs $\vec{\mathbf{u}}$, making $T(\vec{\mathbf{u}}) = 0$. The corresponding dual vector $\vec{\mathbf{p}}$ must be the zero vector $\vec{\mathbf{0}}$, which matches $\vec{\mathbf{v}} \times \vec{\mathbf{w}} = \vec{\mathbf{0}}$.
</details>

---

[⏮️ **Previous: Chapter 10 — Cross Products**](10-cross-products.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 12 — Cramer's Rule Geometrically** ⏭️](12-cramers-rule.md)
