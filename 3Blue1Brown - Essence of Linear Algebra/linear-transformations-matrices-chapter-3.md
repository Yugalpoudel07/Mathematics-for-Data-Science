# Linear Transformations and Matrices
## Essence of Linear Algebra — Chapter 3

> **In simple words:** A matrix is not just a static grid of numbers; it is a **machine that transforms space**. It takes a vector as an input and spits out a new vector as an output. To understand what any matrix does to the entire infinite 2D plane, you only need to track what it does to two single vectors: the standard basis vectors $\hat{\imath}$ and $\hat{\jmath}$. Wherever they land, everything else follows.

---

### 1. Transformations as Vector Functions
A "transformation" is simply a fancy word for a **mathematical function**. While typical algebraic functions take a number and output a number, linear algebra deals with functions that:
* Take a **vector** as an input.
* Spit out a **transformed vector** as an output:
  $$ L(\vec{\mathbf{v}}) = \vec{\mathbf{w}} $$

#### Why "Transformation" Instead of "Function"?
We use "transformation" to suggest a visual, spatial intuition. Instead of plotting a graph (which is impossible for 2D vectors since a 2D input and 2D output would require 4 dimensions), we visualize the function using **movement**:
1. We represent every vector as a **single point in space** (the coordinate at its tip).
2. We watch every point on an infinite grid **migrate** from its starting spot to its ending spot.
3. This turns a dry algebraic formula into a beautiful, continuous morphing of 2D space.

---

### 2. What Makes a Transformation "Linear"?
Not all morphings of space are linear. Visually and algebraically, a transformation $L$ is strictly **linear** if it satisfies the following rules:

| Perspective | Rule | Visual Description |
| :--- | :--- | :--- |
| **Geometric** | **Fixed Origin** | The origin $(0,0)$ must remain absolutely fixed in place. It cannot move. |
| **Geometric** | **Straight Lines** | All straight lines must remain completely straight. No curving, bending, or twisting. |
| **Geometric** | **Parallel Grid Lines** | Grid lines must remain **parallel** and **evenly spaced** throughout the entire morphing. |
| **Formal Math** | **Additivity** | $L(\vec{\mathbf{v}} + \vec{\mathbf{w}}) = L(\vec{\mathbf{v}}) + L(\vec{\mathbf{w}})$ <br> *(Adding vectors before or after the transformation gives the same result)* |
| **Formal Math** | **Homogeneity** | $L(c\vec{\mathbf{v}}) = cL(\vec{\mathbf{v}})$ <br> *(Scaling a vector before or after the transformation gives the same result)* |

If any line curves or the origin shifts, the transformation is **nonlinear**.

---

### 3. The Superpower of Basis Vectors
How does a computer calculate where millions of grid points land during a transformation? Does it need an infinitely long formula? No!

Because of the formal properties of linearity, **if you know where the two basic unit vectors $\hat{\imath}$ and $\hat{\jmath}$ land, you can calculate exactly where ANY arbitrary vector lands.**

Recall that any vector $\vec{\mathbf{v}} = \begin{bmatrix} x \\ y \end{bmatrix}$ is actually a linear combination of our standard basis:
$$ \vec{\mathbf{v}} = x\hat{\imath} + y\hat{\jmath} $$

If we apply a linear transformation $L$, the rules of linearity dictate:
1. **Preserve addition:** $L(\vec{\mathbf{v}}) = L(x\hat{\imath} + y\hat{\jmath}) = L(x\hat{\imath}) + L(y\hat{\jmath})$
2. **Preserve scaling:** $L(\vec{\mathbf{v}}) = xL(\hat{\imath}) + yL(\hat{\jmath})$

This means **the transformed vector $L(\vec{\mathbf{v}})$ is the exact same linear combination of the transformed basis vectors!**

---

### 4. Defining Matrix-Vector Multiplication
This spatial shortcut is exactly where the formula for matrices and matrix-vector multiplication comes from.

Suppose we run a transformation and watch our basis vectors land on new coordinates:
* $\hat{\imath}$ (originally $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$) lands at $\begin{bmatrix} a \\ c \end{bmatrix}$
* $\hat{\jmath}$ (originally $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$) lands at $\begin{bmatrix} b \\ d \end{bmatrix}$

To find where any arbitrary vector $\begin{bmatrix} x \\ y \end{bmatrix}$ lands, we scale these landing spots by $x$ and $y$:
$$ L\left(\begin{bmatrix} x \\ y \end{bmatrix}\right) = x \begin{bmatrix} a \\ c \end{bmatrix} + y \begin{bmatrix} b \\ d \end{bmatrix} = \begin{bmatrix} ax + by \\ cx + dy \end{bmatrix} $$

We pack these four landing numbers into a $2 \times 2$ grid called a **matrix**:
$$ \begin{bmatrix} a & b \\ c & d \end{bmatrix} $$

```text
       Transformed i-hat     Transformed j-hat
             |                     |
             v                     v
       ┌───────────┐         ┌───────────┐
       │     a     │         │     b     │
       │     c     │         │     d     │
       └───────────┘         └───────────┘
             |                     |
             └──────────┬──────────┘
                        v
               Matrix Representation:
                 ┌─── a   b ───┐
                 └─── c   d ───┘
```

