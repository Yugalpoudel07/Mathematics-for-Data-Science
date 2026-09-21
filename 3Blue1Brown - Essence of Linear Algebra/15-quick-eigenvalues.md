[⏮️ **Previous: Chapter 14 — Eigenvectors & Eigenvalues**](14-eigenvectors-eigenvalues.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 16 — Abstract Vector Spaces** ⏭️](16-abstract-vector-spaces.md)

---

# Chapter 15: A Quick Trick for Computing Eigenvalues

**Essence of Linear Algebra — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**  
> Instead of setting up the characteristic polynomial $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ and using the quadratic formula, you can instantly read off the eigenvalues of any $2 \times 2$ matrix by finding the **mean** $m$ of its diagonal entries (half the trace) and its **determinant** $p$. The eigenvalues are simply $m \pm \sqrt{m^2 - p}$.

---

### 1. The Standard Method vs. The Shortcut

To find the eigenvalues of a $2 \times 2$ matrix $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, standard textbooks teach you to solve the characteristic equation:

$$ \det(\mathbf{A} - \lambda \mathbf{I}) = \det\left(\begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix}\right) = 0 $$

Expanding this yields the characteristic polynomial:

$$ \lambda^2 - (a + d)\lambda + (ad - bc) = 0 $$

Applying the quadratic formula requires several algebraic steps of expanding, grouping, and simplifying:

$$ \lambda_{1,2} = \frac{(a + d) \pm \sqrt{(a + d)^2 - 4(ad - bc)}}{2} $$

While this process is straightforward, it requires a lot of mechanical scratch work. For $2 \times 2$ matrices, there is a much more direct, intuitive way to read the answers straight off the matrix.

---

### 2. The Three Fundamental Facts

The quick trick relies on three elegant mathematical facts:

#### Fact 1: The Mean of Eigenvalues is the Mean of the Diagonal (Trace)

The **trace** of a matrix $\text{tr}(\mathbf{A})$ is the sum of its diagonal entries ($a + d$). The trace always equals the sum of the eigenvalues ($\lambda_1 + \lambda_2 = a + d$).
Dividing by $2$ gives the **mean** $m$ of the two eigenvalues:

$$ m = \frac{\lambda_1 + \lambda_2}{2} = \frac{a + d}{2} = \frac{1}{2} \text{tr}(\mathbf{A}) $$

#### Fact 2: The Product of Eigenvalues is the Determinant

The **determinant** of a $2 \times 2$ matrix $p = ad - bc$ always equals the product of its eigenvalues:

$$ p = \lambda_1 \cdot \lambda_2 = \det(\mathbf{A}) $$

#### Fact 3: The Mean-Product Formula (Difference of Squares)

When two numbers $\lambda_1, \lambda_2$ have a known mean $m$ and product $p$, they are positioned symmetrically around $m$ on the number line at some distance $d$:

$$ \lambda_1 = m + d, \quad \lambda_2 = m - d $$

Multiplying them together gives a difference of squares:

$$ p = (m + d)(m - d) = m^2 - d^2 $$

Solving for distance $d$:

$$ d^2 = m^2 - p \implies d = \sqrt{m^2 - p} $$

Putting it all together gives the **Mean-Product Formula**:

$$ \lambda_{1, 2} = m \pm \sqrt{m^2 - p} $$

```text
Visualizing Eigenvalues on the Number Line:

            d                  d
      <----------->      <----------->
  ----+------------+------------+---->
     λ₁ = m - d    m           λ₂ = m + d
                   |
            Mean of diagonal: m = (a + d) / 2
            Distance squared: d² = m² - det(A)
```

---

### 3. Step-by-Step Algorithm for a $2 \times 2$ Matrix

Given any $2 \times 2$ matrix $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:

1. **Calculate the Mean ($m$):** Average the diagonal entries $\to m = \frac{a + d}{2}$.
2. **Calculate the Product ($p$):** Find the determinant $\to p = ad - bc$.
3. **Plug into Formula:** $\lambda_{1, 2} = m \pm \sqrt{m^2 - p}$.

---

### 4. Worked Examples

#### Example A: Standard Matrix

Find the eigenvalues of $\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 4 & 1 \end{bmatrix}$.

1. **Mean ($m$):** $\frac{3 + 1}{2} = 2$
2. **Product ($p$):** $\det(\mathbf{A}) = (3)(1) - (1)(4) = 3 - 4 = -1$
3. **Apply Formula:**
   $$ \lambda_{1, 2} = 2 \pm \sqrt{2^2 - (-1)} = 2 \pm \sqrt{4 + 1} = 2 \pm \sqrt{5} $$

