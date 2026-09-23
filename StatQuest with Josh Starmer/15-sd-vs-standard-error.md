[⏮️ **Previous: 14 — Estimating Mean, Variance & SD**](14-estimating-mean-variance-sd.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 16 — The Standard Error** ⏭️](16-standard-error.md)

---

# 15: Standard Deviation vs Standard Error

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> These two sound alike and are constantly confused. **Standard deviation** describes how spread out the **individual data points** are. **Standard error** describes how spread out your **estimate (e.g. the mean)** would be if you repeated the whole experiment many times. SD is about the data; SE is about your *certainty*. Collect more data and the SD stays about the same, but the SE shrinks.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Two Different Questions

| | **Standard Deviation (SD)** | **Standard Error (SE)** |
| :--- | :--- | :--- |
| **Question** | How much do individual values vary? | How much would my **estimate** vary across repeated samples? |
| **Describes** | The data | The precision of a statistic (e.g. the mean) |
| **With more data** | Stays ≈ the same | **Shrinks** (like $1/\sqrt{n}$) |
| **Formula (for the mean)** | $s$ | $\frac{s}{\sqrt{n}}$ |

---

### 2. The Picture

```text
   Individual measurements (spread = SD):

       .   . .  ... ..... ... . .    .
   ----------------|------------------------
                   mean
       |<------- wide: SD ------->|


   Means of MANY repeated samples (spread = SE):

                 .:::::.
   ----------------|------------------------
                   mean
                |<-->|   narrow: SE = SD / sqrt(n)
```

Averages are much less variable than the individual points they average.

---

### 3. Standard Error as a "Standard Deviation of Means"

The SE is literally the standard deviation of the distribution of sample means:

1. Take a sample of size $n$, compute its mean.
2. Repeat many times.
3. The standard deviation of all those means **is** the standard error.

You don't actually need to repeat the experiment — for the mean, the formula $\frac{s}{\sqrt{n}}$ gives it from one sample. For other statistics without a formula, the **bootstrap** (topic 18) simulates the repetition.

---

### 4. Which One to Report?

| If you want to show… | Report |
| :--- | :--- |
| How variable the thing you measured is | **SD** |
| How precisely you've pinned down the mean | **SE** (or a confidence interval) |
| Whether two group means differ | **SE / CI** |

> **Beware:** SE error bars are always smaller than SD bars. Some reports use SE bars to make results look more precise than the data look. Always label which one you're showing.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **SD across seeds** | Stability of a training recipe | "Accuracy 0.84 ± 0.02 (SD, 5 seeds)" |
| **SE of the mean** | Comparing two models | Is model A's mean really above B's, given the SE? |
| **Label your error bars** | Honest reporting | Plots must state SD, SE, or 95% CI |
| **SE shrinks with n** | Test-set size | A bigger test set tightens the SE of accuracy; the model's variability doesn't change |

---

### 6. Check Your Understanding

**Q1: 100 measurements have SD = 20. What's the SE of the mean? If you collect 400 measurements instead, what happens to each?**
<details>
<summary><b>Reveal Answer</b></summary>

SE $= \frac{20}{\sqrt{100}} = 2$. With 400 measurements, the SD stays ≈ 20 (the data aren't less variable), but SE $= \frac{20}{\sqrt{400}} = 1$ — halved. Four times the data halves the SE.
</details>

**Q2: A paper shows two models with overlapping SD error bars and says "no difference." Is that justified?**
<details>
<summary><b>Reveal Answer</b></summary>

Not necessarily. SD bars show the spread of individual runs, not the uncertainty of the means. The means could still differ reliably — you need SE-based intervals or a proper test (ideally paired, if the same splits/seeds were used).
</details>

---

### 📺 Source

* **Video:** [Standard Deviation vs Standard Error, Clearly Explained](https://youtu.be/A82brFpdr9g)

---

[⏮️ **Previous: 14 — Estimating Mean, Variance & SD**](14-estimating-mean-variance-sd.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 16 — The Standard Error** ⏭️](16-standard-error.md)
