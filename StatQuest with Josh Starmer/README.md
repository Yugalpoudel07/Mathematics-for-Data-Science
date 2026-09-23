[🏠 **Main Repository**](../README.md) &nbsp;•&nbsp; [**Start Reading: 01 — Probability Distributions** ⏭️](01-probability-distributions.md)

---

# 🎬 StatQuest with Josh Starmer — Probability & Statistics

### *Short, clear explainers for the statistics underneath machine learning*

[![Status: In Progress](https://img.shields.io/badge/Status-In_Progress-orange?style=flat-square)](#)
[![Topics](https://img.shields.io/badge/Topics-21_core_%2B_2_optional-blue?style=flat-square)](#-topic-directory)
[![Index](https://img.shields.io/badge/StatQuest-Video_Index-red?style=flat-square&logo=youtube)](https://statquest.org/video_index.html)

> [!NOTE]
> **About this Module:**
> StatQuest is a **lookup library, not a course** — hundreds of videos, of which the 23 below cover probability, distributions, the Central Limit Theorem, uncertainty, bootstrapping and maximum likelihood. Each topic has its own note file with intuition, formulas, ASCII diagrams, a **Connection to Machine Learning & Data Science** table, and self-check questions with worked answers.
>
> Every note starts with an empty **✍️ My one line** field. Fill it in **after watching, before reading the notes** — writing it in your own words is what makes the video stick.
>
> The old `statquest.org/video-index/` link now redirects to **https://statquest.org/video_index.html**. All links below were checked against it on 22 Sep 2026.

---

## 🗺️ Topic Directory

### Part I — Probability Foundations

| # | Topic | Video | Notes | Done |
| :-: | :--- | :--- | :--- | :-: |
| **01** | The Main Ideas behind Probability Distributions | https://youtu.be/oI3hZJqXJuc | [📝 Notes](01-probability-distributions.md) | ☐ |
| **02** | What does it mean to "sample from a distribution"? | https://youtu.be/XLCWeSVzHUU | [📝 Notes](02-sampling-from-a-distribution.md) | ☐ |
| **03** | Conditional Probability | https://youtu.be/_IgyaD7vOOA | [📝 Notes](03-conditional-probability.md) | ☐ |
| **04** | Bayes' Theorem | https://youtu.be/9wCnvr7Xw4E | [📝 Notes](04-bayes-theorem.md) | ☐ |

### Part II — Core Distributions

| # | Topic | Video | Notes | Done |
| :-: | :--- | :--- | :--- | :-: |
| **05** | The Binomial Distribution and Test | https://youtu.be/J8jNoF-K8E8 | [📝 Notes](05-binomial-distribution.md) | ☐ |
| **06** | The Normal Distribution | https://youtu.be/rzFX5NWojp0 | [📝 Notes](06-normal-distribution.md) | ☐ |

### Part III — Expected Value & Relationships Between Variables

| # | Topic | Video | Notes | Done |
| :-: | :--- | :--- | :--- | :-: |
| **07** | Expected Values, Part 1 (discrete) | https://youtu.be/KLs_7b7SKi4 | [📝 Notes](07-expected-values-discrete.md) | ☐ |
| **08** | Expected Values, Part 2 (continuous) | https://youtu.be/OSPr6G6Ka-U | [📝 Notes](08-expected-values-continuous.md) | ☐ |
| **09** | Covariance | https://youtu.be/qtaqvPAeEJY | [📝 Notes](09-covariance.md) | ☐ |
| **10** | Pearson's Correlation | https://youtu.be/xZ_z8KWkhXE | [📝 Notes](10-pearsons-correlation.md) | ☐ |

### Part IV — The Central Limit Theorem & a First Classifier

| # | Topic | Video | Notes | Done |
| :-: | :--- | :--- | :--- | :-: |
| **11** | The Central Limit Theorem | https://youtu.be/YAlJCEDH2uY | [📝 Notes](11-central-limit-theorem.md) | ☐ |
| **12** | Naive Bayes | https://youtu.be/O2L2Uv9pdDA | [📝 Notes](12-naive-bayes.md) | ☐ |

### Part V — Estimation & Uncertainty

| # | Topic | Video | Notes | Done |
| :-: | :--- | :--- | :--- | :-: |
| **13** | Population and Estimated Parameters | https://youtu.be/vikkiwjQqfU | [📝 Notes](13-population-estimated-parameters.md) | ☐ |
| **14** | Estimating the Mean, Variance and Standard Deviation | https://youtu.be/SzZ6GpcfoQY | [📝 Notes](14-estimating-mean-variance-sd.md) | ☐ |
| **15** | Standard Deviation vs Standard Error | https://youtu.be/A82brFpdr9g | [📝 Notes](15-sd-vs-standard-error.md) | ☐ |
| **16** | The Standard Error | https://youtu.be/XNgt7F6FqDU | [📝 Notes](16-standard-error.md) | ☐ |
| **17** | Confidence Intervals | https://youtu.be/TqOeMYtOc1w | [📝 Notes](17-confidence-intervals.md) | ☐ |
| **18** | Bootstrapping, Part 1: Main Ideas | https://youtu.be/Xz0x-8-cgaQ | [📝 Notes](18-bootstrapping-main-ideas.md) | ☐ |

### Part VI — Likelihood & Maximum Likelihood Estimation

| # | Topic | Video | Notes | Done |
| :-: | :--- | :--- | :--- | :-: |
| **19** | Probability vs Likelihood | https://youtu.be/pYxNSUDSFH4 | [📝 Notes](19-probability-vs-likelihood.md) | ☐ |
| **20** | Maximum Likelihood | https://youtu.be/XepXtl9YKwc | [📝 Notes](20-maximum-likelihood.md) | ☐ |
| **21** | Maximum Likelihood — Normal Distribution (worked example) | https://youtu.be/Dn6b9fCIUpM | [📝 Notes](21-mle-normal-distribution.md) | ☐ |
| **22** | Maximum Likelihood — Binomial Distribution *(optional)* | https://youtu.be/4KKV9yZCoM4 | [📝 Notes](22-mle-binomial-distribution.md) | ☐ |
| **23** | Maximum Likelihood — Exponential Distribution *(optional)* | https://youtu.be/p3T-_LMrvBc | [📝 Notes](23-mle-exponential-distribution.md) | ☐ |

### ⏭️ Coming Next — Hypothesis Testing

| Topic | Video |
| :--- | :--- |
| Bootstrapping, Part 2: Calculating p-values | https://youtu.be/N4ZQQqyIf6k |

---

## 🧠 Key Conceptual Pillars

```text
               +-------------------------------------------------+
               |      DISTRIBUTIONS: WHERE VALUES TEND TO LAND    |
               |  Probability = area; parameters define the shape |
               +------------------------+------------------------+
                                        |
                                        v
               +-------------------------------------------------+
               |    CONDITIONING & BAYES: UPDATING ON EVIDENCE    |
               |  P(A|B) shrinks the world; base rates matter     |
               +------------------------+------------------------+
                                        |
                                        v
               +-------------------------------------------------+
               |     SAMPLING & THE CLT: ESTIMATES WOBBLE         |
               |  Means are normal; SE = s / sqrt(n)               |
               +------------------------+------------------------+
                                        |
                                        v
               +-------------------------------------------------+
               |    LIKELIHOOD: PICK THE MODEL THAT FITS BEST     |
               |  Maximum likelihood = the loss function you use  |
               +-------------------------------------------------+
```

1. **Every number is a guess with a range.** You only ever see a sample. Report the estimate *and* its uncertainty (SE, CI) — a bare number is arithmetic, not statistics.
2. **Base rates dominate.** $P(\text{evidence} \mid \text{cause}) \neq P(\text{cause} \mid \text{evidence})$. A 99%-accurate test for a rare condition mostly produces false alarms.
3. **Averages behave nicely even when data don't.** The CLT makes sample means normal regardless of the data's shape — the reason error bars work.
4. **Choosing a likelihood is choosing a loss.** Gaussian noise → MSE. Bernoulli → binary cross-entropy. Categorical → cross-entropy.

---

## 💡 How These Topics Power Machine Learning

| Statistical Concept | Machine Learning / Data Science Role | Concrete Application |
| :--- | :--- | :--- |
| **Distributions & sampling** | Data exploration, generative models | Feature histograms; VAEs, diffusion, LLM token sampling |
| **Conditional probability** | What classifiers output | $P(y \mid x)$ from logistic regression / softmax |
| **Bayes' theorem** | Class imbalance, priors | Precision under rare classes; $L_2$ = Gaussian prior |
| **Expected value** | The training objective | Expected loss (risk); empirical risk = sample average |
| **Covariance & correlation** | Feature redundancy, PCA | Correlation heatmaps; eigenvectors of the covariance matrix |
| **Central Limit Theorem** | Error bars, gradient noise | Mean ± SE over seeds; batch noise $\propto 1/\sqrt{B}$ |
| **Standard error & CIs** | Honest model reporting | "AUC 0.87 [0.84, 0.90]", not "AUC 0.87" |
| **Bootstrapping** | Uncertainty for any metric; bagging | Bootstrap CIs; random forests |
| **Maximum likelihood** | How models are fit | Linear regression (MSE), logistic regression (BCE) |

---

## ⚠️ Gaps You Should Know About

- StatQuest has **no full video on the Poisson or Bernoulli distributions**, and its Exponential-distribution video is only a short song. **Khan Academy Statistics** (already in the plan) covers them.
- Video lengths were **not checked**. Most StatQuest videos run about 5–20 minutes, so the core set should fit a ~5-hour budget including your one-line summaries. If it passes ~7.5 hours, stop and flag it.

---

## 📌 How to Study With These Notes

1. **Watch** the video.
2. **Close it and write your one line** in the ✍️ field at the top of the note — no copying the title.
3. **Then read the note** and fix anything you got wrong.
4. **Answer the Check Your Understanding questions** on paper before expanding them.
5. **Tick** ☐ → ☑ in the table above.

---

## 📺 Source Material

* **Official video index:** [statquest.org/video_index.html](https://statquest.org/video_index.html)
* **Author:** Josh Starmer

---

[🏠 **Back to Main Repository**](../README.md) &nbsp;•&nbsp; [**Start with 01: Probability Distributions** ⏭️](01-probability-distributions.md)
