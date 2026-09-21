[⏮️ **Previous: Chapter 09 — Dot Products & Duality**](09-dot-products-duality.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 11 — Cross Products & Linear Transformations** ⏭️](11-cross-products-extended.md)

---

# Chapter 10: Cross Products

**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> While the dot product combines two vectors to return a single **number** (representing alignment and projection), the **cross product** combines two 3D vectors to return a brand new **vector**. This new vector is perpendicular to the plane formed by the original two vectors, its length equals the area of the parallelogram they span, and its direction is determined by the **right-hand rule**.

---

### 1. The 2D Concept: Parallelogram Area & Orientation

Before moving to 3D, it helps to understand the 2D version of the cross product, which measures the **oriented area** of the parallelogram spanned by two vectors $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$.

```text
Area of the parallelogram spanned by v = [-3, 1] and w = [2, 1]:

            y
            ^
            |      *-----------------*
        1 - |     /                 /
            |    /   Area = |v x w| /
            |   /                 /
        0 - *--+--------+--------+-----> x
           -3  |        0        2
               v = [-3, 1]        w = [2, 1]

  v x w = (-3)(1) - (1)(2) = -5,  so the area is 5 and the
  negative sign means w sits clockwise from v.
```

* **Magnitude (Area):** The length/area of the parallelogram formed by placing $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ tail-to-tail and completing the quadrilateral.
* **Orientation (Sign):**
  * **Positive ($+$):** If $\vec{\mathbf{w}}$ is a **counterclockwise** rotation away from $\vec{\mathbf{v}}$.
  * **Negative ($-$):** If $\vec{\mathbf{w}}$ is a **clockwise** rotation away from $\vec{\mathbf{v}}$.
  * **Order Matters (Anti-commutativity):** Swapping the order flips the orientation sign:
    $$ \vec{\mathbf{v}} \times \vec{\mathbf{w}} = -(\vec{\mathbf{w}} \times \vec{\mathbf{v}}) $$

#### Computing 2D Cross Product via Determinant

In 2D, the cross product is simply the determinant of the $2 \times 2$ matrix whose columns are $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$:

$$ \vec{\mathbf{v}} \times \vec{\mathbf{w}} = \det\left(\begin{bmatrix} v_1 & w_1 \\ v_2 & w_2 \end{bmatrix}\right) = v_1 w_2 - v_2 w_1 $$

* **Why this works:** The determinant measures how much a transformation scales area. Since the unit square spanned by $\hat{\imath}$ and $\hat{\jmath}$ has area $1$, transforming those basis vectors to $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ turns that unit square directly into our parallelogram!

---

### 2. Properties of the Cross Product

1. **Perpendicularity Boost:** The cross product is **largest** when $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$ are perpendicular ($90^\circ$), because a rectangle maximizes area. If the vectors are parallel or point in the same line, the area (and thus the cross product) is **zero**.
2. **Scaling:** Scaling either vector scales the cross product by the same factor:
   $$ (c \vec{\mathbf{v}}) \times \vec{\mathbf{w}} = c (\vec{\mathbf{v}} \times \vec{\mathbf{w}}) $$

---

### 3. The True 3D Cross Product

In 3D space, combining two 3D vectors via the cross product yields a **new 3D vector**:

$$ \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \times \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} p_1 \\ p_2 \\ p_3 \end{bmatrix} $$

```text
The 3D cross product v x w:

            ^  v x w
            |   (perpendicular to the plane of v and w,
            |    length = area of the parallelogram)
            |
            |
            *----------------*
           /                /
          /    v, w plane  /
         /                /
        *----------------*

  Direction is fixed by the right-hand rule:
  point your index finger along v, middle finger along w,
  and your thumb points along v x w.
```

