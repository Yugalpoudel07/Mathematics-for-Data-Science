[⏮️ **Previous: 07 — Expected Values (Discrete)**](07-expected-values-discrete.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 09 — Covariance** ⏭️](09-covariance.md)

---

# 08: Expected Values, Part 2 (Continuous)

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> For a continuous variable there are infinitely many possible values, so you can't list them and add. The idea is unchanged — **each value weighted by how likely it is** — but the sum becomes an **integral** and the probability becomes the **density**. Picture slicing the range into many thin strips, doing the discrete calculation on the strips, and letting them get infinitely thin.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. From Sum to Integral

Discrete (topic 07):
$$ \mathbb{E}[X] = \sum_x x \cdot P(X = x) $$

Continuous: chop the $x$-axis into strips of width $dx$. A strip at $x$ has probability ≈ $f(x)\,dx$. Weight by $x$ and add up the strips:

$$ \boxed{\; \mathbb{E}[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx \;} $$

```text
   Each thin strip contributes  x * f(x) dx

    f(x)
      ^
      |       _---_
      |     / |#| \          strip at x:
      |   /   |#|   \           probability ~= f(x) dx
      | /     |#|     \         contribution = x * f(x) dx
      +-------|#|-------> x
              x
              |dx|

   Add up every strip  ->  integral  ->  E[X]
```

This is exactly the "slice, approximate, sum" idea from Essence of Calculus, chapter 1.

---

### 2. Worked Example: Uniform Distribution

$X \sim \text{Uniform}(0, 10)$ — every value in $[0, 10]$ equally likely. The density is $f(x) = \frac{1}{10}$ on that interval.

$$ \mathbb{E}[X] = \int_0^{10} x \cdot \frac{1}{10}\,dx = \frac{1}{10}\left[\frac{x^2}{2}\right]_0^{10} = \frac{1}{10}\cdot 50 = 5 $$

The midpoint — as symmetry suggests.

### 3. Worked Example: Exponential Waiting Time

Wait times with $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$. With $\lambda = 0.5$ per minute:

$$ \mathbb{E}[X] = \int_0^\infty x\,\lambda e^{-\lambda x}\,dx = \frac{1}{\lambda} = 2 \text{ minutes} $$

(Solved by integration by parts.) The higher the rate $\lambda$, the shorter the expected wait.

---

### 4. Expected Value of a Function

$$ \mathbb{E}[g(X)] = \int g(x)\,f(x)\,dx $$

Variance follows directly:
$$ \text{Var}(X) = \mathbb{E}[(X-\mu)^2] = \int (x - \mu)^2 f(x)\,dx $$

For the normal distribution $N(\mu, \sigma^2)$: $\mathbb{E}[X] = \mu$ and $\text{Var}(X) = \sigma^2$ — which is exactly why those are its two parameters.

---

### 5. Discrete vs Continuous Side by Side

| | Discrete | Continuous |
| :--- | :--- | :--- |
| **Probability of outcomes** | $P(X = x)$ (a mass) | $f(x)\,dx$ (density × width) |
| **Combine by** | Sum $\sum$ | Integral $\int$ |
| **$\mathbb{E}[X]$** | $\sum x\,P(X=x)$ | $\int x\,f(x)\,dx$ |
| **Linearity holds?** | Yes | Yes |

---

### 6. Estimating an Expected Value From Data

You rarely know $f(x)$. But if you have samples $x_1, \dots, x_n$ from it, the **sample average** estimates the expected value:

$$ \mathbb{E}[g(X)] \approx \frac{1}{n}\sum_{i=1}^n g(x_i) $$

This is **Monte Carlo estimation**, and it's how almost every expected value in ML is actually computed.

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **$\int \ell\, f\, dx$** | True risk of a model | $R(\theta) = \int \ell(\theta; x)\,p(x)\,dx$ — the thing you want small |
| **Sample average estimates it** | Empirical risk minimization | The training loss $\frac{1}{n}\sum_i \ell_i$ is a Monte Carlo estimate of $R$ |
| **Generalization gap** | Overfitting | Training loss (sample average) vs true risk (integral) can differ |
| **Expectations of functions** | VAEs, diffusion, RL | ELBO and policy gradients are expectations estimated by sampling |
| **Mean & variance of a normal** | Gaussian models | $\mu$ and $\sigma^2$ are literally $\mathbb{E}[X]$ and $\text{Var}(X)$ |

---

### 8. Check Your Understanding

**Q1: $X$ has density $f(x) = 2x$ on $[0, 1]$. Find $\mathbb{E}[X]$.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

1. Check it's a valid density: $\int_0^1 2x\,dx = [x^2]_0^1 = 1$ ✓
2. $\mathbb{E}[X] = \int_0^1 x \cdot 2x\,dx = \int_0^1 2x^2\,dx = \left[\frac{2x^3}{3}\right]_0^1 = \frac{2}{3}$

More density sits near 1, so the mean (0.667) is above the midpoint 0.5.
</details>

**Q2: Why is training loss usually lower than test loss, in expected-value terms?**
<details>
<summary><b>Reveal Answer</b></summary>

Both are sample averages estimating the same integral (the true risk). But the model's parameters were **chosen to make the training average small**, so the training sample is no longer an unbiased estimate — it's optimistically biased. The test set was not used to fit parameters, so its average remains an unbiased estimate of the true risk.
</details>

---

### 📺 Source

* **Video:** [Expected Values, Part 2](https://youtu.be/OSPr6G6Ka-U)

---

[⏮️ **Previous: 07 — Expected Values (Discrete)**](07-expected-values-discrete.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 09 — Covariance** ⏭️](09-covariance.md)
