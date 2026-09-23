[⏮️ **Previous: 11 — The Central Limit Theorem**](11-central-limit-theorem.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 13 — Population & Estimated Parameters** ⏭️](13-population-estimated-parameters.md)

---

# 12: Naive Bayes

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Naive Bayes classifies something (say, an email) by asking: **"Which class makes these words most likely?"** It starts with how common each class is (the prior), then multiplies in how probable each word is under that class. The "naive" part is pretending every word is independent of the others given the class — obviously false ("Dear" and "Friend" appear together), yet the classifier works remarkably well because it only needs to **rank** the classes correctly, not get the probabilities exactly right.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. The Setup: Normal vs Spam Messages

Training data: 8 normal messages and 4 spam messages. Count words in each group.

| Word | Count in **Normal** | $P(\text{word} \mid \text{Normal})$ | Count in **Spam** | $P(\text{word} \mid \text{Spam})$ |
| :--- | :-: | :-: | :-: | :-: |
| Dear | 8 | 8/17 ≈ 0.47 | 2 | 2/7 ≈ 0.29 |
| Friend | 5 | 5/17 ≈ 0.29 | 1 | 1/7 ≈ 0.14 |
| Lunch | 3 | 3/17 ≈ 0.18 | 0 | 0/7 = 0 |
| Money | 1 | 1/17 ≈ 0.06 | 4 | 4/7 ≈ 0.57 |
| **Total words** | **17** | | **7** | |

**Priors** (how common each class is):
$$ P(\text{N}) = \frac{8}{12} \approx 0.67 \qquad P(\text{S}) = \frac{4}{12} \approx 0.33 $$

*(Illustrative counts in the style of the video.)*

---

### 2. Classifying "Dear Friend"

**Score for Normal** = prior × probability of each word:
$$ 0.67 \times 0.47 \times 0.29 \approx 0.091 $$

**Score for Spam:**
$$ 0.33 \times 0.29 \times 0.14 \approx 0.013 $$

Normal wins (0.091 > 0.013) → classify as **Normal**.

```text
   The decision:

   Normal:  P(N) x P(Dear|N) x P(Friend|N)  =  0.091   <- bigger
   Spam:    P(S) x P(Dear|S) x P(Friend|S)  =  0.013

   Pick the class with the larger score.
```

---

### 3. Why This Is Bayes' Theorem

By Bayes (topic 04):
$$ P(\text{class} \mid \text{words}) = \frac{P(\text{words} \mid \text{class})\,P(\text{class})}{P(\text{words})} $$

The denominator is the **same for every class**, so to compare classes we can drop it:
$$ P(\text{class} \mid \text{words}) \;\propto\; P(\text{class}) \prod_{i} P(\text{word}_i \mid \text{class}) $$

The product is the **naive independence assumption**: $P(\text{Dear, Friend} \mid \text{class}) = P(\text{Dear} \mid \text{class})\,P(\text{Friend} \mid \text{class})$.

---

### 4. Problem 1: A Zero Kills Everything

Classify "Lunch Money Money Money Money". Spam has **zero** "Lunch" in training, so $P(\text{Lunch} \mid \text{S}) = 0$ and the whole Spam score becomes 0 — even though "Money ×4" screams spam.

**Fix — Laplace (add-one) smoothing:** add 1 to every word count (a "pseudocount") before computing probabilities.

$$ P(\text{word} \mid \text{class}) = \frac{\text{count} + \alpha}{\text{total} + \alpha \cdot V} $$

where $V$ is the vocabulary size and usually $\alpha = 1$. No probability is ever exactly zero.

---

### 5. Problem 2: Underflow — Use Logs

Multiplying hundreds of small probabilities gives numbers too small for a computer to store (they round to 0). Take logs: products become sums.

$$ \log P(\text{class}) + \sum_i \log P(\text{word}_i \mid \text{class}) $$

Same winner, no underflow.

---

### 6. Why "Naive" Works Anyway

* Word order and correlations are ignored — treating a message like a **bag of words**.
* The probability estimates are often badly calibrated (too extreme).
* But classification only needs the **correct class to score highest**, and that ranking is often right.
* It's fast, needs little data, and is an excellent **baseline** for text classification.

| Strengths | Weaknesses |
| :--- | :--- |
| Very fast to train and predict | Independence assumption is false |
| Works with small datasets | Probabilities poorly calibrated |
| Handles many features (words) | Ignores word order |
| Strong text baseline | Beaten by modern models on hard tasks |

**Variants:** Multinomial NB (word counts), Bernoulli NB (word present/absent), **Gaussian NB** (continuous features, each modeled as a normal distribution per class).

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Generative classifier** | Contrast with discriminative models | NB models $P(x\mid y)$; logistic regression models $P(y \mid x)$ directly |
| **Laplace smoothing** | Regularization | Pseudocounts are a prior; same idea in language model smoothing |
| **Log-probabilities** | Numerical stability | Everywhere: log-likelihood, log-softmax, `logsumexp` |
| **Baseline** | Honest evaluation | Any fancy text classifier must beat NB + TF-IDF to be worth it |
| **Bag of words** | Feature engineering | `CountVectorizer` / TF-IDF representations |

---

### 8. Check Your Understanding

**Q1: Using the table (no smoothing), classify "Money Money".**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

* Normal: $0.67 \times 0.06 \times 0.06 \approx 0.0024$
* Spam: $0.33 \times 0.57 \times 0.57 \approx 0.107$

Spam wins by a wide margin → **Spam**.
</details>

**Q2: Why can we ignore the denominator $P(\text{words})$ when classifying?**
<details>
<summary><b>Reveal Answer</b></summary>

It's identical for every class — it depends only on the message, not the class being scored. Dividing every class's score by the same positive number can't change which one is biggest. (You'd need it only if you wanted the actual probabilities, not just the winner.)
</details>

**Q3: A classmate's NB spam filter has 97% accuracy. What else must you ask before you're impressed?**
<details>
<summary><b>Reveal Answer</b></summary>

* What fraction of the data is spam? If 97% is normal, "always predict normal" also scores 97% — that's the **baseline** to beat.
* Precision and recall on the spam class.
* Was it evaluated on a held-out test set, and how much does the score vary across splits/seeds?

One accuracy number with no baseline is not a result yet.
</details>

---

### 📺 Source

* **Video:** [Naive Bayes, Clearly Explained](https://youtu.be/O2L2Uv9pdDA)

---

[⏮️ **Previous: 11 — The Central Limit Theorem**](11-central-limit-theorem.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 13 — Population & Estimated Parameters** ⏭️](13-population-estimated-parameters.md)
