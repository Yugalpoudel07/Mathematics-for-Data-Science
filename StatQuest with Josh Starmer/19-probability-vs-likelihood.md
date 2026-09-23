[⏮️ **Previous: 18 — Bootstrapping — Main Ideas**](18-bootstrapping-main-ideas.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 20 — Maximum Likelihood** ⏭️](20-maximum-likelihood.md)

---

# 19: Probability vs Likelihood

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> In everyday speech they're synonyms. In statistics they are **opposite questions about the same curve**. **Probability:** the distribution is fixed, and you ask how likely various *data* are — the **area** under the curve over a range. **Likelihood:** the data are fixed (you've already observed them), and you ask how well various *distributions* fit — the **height** of the curve at your observed point, as you slide or reshape the curve. Likelihood is the engine of maximum likelihood, which is how most ML models are trained.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Probability: Fix the Distribution, Vary the Data

Mouse weights are $N(\mu = 32, \sigma = 2.5)$. What's the probability a mouse weighs between 32 and 34 g?

```text
   Distribution FIXED.  Ask about a RANGE of data.

    density
      ^          _---_
      |        /  |###\
      |      /    |### \          P(32 <= weight <= 34)
      |    /      |###   \        = shaded AREA  ~= 0.29
      |  /        |###     \
      +-/---------|###------\---> weight
                 32  34
```

$$ P(32 \le X \le 34 \mid \mu = 32, \sigma = 2.5) = \text{area} $$

---

### 2. Likelihood: Fix the Data, Vary the Distribution

You weighed **one** mouse: 34 g. Which distribution explains it well?

```text
   Data FIXED at 34.  Slide the distribution around.

   mu = 30:           _---_                    height at 34: LOW
                    /       \   |
                  /           \ |
                                * 34

   mu = 34:                 _---_              height at 34: HIGHEST
                          /   *   \
                        /     |     \
                              34

   L(mu, sigma | data) = the HEIGHT of the curve at the observed point
```

$$ L(\mu = 32, \sigma = 2.5 \mid x = 34) = f(34;\,32,\,2.5) \approx 0.12 $$

---

### 3. Side by Side

| | **Probability** | **Likelihood** |
| :--- | :--- | :--- |
| **What's fixed** | The distribution (parameters) | The observed data |
| **What varies** | The data (a range of outcomes) | The parameters |
| **Read off the curve as** | **Area** over a range | **Height** at the observed point(s) |
| **Notation** | $P(\text{data} \mid \theta)$ | $L(\theta \mid \text{data})$ |
| **Sums/integrates to 1?** | Yes, over all data | **No** — over all parameters, it need not |
| **Question** | "Given this model, how likely is this data?" | "Given this data, how plausible is this model?" |

> Note: $L(\theta \mid \text{data})$ and $f(\text{data} \mid \theta)$ are the **same formula** — just viewed as a function of $\theta$ instead of the data. Likelihood is **not** the probability that $\theta$ is correct (that would need Bayes and a prior).

---

### 4. Many Data Points

With several independent observations, multiply their heights:

$$ L(\theta \mid x_1, \ldots, x_n) = \prod_{i=1}^n f(x_i \mid \theta) $$

In practice, take logs (products → sums, and no underflow):

$$ \log L(\theta) = \sum_{i=1}^n \log f(x_i \mid \theta) $$

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Likelihood of parameters** | Training objective | Fitting a model = finding parameters that make the training data most likely |
| **Log-likelihood** | Loss functions | Negative log-likelihood (NLL) is the loss for classification and density models |
| **Product over data** | Independence assumption | i.i.d. data → log-likelihood is a sum over examples → batchable |
| **Likelihood ≠ probability of model** | Avoiding misinterpretation | A high likelihood doesn't mean the model is "probably true" |
| **Model comparison** | AIC, BIC, likelihood ratio | Compare fitted likelihoods, penalized for complexity |

---

### 6. Check Your Understanding

**Q1: For each, say whether it's a probability or a likelihood question: (a) "If a coin is fair, what's the chance of 7+ heads in 10 flips?" (b) "I got 7 heads in 10 flips — is $p = 0.5$ or $p = 0.7$ a better fit?"**
<details>
<summary><b>Reveal Answer</b></summary>

(a) **Probability** — the model ($p = 0.5$) is fixed; we ask about data.
(b) **Likelihood** — the data (7/10) are fixed; we compare parameters. Here $L(0.7) = \binom{10}{7}0.7^7 0.3^3 \approx 0.267$ vs $L(0.5) \approx 0.117$, so $p = 0.7$ fits better.
</details>

**Q2: Why can a likelihood value be larger than 1?**
<details>
<summary><b>Reveal Answer</b></summary>

For continuous data, likelihood is a **density height**, not a probability — and densities can exceed 1 for narrow distributions. Likelihoods are only meaningful for **comparing** parameter values on the same data, not as absolute probabilities.
</details>

---

### 📺 Source

* **Video:** [Probability is not Likelihood. Find out why!!!](https://youtu.be/pYxNSUDSFH4)

---

[⏮️ **Previous: 18 — Bootstrapping — Main Ideas**](18-bootstrapping-main-ideas.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 20 — Maximum Likelihood** ⏭️](20-maximum-likelihood.md)
