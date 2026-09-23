[⏮️ **Previous: 03 — Conditional Probability**](03-conditional-probability.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 05 — The Binomial Distribution** ⏭️](05-binomial-distribution.md)

---

# 04: Bayes' Theorem

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Bayes' theorem is the rule for **updating a belief when new evidence arrives**. You start with how common something is (the **prior**), you see evidence, and you ask how much more likely that evidence is if your hypothesis is true. The result (the **posterior**) is your updated belief. Its most important lesson is humbling: **a highly accurate test for a rare condition still produces mostly false alarms**, because the rarity (the base rate) matters as much as the accuracy.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Where It Comes From

From topic 03, the joint probability can be written two ways:

$$ P(A \text{ and } B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A) $$

Set the two right-hand sides equal and divide by $P(B)$:

$$ \boxed{\; P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)} \;} $$

That's it — Bayes' theorem is two lines of algebra on the definition of conditional probability. Its power comes from what it lets you **flip**: you usually know $P(\text{evidence} \mid \text{cause})$ and want $P(\text{cause} \mid \text{evidence})$.

---

### 2. The Names of the Parts

$$ \underbrace{P(H \mid E)}_{\text{posterior}} = \frac{\overbrace{P(E \mid H)}^{\text{likelihood}} \; \overbrace{P(H)}^{\text{prior}}}{\underbrace{P(E)}_{\text{evidence}}} $$

| Term | Meaning | Medical-test example |
| :--- | :--- | :--- |
| **Prior** $P(H)$ | Belief *before* seeing evidence | How common the disease is |
| **Likelihood** $P(E \mid H)$ | How probable the evidence is if $H$ is true | Test sensitivity |
| **Evidence** $P(E)$ | Overall probability of the evidence | Fraction of *all* tests that come back positive |
| **Posterior** $P(H \mid E)$ | Belief *after* seeing evidence | Chance you're sick given a positive test |

The evidence term expands with the **law of total probability**:
$$ P(E) = P(E \mid H)\,P(H) + P(E \mid \text{not } H)\,P(\text{not } H) $$

---

### 3. The Base-Rate Problem (Worked Example)

A disease affects **1%** of people. A test catches **99%** of sick people (sensitivity) and has a **5%** false-positive rate. You test positive. **How likely is it you're sick?**

Most people guess ~99%. Let's count with 10,000 people:

```text
                         10,000 people
                        /             \
               100 sick                9,900 healthy
              /       \                /           \
        99 test +    1 test -    495 test +     9,405 test -
         (true +)                (false +)

   Total positives = 99 + 495 = 594
   Sick among positives = 99

   P(sick | positive) = 99 / 594  ~=  0.167
```

**With the formula:**
$$ P(\text{sick} \mid +) = \frac{0.99 \times 0.01}{0.99 \times 0.01 + 0.05 \times 0.99} = \frac{0.0099}{0.0099 + 0.0495} = \frac{0.0099}{0.0594} \approx 0.167 $$

> **Only about 17%.** The healthy group is so large that even a small 5% false-positive rate generates five times more false alarms than true detections. **Ignoring the base rate** is one of the most common reasoning errors in medicine, law, security, and ML.

---

### 4. Updating Again

Test positive a **second** time (independent test). The old posterior becomes the new prior:

$$ P(\text{sick} \mid ++) = \frac{0.99 \times 0.167}{0.99 \times 0.167 + 0.05 \times 0.833} = \frac{0.165}{0.165 + 0.0417} \approx 0.80 $$

```text
   Belief updating:

   prior      after test 1      after test 2
   1%   ---->    17%     ---->     80%

   Evidence accumulates. Each posterior is the next prior.
```

---

### 5. Bayes' Theorem With Counts (the Easy Way)

When in doubt, **imagine a concrete population** (10,000 or 100,000 people) and count. It avoids formula mistakes and makes the base-rate effect obvious. This is sometimes called "natural frequencies," and people reason about it far more accurately than about percentages.

---

### 6. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Posterior $\propto$ likelihood × prior** | Naive Bayes classification | $P(\text{spam} \mid \text{words}) \propto P(\text{words}\mid\text{spam})P(\text{spam})$ (topic 12) |
| **Base rates** | Class imbalance | Fraud at 0.1%: a "99% accurate" model can be useless; look at precision |
| **Priors** | Regularization | $L_2$ weight decay $=$ a Gaussian prior on weights (MAP estimation) |
| **Sequential updating** | Online learning, A/B testing | Bayesian A/B tests update conversion beliefs as data arrives |
| **Evidence $P(E)$** | Bayesian model comparison | The (often intractable) normalizer that variational inference approximates |
| **Precision vs sensitivity** | Choosing a threshold | Precision is literally $P(\text{positive}\mid\text{flagged})$ — a Bayes posterior |

---

### 7. Check Your Understanding

**Q1: A factory's machine A makes 60% of parts with 2% defective; machine B makes 40% with 5% defective. A part is defective. What's the probability it came from B?**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

1. **Evidence:** $P(\text{def}) = 0.02(0.6) + 0.05(0.4) = 0.012 + 0.020 = 0.032$
2. **Bayes:**
   $$ P(B \mid \text{def}) = \frac{0.05 \times 0.4}{0.032} = \frac{0.020}{0.032} = 0.625 $$

* **Result:** 62.5%. Even though B makes fewer parts, its higher defect rate makes it the more likely source.
</details>

**Q2: In the disease example, what happens to $P(\text{sick}\mid +)$ if the disease affects 20% of the tested population instead of 1%? What does this tell you?**
<details>
<summary><b>Reveal Answer</b></summary>

$$ P(\text{sick}\mid +) = \frac{0.99 \times 0.2}{0.99\times0.2 + 0.05\times0.8} = \frac{0.198}{0.198 + 0.04} \approx 0.832 $$

The **same test** now gives 83% instead of 17%. A test's usefulness depends on **who** is being tested. This is why doctors test people with symptoms (higher prior) rather than screening everyone.
</details>

**Q3: A fraud model has 99% accuracy on a dataset where 0.5% of transactions are fraud. Why might this be meaningless?**
<details>
<summary><b>Reveal Answer</b></summary>

A model that **always predicts "not fraud"** is right 99.5% of the time — better than the reported 99% — while catching zero fraud. With a tiny base rate, accuracy is dominated by the majority class. You need precision, recall, and a baseline comparison. A "result" without a baseline is not yet a result.
</details>

---

### 📺 Source

* **Video:** [Bayes' Theorem](https://youtu.be/9wCnvr7Xw4E)

---

[⏮️ **Previous: 03 — Conditional Probability**](03-conditional-probability.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 05 — The Binomial Distribution** ⏭️](05-binomial-distribution.md)
