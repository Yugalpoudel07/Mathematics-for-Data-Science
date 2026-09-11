[⏮️ **Previous: Chapter 04 — Matrix Multiplication as Composition**](04-matrix-multiplication-composition.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 06 — The Determinant: Scaling Space** ⏭️](06-determinant.md)

---

# Chapter 05: Three-Dimensional Linear Transformations
**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> Extending linear algebra from 2D to 3D is incredibly simple because the rules do not change. A 3D linear transformation is still a machine that takes in a vector and spits out a new one while keeping the origin fixed and all grid lines parallel and evenly spaced. Instead of tracking two basis vectors ($\hat{\imath}$ and $\hat{\jmath}$), we now track three ($\hat{\imath}$, $\hat{\jmath}$, and $\hat{k}$). Their landing spots become the columns of a $3 \times 3$ matrix, which acts as a complete visual description of how the transformation bends, rotates, or stretches 3D space.

---

### 1. The Leap to the Third Dimension
In 2D space, we visualised linear transformations by watching how a flat coordinate grid warped. In 3D space, we do the exact same thing, but with a **three-dimensional coordinate grid**. 

A transformation in 3D is **linear** if it satisfies the same spatial constraints:
1. **The origin remains fixed** at $(0,0,0)$.
2. **All grid lines must remain straight** (no bending or curving).
3. **All grid lines must remain parallel and evenly spaced**.

```text
Visualising 3D Space (Right-Hand Rule):
          z (Blue)
          ^
          |   / y (Green - points into/out of page)
          |  /
          | /
          +-------------> x (Red - points right)
         /
        / 
       v
```
Instead of visualising the entire infinite 3D grid moving (which becomes incredibly crowded and hard to track), we focus entirely on what happens to our three fundamental unit basis vectors:
* **$\hat{\imath}$ (i-hat):** The unit vector pointing along the $+x$ axis $\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$.
* **$\hat{\jmath}$ (j-hat):** The unit vector pointing along the $+y$ axis $\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$.
* **$\hat{k}$ (k-hat):** The unit vector pointing along the $+z$ axis $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$.

---

### 2. The $3 \times 3$ Matrix: Nine Numbers that Define Space
Just as a 2D transformation is completely determined by where the two basis vectors land, a **3D linear transformation is completely determined by where $\hat{\imath}$, $\hat{\jmath}$, and $\hat{k}$ land**.

We bundle these three landing coordinates side-by-side to create a **$3 \times 3$ matrix**:

$$
M = \begin{bmatrix} 
| & | & | \\ 
\text{Landing of } \hat{\imath} & \text{Landing of } \hat{\jmath} & \text{Landing of } \hat{k} \\ 
| & | & | 
\end{bmatrix} 
= \begin{bmatrix} 
a & b & c \\ 
d & e & f \\ 
g & h & i 
\end{bmatrix}
$$

To transform any arbitrary 3D vector $\vec{\mathbf{v}} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$, we scale each of the transformed basis vectors by its respective coordinate and add them together. This is **matrix-vector multiplication**:

$$
M \vec{\mathbf{v}} = 
x \begin{bmatrix} a \\ d \\ g \end{bmatrix} + 
y \begin{bmatrix} b \\ e \\ h \end{bmatrix} + 
z \begin{bmatrix} c \\ f \\ i \end{bmatrix} 
= \begin{bmatrix} 
ax + by + cz \\ 
dx + ey + fz \\ 
gx + hy + iz 
\end{bmatrix}
$$

---

### 3. Geometric Examples in 3D Space

Let's practice translating 3D spatial movements into $3 \times 3$ matrices by tracking our basis vectors.

#### A. 90-Degree Rotation around the $y$-axis
Imagine space rotating 90 degrees around the vertical $y$-axis. Look down the $+y$ axis towards the $xz$-plane to establish direction:
* **$\hat{\jmath}$ is on the axis of rotation**, so it does not move at all:
  $$ \hat{\jmath} \rightarrow \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} $$
* **$\hat{\imath}$ (pointing along $+x$)** rotates 90 degrees to point along the $-z$ direction:
  $$ \hat{\imath} \rightarrow \begin{bmatrix} 0 \\ 0 \\ -1 \end{bmatrix} $$
* **$\hat{k}$ (pointing along $+z$)** rotates 90 degrees to point along the $+x$ direction:
  $$ \hat{k} \rightarrow \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} $$

Placing these landing spots into columns gives us our rotation matrix:
$$ R_y(90^\circ) = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{bmatrix} $$

```text
Rotation around the y-axis:
         y (rotation axis stays fixed)
         ^
         |      
  [-1] < - - - - - [1]  (z-axis rotates into x-axis)
         |     / 
         |    /  
  -------+---/---------> x
        /   /
       /   v
      z 
```

---

#### B. 90-Degree Counterclockwise Rotation around the $z$-axis
Imagine looking down from the positive $z$-axis toward the $xy$-plane (like looking at a clock lying flat facing you):
* **$\hat{k}$ is on the axis of rotation**, so it stays fixed:
  $$ \hat{k} \rightarrow \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} $$
