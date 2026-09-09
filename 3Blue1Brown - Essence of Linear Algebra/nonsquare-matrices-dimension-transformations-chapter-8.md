# Nonsquare Matrices as Transformations Between Dimensions
## Essence of Linear Algebra — Chapter 8

> **In simple words:** A matrix does not have to be square. If you see a nonsquare matrix (like a $3 \times 2$ or $2 \times 3$ matrix), it just means you are transforming space between **different dimensions**. It is a machine that takes in vectors of one size (e.g., 2D) and spits out vectors of a completely different size (e.g., 3D). The number of **columns** tells you how many dimensions you start with, and the number of **rows** tells you how many dimensions you end up with.

---

### 1. The Golden Rule of Matrix Dimensions ($m \times n$)

When dealing with a matrix of size $m \times n$ (where $m$ is the number of rows and $n$ is the number of columns), you can read its geometric purpose instantly using this rule:

$$\text{An } \mathbf{m \times n} \text{ matrix represents a linear transformation from } \mathbf{n}\text{\textbf{-D space}} \to \mathbf{m}\text{\textbf{-D space}}.$$

*   **The Number of Columns ($n$):** This is the dimensionality of your **input space**. Why? Because each column of a matrix represents where one of your input basis vectors lands. If you have $n$ columns, it means you have $n$ starting basis vectors (e.g., 2 columns = 2D space, 3 columns = 3D space).
*   **The Number of Rows ($m$):** This is the dimensionality of your **output space**. Why? Because each column needs $m$ coordinates to describe where that basis vector lands in the new, target space (e.g., 3 coordinates per column = 3D output space).

```text
               Output Dimension (m rows)
                     [ landed-i_x   landed-j_x ]
      Matrix A =     [ landed-i_y   landed-j_y ]
                     [ landed-i_z   landed-j_z ]
                            |            |
                            v            v
                    Input Dimension (n = 2 columns)
```

---

### 2. Up-Dimensional Mapping: 2D to 3D ($3 \times 2$ Matrix)

A transformation from **2D to 3D** takes a flat sheet of paper (2D plane) and maps it into a 3D room. 

*   **Basis Vectors:** We start with two basis vectors in 2D space: $\hat{\imath}$ and $\hat{\jmath}$.
*   **The Transformation:** When we transform space, $\hat{\imath}$ and $\hat{\jmath}$ move into 3D space, which means they now require **three coordinates** to describe their positions.
*   **Example Matrix:**
    $$ A = \begin{bmatrix} 2 & 0 \\ -1 & 1 \\ -1 & 1 \end{bmatrix} $$
    *   $\hat{\imath}$ lands at $\begin{bmatrix} 2 \\ -1 \\ -1 \end{bmatrix}$ in 3D.
    *   $\hat{\jmath}$ lands at $\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$ in 3D.
*   **The Matrix Size:** It has **3 rows** and **2 columns**, making it a **$3 \times 2$ matrix**.

#### Geometric Intuition & Column Space
*   **Unconnected Spaces:** It is important to emphasize that 2D input vectors are a completely different animal from 3D output vectors. They live in separate, unconnected spaces.
*   **The Column Space:** The set of all possible outputs of this matrix (its column space) is the **span of its columns**. Since we are scaling and adding two 3D vectors that are not pointing in the same direction, their span is a **2D plane** slicing through the origin of 3D space.
*   **Rank:** Because the column space is a 2D plane, the rank of the matrix is **2**. This is a **full-rank** matrix because the output dimension ($2$) matches the input dimension ($2$).

```text
  INPUT SPACE (2D)                   OUTPUT SPACE (3D)
         y                                  z
         ^                                  ^   L(j)
         |  j                               |  /
         +---> x                            | /____> y
        /                                  / /   /
       v i                                / /_L(i)
                                         v /
                                        x
   (Flat xy-plane)                     (2D plane slicing through 3D space)
```

---

### 3. Down-Dimensional Mapping: 3D to 2D ($2 \times 3$ Matrix)

A transformation from **3D to 2D** takes a 3D room and collapses it down onto a flat 2D sheet of paper.

*   **Basis Vectors:** We start with three basis vectors in 3D space: $\hat{\imath}$, $\hat{\jmath}$, and $\hat{k}$.
*   **The Transformation:** When transformed, all three vectors land on a 2D plane, requiring only **two coordinates** each.
*   **Example Matrix:**
    $$ B = \begin{bmatrix} 3 & 1 & 4 \\ 2 & -1 & 0 \end{bmatrix} $$
    *   $\hat{\imath}$ lands at $\begin{bmatrix} 3 \\ 2 \end{bmatrix}$
    *   $\hat{\jmath}$ lands at $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$
    *   $\hat{k}$ lands at $\begin{bmatrix} 4 \\ 0 \end{bmatrix}$
