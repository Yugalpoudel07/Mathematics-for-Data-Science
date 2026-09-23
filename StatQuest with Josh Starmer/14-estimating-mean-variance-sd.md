[⏮️ **Previous: 13 — Population & Estimated Parameters**](13-population-estimated-parameters.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 15 — SD vs Standard Error** ⏭️](15-sd-vs-standard-error.md)

---

# 14: Estimating the Mean, Variance and Standard Deviation

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> To estimate the population's mean, just average your sample. To estimate its spread, average the squared distances from the mean — **but divide by $n-1$ instead of $n$**. Why? Your sample mean is, by construction, the point closest to your own data. Measuring distances from it makes your data look slightly less spread out than it really is. Dividing by $n-1$ corrects exactly for that underestimate.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Estimating the Mean

$$ \hat{\mu} = \bar{x} = \frac{1}{n}\sum_{i=1}^n x_i $$

On average (across many samples), $\bar{x}$ equals the true $\mu$ — it's **unbiased**.

---

### 2. Variance: Average Squared Distance

**Population variance** (if you knew $\mu$ and had everything):
$$ \sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2 $$

**Why square the distances?**

* Positive and negative deviations would cancel out otherwise (they always sum to zero around the mean).
* Squaring makes all distances positive and penalizes large deviations more.

---

### 3. The $n - 1$ Correction

In practice we don't know $\mu$; we plug in $\bar{x}$:

$$ \boxed{\; s^2 = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar{x})^2 \;} $$

#### Why Divide by $n - 1$?

```text
   The sample mean is the point that minimizes squared distance
   to YOUR data points:

         x1       x2   xbar   x3            mu (true, unknown)
   ------o--------o-----|-----o----------------|-----------

   Distances measured from xbar are, on average, SMALLER than
   distances measured from the true mu — because xbar was chosen
   to hug these particular points.

   Dividing by n would therefore UNDERESTIMATE the true variance.
   Dividing by the slightly smaller n - 1 inflates it just enough
   to be right on average.
```

**Another way to see it — degrees of freedom:** once you know $\bar{x}$ and $n-1$ of the values, the last value is determined. Only $n - 1$ deviations are free to vary.

| Divide by | Name | Bias |
| :--- | :--- | :--- |
| $n$ | "Population" formula applied to a sample | Underestimates $\sigma^2$ on average |
| $n - 1$ | **Sample variance** (Bessel's correction) | Unbiased for $\sigma^2$ |

For large $n$ the difference is negligible; for small samples it matters.

---

### 4. Standard Deviation

$$ s = \sqrt{s^2} $$

Taking the square root puts the spread back in the **original units** (cm, not cm²), which makes it interpretable: "heights typically vary by about 8 cm from the average."

> **Subtle point:** $s^2$ is unbiased for $\sigma^2$, but $s$ is *slightly* biased low for $\sigma$ (square roots don't pass through averages). In practice nobody corrects for this; it's tiny.

---

### 5. Worked Example

Sample: $[2, 4, 4, 5, 10]$, $n = 5$.

1. **Mean:** $\bar{x} = \frac{25}{5} = 5$
2. **Deviations:** $-3, -1, -1, 0, 5$
3. **Squared:** $9, 1, 1, 0, 25$ → sum $= 36$
4. **Sample variance:** $s^2 = \frac{36}{5 - 1} = 9$
5. **Sample SD:** $s = 3$

(Dividing by $n$ would have given 7.2 — noticeably smaller.)

---

### 6. In Code: Watch the Defaults

```python
import numpy as np
x = np.array([2, 4, 4, 5, 10])
np.var(x)          # 7.2  -> divides by n     (ddof=0 default!)
np.var(x, ddof=1)  # 9.0  -> divides by n - 1
import pandas as pd
pd.Series(x).var() # 9.0  -> pandas defaults to n - 1
```

> **NumPy and pandas use different defaults.** This is a real, common source of mismatched results. Always set `ddof` explicitly.

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Sample mean & SD** | Standardization | `StandardScaler` subtracts $\bar{x}$ and divides by $s$ per feature |
| **Fit on train only** | Avoiding leakage | Compute $\bar{x}$, $s$ on the training set; apply to test |
| **$n-1$ vs $n$** | Reporting variability across seeds | With 5 seeds, the correction changes the std noticeably |
| **Running estimates** | BatchNorm | Tracks running mean/variance of activations |
| **Variance** | Bias–variance trade-off | Model variance = how much predictions change across training samples |

---

### 8. Check Your Understanding

**Q1: Compute $\bar{x}$, $s^2$ and $s$ for $[10, 12, 14]$.**
<details>
<summary><b>Reveal Answer</b></summary>

$\bar{x} = 12$. Deviations $-2, 0, 2$; squares $4, 0, 4$; sum 8.
$s^2 = \frac{8}{2} = 4$, $s = 2$.
</details>

**Q2: You report the std of accuracy over 5 random seeds using `np.std(scores)`. What's subtly wrong?**
<details>
<summary><b>Reveal Answer</b></summary>

`np.std` defaults to `ddof=0` (divide by $n$), which underestimates the spread — with $n = 5$ the variance is too small by a factor of $4/5$. Use `np.std(scores, ddof=1)` when estimating variability from a sample of runs.
</details>

---

### 📺 Source

* **Video:** [Estimating the Mean, Variance and Standard Deviation](https://youtu.be/SzZ6GpcfoQY)

---

[⏮️ **Previous: 13 — Population & Estimated Parameters**](13-population-estimated-parameters.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 15 — SD vs Standard Error** ⏭️](15-sd-vs-standard-error.md)
