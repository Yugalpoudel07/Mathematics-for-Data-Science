[⏮️ **Previous: 12 — Naive Bayes**](12-naive-bayes.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 14 — Estimating Mean, Variance & SD** ⏭️](14-estimating-mean-variance-sd.md)

---

# 13: Population and Estimated Parameters

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> The **population** is everything you care about — every person, every transaction, every possible measurement. You almost never get to measure all of it. So you measure a **sample**, and use it to **estimate** the population's true numbers (its **parameters**, like the true mean). The estimate is a guess, and a different sample would give a slightly different guess. The whole rest of statistics is about how good those guesses are.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Population vs Sample

```text
   POPULATION (everything)                 SAMPLE (what you measured)

   o o o o o o o o o o o o o o o
   o o o o o o o o o o o o o o o    --->     o   o   o
   o o o o o o o o o o o o o o o   random    o o   o
   o o o o o o o o o o o o o o o   sample      o  o
   o o o o o o o o o o o o o o o

   true mean  mu    (unknown)                sample mean  xbar  (computed)
   true SD    sigma (unknown)                sample SD    s     (computed)
```

| | Population | Sample |
| :--- | :--- | :--- |
| **Size** | Usually huge or infinite | $n$ (what you could afford) |
| **Mean** | $\mu$ — a **parameter** | $\bar{x}$ — an **estimate** (statistic) |
| **Standard deviation** | $\sigma$ | $s$ |
| **Known?** | Almost never | Yes — you computed it |

**Convention:** Greek letters for population parameters ($\mu$, $\sigma$), Latin letters or hats for estimates ($\bar{x}$, $s$, $\hat{\mu}$).

---

### 2. Parameters Describe the Population's Distribution

If the population follows a normal distribution, two parameters pin it down: $\mu$ and $\sigma$. **Estimating the parameters = estimating the whole distribution.**

```text
   The population curve is unknown.
   The sample gives us an ESTIMATED curve:

            true (unknown)        estimated from sample
              _---_                     _---_
            /   |   \                 /   |   \
          /     |     \             /     |     \
      __/       |       \__     __/       |       \__
               mu                        xbar

   Close, but not identical — and a new sample would shift it.
```

---

### 3. Why Estimates Wobble

Draw three different samples of 5 from the same population:

| Sample | Values | $\bar{x}$ |
| :-: | :--- | :-: |
| 1 | 21, 25, 19, 30, 24 | 23.8 |
| 2 | 18, 22, 27, 20, 23 | 22.0 |
| 3 | 26, 29, 24, 31, 22 | 26.4 |

Same population, three different estimates. The estimate is itself a **random quantity**. Quantifying that wobble is the job of the standard error (topics 15–16) and confidence intervals (topic 17).

---

### 4. What Makes a Good Sample

* **Random:** every member has a fair chance of being chosen.
* **Representative:** matches the population on things that matter.
* **Large enough:** larger samples → estimates closer to the truth (Law of Large Numbers).

#### How Sampling Goes Wrong

| Bias | Example |
| :--- | :--- |
| **Selection bias** | Surveying only people who answer phone calls during work hours |
| **Survivorship bias** | Studying only companies that still exist |
| **Non-response bias** | Only unhappy customers fill in the feedback form |
| **Convenience sampling** | Surveying your friends about a national question |

> **More data does not fix a biased sample.** A million biased responses give a precise estimate of the wrong number.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Training set = sample** | Generalization | A model learns from a sample; it must work on the population |
| **Estimates wobble** | Seed and split variance | Test accuracy changes with the split — report mean ± std |
| **Sampling bias** | Distribution shift | A model trained on one hospital's data fails at another |
| **Parameters** | Model fitting | Training *is* estimating parameters from a sample (MLE, topic 20) |
| **Bigger isn't unbiased** | Data quality | Scraping more biased data doesn't fix the bias |

---

### 6. Check Your Understanding

**Q1: A company measures satisfaction from the 300 customers who completed an optional survey. Which is the population, which is the sample, and what's the main risk?**
<details>
<summary><b>Reveal Answer</b></summary>

* **Population:** all of the company's customers.
* **Sample:** the 300 who answered.
* **Risk:** non-response bias — people who choose to answer (very happy or very unhappy) may not represent the rest. The estimate can be precise and still wrong.
</details>

**Q2: Why is $\bar{x}$ called a "random variable" even though you computed it exactly?**
<details>
<summary><b>Reveal Answer</b></summary>

Because it depends on **which** sample you happened to draw. Repeat the sampling and you'd get a different $\bar{x}$. Across all possible samples, $\bar{x}$ has its own distribution (approximately normal by the CLT), with spread given by the standard error.
</details>

---

### 📺 Source

* **Video:** [Population and Estimated Parameters](https://youtu.be/vikkiwjQqfU)

---

[⏮️ **Previous: 12 — Naive Bayes**](12-naive-bayes.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 14 — Estimating Mean, Variance & SD** ⏭️](14-estimating-mean-variance-sd.md)