* **$\hat{\imath}$ (pointing along $+x$)** rotates 90 degrees counterclockwise to point along the $+y$ direction:
  $$ \hat{\imath} \rightarrow \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} $$
* **$\hat{\jmath}$ (pointing along $+y$)** rotates 90 degrees counterclockwise to point along the $-x$ direction:
  $$ \hat{\jmath} \rightarrow \begin{bmatrix} -1 \\ 0 \\ 0 \end{bmatrix} $$

Our resulting matrix is:
$$ R_z(90^\circ) = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

---

### 4. Composition of 3D Transformations
Composing 3D transformations works exactly like composing 2D transformations: we multiply the matrices.

$$ \text{Total Effect} = M_2 M_1 \vec{\mathbf{v}} $$

We read the operations **right-to-left**: first apply the transformation on the right ($M_1$), then apply the transformation on the left ($M_2$).

Composition of $3 \times 3$ matrices is the absolute bedrock of **computer graphics, 3D game engines, and robotics**:
* A robot arm needs to calculate its hand's position by composing rotations of its shoulder, elbow, and wrist joints.
* A game engine describes a camera's view of a 3D world by composing a sequence of rotations (pitch, yaw, roll) and translations. Composing these into a single combined matrix allows the graphics hardware to transform millions of vertices in parallel.

---

### 5. Concept Teaser: Transformations Between Dimensions
Can you have a transformation between different dimensions? For example, mapping a 2D input to a 3D output?

Yes! If we have a transformation $T: \mathbb{R}^2 \rightarrow \mathbb{R}^3$:
* Since the input is 2D, we only track **two** basis vectors ($\hat{\imath}$ and $\hat{\jmath}$).
* Since the output is 3D, their landing spots are represented as 3D coordinates.
* The columns of our matrix will be 3D vectors, meaning the matrix has **3 rows and 2 columns** (a $3 \times 2$ matrix).
* The **column space** (all possible landing spots) will be a 2D plane slicing through the origin of 3D space.

We will dive deeper into non-square matrices in a future chapter, but it shows how beautifully this geometric framework scales to any dimensions!

---

### 6. Check Your Understanding

**Q1: Given the linear transformation defined by the matrix below, where does the vector $\vec{\mathbf{v}} = \begin{bmatrix} 1 \\ 0 \\ -2 \end{bmatrix}$ land?**
$$ A = \begin{bmatrix} 0 & 0.5 & -0.5 \\ 0 & 0.5 & 1 \\ 1 & 0 & 0.5 \end{bmatrix} $$

<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

1. **Step 1:** Express the multiplication as a linear combination of the columns of $A$, scaled by the components of $\vec{\mathbf{v}}$:
   $$ A\vec{\mathbf{v}} = 1 \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} + 0 \begin{bmatrix} 0.5 \\ 0.5 \\ 0 \end{bmatrix} - 2 \begin{bmatrix} -0.5 \\ 1 \\ 0.5 \end{bmatrix} $$
2. **Step 2:** Compute the scaled columns:
   $$ 1 \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} $$
   $$ 0 \begin{bmatrix} 0.5 \\ 0.5 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$
   $$ -2 \begin{bmatrix} -0.5 \\ 1 \\ 0.5 \end{bmatrix} = \begin{bmatrix} 1 \\ -2 \\ -1 \end{bmatrix} $$
3. **Step 3:** Sum the results:
   $$ \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 \\ -2 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 + 0 + 1 \\ 0 + 0 - 2 \\ 1 + 0 - 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix} $$
* **Result:** The transformed vector is $\begin{bmatrix} 1 \\ -2 \\ 0 \end{bmatrix}$.
</details>

**Q2: Why does the first column of a $3 \times 3$ matrix represent where the basis vector $\hat{\imath} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ lands? Prove it algebraically using matrix-vector multiplication.**
<details>
<summary><b>Reveal Answer & Algebraic Proof</b></summary>

Let our general $3 \times 3$ matrix $M$ have columns $\vec{\mathbf{c}}_1, \vec{\mathbf{c}}_2, \vec{\mathbf{c}}_3$:
$$ M = \begin{bmatrix} | & | & | \\ \vec{\mathbf{c}}_1 & \vec{\mathbf{c}}_2 & \vec{\mathbf{c}}_3 \\ | & | & | \end{bmatrix} $$
To find where $\hat{\imath} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ lands under $M$, we perform the multiplication:
$$ M \hat{\imath} = 1 \cdot \vec{\mathbf{c}}_1 + 0 \cdot \vec{\mathbf{c}}_2 + 0 \cdot \vec{\mathbf{c}}_3 = \vec{\mathbf{c}}_1 $$
Because the $y$ and $z$ coordinates are $0$, they completely cancel out any influence from the second and third columns. Thus, the output is exactly the first column $\vec{\mathbf{c}}_1$. This proves that the first column is literally the destination of $\hat{\imath}$.
</details>

---

[⏮️ **Previous: Chapter 04 — Matrix Multiplication as Composition**](04-matrix-multiplication-composition.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 06 — The Determinant: Scaling Space** ⏭️](06-determinant.md)
