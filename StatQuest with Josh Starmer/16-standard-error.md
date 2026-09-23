[⏮️ **Previous: 15 — SD vs Standard Error**](15-sd-vs-standard-error.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 17 — Confidence Intervals** ⏭️](17-confidence-intervals.md)

---

# 16: The Standard Error

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Every estimate has a "wobble" — if you redid the experiment, you'd get a slightly different number. The **standard error** measures the size of that wobble. For a mean there's a neat formula, $s/\sqrt{n}$. For almost anything else (a median, a correlation, a model's AUC), there isn't, and you estimate the wobble by **resampling** your data many times (bootstrapping) and seeing how much the statistic moves.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Defining It by Brute Force

The most honest definition:

```text
   1. Collect a sample, compute the statistic (e.g. the mean).
   2. Collect ANOTHER sample, compute it again.
   3. Repeat many times.

      sample 1  ->  mean = 23.8
      sample 2  ->  mean = 22.0
      sample 3  ->  mean = 26.4
      ...
      sample 1000 -> mean = 24.1

   4. The standard deviation of all those means = the STANDARD ERROR.
```

In practice you can't repeat the experiment 1000 times — which is why we need shortcuts.

---

### 2. Shortcut 1: The Formula for the Mean

$$ \boxed{\; \text{SE}(\bar{x}) = \frac{s}{\sqrt{n}} \;} $$

**Where it comes from:** the variance of a sum of $n$ independent values is $n\sigma^2$, so the variance of their average is $\frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$. Take the square root.

**Other common formulas:**

| Statistic | Standard error |
| :--- | :--- |
| Mean | $\dfrac{s}{\sqrt{n}}$ |
| Proportion $\hat{p}$ | $\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$ |
| Difference of two means | $\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ |

---

### 3. Shortcut 2: Bootstrapping (When There's No Formula)

```text
   Your one sample:  [3, 7, 2, 9, 5, 6, 1, 8]

   Resample WITH replacement, same size, many times:

      [7, 7, 2, 9, 5, 1, 1, 8]  ->  median = 6
      [3, 2, 2, 9, 6, 6, 8, 5]  ->  median = 5.5
      [9, 5, 3, 1, 6, 8, 8, 7]  ->  median = 6.5
      ... (1000s of times)

   SE of the median  ~=  standard deviation of those medians
```

Covered fully in topic 18. It works for medians, correlations, model metrics — anything you can compute.

---

### 4. What Makes the SE Small

$$ \text{SE} = \frac{s}{\sqrt{n}} $$

* **Less variable data** (smaller $s$) → smaller SE.
* **More data** (bigger $n$) → smaller SE, but with diminishing returns: 4× data for 2× precision.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **SE of a proportion** | Uncertainty in accuracy | 90% accuracy on 200 test items: SE $= \sqrt{0.9 \cdot 0.1/200} \approx 0.021$ |
| **Bootstrap SE** | Metrics without formulas | SE of AUC, F1, or median error by resampling the test set |
| **SE of a difference** | Is model A better than B? | Compare the gap to its SE |
| **$\sqrt{n}$ law** | Planning test-set size | To halve the SE of a metric, quadruple the test set |

---

### 6. Check Your Understanding

**Q1: A model is 85% accurate on 400 test examples. Estimate the SE and a rough 95% range.**
<details>
<summary><b>Reveal Answer</b></summary>

SE $= \sqrt{\frac{0.85 \times 0.15}{400}} = \sqrt{0.000319} \approx 0.0179$.
Rough 95% range: $0.85 \pm 2(0.018) \approx [0.81, 0.89]$. So "85%" really means "somewhere around 81–89%."
</details>

**Q2: Why can't you use $s/\sqrt{n}$ for the standard error of a median?**
<details>
<summary><b>Reveal Answer</b></summary>

That formula is derived specifically from how **averages** combine variances. The median isn't an average of the values, so its variability behaves differently (and depends on the shape of the distribution). Use the bootstrap instead.
</details>

---

### 📺 Source

* **Video:** [The Standard Error, Clearly Explained](https://youtu.be/XNgt7F6FqDU)

---

[⏮️ **Previous: 15 — SD vs Standard Error**](15-sd-vs-standard-error.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 17 — Confidence Intervals** ⏭️](17-confidence-intervals.md)
