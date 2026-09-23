[⏮️ **Previous: 01 — Probability Distributions**](01-probability-distributions.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 03 — Conditional Probability** ⏭️](03-conditional-probability.md)

---

# 02: What Does It Mean to "Sample from a Distribution"?

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> A distribution is a recipe; **sampling** is cooking with it. To sample from a distribution means to generate random values in a way that respects its shape — values from the tall part of the curve come up often, values from the tails come up rarely. Every simulation, every bootstrap, every random train/test split, and every generative model is built on this one operation.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Idea in Plain Words

Imagine a distribution of heights where most people are around 170 cm. "Drawing a sample" is like picking a random person from that population and measuring them.

```text
   Sampling respects the shape:

    density
      ^          _---_
      |        /  |||  \          <- LOTS of samples land here
      |      /    |||    \
      |    / .    |||    . \      <- a few land out here
      +--./--.----|||----.--\.--> x
          ^                   ^
       rare                 rare

   Draw 10 values: 168, 171, 174, 166, 170, 169, 181, 172, 165, 170
   Most cluster near the peak; one (181) came from the tail.
```

> **Key point:** each individual draw is **random** and unpredictable. But **many draws together** reproduce the shape of the distribution.

---

### 2. Samples Rebuild the Distribution

```text
   Histogram of samples as the number of draws grows:

   5 draws            50 draws             5000 draws
      #                 ###                  _###_
   #  # #             #######              #########
  ## ## #  #         #########           #############

   looks nothing      starting to look     indistinguishable
   like the curve     like it              from the curve
```

This is the **Law of Large Numbers** in action: the more you sample, the closer your sample's histogram (and its mean) gets to the true distribution.

---

### 3. How a Computer Actually Samples

A computer can natively produce **uniform** random numbers between 0 and 1. Every other distribution is built from those.

#### Inverse Transform Sampling

1. Draw $u \sim \text{Uniform}(0,1)$.
2. Find the value $x$ where the cumulative distribution function (CDF) equals $u$: $x = F^{-1}(u)$.

```text
   CDF F(x): the running total of probability

      1 +                 ________
        |              _/
    u --+- - - - - - -*             <- pick u at random on the y-axis
        |          _/ |
        |       _/    |
      0 +____--/------+--------> x
                      x = F^-1(u)   <- read off the matching x

   Steep parts of the CDF (= the peak of the PDF) catch MORE
   random u values, so x lands there more often.
```

In practice you call a library:

```python
import numpy as np
rng = np.random.default_rng(seed=42)       # fix the seed -> reproducible
heights = rng.normal(loc=170, scale=8, size=1000)
coin    = rng.binomial(n=1, p=0.5, size=1000)
```

> **Always set a seed.** Without one, your results change every run and nobody (including you next week) can reproduce them.

---

### 4. Sampling With vs Without Replacement

| | **With replacement** | **Without replacement** |
| :--- | :--- | :--- |
| **What happens** | Put each item back after drawing it | Each item can be drawn only once |
| **Can repeats occur?** | Yes | No |
| **Draws independent?** | Yes | No — each draw changes what is left |
| **Used for** | Bootstrapping (topic 18) | Train/test splits, surveys |

---

### 5. Why Sampling Matters

* **Simulation:** can't solve it with a formula? Sample it 10,000 times and look at the results (Monte Carlo).
* **Understanding variability:** different samples give different means. That wobble is what standard error measures (topics 15–16).
* **Generating data:** create realistic synthetic data to test a method where you know the true answer.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Sampling** | Mini-batch SGD | Each batch is a sample from the training set |
| **Seeds & reproducibility** | Honest experiments | Report mean ± std over ≥5 seeds, not one lucky run |
| **Inverse transform** | Sampling from learned distributions | Normalizing flows are a learned, invertible version of $F^{-1}$ |
| **With replacement** | Bagging and random forests | Each tree trains on a bootstrap sample |
| **Monte Carlo** | Estimating intractable quantities | Dropout at test time (MC dropout), RL returns, Bayesian posteriors |
| **Generative sampling** | Text and image generation | LLMs sample the next token from a predicted distribution |

---

### 7. Check Your Understanding

**Q1: You sample 5 values from a normal distribution with mean 100 and get a sample mean of 108. Is the distribution wrong?**
<details>
<summary><b>Reveal Answer</b></summary>

Not necessarily. With only 5 draws, the sample mean wobbles a lot around the true mean. A sample mean of 108 is quite possible by chance if the spread is large. The Law of Large Numbers says the sample mean approaches 100 only as the number of draws grows. How unusual 108 is depends on the standard error $\sigma/\sqrt{5}$ — which you'll meet in topic 16.
</details>

**Q2: Why must bootstrapping sample *with* replacement?**
<details>
<summary><b>Reveal Answer</b></summary>

If you draw $n$ items **without** replacement from a dataset of size $n$, you just get the same dataset back in a different order — every resample would have the identical mean. Sampling **with** replacement lets some points appear twice and others not at all, so each resample differs. That variation between resamples is exactly what mimics collecting a fresh dataset.
</details>

---

### 📺 Source

* **Video:** [What does it mean to "sample from a distribution"?](https://youtu.be/XLCWeSVzHUU)

---

[⏮️ **Previous: 01 — Probability Distributions**](01-probability-distributions.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 03 — Conditional Probability** ⏭️](03-conditional-probability.md)
