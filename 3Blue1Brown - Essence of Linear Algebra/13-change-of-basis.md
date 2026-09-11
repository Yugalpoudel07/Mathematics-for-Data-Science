[⏮️ **Previous: Chapter 12 — Cramer's Rule Geometrically**](12-cramers-rule.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 14 — Eigenvectors & Eigenvalues** ⏭️](14-eigenvectors-eigenvalues.md)

---

# Chapter 13: Change of Basis
**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> Space itself has no intrinsic grid or default coordinate axes. A coordinate system is just a language we invent to describe vectors using numbers. The choice of **basis vectors** defines the language. When two people use different basis vectors, they are describing the exact same physical vectors and transformations in different languages. Changing your basis means translating descriptions back and forth between these mathematical languages.

---

### 1. Two Languages, Same Space
When we say a vector has coordinates $\begin{bmatrix} 3 \\ 2 \end{bmatrix}$, we are implicitly scaling our standard basis vectors $\hat{\imath} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\hat{\jmath} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$:

$$ \vec{\mathbf{v}} = 3\hat{\imath} + 2\hat{\jmath} $$

Now imagine a friend, **Jennifer**, who uses her own set of basis vectors $\vec{\mathbf{b}}_1$ and $\vec{\mathbf{b}}_2$:
* From our perspective, her basis vectors are $\vec{\mathbf{b}}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ and $\vec{\mathbf{b}}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$.
* From **her** perspective, they are simply her unit vectors $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

```text
  Our System (Standard Grid)             Jennifer's System (Tilted Grid)
           y                                       b2
           ^                                        ^  /
           |  (3,2)                                 | /  (5/3, 1/3)
  ---------+---------> x                   ---------+---------> b1
           |                                       /|
           |                                      / |
```

If Jennifer describes a vector as $\begin{bmatrix} 5/3 \\ 1/3 \end{bmatrix}$, she means:

$$ \frac{5}{3}\vec{\mathbf{b}}_1 + \frac{1}{3}\vec{\mathbf{b}}_2 $$

When calculated using our coordinate system, this yields:

$$ \frac{5}{3}\begin{bmatrix} 2 \\ 1 \end{bmatrix} + \frac{1}{3}\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 10/3 - 1/3 \\ 5/3 + 1/3 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix} $$

Both of us are pointing to the exact same arrow in space, but using different numbers to describe it.

---

### 2. The Change of Basis Matrix ($P$)

#### A. Translating Her Language to Ours
To convert a vector from Jennifer's coordinates ($\vec{\mathbf{v}}_{\text{Jennifer}}$) to our coordinates ($\vec{\mathbf{v}}_{\text{Our}}$), place her basis vectors as the columns of a matrix $P$:

$$ P = \begin{bmatrix} \vec{\mathbf{b}}_1 & \vec{\mathbf{b}}_2 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix} $$

Multiplying her coordinates by $P$ computes the linear combination of her basis vectors:

$$ \vec{\mathbf{v}}_{\text{Our}} = P \cdot \vec{\mathbf{v}}_{\text{Jennifer}} $$

*Example:* If Jennifer gives us $\vec{\mathbf{v}}_{\text{Jennifer}} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$:

$$ \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \end{bmatrix} = -1\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 2\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ 1 \end{bmatrix}_{\text{Our}} $$

---

#### B. Translating Our Language to Hers
To convert a vector from our coordinates ($\vec{\mathbf{v}}_{\text{Our}}$) to Jennifer's coordinates ($\vec{\mathbf{v}}_{\text{Jennifer}}$), we reverse the process using the **inverse matrix** $P^{-1}$:

$$ \vec{\mathbf{v}}_{\text{Jennifer}} = P^{-1} \cdot \vec{\mathbf{v}}_{\text{Our}} $$

For $P = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$, $\det(P) = (2)(1) - (-1)(1) = 3$. The inverse is:

$$ P^{-1} = \frac{1}{3} \begin{bmatrix} 1 & 1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{bmatrix} $$

