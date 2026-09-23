[⏮️ **Previous: 22 — MLE — Binomial Distribution**](22-mle-binomial-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [🏠 **Repository Home**](../README.md)

---

# 23: Maximum Likelihood for the Exponential Distribution *(Optional)*

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> The exponential distribution models **waiting times** — time until the next customer, the next failure, the next click. Its single parameter $\lambda$ is the **rate** (events per unit time). Given observed waiting times, maximum likelihood says the best rate is **one over the average wait**: if customers arrive on average every 4 minutes, the rate is 0.25 per minute. Another case where MLE confirms intuition — through the same five-step recipe.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Exponential Distribution

$$ f(x \mid \lambda) = \lambda e^{-\lambda x}, \qquad x \ge 0 $$

```text
   Exponential densities:

    f(x)
      ^
  2.0 +\                        lambda = 2   (fast events, short waits)
      | \
  1.0 +  \\                     lambda = 1
      |   \ \
  0.5 +    \  \__               lambda = 0.5 (slow events, long waits)
      |     \__  ---___
      +--------------------------> x (waiting time)
      0

   Short waits are always most likely; long waits are rare.
   Mean wait = 1 / lambda.
```

---

### 2. Likelihood and Log-Likelihood

Observed waits $x_1, \ldots, x_n$:

$$ L(\lambda) = \prod_{i=1}^n \lambda e^{-\lambda x_i} = \lambda^n e^{-\lambda \sum x_i} $$

$$ \ell(\lambda) = n\log\lambda - \lambda\sum_{i=1}^n x_i $$

### 3. Differentiate and Solve

$$ \frac{d\ell}{d\lambda} = \frac{n}{\lambda} - \sum_{i=1}^n x_i = 0 $$

$$ \boxed{\; \hat{\lambda} = \frac{n}{\sum x_i} = \frac{1}{\bar{x}} \;} $$

**Check it's a maximum:** $\frac{d^2\ell}{d\lambda^2} = -\frac{n}{\lambda^2} < 0$ ✓ (the second-derivative test from Essence of Calculus, ch. 10).

---

### 4. Worked Example

Waiting times (minutes): $[2, 5, 1, 4, 3]$.

$$ \bar{x} = \frac{15}{5} = 3 \;\Longrightarrow\; \hat{\lambda} = \frac{1}{3} \approx 0.333 \text{ per minute} $$

About one event every 3 minutes.

---

### 5. The Memoryless Property

The exponential distribution "forgets": if you've already waited 10 minutes, the chance of waiting 5 more is the same as the chance of waiting 5 from the start.

$$ P(X > s + t \mid X > s) = P(X > t) $$

Good for random arrivals; bad for things that wear out (machines get *more* likely to fail with age — use a Weibull distribution instead).

> **Gap note:** StatQuest's own video on the exponential distribution itself is only a short song. Use Khan Academy Statistics (already in the plan) for the distribution; this video covers its MLE.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Rate estimation** | Event modeling | Requests per second, churn rates, failure rates |
| **Waiting times** | Survival analysis | Time-to-churn, time-to-failure models |
| **Poisson ↔ exponential** | Count models | Counts per interval are Poisson when waits are exponential |
| **Same MLE recipe** | Generality | Any parametric model: write $\ell$, differentiate, solve or optimize |

---

### 7. Check Your Understanding

**Q1: Server requests arrive with average gap 0.2 seconds. Find $\hat{\lambda}$ and interpret.**
<details>
<summary><b>Reveal Answer</b></summary>

$\hat{\lambda} = \frac{1}{0.2} = 5$ requests per second.
</details>

**Q2: Why is the exponential a poor model for the lifetime of car tires?**
<details>
<summary><b>Reveal Answer</b></summary>

It's memoryless — it assumes a tire with 50,000 km on it is as likely to survive the next 1,000 km as a brand-new tire. Tires **wear out**, so failure becomes more likely with age. A distribution with an increasing hazard rate (e.g. Weibull) fits better.
</details>

---

### 📺 Source

* **Video:** [Maximum Likelihood for the Exponential Distribution](https://youtu.be/p3T-_LMrvBc)

---

[⏮️ **Previous: 22 — MLE — Binomial Distribution**](22-mle-binomial-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [🏠 **Repository Home**](../README.md)
