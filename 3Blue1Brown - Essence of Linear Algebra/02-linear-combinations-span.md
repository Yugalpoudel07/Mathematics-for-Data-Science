[⏮️ **Previous: Chapter 01 — Vectors: What Even Are They?**](01-vectors.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 03 — Linear Transformations & Matrices** ⏭️](03-linear-transformations-matrices.md)

---

# Chapter 02: Linear Combinations, Span, and Basis Vectors

**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> When you look at coordinates like $\begin{bmatrix} 3 \\ -2 \end{bmatrix}$, you are actually scaling two fundamental unit arrows—one pointing right ($\hat{\imath}$) and one pointing up ($\hat{\jmath}$)—and adding them together. This simple action of scaling and adding is called a **linear combination**. The **span** is the entire region of space you can reach by playing with these scalars. By understanding these concepts, we can define a **basis** of any space as the minimum set of non-redundant vectors needed to map it out completely.

---

### 1. The True Meaning of Coordinates: Basis Vectors

Normally, coordinates are introduced as numerical instructions for plotting points. But in linear algebra, there is a much more powerful spatial intuition: **coordinates are scalars that stretch or squish fundamental arrows called basis vectors.**

In the standard 2D Cartesian plane, there are two special unit vectors:

* **$\hat{\imath}$ ("i-hat"):** The unit vector pointing to the right along the x-axis with a length of $1$. Coordinates: $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
* **$\hat{\jmath}$ ("j-hat"):** The unit vector pointing straight up along the y-axis with a length of $1$. Coordinates: $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

```text
Visualizing Standard Basis Vectors:
            y
            ^
            |  j-hat [0, 1]
            |   ^
            |   |
            +---+-------> x
            0   i-hat [1, 0]
```

When you write a vector like $\vec{\mathbf{v}} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}$, you are actually performing a vector addition of scaled basis vectors:
$$ \vec{\mathbf{v}} = 3\hat{\imath} - 2\hat{\jmath} = 3\begin{bmatrix} 1 \\ 0 \end{bmatrix} - 2\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ -2 \end{bmatrix} $$

These two vectors, $\hat{\imath}$ and $\hat{\jmath}$, are called the **basis** of our standard coordinate system.

---

### 2. Choosing Different Basis Vectors

What makes linear algebra beautiful is that the standard basis is not sacred. We are free to choose a different pair of vectors to serve as our basis, which creates an entirely new coordinate system.

Imagine choosing two different vectors, $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$, that do not point in the same direction:

* We can declare $\vec{\mathbf{v}}$ as our new "i-hat" and $\vec{\mathbf{w}}$ as our new "j-hat".
* Every pair of numbers $\begin{bmatrix} a \\ b \end{bmatrix}$ now refers to a new vector built by scaling and adding: $a\vec{\mathbf{v}} + b\vec{\mathbf{w}}$.

```text
   Standard Grid (i-hat, j-hat)         Alternative Grid (v, w)
          y                                    \        /
          ^                                     \  w   /
          |                                      \ ^  /
          |                                       \| /
          +-------> x                              +-------> v
                                                    \
```

Any coordinate system—and any numerical representation of vectors—depends entirely on **your choice of basis vectors**.

---

### 3. Linear Combinations

Any mathematical expression where you scale multiple vectors and add them together is called a **linear combination**:
$$ a\vec{\mathbf{v}} + b\vec{\mathbf{w}} $$
Where $a$ and $b$ are scalars that can range freely over all real numbers.

#### Why is it called "Linear"?

If you keep one scalar constant (e.g., $b = 0$) and let the other scalar $a$ range freely, the vector $a\vec{\mathbf{v}}$ sweeps out an **infinite straight line** passing through the origin. Combining these scaled vectors is essentially a geometric way of "combining lines" to cover space.

For a pair of 2D vectors $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$, there are three geometric scenarios when you take all possible linear combinations:

| Scenario | Geometric Realization | Visual Layout |
| :--- | :--- | :--- |
| **Vectors point in different directions** | You can reach **every single point** on the 2D plane. | A complete, infinite flat sheet. |
| **Vectors are colinear (line up)** | You are stuck on a **single line** passing through the origin. | A single line cutting through the origin. |
| **Both vectors are the zero vector** | You are stuck at a **single point** (the origin). | Just the origin point $(0,0)$. |

---

### 4. The Concept of "Span"

> **Definition:** The **span** of a set of vectors is the set of all possible vectors that can be reached using linear combinations of those vectors.
> 
> *“What are all the possible places we can travel using only our allowed operations of vector addition and scalar multiplication?”*

#### Visualizing Collections: Vectors as Points

Thinking of vectors as arrows gets incredibly messy when you visualize hundreds of them at once. To clean this up, we represent collections of vectors by **plotting only their tips as points in space**, assuming their tails are all anchored at the origin.

* **A Span of a single vector** $\vec{\mathbf{v}}$ is an infinite **line** of points.
* **A Span of two non-colinear vectors** $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ is an infinite **flat sheet** of points representing the entire 2D plane.