*Example:* Converting our vector $\begin{bmatrix} 3 \\ 2 \end{bmatrix}$ to Jennifer's system:

$$ \begin{bmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 3/3 + 2/3 \\ -3/3 + 4/3 \end{bmatrix} = \begin{bmatrix} 5/3 \\ 1/3 \end{bmatrix}_{\text{Jennifer}} $$

---

### 3. Translating Transformations ($P^{-1} M P$)

Suppose we have a linear transformation $M$ defined in our coordinate system (for example, a $90^\circ$ counterclockwise rotation $M = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$). How would Jennifer describe this same physical transformation in **her** language?

We cannot just multiply her vectors directly by $M$, because $M$ expects inputs in *our* language and produces outputs in *our* language. 

To apply $M$ to a vector $\vec{\mathbf{v}}_{\text{Jennifer}}$ in Jennifer's language, we follow a 3-step pipeline:

```text
Jennifer's Input Vector:  v_Jennifer
       │
       │  1. Multiply by P (Translate to Our Language)
       ▼
   P · v_Jennifer
       │
       │  2. Multiply by M (Apply Transformation in Our Language)
       ▼
 M · P · v_Jennifer
       │
       │  3. Multiply by P⁻¹ (Translate Back to Jennifer's Language)
       ▼
Jennifer's Output Vector: P⁻¹ M P · v_Jennifer
```

#### The "Mathematical Empathy" Formula:
$$ M_{\text{Jennifer}} = P^{-1} M P $$

* **$P$ (Translate in):** Converts Jennifer's vector into our language.
* **$M$ (Transform):** Performs the linear transformation as we understand it.
* **$P^{-1}$ (Translate out):** Converts the transformed result back into Jennifer's language.

Whenever you see the structure **$P^{-1} M P$**, think of it as **perspective shifting** or "mathematical empathy"—performing a transformation as seen from another coordinate system.

---

### 4. Summary Table of Basis Translation

| Operation | Formula | Meaning |
| :--- | :--- | :--- |
| **Jennifer $\to$ Our Vector** | $\vec{\mathbf{v}}_{\text{Our}} = P \vec{\mathbf{v}}_{\text{Jennifer}}$ | Scale her basis vectors by her coordinates. |
| **Our $\to$ Jennifer Vector** | $\vec{\mathbf{v}}_{\text{Jennifer}} = P^{-1} \vec{\mathbf{v}}_{\text{Our}}$ | Apply the inverse change of basis matrix. |
| **Transformation in Her Basis** | $M_{\text{Jennifer}} = P^{-1} M P$ | Translate to our basis, transform, and translate back. |

---

### 5. Check Your Understanding

**Q1: If Jennifer's basis vectors are $\vec{\mathbf{b}}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ and $\vec{\mathbf{b}}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$, what is the vector $\begin{bmatrix} 2 \\ -3 \end{bmatrix}_{\text{Jennifer}}$ expressed in the standard basis?**
<details>
<summary><b>Reveal Answer & Calculation</b></summary>

$$ \vec{\mathbf{v}}_{\text{Our}} = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ -3 \end{bmatrix} = 2\begin{bmatrix} 2 \\ 1 \end{bmatrix} - 3\begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 + 3 \\ 2 - 3 \end{bmatrix} = \begin{bmatrix} 7 \\ -1 \end{bmatrix} $$
</details>

**Q2: What is the geometric interpretation of the matrix product $P^{-1} M P$?**
<details>
<summary><b>Reveal Answer</b></summary>

It performs the linear transformation $M$ (defined in standard coordinates) on a vector expressed in an alternate basis $P$, by first translating the vector to standard coordinates ($P$), applying the transformation ($M$), and translating the result back to the alternate basis ($P^{-1}$).
</details>

---

[⏮️ **Previous: Chapter 12 — Cramer's Rule Geometrically**](12-cramers-rule.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 14 — Eigenvectors & Eigenvalues** ⏭️](14-eigenvectors-eigenvalues.md)
