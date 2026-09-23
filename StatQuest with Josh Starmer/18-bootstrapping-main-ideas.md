[⏮️ **Previous: 17 — Confidence Intervals**](17-confidence-intervals.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 19 — Probability vs Likelihood** ⏭️](19-probability-vs-likelihood.md)

---

# 18: Bootstrapping, Part 1 — Main Ideas

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> You'd love to repeat your experiment 10,000 times to see how much your result varies — but you only have one dataset. The bootstrap fakes the repetition: **treat your sample as a stand-in for the population, and resample from it with replacement**, computing your statistic each time. The spread of those resampled statistics approximates the real sampling variability. It works for almost any statistic, needs no formulas, and takes about ten lines of code.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Problem It Solves

You gave a drug to 8 people and measured improvement. Mean improvement = 0.5. **How sure are you?** Would another group of 8 give 0.5 again, or −2, or 3?

The ideal answer — rerun the trial thousands of times — is impossible. The bootstrap is the next best thing.

---

### 2. The Procedure

```text
   Original sample (n = 8):
      [-3.5, -1.2, 0.3, 0.8, 1.1, 1.5, 2.0, 3.0]     mean = 0.5

   STEP 1: Draw 8 values WITH replacement (same size as the original).
      [ 1.5, -3.5, 1.5, 0.8, 3.0, 3.0, 0.3, -1.2]    mean = 0.675
               ^ repeats allowed   ^ some values missing

   STEP 2: Compute the statistic (here, the mean) on that resample.

   STEP 3: Repeat thousands of times.

   STEP 4: Look at the distribution of the resampled means:

                     _---_
                   /       \
                 /           \
             __/               \__
          -1.5        0.5        2.5

      Its SD  ~= standard error of the mean
      Its middle 95% ~= a 95% confidence interval
```

---

### 3. Why With Replacement?

Resampling **without** replacement at the same size just shuffles the original data — every resample has the identical mean. **With** replacement, each resample leaves some points out and duplicates others, creating realistic variation — as if you'd drawn a fresh sample from a population that looks like your data.

---

### 4. In Code (From Scratch)

```python
import numpy as np

def bootstrap(data, stat=np.mean, n_boot=10_000, seed=0):
    rng = np.random.default_rng(seed)
    n = len(data)
    stats = np.empty(n_boot)
    for b in range(n_boot):
        resample = rng.choice(data, size=n, replace=True)
        stats[b] = stat(resample)
    return stats

data = np.array([-3.5, -1.2, 0.3, 0.8, 1.1, 1.5, 2.0, 3.0])
boot = bootstrap(data)
se = boot.std(ddof=1)
ci = np.percentile(boot, [2.5, 97.5])   # percentile 95% CI
```

Swap `np.mean` for `np.median`, a correlation, or a model metric — nothing else changes. **That generality is the whole point.**

> Your Week 4 task is to build this from scratch and check it against `scipy.stats.bootstrap`.

---

### 5. Does 0 Sit Inside the Interval?

If the 95% bootstrap CI for mean improvement is, say, [−1.3, 2.1], it **includes 0** → you can't rule out "the drug does nothing." If it were [0.4, 2.1], you could. (Turning this into a p-value is Bootstrapping Part 2, in Week 5.)

---

### 6. Limitations

| Limitation | Why |
| :--- | :--- |
| **Tiny samples** | Your sample may not resemble the population, so resampling from it misleads |
| **Assumes independent data** | Time series and grouped data need block / cluster bootstrap |
| **Extremes (max, min)** | The bootstrap does poorly for statistics driven by the most extreme values |
| **Biased sample stays biased** | Resampling can't create information that wasn't collected |

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Bootstrap CIs** | Uncertainty on any metric | 95% CI for test AUC by resampling test examples |
| **Resampling with replacement** | Bagging / random forests | Each tree is trained on a bootstrap sample (Week 14 from-scratch) |
| **Out-of-bag samples** | Free validation | ~37% of points are left out of each bootstrap sample — used to evaluate the tree |
| **No formula needed** | Complex pipelines | Uncertainty for custom business metrics |
| **Model comparison** | Paired bootstrap | Resample test items, compute metric difference between two models each time |

---

### 8. Check Your Understanding

**Q1: Why is a bootstrap resample the same size as the original sample?**
<details>
<summary><b>Reveal Answer</b></summary>

Because variability depends on sample size (SE $\propto 1/\sqrt{n}$). To mimic the uncertainty of *your* experiment, each fake experiment must have the same $n$. A smaller resample would exaggerate the variability; a larger one would understate it.
</details>

**Q2: About what fraction of the original data points are missing from a typical bootstrap sample (large $n$)?**
<details>
<summary><b>Reveal Answer</b></summary>

Each point has probability $(1 - \frac{1}{n})^n$ of never being drawn, which tends to $e^{-1} \approx 0.368$. So about **37%** of points are left out of each resample — the "out-of-bag" points used by random forests.
</details>

**Q3: Your bootstrap 95% CI for "new model accuracy − old model accuracy" is [−0.004, 0.019]. What do you conclude?**
<details>
<summary><b>Reveal Answer</b></summary>

The interval includes 0, so you **cannot** claim the new model is better on this evidence — the observed gain is consistent with no real difference. Either collect a larger test set or report the result honestly as inconclusive.
</details>

---

### 📺 Source

* **Video:** [Bootstrapping Main Ideas!!!](https://youtu.be/Xz0x-8-cgaQ)

---

[⏮️ **Previous: 17 — Confidence Intervals**](17-confidence-intervals.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 19 — Probability vs Likelihood** ⏭️](19-probability-vs-likelihood.md)
