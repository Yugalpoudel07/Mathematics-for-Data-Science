[⏮️ **Previous: 19 — Probability vs Likelihood**](19-probability-vs-likelihood.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 21 — MLE — Normal Distribution** ⏭️](21-mle-normal-distribution.md)

---

# 20: Maximum Likelihood

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> You've collected data and chosen a type of distribution (say, normal). Which specific version — which mean, which spread — should you use? **Maximum likelihood** answers: pick the parameters that make **the data you actually observed as likely as possible**. Slide the curve around until it sits where your data are densest. This single principle is behind linear regression, logistic regression, and the loss functions of most neural networks.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Idea by Sliding a Curve

```text
   Observed mouse weights:   .  . ... .. .  .

   mu too low:     _---_
                 /       \          most data sit in the right tail
               /           \        -> product of heights is SMALL
           .  . ... .. .  .

   mu just right:        _---_
                       /       \    data sit under the peak
                     /           \  -> product of heights is LARGEST
           .  . ... .. .  .

   mu too high:                  _---_
                               /       \   data in the left tail
           .  . ... .. .  .  /           \  -> SMALL again
```

Plot the likelihood against $\mu$:

```text
   likelihood
       ^
       |            _*_           * = maximum likelihood estimate
       |          /     \
       |        /         \
       |      /             \
       +---------------------------> mu
                    mu_hat
```

The peak is the **maximum likelihood estimate (MLE)**.

---

### 2. The Recipe

1. **Choose a distribution family** with parameters $\theta$ (e.g. normal: $\mu, \sigma$).
2. **Write the likelihood** of all the data (assuming independence):
   $$ L(\theta) = \prod_{i=1}^n f(x_i \mid \theta) $$
3. **Take the log** (easier to differentiate, no underflow):
   $$ \ell(\theta) = \sum_{i=1}^n \log f(x_i \mid \theta) $$
4. **Differentiate and set to zero** (the peak has slope 0 — Essence of Calculus, ch. 10):
   $$ \frac{\partial \ell}{\partial \theta} = 0 $$
5. **Solve** for $\theta$. If there's no closed form, use gradient ascent / an optimizer.

> **Why the log doesn't change the answer:** $\log$ is always increasing, so whatever maximizes $L$ also maximizes $\log L$.

---

### 3. Key Results You'll Derive

| Distribution | MLE | Derived in |
| :--- | :--- | :--- |
| Normal | $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i - \bar{x})^2$ | Topic 21 |
| Binomial | $\hat{p} = \frac{k}{n}$ (fraction of successes) | Topic 22 |
| Exponential | $\hat{\lambda} = \frac{1}{\bar{x}}$ | Topic 23 |

These all match intuition — MLE usually gives the "obvious" estimate, but now with a principled justification that extends to cases where there is no obvious answer.

> **Notice:** the normal MLE for variance divides by $n$, not $n-1$ — so it's slightly biased (topic 14). MLE optimizes fit, not unbiasedness.

---

### 4. MLE vs Least Squares vs Other Losses

The punchline for ML: **choosing a likelihood = choosing a loss function.**

| Assumed noise / output distribution | Negative log-likelihood becomes | Used in |
| :--- | :--- | :--- |
| Normal (fixed $\sigma$) | **Mean squared error** | Linear regression |
| Bernoulli | **Binary cross-entropy** | Logistic regression |
| Categorical | **Cross-entropy** (with softmax) | Multi-class classification |
| Laplace | **Mean absolute error** | Robust regression |
| Poisson | Poisson loss | Count prediction |

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **MLE** | The default way to fit models | Linear regression (W9), logistic regression (W11) from scratch |
| **Negative log-likelihood** | Training loss | Minimizing NLL = maximizing likelihood |
| **No closed form → optimize** | Gradient descent | Logistic regression and neural nets have no closed-form MLE |
| **MLE overfits** | Regularization | Adding a prior gives MAP estimation = MLE + penalty ($L_2$ ⇔ Gaussian prior) |
| **Likelihood = loss choice** | Modeling decisions | Picking MSE silently assumes Gaussian noise |

---

### 6. Check Your Understanding

**Q1: Why maximize the log-likelihood instead of the likelihood itself?**
<details>
<summary><b>Reveal Answer</b></summary>

1. **Same maximizer:** log is monotonically increasing.
2. **Products become sums:** much easier to differentiate.
3. **Numerical stability:** multiplying thousands of small densities underflows to 0; summing logs doesn't.
</details>

**Q2: A friend fits a regression with MSE loss. What assumption about the errors have they implicitly made?**
<details>
<summary><b>Reveal Answer</b></summary>

That the errors are (approximately) **normally distributed with constant variance**. Minimizing MSE is exactly maximum likelihood under Gaussian noise. If the errors have heavy tails or outliers, MSE (and the implied normal model) can be a poor choice; MAE (Laplace) is more robust.
</details>

---

### 📺 Source

* **Video:** [Maximum Likelihood, Clearly Explained!!!](https://youtu.be/XepXtl9YKwc)

---

[⏮️ **Previous: 19 — Probability vs Likelihood**](19-probability-vs-likelihood.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 21 — MLE — Normal Distribution** ⏭️](21-mle-normal-distribution.md)