When we multiply a matrix by a vector, we are just executing this linear combination:
$$ \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = x \begin{bmatrix} a \\ c \end{bmatrix} + y \begin{bmatrix} b \\ d \end{bmatrix} = \begin{bmatrix} ax + by \\ cx + dy \end{bmatrix} $$

*The columns are the transformed basis vectors. The vector coordinates are the weights scaling those columns.*

---

### 5. Classic Visual Examples

#### A. 90-Degree Counterclockwise Rotation
If we rotate the entire plane $90^\circ$ counterclockwise:
* $\hat{\imath}$ rotates straight up, landing on $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$.
* $\hat{\jmath}$ rotates left, landing on $\begin{bmatrix} -1 \\ 0 \end{bmatrix}$.

```text
         y                          y
         ^ (j-hat)                  ^ (i-hat lands here)
         |                          | /
         |                          |/  L(i-hat) = [0, 1]
    -----+-----> x     ====>   <----+-----+-----> x
         |  \                       |     \ 
         |   i-hat                  |      L(j-hat) = [-1, 0]
                               (j-hat lands here)
```

The resulting matrix is:
$$ \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} $$

To rotate any vector $\begin{bmatrix} x \\ y \end{bmatrix}$, we compute:
$$ \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = x \begin{bmatrix} 0 \\ 1 \end{bmatrix} + y \begin{bmatrix} -1 \\ 0 \end{bmatrix} = \begin{bmatrix} -y \\ x \end{bmatrix} $$

---

#### B. A Shear Transformation
In a shear, we hold the $x$-axis fixed but slide the top of the grid to the right:
* $\hat{\imath}$ remains completely unchanged: $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
* $\hat{\jmath}$ tilts and slides over to $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$.

```text
       y                                    y
       ^ (j-hat)                            ^   (j-hat slides)
       |                                    |  /  L(j-hat) = [1, 1]
       |                                    | /
  -----+-----> x       ====>           -----+-----> x
       |  \                                 |  \ 
       |   i-hat (fixed)                    |   L(i-hat) = [1, 0] (fixed)
```

The resulting matrix is:
$$ \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} $$

---

### 6. Special Case: Linearly Dependent Columns
If the columns of a $2 \times 2$ matrix are linearly dependent (i.e., one column is a scalar multiple of another), it means the landing spot of $\hat{\imath}$ and the landing spot of $\hat{\jmath}$ point along the exact same line.

* **The Geometric Consequence:** Instead of maintaining a 2D plane, the entire 2D space gets **squished down onto a single 1D line** (the span of those two vectors).
* This marks a loss of dimensionality and will be key when learning about **determinants, null spaces, and matrix inverses** in future chapters.

---

### 7. Check Your Understanding

**Q1: A transformation leaves $\hat{\imath}$ fixed but flips $\hat{\jmath}$ upside down (meaning $\hat{\jmath}$ lands on $\begin{bmatrix} 0 \\ -1 \end{bmatrix}$). What is the matrix of this transformation, and what is its geometric effect?**
<details>
<summary><b>Reveal Answer</b></summary>

1. **Find the landing spots:**
   * $\hat{\imath}$ lands on $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ (first column).
   * $\hat{\jmath}$ lands on $\begin{bmatrix} 0 \\ -1 \end{bmatrix}$ (second column).
2. **Assemble the matrix:**
   $$ \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} $$
3. **Geometric Effect:** This is a **reflection across the $x$-axis**.
</details>

**Q2: If a linear transformation is described by the matrix $\begin{bmatrix} 2 & 3 \\ -1 & 5 \end{bmatrix}$, where does the vector $\begin{bmatrix} 2 \\ 4 \end{bmatrix}$ land?**
<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

We use matrix-vector multiplication as a linear combination of the columns scaled by the coordinates:
$$ \begin{bmatrix} 2 & 3 \\ -1 & 5 \end{bmatrix} \begin{bmatrix} 2 \\ 4 \end{bmatrix} = 2 \begin{bmatrix} 2 \\ -1 \end{bmatrix} + 4 \begin{bmatrix} 3 \\ 5 \end{bmatrix} $$
1. **Scale the first column:**
   $$ 2 \cdot \begin{bmatrix} 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 4 \\ -2 \end{bmatrix} $$
2. **Scale the second column:**
   $$ 4 \cdot \begin{bmatrix} 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 12 \\ 20 \end{bmatrix} $$
3. **Add the results:**
   $$ \begin{bmatrix} 4 \\ -2 \end{bmatrix} + \begin{bmatrix} 12 \\ 20 \end{bmatrix} = \begin{bmatrix} 4 + 12 \\ -2 + 20 \end{bmatrix} = \begin{bmatrix} 16 \\ 18 \end{bmatrix} $$

* **Result:** The vector lands on $\begin{bmatrix} 16 \\ 18 \end{bmatrix}$.
</details>
