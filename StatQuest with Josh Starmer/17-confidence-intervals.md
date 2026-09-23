[⏮️ **Previous: 16 — The Standard Error**](16-standard-error.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 18 — Bootstrapping — Main Ideas** ⏭️](18-bootstrapping-main-ideas.md)

---

# 17: Confidence Intervals

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> A confidence interval turns a single guess into a **range with a guarantee about the method**. A 95% confidence interval is built by a procedure that, if you repeated the whole experiment many times, would **capture the true value in 95% of those repetitions**. It is *not* "a 95% chance the true value is in this particular interval" — the true value is fixed; it's the interval that's random. Getting this exactly right is one of the most-asked interview questions in data science.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Building One (Bootstrap Way)

```text
   1. Take your sample. Compute the mean.
   2. Bootstrap: resample with replacement, compute the mean. Repeat 10,000x.
   3. Sort the 10,000 bootstrap means.
   4. Cut off the lowest 2.5% and highest 2.5%.

      |###|=======================================|###|
      2.5%          middle 95%                     2.5%
          ^                                        ^
       lower                                    upper
       bound                                    bound

   The middle 95% is the 95% confidence interval.
```

This is the **percentile bootstrap** interval — no formulas, and it works for almost any statistic.

---

### 2. Building One (Formula Way, for a Mean)

Using the CLT (topic 11), the sample mean is approximately normal with SD equal to the standard error:

$$ \boxed{\; \bar{x} \pm z^{*} \cdot \frac{s}{\sqrt{n}} \;} $$

| Confidence | $z^{*}$ |
| :-: | :-: |
| 90% | 1.645 |
| 95% | 1.96 |
| 99% | 2.576 |

For small samples, use the $t$-distribution value $t^{*}_{n-1}$ instead of $z^{*}$ (slightly wider).

**Example:** $\bar{x} = 50$, $s = 10$, $n = 100$ → SE $= 1$ → 95% CI $= 50 \pm 1.96 = [48.04, 51.96]$.

---

### 3. What 95% Actually Means

```text
   Repeat the experiment 20 times; build a 95% CI each time:

   true mu ------------------|------------------
   CI  1        [-----------+------]
   CI  2           [--------+---------]
   CI  3     [--------------+---]
   CI  4                 [--+-----------]
   ...                      |
   CI 17   [-----------]    |               <- MISSES the true value
   ...                      |
   CI 20         [----------+------]

   About 19 of the 20 intervals contain mu.  One misses.
   For any single interval, you don't know which kind it is.
```

| ✅ Correct | ❌ Wrong |
| :--- | :--- |
| "If we repeated this procedure many times, 95% of the intervals built would contain the true mean." | "There is a 95% probability the true mean is in [48.04, 51.96]." |
| "The method has 95% coverage." | "95% of the data lie in this interval." |
| | "If we repeated the experiment, 95% of sample means would fall in this interval." |

> **Why the wrong version is wrong:** in the standard (frequentist) framework, the true mean is a fixed number — it's either in the interval or not. The 95% describes the long-run success rate of the **procedure**. (A Bayesian *credible interval* does support the "95% probability" reading, but it's a different object built with a prior.)

---

### 4. What Controls the Width

$$ \text{width} \propto z^{*} \cdot \frac{s}{\sqrt{n}} $$

| Change | Effect on width |
| :--- | :--- |
| More data ($n \uparrow$) | Narrower |
| More variable data ($s \uparrow$) | Wider |
| Higher confidence (99% vs 95%) | Wider |

There's a trade-off: more confidence means a wider, less precise interval.

---

### 5. Using CIs to Compare

* If a 95% CI for a **difference** excludes 0, the difference is statistically significant at about the 5% level.
* Two separate CIs that don't overlap → significant difference. But overlapping CIs **do not** prove no difference — compute the CI of the difference directly.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **CIs on metrics** | Honest model reporting | "AUC 0.87, 95% CI [0.84, 0.90]" instead of "AUC 0.87" |
| **Bootstrap CI** | Metrics without formulas | Resample the test set to get a CI for F1 or AUC (from-scratch in Week 4) |
| **CI of a difference** | Model comparison, A/B tests | Is the new model's improvement distinguishable from zero? |
| **Coverage simulation** | Verifying your understanding | Simulate 1000 experiments; ~950 intervals should contain the truth |
| **Interview staple** | Job hunting | The correct vs wrong interpretation is asked constantly |

---

### 7. Check Your Understanding

**Q1: $\bar{x} = 120$, $s = 15$, $n = 36$. Build a 95% CI.**
<details>
<summary><b>Reveal Answer</b></summary>

SE $= \frac{15}{6} = 2.5$. Margin $= 1.96 \times 2.5 = 4.9$.
95% CI $= [115.1, 124.9]$. (With $n = 36$, using $t^*_{35} \approx 2.03$ gives $[114.9, 125.1]$ — very similar.)
</details>

**Q2: Write the correct interpretation of a 95% CI of [115.1, 124.9], and the most common wrong one.**
<details>
<summary><b>Reveal Answer</b></summary>

* **Correct:** "This interval came from a procedure that captures the true mean in 95% of repeated experiments."
* **Common wrong:** "There's a 95% chance the true mean is between 115.1 and 124.9."

(This is literally Gate 1, question 4.)
</details>

**Q3: A colleague's CI is very narrow — [0.891, 0.893] — from a test set of 50 examples. What should you suspect?**
<details>
<summary><b>Reveal Answer</b></summary>

With $n=50$, an accuracy near 0.89 should have SE $\approx \sqrt{0.89 \cdot 0.11/50} \approx 0.044$, so the 95% CI should be roughly ±0.09 wide, not ±0.001. Likely causes: they reported an SE of something else, resampled the wrong thing (e.g. model predictions without resampling examples), or used training data. The interval is implausibly precise.
</details>

---

### 📺 Source

* **Video:** [Confidence Intervals, Clearly Explained](https://youtu.be/TqOeMYtOc1w)

---

[⏮️ **Previous: 16 — The Standard Error**](16-standard-error.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 18 — Bootstrapping — Main Ideas** ⏭️](18-bootstrapping-main-ideas.md)
