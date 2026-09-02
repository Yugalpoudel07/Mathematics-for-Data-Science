# Vectors: What Even Are They?
## Essence of Linear Algebra — Chapter 1

> **In simple words:** Linear algebra is the mathematics of space and movement. A vector is its fundamental building block. Rather than arguing about whether a vector is an arrow or a list of numbers, the true power of linear algebra lies in **translating back and forth** between these two viewpoints. It lets you visualize complex data tables geometrically, and let computers crunch spatial operations numerically.

---

### 1. Three Perspectives of a Vector
Depending on your background, a vector means different things. Linear algebra bridges all three:

| Perspective | Core Definition | Visual Representation | Use Case |
| :--- | :--- | :--- | :--- |
| **Physics Student** | An arrow pointing in space, characterized by its **length (magnitude)** and **direction**. | An arrow that you can slide around freely. | Describing forces, velocities, and acceleration. |
| **Computer Scientist** | An **ordered list of numbers** where the length of the list determines the dimensionality. | A sequence or column of values. | Modelling multi-feature data (e.g., house square footage and price). |
| **Mathematician** | An abstract object where there is a sensible way to **add two vectors** and **multiply a vector by a number**. | Anything satisfying the vector space axioms. | Generalizing operations to functions, matrices, and abstract spaces. |

---

### 2. The Coordinate System: The Bridge
In linear algebra, we always **root our vectors at the origin $(0,0)$**. This ties the physics arrow directly to the computer science list of numbers.

* **The Origin $(0,0)$:** The center of space and the tail of every vector.
* **Vector Coordinates:** A set of instructions on how to travel from the origin to the vector's tip.
* **Vertical Notation:** Coordinates are written vertically in square brackets to distinguish them from points:
  $$ \vec{\mathbf{v}} = \begin{bmatrix} x \\ y \end{bmatrix} $$

```text
Visualizing Vector [3, -2]:
        y
        ^
        |
     0 -+---+---+---+---> x
        |   1   2   3
    -1 -|            
        |            \ 
    -2 -|-------------> (3, -2) [Tip of Vector]
        |   \        /
        |    \  v   /
        v     v    v
```

* **In 2D:** $\begin{bmatrix} 3 \\ -2 \end{bmatrix}$ means: "Go $3$ units along the positive x-axis (right), then $2$ units parallel to the negative y-axis (down)."
* **In 3D:** We add a third perpendicular axis ($z$-axis). A vector $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ gives instructions to move along the $x$, $y$, and $z$ axes sequentially. This easily extends to $N$-dimensions (e.g., a 100D vector of features), which is easy to represent numerically but impossible to draw.

---

### 3. The Two Fundamental Operations
All of linear algebra is built upon two operations: **Vector Addition** and **Scalar Multiplication**.

#### A. Vector Addition (Combining Movements)
* **Geometric View (Tip-to-Tail):** Move the tail of the second vector to the tip of the first. The sum is the arrow drawn from the tail of the first to the tip of the second.
* **Why this works:** If you take a step along vector $\vec{\mathbf{v}}$, then a step along vector $\vec{\mathbf{w}}$, the overall displacement is exactly the same as walking directly along their sum $\vec{\mathbf{v}} + \vec{\mathbf{w}}$.

```text
        y
        ^
     2 -|       .(1,2) [Tip of v / Tail of w]
        |      / \
     1 -|     /   \  w = [3, -1]
        |  v /     \
        |   /       v
     0 -+---+---+---+---> x
        0   1   2   3   4 (4,1) [Tip of sum v+w]
        |   \       /
        |    \_____/
        |   Sum = [4, 1]
```

* **Numerical View (Component-wise):** You simply match up corresponding components and add them together.
  $$ \begin{bmatrix} x_1 \\ y_1 \end{bmatrix} + \begin{bmatrix} x_2 \\ y_2 \end{bmatrix} = \begin{bmatrix} x_1 + x_2 \\ y_1 + y_2 \end{bmatrix} $$
  *Example:*
  $$ \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 1+3 \\ 2+(-1) \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix} $$

---

#### B. Scalar Multiplication (Scaling Space)
* **Geometric View (Scaling):** Multiplying a vector by a number stretches, squishes, or reverses its direction.
  * Multiplying by $2$: Doubles the length (stretches).
  * Multiplying by $1/3$: Squishes it to one-third of its length.
  * Multiplying by $-1.5$: Flips the direction (reverses) and stretches it by $1.5\times$.
* **Why "Scalar"?** Because the numbers act like they are **scaling** the vectors. In linear algebra, the words "scalar" and "number" are used interchangeably.

```text
Original Vector v:
  (0,0) --------> (x, y)
  
Scaled by 2 (2v): [Stretching]
  (0,0) ----------------------------> (2x, 2y)
  
Scaled by 1/3 ((1/3)v): [Squishing]
  (0,0) ---> (x/3, y/3)
  
Scaled by -1.5 (-1.5v): [Reversing & Stretching]
  (-1.5x, -1.5y) <------------------------ (0,0)
```

* **Numerical View (Component-wise):** Multiply every single number inside the vector list by that scalar.
  $$ c \cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} c \cdot x \\ c \cdot y \end{bmatrix} $$
  *Example:*
  $$ 2 \cdot \begin{bmatrix} 3 \\ -4 \end{bmatrix} = \begin{bmatrix} 2 \cdot 3 \\ 2 \cdot (-4) \end{bmatrix} = \begin{bmatrix} 6 \\ -8 \end{bmatrix} $$

---

### 4. Why This Translation is a Superpower
1. **For Computer Graphics & Game Devs / Physicists:** You can start with a physical concept (like a camera angle or a physics force in 3D space), translate it into numbers, and write an algorithm for the computer to process it.
2. **For Data Scientists & ML Engineers:** It lets you treat massive, non-visual datasets (like housing data, user preferences, or text embeddings) as geometric objects in a high-dimensional space. By understanding operations geometrically, we can find clusters, trends, and patterns that would be invisible in tables of numbers.

---

### 5. Check Your Understanding
**Q1: If vector $\vec{\mathbf{a}} = \begin{bmatrix} 2 \\ 5 \end{bmatrix}$ and vector $\vec{\mathbf{b}} = \begin{bmatrix} -4 \\ 1 \end{bmatrix}$, what are the coordinates of $3\vec{\mathbf{a}} + \vec{\mathbf{b}}$?**
<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

1. **Step 1:** Scale $\vec{\mathbf{a}}$ by 3:
   $$ 3 \cdot \begin{bmatrix} 2 \\ 5 \end{bmatrix} = \begin{bmatrix} 3 \cdot 2 \\ 3 \cdot 5 \end{bmatrix} = \begin{bmatrix} 6 \\ 15 \end{bmatrix} $$
2. **Step 2:** Add $\vec{\mathbf{b}}$:
   $$ \begin{bmatrix} 6 \\ 15 \end{bmatrix} + \begin{bmatrix} -4 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 + (-4) \\ 15 + 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 16 \end{bmatrix} $$
* **Result:** $3\vec{\mathbf{a}} + \vec{\mathbf{b}} = \begin{bmatrix} 2 \\ 16 \end{bmatrix}$
</details>

**Q2: What is the geometric effect of multiplying a vector by $-0.5$?**
<details>
<summary><b>Reveal Answer</b></summary>
The negative sign flips the direction of the vector by $180^\circ$ (reverses it), and the magnitude $0.5$ squishes its length to exactly half of the original size.
</details>
