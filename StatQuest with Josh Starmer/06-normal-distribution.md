[⏮️ **Previous: 05 — The Binomial Distribution**](05-binomial-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 07 — Expected Values (Discrete)** ⏭️](07-expected-values-discrete.md)

---

# 06: The Normal Distribution

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> The normal (Gaussian) distribution is the familiar **bell curve**: symmetric, peaked at the mean, with tails that fade quickly. It is described completely by just two numbers — the **mean** (where the center is) and the **standard deviation** (how wide it is). It shows up everywhere because of the Central Limit Theorem: whenever a quantity is the sum of many small, independent effects, it ends up approximately normal.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Shape

```text
   The normal distribution N(mu, sigma^2):

    density
      ^
      |               _---_
      |             /   |   \
      |           /     |     \
      |         /       |       \
      |       /         |         \
      |  __--           |           --__
      +--+-----+-----+--+--+-----+-----+--> x
        -3s   -2s   -1s mu +1s   +2s   +3s

   Symmetric around the mean mu.
   Width controlled by the standard deviation sigma.
```

| Parameter | Controls | Effect of increasing it |
| :--- | :--- | :--- |
| **Mean** $\mu$ | Location of the peak | Slides the curve right |
| **Standard deviation** $\sigma$ | Spread | Curve gets wider **and** shorter (area stays 1) |

---

### 2. The Formula

$$ \boxed{\; f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \;} $$

Read it piece by piece:

* $(x - \mu)^2$ — squared distance from the center.
* Divided by $2\sigma^2$ — measured in units of the spread.
* $\exp(-\ldots)$ — decays fast as you move away from the center.
* $\frac{1}{\sigma\sqrt{2\pi}}$ — a scaling constant so the total area is exactly 1.

> **Why the curve gets shorter when wider:** area must stay 1. Double $\sigma$ and the curve spreads over twice the width, so the peak height $\frac{1}{\sigma\sqrt{2\pi}}$ halves.

---

### 3. The 68–95–99.7 Rule

For **any** normal distribution:

```text
                          _---_
                        /   |   \
                      /|    |    |\
                    /  |    |    |  \
                  / |  |    |    |  | \
              __--  |  |    |    |  |  --__
            --+-----+--+----+----+--+-----+--
             -3s   -2s -1s  mu  +1s +2s   +3s
                       |<- 68% ->|
                    |<---- 95% ---->|
              |<-------- 99.7% -------->|
```

| Range | Fraction of values |
| :--- | :-: |
| $\mu \pm 1\sigma$ | ≈ 68% |
| $\mu \pm 2\sigma$ | ≈ 95% |
| $\mu \pm 3\sigma$ | ≈ 99.7% |

**Example:** adult heights with $\mu = 170$ cm, $\sigma = 8$ cm → about 95% of people are between 154 and 186 cm.

---

### 4. Z-Scores: One Scale for Every Normal

Convert any value to "how many standard deviations from the mean":

$$ z = \frac{x - \mu}{\sigma} $$

A z-score lets you compare values from completely different distributions. A height of 186 cm has $z = \frac{186-170}{8} = 2$: two standard deviations above average, about the top 2.5%.

The **standard normal** is $N(0, 1)$ — the normal with $\mu = 0$ and $\sigma = 1$. Every normal is a stretched and shifted copy of it.

---

### 5. Why It's Everywhere (and When It Isn't)

**Why:** the Central Limit Theorem (topic 11) — sums and averages of many independent effects become normal, whatever the original distribution.

**When NOT to assume it:**

| Data | Why it's not normal |
| :--- | :--- |
| Incomes, house prices | Heavily right-skewed (long upper tail) |
| Counts (clicks per day) | Discrete and can't go negative |
| Waiting times | Can't be negative; often exponential |
| Financial returns | "Fat tails" — extreme events far more common than normal predicts |

> **Always plot your data before assuming normality.** A normal model on fat-tailed data will badly underestimate how often extreme events happen.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Normal errors** | Where MSE loss comes from | Maximizing a normal likelihood ⇔ minimizing squared error (topic 21) |
| **Z-scores** | Feature standardization | `StandardScaler` rescales features to mean 0, std 1 |
| **Weight initialization** | Stable training | He/Xavier initialization draw weights from a scaled normal |
| **Gaussian noise** | Diffusion models, data augmentation | Diffusion models add and learn to remove Gaussian noise |
| **68–95–99.7** | Quick anomaly rules | Flag values more than 3σ from the mean |
| **Priors** | Regularization | A Gaussian prior on weights ⇔ $L_2$ weight decay |

---

### 7. Check Your Understanding

**Q1: Test scores are normal with $\mu = 70$, $\sigma = 10$. Roughly what fraction of students score above 90?**
<details>
<summary><b>Reveal Answer</b></summary>

$z = \frac{90 - 70}{10} = 2$. By the 68–95–99.7 rule, 95% lie within ±2σ, so 5% lie outside, split evenly between the tails: **about 2.5%** score above 90. (The exact value is 2.28%.)
</details>

**Q2: Distribution A is $N(0, 1)$ and B is $N(0, 4)$ (variance 4). Which has the taller peak, and by how much?**
<details>
<summary><b>Reveal Answer</b></summary>

B has $\sigma = 2$. Peak height is $\frac{1}{\sigma\sqrt{2\pi}}$, so A's peak is $\frac{1}{\sqrt{2\pi}} \approx 0.399$ and B's is $\frac{1}{2\sqrt{2\pi}} \approx 0.199$. **A is twice as tall.** B is twice as wide, so both enclose area 1.
</details>

**Q3: You model daily stock returns as normal and conclude a 5σ drop "should happen once in several million days." Why is this dangerous?**
<details>
<summary><b>Reveal Answer</b></summary>

Financial returns have **fat tails** — extreme moves occur far more often than a normal distribution predicts. The normal model's tail probability is wildly optimistic, so risk is badly underestimated. The model assumption, not the arithmetic, is wrong. Check the tails of your data (e.g. a Q-Q plot) before trusting normal-based probabilities of extreme events.
</details>

---

### 📺 Source

* **Video:** [The Normal Distribution](https://youtu.be/rzFX5NWojp0)

---

[⏮️ **Previous: 05 — The Binomial Distribution**](05-binomial-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 07 — Expected Values (Discrete)** ⏭️](07-expected-values-discrete.md)