---

#### Example B: Integer Eigenvalues

Find the eigenvalues of $\mathbf{B} = \begin{bmatrix} 2 & 7 \\ 1 & 8 \end{bmatrix}$.

1. **Mean ($m$):** $\frac{2 + 8}{2} = 5$
2. **Product ($p$):** $\det(\mathbf{B}) = (2)(8) - (7)(1) = 16 - 7 = 9$
3. **Apply Formula:**
   $$ \lambda_{1, 2} = 5 \pm \sqrt{5^2 - 9} = 5 \pm \sqrt{25 - 9} = 5 \pm \sqrt{16} = 5 \pm 4 $$
   * **Result:** $\lambda_1 = 9, \quad \lambda_2 = 1$

---

#### Example C: Quantum Mechanics Application (Pauli Spin Matrices)

In physics, the **Pauli spin matrices** describe quantum particle spin:

$$ \sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} $$

* For all three matrices, the diagonal mean $m = 0$ and the determinant $p = -1$.
* Using the shortcut: $\lambda_{1,2} = 0 \pm \sqrt{0^2 - (-1)} = \pm 1$.

Furthermore, for a general normalized measurement direction $a\sigma_x + b\sigma_y + c\sigma_z$ (where $a^2 + b^2 + c^2 = 1$):

* Matrix: $\begin{bmatrix} c & a - bi \\ a + bi & -c \end{bmatrix}$
* **Mean ($m$):** $\frac{c + (-c)}{2} = 0$
* **Product ($p$):** $-c^2 - (a - bi)(a + bi) = -c^2 - (a^2 + b^2) = -(a^2 + b^2 + c^2) = -1$
* **Eigenvalues:** $\lambda_{1,2} = 0 \pm \sqrt{0 - (-1)} = \pm 1$

While computing the characteristic polynomial for a complex combination matrix is tedious, the mean-product trick yields the physical eigenvalues ($\pm 1$) instantly in your head.

---

### 5. Why This Reframes the Quadratic Formula

Mathematically, $m \pm \sqrt{m^2 - p}$ is identical to the quadratic formula for $\lambda^2 - 2m\lambda + p = 0$. However, the standard quadratic formula relies on abstract coefficients ($A, B, C$), whereas the **mean-product formula** directly connects the math to meaningful geometric properties of the transformation:

| Term | Algebraic Symbol | Geometric / Structural Meaning |
| :--- | :--- | :--- |
| **$m$** | $-\frac{B}{2A}$ | Center point of the eigenvalues (Average diagonal stretch) |
| **$p$** | $\frac{C}{A}$ | Area / volume scaling factor (Determinant) |
| **$d = \sqrt{m^2 - p}$** | $\frac{\sqrt{B^2 - 4AC}}{2A}$ | Spread / distance of eigenvalues from the mean |

---

### 6. Check Your Understanding

**Q1: What are the eigenvalues of $\mathbf{M} = \begin{bmatrix} 2 & 3 \\ 2 & 4 \end{bmatrix}$?**
<details>
<summary><b>Reveal Answer & Step-by-Step Solution</b></summary>

1. **Mean ($m$):** $\frac{2 + 4}{2} = 3$
2. **Product ($p$):** $\det(\mathbf{M}) = (2)(4) - (3)(2) = 8 - 6 = 2$
3. **Eigenvalues:** $m \pm \sqrt{m^2 - p} = 3 \pm \sqrt{3^2 - 2} = 3 \pm \sqrt{7}$
</details>

**Q2: What are the eigenvalues of $\mathbf{N} = \begin{bmatrix} 8 & 4 \\ 2 & 6 \end{bmatrix}$?**
<details>
<summary><b>Reveal Answer & Step-by-Step Solution</b></summary>

1. **Mean ($m$):** $\frac{8 + 6}{2} = 7$
2. **Product ($p$):** $\det(\mathbf{N}) = (8)(6) - (4)(2) = 48 - 8 = 40$
3. **Eigenvalues:** $m \pm \sqrt{m^2 - p} = 7 \pm \sqrt{7^2 - 40} = 7 \pm \sqrt{49 - 40} = 7 \pm \sqrt{9} = 7 \pm 3$
* **Result:** $\lambda_1 = 10, \quad \lambda_2 = 4$
</details>

---

[⏮️ **Previous: Chapter 14 — Eigenvectors & Eigenvalues**](14-eigenvectors-eigenvalues.md) &nbsp;•&nbsp; [📚 **Essence of Linear Algebra Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 16 — Abstract Vector Spaces** ⏭️](16-abstract-vector-spaces.md)
