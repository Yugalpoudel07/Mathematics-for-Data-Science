[⏮️ **Previous: 09 — Covariance**](09-covariance.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 11 — The Central Limit Theorem** ⏭️](11-central-limit-theorem.md)

---

# 10: Pearson's Correlation

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Correlation is covariance with the units stripped off. Divide covariance by the two standard deviations and you get a number always between **−1 and +1** that says **how tightly the points hug a straight line**. +1 is a perfect upward line, −1 a perfect downward line, 0 no linear pattern. It measures *how predictable* $y$ is from $x$ with a line — **not** how steep the line is, and **not** whether one causes the other.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Formula

$$ \boxed{\; r = \frac{\text{Cov}(x, y)}{s_x\, s_y} \;} $$

Dividing by the standard deviations cancels the units, so $r$ is comparable across any datasets.

**Worked example** (from topic 09): $x = [1,2,3,4,5]$, $y = [2,3,4,5,6]$, $\text{Cov} = 2.5$, $s_x = s_y = \sqrt{2.5}$:
$$ r = \frac{2.5}{\sqrt{2.5}\cdot\sqrt{2.5}} = 1 $$
A perfect line — $y = x + 1$.

---

### 2. What Different Values Look Like

```text
   r = +1.0         r = +0.7          r = 0            r = -0.7         r = -1.0
      .              . .               . .  .           . .              .
     .             .  . .            .   .  .          .  . .             .
    .             . . .                .  .   .          . . .             .
   .            . . .              .  .   .               . .               .
  .             .                   .    .                  .                .

  perfect        tight-ish         no linear          tight-ish         perfect
  upward         upward            pattern            downward          downward
```

---

### 3. Correlation Is NOT the Slope

```text
   Both have r = 1.0:

    y                          y
    ^         .                ^
    |       .                  |
    |     .                    |               .  .  .
    |   .                      |   .  .  .  .
    | .                        +------------------------> x
    +--------------> x

    steep slope                shallow slope
```

Both lines are perfectly predictable, so both have $r = 1$. Slope comes from regression, not correlation.

---

### 4. $R^2$: Fraction of Variation Explained

Squaring gives $r^2$ (for simple linear regression, $R^2$): the **fraction of the variation in $y$ explained by a straight line in $x$**.

| $r$ | $r^2$ | Interpretation |
| :-: | :-: | :--- |
| 0.9 | 0.81 | 81% of the variation in $y$ explained |
| 0.7 | 0.49 | Under half explained |
| 0.3 | 0.09 | Only 9% explained — weak |

> **$r = 0.7$ sounds strong, but it explains less than half the variation.** $r^2$ is often the more honest number to report.

---

### 5. Is the Correlation Real? Sample Size Matters

With few points, a large $r$ can appear by pure chance. Two random points *always* lie on a line ($r = \pm 1$).

| Sample size | Typical $r$ from pure noise |
| :-: | :--- |
| 5 | easily ±0.8 |
| 30 | usually within ±0.35 |
| 1000 | usually within ±0.06 |

StatQuest emphasizes pairing $r$ (or $R^2$) with a **p-value** or confidence interval, which accounts for sample size.

---

### 6. The Big Warnings

1. **Correlation ≠ causation.** Ice-cream sales and drownings correlate — both are driven by hot weather (a **confounder**).
2. **Only linear relationships.** A perfect U-shape can give $r \approx 0$.
3. **Outliers dominate.** One extreme point can create or destroy a correlation.

```text
   One outlier fakes a correlation:

    y
    ^                              .   <- one extreme point
    |
    |  . .  .
    | .  .  .  .                   r jumps from ~0 to ~0.8
    |  .  . .
    +--------------------------> x
```

Always plot before computing $r$. (Look up **Anscombe's quartet**: four datasets with identical $r$ and wildly different shapes.)

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Correlation matrix** | Feature screening / EDA | Heatmap of feature correlations; drop near-duplicate features |
| **$R^2$** | Regression evaluation | Reported by every regression model; compare to a baseline |
| **Correlation ≠ causation** | Honest conclusions | A predictive feature is not a lever you can pull — needs experiments |
| **Cosine similarity** | Embeddings | Pearson $r$ is the cosine similarity of **mean-centered** vectors |
| **Outlier sensitivity** | Robust statistics | Spearman rank correlation is used when outliers or monotone curves are present |
| **Spurious correlations** | Data leakage | A feature suspiciously correlated with the target often leaks the answer |

---

### 8. Check Your Understanding

**Q1: $\text{Cov}(x,y) = -12$, $s_x = 4$, $s_y = 5$. Find $r$ and $r^2$ and interpret.**
<details>
<summary><b>Reveal Answer</b></summary>

$r = \frac{-12}{4 \times 5} = -0.6$, $r^2 = 0.36$. A moderate negative linear relationship; a line in $x$ explains 36% of the variation in $y$.
</details>

**Q2: A dataset of 6 cities shows $r = 0.85$ between number of coffee shops and average income. Give two reasons not to conclude "opening coffee shops raises incomes."**
<details>
<summary><b>Reveal Answer</b></summary>

1. **Causation direction / confounding:** richer cities attract coffee shops (reverse causation), and city size drives both (confounder).
2. **Tiny sample:** with $n=6$, a large $r$ can arise by chance; the p-value or confidence interval would be wide.

(Also: one big city could be an outlier driving the whole correlation.)
</details>

---

### 📺 Source

* **Video:** [Pearson's Correlation](https://youtu.be/xZ_z8KWkhXE)

---

[⏮️ **Previous: 09 — Covariance**](09-covariance.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 11 — The Central Limit Theorem** ⏭️](11-central-limit-theorem.md)
