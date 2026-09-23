[⏮️ **Previous: 04 — Bayes' Theorem**](04-bayes-theorem.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 06 — The Normal Distribution** ⏭️](06-normal-distribution.md)

---

# 05: The Binomial Distribution and Test

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> The binomial distribution answers one question: **"If I repeat a yes/no trial $n$ times, each with the same chance $p$ of 'yes', how likely is it that I get exactly $k$ yeses?"** Coin flips, click-throughs, defective parts, people who prefer product A — anything with a fixed number of independent two-outcome trials. The **binomial test** then flips the question around: given what I observed, is the true $p$ plausibly what I assumed?

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Setup: Four Conditions

A count $X$ is binomial, written $X \sim \text{Binomial}(n, p)$, when:

1. **Fixed number of trials** $n$.
2. **Two outcomes** per trial (success / failure).
3. **Same probability** $p$ of success on every trial.
4. **Independent** trials.

> The single-trial case ($n=1$) is called a **Bernoulli** trial. A binomial count is just the sum of $n$ Bernoulli trials.

---

### 2. Building the Formula From Scratch

**Question:** 3 people each choose between pumpkin pie and blueberry pie; each prefers pumpkin with $p = 0.7$. What's the chance **exactly 2** prefer pumpkin?

**Step 1 — One specific arrangement.** Pumpkin, Pumpkin, Blueberry:
$$ 0.7 \times 0.7 \times 0.3 = 0.147 $$

**Step 2 — Count the arrangements.** Which 2 of the 3 people chose pumpkin?

```text
   All arrangements with exactly 2 pumpkins:

      P P B      P B P      B P P
      0.147      0.147      0.147

   3 arrangements, each with the same probability.
```

**Step 3 — Multiply:**
$$ P(X = 2) = 3 \times 0.147 = 0.441 $$

**The number of arrangements** is "$n$ choose $k$":
$$ \binom{n}{k} = \frac{n!}{k!\,(n-k)!} \qquad \binom{3}{2} = \frac{6}{2 \cdot 1} = 3 $$

---

### 3. The Binomial Formula

$$ \boxed{\; P(X = k) = \binom{n}{k}\,p^k\,(1-p)^{n-k} \;} $$

| Piece | Meaning |
| :--- | :--- |
| $\binom{n}{k}$ | How many ways to arrange $k$ successes among $n$ trials |
| $p^k$ | Probability of the $k$ successes |
| $(1-p)^{n-k}$ | Probability of the $n-k$ failures |

#### The Full Distribution for $n = 3$, $p = 0.7$

| $k$ | Calculation | $P(X=k)$ |
| :-: | :--- | :-: |
| 0 | $1 \cdot 0.3^3$ | 0.027 |
| 1 | $3 \cdot 0.7 \cdot 0.3^2$ | 0.189 |
| 2 | $3 \cdot 0.7^2 \cdot 0.3$ | 0.441 |
| 3 | $1 \cdot 0.7^3$ | 0.343 |
| | **Total** | **1.000** ✓ |

```text
   P(X = k)
     ^
 0.4 +             ###
     |             ###   ###
 0.2 +       ###   ###   ###
     |       ###   ###   ###
   0 +-###---###---###---###--> k
        0     1     2     3
```

---

### 4. Mean and Variance

$$ \mathbb{E}[X] = np \qquad \text{Var}(X) = np(1-p) $$

**Why $np$:** each trial contributes $p$ successes on average; $n$ trials contribute $np$.
**Why variance peaks at $p = 0.5$:** $p(1-p)$ is largest at $0.25$ — outcomes are most unpredictable when both are equally likely.

For $n=3$, $p=0.7$: mean $= 2.1$, variance $= 0.63$.

---

### 5. The Binomial Test

**Scenario:** you assume people have no preference ($p = 0.5$). You survey 7 people and **all 7** prefer pumpkin. Is "no preference" still believable?

**Step 1 — Probability of a result this extreme or more**, assuming $p = 0.5$:
$$ P(X = 7) = 0.5^7 = \frac{1}{128} \approx 0.0078 $$

**Step 2 — Two-sided:** "extreme" also includes all 7 preferring blueberry:
$$ p\text{-value} = 2 \times 0.0078 \approx 0.0156 $$

**Step 3 — Interpret:** if there were truly no preference, a result this lopsided would happen only ~1.6% of the time. That's unusual enough (below the common 0.05 threshold) to doubt the "no preference" assumption.

> **Careful with the meaning:** the p-value is $P(\text{data this extreme} \mid \text{assumption true})$ — **not** the probability the assumption is true. (That confusion is exactly the reversed-conditional trap from topic 03. Hypothesis testing gets the full treatment in Week 5.)

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Bernoulli / binomial** | Modeling binary outcomes | Logistic regression models each label as Bernoulli($p$) |
| **Binomial likelihood** | Where binary cross-entropy comes from | $-\log[p^y(1-p)^{1-y}]$ = BCE loss (topics 20, 22) |
| **Binomial test** | Is a classifier better than chance? | 70 correct out of 100 on a balanced task — test vs $p=0.5$ |
| **Variance $np(1-p)$** | Uncertainty in accuracy estimates | Accuracy on $n$ test items has standard error $\sqrt{p(1-p)/n}$ |
| **A/B testing** | Conversion experiments | Clicks out of visitors in each variant are binomial counts |

---

### 7. Check Your Understanding

**Q1: A model is 80% accurate. On 5 random test items, what's the probability it gets exactly 4 right?**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

$$ P(X=4) = \binom{5}{4}(0.8)^4(0.2)^1 = 5 \times 0.4096 \times 0.2 = 0.4096 $$

* **Result:** about 41%.
</details>

**Q2: Your model scores 540/1000 on a balanced binary task. Estimate the standard error of its accuracy. Is it clearly better than a coin flip?**
<details>
<summary><b>Reveal Answer</b></summary>

Under chance ($p=0.5$): $\text{SE} = \sqrt{0.5 \times 0.5 / 1000} \approx 0.0158$. The observed 0.54 is $\frac{0.04}{0.0158} \approx 2.5$ standard errors above 0.5 — unlikely by chance alone (roughly $p \approx 0.01$). So it is probably better than a coin flip, but only modestly. Still compare against a real baseline (e.g. majority class, simple logistic regression), not just chance.
</details>

**Q3: Why isn't "number of heads until the first tail" binomial?**
<details>
<summary><b>Reveal Answer</b></summary>

It breaks condition 1: the number of trials is **not fixed** — you keep flipping until a tail appears. That count follows a **geometric** distribution instead.
</details>

---

### 📺 Source

* **Video:** [The Binomial Distribution and Test](https://youtu.be/J8jNoF-K8E8)

---

[⏮️ **Previous: 04 — Bayes' Theorem**](04-bayes-theorem.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 06 — The Normal Distribution** ⏭️](06-normal-distribution.md)