*   **The Matrix Size:** It has **2 rows** and **3 columns**, making it a **$2 \times 3$ matrix**.

#### Geometric Intuition
*   Since we are starting with 3 dimensions and squishing them into 2, we are guaranteed to lose information.
*   The column space (all possible outputs) is the span of these three 2D vectors. If the vectors are non-zero and don't all align, they will span the entire 2D plane, giving this transformation a **rank of 2**.
*   **Not Full Rank:** Although the output spans the entire 2D target space, the matrix itself is **not full rank** relative to its input dimension ($3$). This means there must be a non-trivial **null space** (a line of vectors in 3D that all get flattened onto the 2D origin).

---

### 4. Squeezing Space to a Line: 2D to 1D ($1 \times 2$ Matrix)

A transformation from **2D to 1D** takes a 2D plane and squishes every vector down onto a simple, 1D number line.

*   **Basis Vectors:** We start with $\hat{\imath}$ and $\hat{\jmath}$ in 2D space.
*   **The Transformation:** When transformed, both land on the number line, becoming simple **scalar values** (1D vectors).
*   **Example Matrix:**
    $$ C = \begin{bmatrix} 1 & -2 \end{bmatrix} $$
    *   $\hat{\imath}$ lands on the number $1$.
    *   $\hat{\jmath}$ lands on the number $-2$.
*   **The Matrix Size:** It has **1 row** and **2 columns**, making it a **$1 \times 2$ matrix**.

#### Visualizing Linearity on a Number Line
*   How do we visualize "lines remaining lines" when there are no grids in 1D?
*   **The Spacing Rule:** A transformation to 1D is linear if a line of **evenly spaced dots** in 2D remains **evenly spaced** once mapped onto the 1D number line.

```text
  INPUT (2D Grid Dots)                 OUTPUT (1D Number Line)
       *     *     *                   
       *     *     *      ------*--*--*--*--*--*------>
       *     *     *             -2 -1  0  1  2  3
  (Evenly spaced dots)               (Still evenly spaced)
```

*   **The Dot Product Preview:** Taking a 2D vector $\begin{bmatrix} x \\ y \end{bmatrix}$ and multiplying it by this $1 \times 2$ matrix gives a single number:
    $$ \begin{bmatrix} 1 & -2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = 1x - 2y $$
    This is mathematically identical to taking the **dot product** of $\begin{bmatrix} x \\ y \end{bmatrix}$ with the vector $\begin{bmatrix} 1 \\ -2 \end{bmatrix}$. This beautiful link is called **Duality** and is the core of Chapter 9.

---

### 5. Check Your Understanding

**Q1: You see a matrix of size $4 \times 5$. What are the dimensions of its input and output spaces? Does it have a determinant?**
<details>
<summary><b>Reveal Answer & Geometric Logic</b></summary>

*   **Input Space:** **5D** (since there are 5 columns, meaning 5 starting basis vectors).
*   **Output Space:** **4D** (since there are 4 rows, meaning each of those basis vectors lands at a coordinate with 4 components).
*   **Determinant:** **No**. Determinants measure how much a transformation scales areas or volumes within the *same* dimension. Because this transformation changes the dimensionality of space, measuring a scaling factor is meaningless. Only **square matrices** ($n \times n$) have determinants!
</details>

**Q2: Given the $2 \times 3$ matrix $B = \begin{bmatrix} 1 & -2 & 3 \\ 0 & 4 & -1 \end{bmatrix}$, where does the 3D vector $\vec{\mathbf{v}} = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}$ land?**
<details>
<summary><b>Reveal Answer & Step-by-Step Calculation</b></summary>

To find where $\vec{\mathbf{v}}$ lands, we take a linear combination of the matrix's columns, using the components of $\vec{\mathbf{v}}$ as scalars:
$$ B\vec{\mathbf{v}} = 2\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 1\begin{bmatrix} -2 \\ 4 \end{bmatrix} + 3\begin{bmatrix} 3 \\ -1 \end{bmatrix} $$
Let's calculate each component:
*   **Top Component:** $(2 \cdot 1) + (1 \cdot -2) + (3 \cdot 3) = 2 - 2 + 9 = 9$
*   **Bottom Component:** $(2 \cdot 0) + (1 \cdot 4) + (3 \cdot -1) = 0 + 4 - 3 = 1$

*   **Result:** The vector lands at $\begin{bmatrix} 9 \\ 1 \end{bmatrix}$ in 2D space.
</details>