```text
Vectors as arrows (cluttered)          Vectors as points (clean)

          ^  ^  /                                .    .   .
           \ | /                                   .  .  .
            \|/                                  .   .    .
        <----o---->                                .  o  .        o = origin
            /|\                                  .    .   .
           / | \                                   .  .  .
          v  v  v                                .   .    .

  Every arrow is anchored at the origin,    Plot only the tips. Now the span
  so the picture gets crowded fast.         of a set is just a line or a sheet.
```

---

### 5. Span in 3D and Higher Dimensions

The true power of this framework shines when we go to three dimensions:

1. **Two Vectors in 3D:** If you take two vectors $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ in 3D space that do not line up, their span is a **2D flat sheet (plane)** slicing through the origin.
2. **Adding a Third Vector $\vec{\mathbf{u}}$:** What happens to the span of $a\vec{\mathbf{v}} + b\vec{\mathbf{w}} + c\vec{\mathbf{u}}$?
   * **Case A (Redundant):** If $\vec{\mathbf{u}}$ happens to sit on the flat sheet spanned by $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$, the span **does not change**. You are still trapped on that same 2D plane.
   * **Case B (Dimensional Leap):** If $\vec{\mathbf{u}}$ points in any other direction (not on that plane), it acts as a third knob. As you scale $\vec{\mathbf{u}}$, it sweeps the 2D plane through the third dimension, **spanning the entire 3D space**!

---

### 6. Linear Independence vs. Dependence

In high-dimensional datasets, we often have redundant vectors that do not add any new spatial directions.

* **Linearly Dependent:** If you have a set of vectors and you can remove at least one without shrinking their overall span, they are linearly dependent. In other words, **at least one vector can be written as a linear combination of the others** (it is already in their span).
  $$ \vec{\mathbf{u}} = a\vec{\mathbf{v}} + b\vec{\mathbf{w}} $$
* **Linearly Independent:** If each vector in your set adds a brand-new dimension to your span, they are linearly independent. No vector in the set can be built from a combination of the others.

#### The Formal Definition of a Basis

We can now state the rigorous mathematical definition of a basis:
> **A Basis of a space is a set of linearly independent vectors that span that space.**

This means a basis must satisfy two conditions:

1. It must **span** the space (you can reach everything).
2. It must be **linearly independent** (there are no redundant elements; it is the absolute minimum set of vectors required).

---

### 7. Check Your Understanding

**Q1: What is the span of the following two vectors?**
$$ \vec{\mathbf{v}} = \begin{bmatrix} 2 \\ -3 \end{bmatrix}, \quad \vec{\mathbf{w}} = \begin{bmatrix} -4 \\ 6 \end{bmatrix} $$
<details>
<summary><b>Reveal Answer & Mathematical Proof</b></summary>

* **Answer:** A single **line** passing through the origin.
* **Proof:** Notice that $\vec{\mathbf{w}}$ is a direct scalar multiple of $\vec{\mathbf{v}}$:
  $$ \vec{\mathbf{w}} = -2 \vec{\mathbf{v}} $$
  Because they are colinear (they point along the same straight line), adding them together can never pull you off that line. They are linearly dependent, so their span is reduced from a 2D plane to a 1D line.
</details>

**Q2: If you have three vectors in 3D space, and one of them is the zero vector $\vec{\mathbf{0}}$, can this set ever be a basis for 3D space?**
<details>
<summary><b>Reveal Answer & Explanation</b></summary>

* **Answer:** **No.**
* **Explanation:** A basis requires all vectors to be **linearly independent**. Any set containing the zero vector is automatically linearly dependent because you can write the zero vector as a linear combination of the other vectors by setting all their scalars to $0$ (e.g., $0\vec{\mathbf{v}} + 0\vec{\mathbf{w}} = \vec{\mathbf{0}}$). Geometrically, the zero vector adds zero new spatial dimensions or "knobs" to your span.
</details>

**Q3: Find the scalars $a$ and $b$ such that the linear combination of $\vec{\mathbf{v}} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ and $\vec{\mathbf{w}} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$ equals $\begin{bmatrix} 7 \\ -4 \end{bmatrix}$.**
<details>
<summary><b>Reveal Answer & Derivation</b></summary>

We set up the system of linear equations:
$$ a\vec{\mathbf{v}} + b\vec{\mathbf{w}} = a\begin{bmatrix} 2 \\ 1 \end{bmatrix} + b\begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 7 \\ -4 \end{bmatrix} $$

This corresponds to the two equations:
1) $2a - b = 7 \implies b = 2a - 7$
2) $a + 2b = -4$

Substitute the first into the second:
$$ a + 2(2a - 7) = -4 $$
$$ a + 4a - 14 = -4 $$
$$ 5a = 10 \implies a = 2 $$

Now find $b$:
$$ b = 2(2) - 7 = 4 - 7 = -3 $$

* **Result:** $a = 2$, $b = -3$.
</details>

---

[⏮️ **Previous: Chapter 01 — Vectors: What Even Are They?**](01-vectors.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 03 — Linear Transformations & Matrices** ⏭️](03-linear-transformations-matrices.md)