1. **Magnitude:** The length of $\vec{\mathbf{v}} \times \vec{\mathbf{w}}$ equals the **area** of the 3D parallelogram spanned by $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$:
   $$ \|\vec{\mathbf{v}} \times \vec{\mathbf{w}}\| = \|\vec{\mathbf{v}}\| \|\vec{\mathbf{w}}\| \sin(\theta) $$
2. **Direction:** The vector points **perpendicular (orthogonal)** to the plane containing $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$.
3. **The Right-Hand Rule:** Out of the two possible opposite perpendicular directions, choose the direction using your right hand:
   * Point index finger in the direction of $\vec{\mathbf{v}}$.
   * Point middle finger in the direction of $\vec{\mathbf{w}}$.
   * Your extended thumb points in the direction of $\vec{\mathbf{v}} \times \vec{\mathbf{w}}$.

---

### 4. Computing the 3D Cross Product

To compute the 3D cross product, we use a symbolic $3 \times 3$ determinant where the first column contains the basis vectors $\hat{\imath}, \hat{\jmath}, \hat{k}$, and the second and third columns contain $\vec{\mathbf{v}}$ and $\vec{\mathbf{w}}$:

$$ \vec{\mathbf{v}} \times \vec{\mathbf{w}} = \det\left(\begin{bmatrix} \hat{\imath} & v_1 & w_1 \\ \hat{\jmath} & v_2 & w_2 \\ \hat{k} & v_3 & w_3 \end{bmatrix}\right) $$

Expanding along the first column gives:

$$ \vec{\mathbf{v}} \times \vec{\mathbf{w}} = \hat{\imath}(v_2 w_3 - v_3 w_2) - \hat{\jmath}(v_1 w_3 - v_3 w_1) + \hat{k}(v_1 w_2 - v_2 w_1) $$

In component form:

$$ \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \times \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} v_2 w_3 - v_3 w_2 \\ v_3 w_1 - v_1 w_3 \\ v_1 w_2 - v_2 w_1 \end{bmatrix} $$

*Note: While placing basis vectors inside a matrix seems like a "notational trick," Chapter 11 will show that this arises naturally from linear transformations and mathematical duality!*

---

### 5. Check Your Understanding

**Q1: What is the 2D cross product of $\vec{\mathbf{v}} = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$ and $\vec{\mathbf{w}} = \begin{bmatrix} 4 \\ 3 \end{bmatrix}$?**
<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

$$ \det\left(\begin{bmatrix} 1 & 4 \\ -2 & 3 \end{bmatrix}\right) = (1)(3) - (4)(-2) = 3 - (-8) = 11 $$

* **Result:** $11$. Since it is positive, $\vec{\mathbf{w}}$ is a counterclockwise rotation away from $\vec{\mathbf{v}}$.
</details>

**Q2: Given $\vec{\mathbf{v}} = \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}$ and $\vec{\mathbf{w}} = \begin{bmatrix} 0 \\ -3 \\ 0 \end{bmatrix}$, calculate their 3D cross product $\vec{\mathbf{v}} \times \vec{\mathbf{w}}$.**
<details>
<summary><b>Reveal Answer & Step-by-Step Derivation</b></summary>

Using the component formula or right-hand rule:

* $\vec{\mathbf{v}}$ points $2$ units along the $+x$ axis ($\hat{\imath}$).
* $\vec{\mathbf{w}}$ points $3$ units along the $-y$ axis ($-\hat{\jmath}$).
* Area of the rectangle $= 2 \times 3 = 6$.
* Right-hand rule: Index finger along $+x$, middle finger along $-y$ $\rightarrow$ Thumb points straight down along $-z$ ($-\hat{k}$).

$$ \vec{\mathbf{v}} \times \vec{\mathbf{w}} = \begin{bmatrix} 0 \\ 0 \\ -6 \end{bmatrix} $$
</details>

---

[⏮️ **Previous: Chapter 09 — Dot Products & Duality**](09-dot-products-duality.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 11 — Cross Products & Linear Transformations** ⏭️](11-cross-products-extended.md)
