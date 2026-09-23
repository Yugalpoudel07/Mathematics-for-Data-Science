[⏮️ **Previous: 20 — Maximum Likelihood**](20-maximum-likelihood.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 22 — MLE — Binomial Distribution** ⏭️](22-mle-binomial-distribution.md)

---

# 21: Maximum Likelihood for the Normal Distribution (Worked Example)

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Apply the maximum-likelihood recipe to the normal distribution and the calculus spits out two familiar answers: the best mean is **the sample average**, and the best variance is **the average squared distance from that average**. So "use the average" isn't just a habit — it's the choice that makes your data most likely under a normal model. And the same algebra is why **least squares** is the natural loss for regression.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Set Up the Likelihood

Data $x_1, \dots, x_n$ assumed independent from $N(\mu, \sigma^2)$:

$$ f(x_i \mid \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right) $$

$$ L(\mu, \sigma) = \prod_{i=1}^n \frac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right) $$

### 2. Take the Log

The log of a product is a sum; the log undoes the exp:

$$ \ell(\mu, \sigma) = \sum_{i=1}^n \left[ -\log\sigma - \tfrac{1}{2}\log(2\pi) - \frac{(x_i - \mu)^2}{2\sigma^2} \right] $$

$$ \boxed{\; \ell(\mu, \sigma) = -n\log\sigma - \frac{n}{2}\log(2\pi) - \frac{1}{2\sigma^2}\sum_{i=1}^n (x_i - \mu)^2 \;} $$

---

### 3. Solve for $\mu$

Differentiate with respect to $\mu$. Only the last term depends on $\mu$:

$$ \frac{\partial \ell}{\partial \mu} = -\frac{1}{2\sigma^2}\sum_{i=1}^n 2(x_i - \mu)(-1) = \frac{1}{\sigma^2}\sum_{i=1}^n (x_i - \mu) $$

Set to zero:
$$ \sum_{i=1}^n (x_i - \mu) = 0 \;\Longrightarrow\; \sum x_i - n\mu = 0 \;\Longrightarrow\; \boxed{\hat{\mu} = \frac{1}{n}\sum_{i=1}^n x_i = \bar{x}} $$

> **The MLE of the mean is the sample average.**

---

### 4. Solve for $\sigma$

Differentiate with respect to $\sigma$:

$$ \frac{\partial \ell}{\partial \sigma} = -\frac{n}{\sigma} + \frac{1}{\sigma^3}\sum_{i=1}^n (x_i - \mu)^2 $$

Set to zero and multiply through by $\sigma^3$:
$$ -n\sigma^2 + \sum (x_i - \mu)^2 = 0 \;\Longrightarrow\; \boxed{\hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2} $$

> **Divides by $n$, not $n - 1$** — so the MLE variance is slightly biased low (topic 14). MLE maximizes fit to the observed data; it doesn't aim for unbiasedness.

---

### 5. The Connection to Least Squares

Look again at the log-likelihood. For a fixed $\sigma$, maximizing $\ell$ means **minimizing**
$$ \sum_{i=1}^n (x_i - \mu)^2 $$

Now replace the constant $\mu$ with a regression prediction $\hat{y}_i = w x_i + b$:

$$ \text{maximize likelihood} \iff \text{minimize } \sum_i (y_i - \hat{y}_i)^2 $$

```text
   Why least squares is not arbitrary:

   Assume:  y = (w x + b) + noise,   noise ~ Normal(0, sigma^2)
                     |
                     v
   Maximum likelihood for w, b
                     |
                     v
   Minimize the SUM OF SQUARED ERRORS  =  MSE loss
```

This is exactly the derivation you'll do on paper for **linear regression from scratch in Week 9**.

---

### 6. Numeric Check

Data: $[30, 32, 34, 33, 31]$.

* $\hat{\mu} = \frac{160}{5} = 32$
* Squared deviations: $4, 0, 4, 1, 1$ → sum $= 10$
* $\hat{\sigma}^2_{\text{MLE}} = \frac{10}{5} = 2$ (vs unbiased $s^2 = \frac{10}{4} = 2.5$)

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **MLE → sample mean** | Justifies averaging | Mean predictor is the MLE baseline for regression |
| **Gaussian NLL → MSE** | Regression loss | `nn.MSELoss` assumes Gaussian noise with fixed variance |
| **Learning $\sigma$ too** | Uncertainty-aware regression | Predict both $\mu(x)$ and $\sigma(x)$ with Gaussian NLL (heteroscedastic models) |
| **Derivative = 0** | Closed-form solutions | Normal equations for linear regression come from the same step |
| **MLE bias** | Small-sample caution | Divide-by-$n$ variance underestimates spread |

---

### 8. Check Your Understanding

**Q1: Compute the MLE of $\mu$ and $\sigma^2$ for $[4, 6, 8, 10]$.**
<details>
<summary><b>Reveal Answer</b></summary>

$\hat{\mu} = 7$. Squared deviations: $9, 1, 1, 9$ → sum 20. $\hat{\sigma}^2 = \frac{20}{4} = 5$ (unbiased version: $\frac{20}{3} \approx 6.67$).
</details>

**Q2: In the $\mu$ derivation, why did $\sigma$ disappear from the final answer?**
<details>
<summary><b>Reveal Answer</b></summary>

After setting $\frac{1}{\sigma^2}\sum(x_i - \mu) = 0$, the positive factor $\frac{1}{\sigma^2}$ can be divided out — it doesn't change where the expression equals zero. So the best $\mu$ is the sample mean **regardless of $\sigma$**. That's also why MSE regression doesn't need to know the noise level to find the best line.
</details>

---

### 📺 Source

* **Video:** [Maximum Likelihood for the Normal Distribution, step-by-step!](https://youtu.be/Dn6b9fCIUpM)

---

[⏮️ **Previous: 20 — Maximum Likelihood**](20-maximum-likelihood.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 22 — MLE — Binomial Distribution** ⏭️](22-mle-binomial-distribution.md)
