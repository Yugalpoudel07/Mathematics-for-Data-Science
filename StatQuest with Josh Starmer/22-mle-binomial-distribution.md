[⏮️ **Previous: 21 — MLE — Normal Distribution**](21-mle-normal-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 23 — MLE — Exponential Distribution** ⏭️](23-mle-exponential-distribution.md)

---

# 22: Maximum Likelihood for the Binomial Distribution *(Optional)*

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> You flipped a coin (or showed an ad, or ran a test) $n$ times and got $k$ successes. What's the best estimate of the success probability $p$? Maximum likelihood gives the answer your gut already knew — **$\hat{p} = k/n$**, the observed fraction — but the derivation matters: the same log-likelihood, written per example, **is binary cross-entropy**, the loss behind logistic regression.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Likelihood

$k$ successes in $n$ trials (topic 05):

$$ L(p \mid n, k) = \binom{n}{k} p^k (1-p)^{n-k} $$

Now $n$ and $k$ are **fixed** (observed); we vary $p$.

```text
   Likelihood of p after seeing 7 successes in 10 trials:

   L(p)
     ^
     |                    _*_
     |                 _/     \_
     |              _/           \
     |           _/                \
     |        _/                     \
     +-----+-----+-----+-----+-----+--\--> p
     0    0.2   0.4   0.6  0.7  0.8   1.0
                            ^
                         p_hat = 0.7
```

---

### 2. Take the Log

$$ \ell(p) = \log\binom{n}{k} + k\log p + (n - k)\log(1 - p) $$

The first term doesn't depend on $p$, so it won't affect the maximum.

### 3. Differentiate and Solve

$$ \frac{d\ell}{dp} = \frac{k}{p} - \frac{n - k}{1 - p} $$

Set to zero:
$$ \frac{k}{p} = \frac{n-k}{1-p} \;\Longrightarrow\; k(1 - p) = (n - k)p \;\Longrightarrow\; k - kp = np - kp $$

$$ \boxed{\; \hat{p} = \frac{k}{n} \;} $$

For 7 heads in 10 flips: $\hat{p} = 0.7$.

---

### 4. From Here to Binary Cross-Entropy

Write the same thing **one trial at a time**, with $y_i \in \{0, 1\}$:

$$ \ell(p) = \sum_{i=1}^n \big[\, y_i \log p + (1 - y_i)\log(1 - p) \,\big] $$

Let $p$ depend on the input features — $p_i = \sigma(w^\top x_i + b)$ — and negate (minimize instead of maximize):

$$ \text{BCE} = -\frac{1}{n}\sum_{i=1}^n \big[\, y_i \log p_i + (1-y_i)\log(1-p_i) \,\big] $$

> **Binary cross-entropy is exactly the negative Bernoulli log-likelihood.** Logistic regression (Week 11 from scratch) is maximum likelihood with $p$ modeled as a function of the features.

---

### 5. A Warning: Small Samples

3 flips, 3 heads → $\hat{p} = 1$. MLE claims tails is **impossible**. With little data, MLE can be extreme and overconfident. Fixes: add pseudocounts (like Laplace smoothing in Naive Bayes, topic 12), or a prior (Bayesian / MAP estimation).

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **$\hat{p} = k/n$** | Estimating rates | Click-through rate, conversion rate, accuracy |
| **Bernoulli NLL = BCE** | Binary classification loss | `nn.BCELoss` / logistic regression |
| **Extreme MLE with little data** | Overconfidence | Smoothing and priors in rare-category estimates |
| **Log-likelihood derivative** | Gradient of BCE | With a sigmoid, $\frac{\partial \text{BCE}}{\partial z} = p - y$ |

---

### 7. Check Your Understanding

**Q1: 45 of 150 users clicked an ad. Find the MLE of the click probability and its standard error.**
<details>
<summary><b>Reveal Answer</b></summary>

$\hat{p} = \frac{45}{150} = 0.3$. SE $= \sqrt{\frac{0.3 \times 0.7}{150}} = \sqrt{0.0014} \approx 0.037$. So roughly $0.30 \pm 0.07$ at 95%.
</details>

**Q2: Show that the BCE for a single example with $y = 1$ is $-\log p$, and explain what happens as $p \to 0$.**
<details>
<summary><b>Reveal Answer</b></summary>

With $y = 1$: $-[1 \cdot \log p + 0 \cdot \log(1-p)] = -\log p$. As $p \to 0$ (the model is confidently wrong), $-\log p \to \infty$. BCE punishes confident mistakes extremely harshly — which is the intended behavior.
</details>

---

### 📺 Source

* **Video:** [Maximum Likelihood for the Binomial Distribution](https://youtu.be/4KKV9yZCoM4)

---

[⏮️ **Previous: 21 — MLE — Normal Distribution**](21-mle-normal-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 23 — MLE — Exponential Distribution** ⏭️](23-mle-exponential-distribution.md)
