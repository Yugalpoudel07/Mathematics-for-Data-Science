[⏮️ **Previous: 08 — Expected Values (Continuous)**](08-expected-values-continuous.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 10 — Pearson's Correlation** ⏭️](10-pearsons-correlation.md)

---

# 09: Covariance

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Covariance tells you whether two variables **move together**. If one tends to be above its average when the other is above its average, covariance is **positive**. If one tends to be high when the other is low, it's **negative**. If there's no consistent pattern, it's near **zero**. What covariance does **not** tell you well is *how strongly* they move together — its size depends on the units, which is why correlation (next topic) exists.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Picture

```text
   Positive covariance      Negative covariance      ~Zero covariance

     y                        y                        y
     ^        . .             ^ . .                    ^  .   .  .
     |      . .               |   . .                  | .  .  .
     |    . .                 |     . .                |   .  .   .
     |  . .                   |       . .              |  .   . .
     +---------> x            +---------> x            +---------> x

   high x with high y      high x with low y        no pattern
```

---

### 2. The Formula, Built Up

For each point, measure how far $x$ and $y$ are from their means, and **multiply** the two distances:

$$ (x_i - \bar{x})(y_i - \bar{y}) $$

```text
   The four quadrants around the mean point (xbar, ybar):

              y
              ^
     (-)(+)   |   (+)(+)
     product  |   product
     NEGATIVE |   POSITIVE
    ----------+-----------> x      (centered at xbar, ybar)
     (-)(-)   |   (+)(-)
     product  |   product
     POSITIVE |   NEGATIVE

   Points in the top-right and bottom-left push covariance UP.
   Points in the top-left and bottom-right push it DOWN.
```

Average those products:

$$ \boxed{\; \text{Cov}(x, y) = \frac{1}{n - 1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y}) \;} $$

(The $n-1$ is the same correction used for estimating variance — see topic 14.)

---

### 3. Worked Example

| $x$ | $y$ | $x - \bar{x}$ | $y - \bar{y}$ | product |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 2 | −2 | −2 | 4 |
| 2 | 3 | −1 | −1 | 1 |
| 3 | 4 | 0 | 0 | 0 |
| 4 | 5 | 1 | 1 | 1 |
| 5 | 6 | 2 | 2 | 4 |

$\bar{x} = 3$, $\bar{y} = 4$, sum of products $= 10$.

$$ \text{Cov}(x, y) = \frac{10}{5 - 1} = 2.5 $$

Positive — as $x$ rises, $y$ rises.

---

### 4. The Units Problem

Measure $x$ in metres instead of centimetres and covariance changes by a factor of 100 — even though the relationship is identical.

$$ \text{Cov}(aX, bY) = ab\,\text{Cov}(X, Y) $$

> **So the sign of covariance is meaningful, but its size is not comparable across datasets.** A covariance of 2.5 could be a strong or a weak relationship. Correlation fixes this by dividing out the spreads.

---

### 5. Related Facts

* $\text{Cov}(X, X) = \text{Var}(X)$ — variance is covariance of a variable with itself.
* $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)$
* Independent ⇒ covariance 0. **But covariance 0 does NOT imply independent** — covariance only detects **linear** relationships. ($y = x^2$ for symmetric $x$ has zero covariance yet is perfectly dependent.)

#### The Covariance Matrix

With many features, collect all pairwise covariances in a matrix $\Sigma$:

$$ \Sigma = \begin{bmatrix} \text{Var}(x_1) & \text{Cov}(x_1, x_2) \\ \text{Cov}(x_2, x_1) & \text{Var}(x_2) \end{bmatrix} $$

Symmetric, with variances on the diagonal. Its **eigenvectors** are the principal components (PCA) — see Essence of Linear Algebra, chapter 14.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Covariance matrix** | PCA | Principal components = eigenvectors of $\Sigma$ (Week 16 from-scratch) |
| **Feature co-movement** | Multicollinearity | Highly covarying features make regression coefficients unstable |
| **$\text{Var}(X+Y)$ formula** | Ensembling | Averaging models helps most when their errors have low covariance |
| **Multivariate normal** | Gaussian models | $N(\mu, \Sigma)$ — the covariance matrix defines the ellipse shape |
| **Whitening** | Preprocessing | Transform data so $\Sigma = I$ (uncorrelated, unit variance) |

---

### 7. Check Your Understanding

**Q1: Compute the covariance of $x = [2, 4, 6]$ and $y = [9, 6, 3]$.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

$\bar{x} = 4$, $\bar{y} = 6$. Products: $(-2)(3) = -6$, $(0)(0) = 0$, $(2)(-3) = -6$. Sum $= -12$.
$$ \text{Cov} = \frac{-12}{3 - 1} = -6 $$
Negative: as $x$ rises, $y$ falls.
</details>

**Q2: Two features have covariance 0. Can you safely say they're unrelated?**
<details>
<summary><b>Reveal Answer</b></summary>

No. Zero covariance only rules out a **linear** relationship. A U-shaped or circular relationship can have zero covariance while $y$ is completely determined by $x$. Always plot the data.
</details>

---

### 📺 Source

* **Video:** [Covariance](https://youtu.be/qtaqvPAeEJY)

---

[⏮️ **Previous: 08 — Expected Values (Continuous)**](08-expected-values-continuous.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 10 — Pearson's Correlation** ⏭️](10-pearsons-correlation.md)
