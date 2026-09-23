[⏮️ **Previous: 02 — Sampling from a Distribution**](02-sampling-from-a-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 04 — Bayes' Theorem** ⏭️](04-bayes-theorem.md)

---

# 03: Conditional Probability

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> Conditional probability is probability **after you've learned something**. "What fraction of people like jazz?" is one question. "What fraction of people *who play an instrument* like jazz?" is a different question — you've **shrunk the world** to only the people who match the condition, then asked the question inside that smaller world. That shrinking is the whole idea, and it's the foundation of Bayes' theorem and every classifier.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. Start With a Table of Counts

Survey 100 people about two things: do they like **candy**, and do they like **soda**?

| | Likes soda | Dislikes soda | **Total** |
| :--- | :-: | :-: | :-: |
| **Likes candy** | 30 | 20 | **50** |
| **Dislikes candy** | 10 | 40 | **50** |
| **Total** | **40** | **60** | **100** |

**Plain probabilities** use the whole table (all 100 people):

* $P(\text{soda}) = \frac{40}{100} = 0.40$
* $P(\text{candy and soda}) = \frac{30}{100} = 0.30$ ← a **joint** probability

---

### 2. Conditioning = Shrinking the World

**Question:** among people who like candy, what fraction like soda?

```text
   Restrict attention to ONE row:

                  soda   no soda   total
   likes candy  [  30  ,   20   ]   50    <- our new "whole world"
   no candy        10      40       50

   P(soda | candy) = 30 / 50 = 0.60
```

$$ P(\text{soda} \mid \text{candy}) = \frac{30}{50} = 0.60 $$

Read the vertical bar $\mid$ as **"given"**. Knowing someone likes candy **raises** the chance they like soda from $0.40$ to $0.60$.

---

### 3. The Formula

Dividing counts by the grand total turns the same calculation into probabilities:

$$ \boxed{\; P(A \mid B) = \frac{P(A \text{ and } B)}{P(B)} \;} $$

Check with the table:
$$ P(\text{soda} \mid \text{candy}) = \frac{0.30}{0.50} = 0.60 \;\checkmark $$

```text
   Venn picture:

       +--------------------------------+
       |   everyone                     |
       |      +-------+                 |
       |      |   A   |---+             |
       |      |    ###|   |             |   P(A|B) = the part of B
       |      +----###+   |             |            that is also A,
       |           |  B   |             |            as a fraction of B
       |           +------+             |
       +--------------------------------+
                 ### = A and B
```

---

### 4. Order Matters: $P(A \mid B) \neq P(B \mid A)$

$$ P(\text{candy} \mid \text{soda}) = \frac{30}{40} = 0.75 \qquad P(\text{soda} \mid \text{candy}) = \frac{30}{50} = 0.60 $$

Same overlap (30), **different denominators** (the size of the world you shrank to).

> **The classic trap:** $P(\text{positive test} \mid \text{disease})$ is **not** $P(\text{disease} \mid \text{positive test})$. Confusing them is called the **prosecutor's fallacy**, and it has sent innocent people to prison. Bayes' theorem (next topic) is the tool that converts one into the other.

---

### 5. Independence

Two events are **independent** if learning one tells you nothing about the other:

$$ A, B \text{ independent} \iff P(A \mid B) = P(A) \iff P(A \text{ and } B) = P(A)\,P(B) $$

In our table, $P(\text{soda} \mid \text{candy}) = 0.60 \neq 0.40 = P(\text{soda})$, so candy and soda preferences are **dependent**.

| Example | Independent? |
| :--- | :--- |
| Two separate coin flips | Yes |
| Rain today and carrying an umbrella | No |
| Your height and the last digit of your phone number | Yes (for all practical purposes) |

---

### 6. The Multiplication Rule

Rearranging the formula gives a way to compute joint probabilities:

$$ P(A \text{ and } B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A) $$

That symmetry — two ways to write the same joint probability — is precisely where Bayes' theorem comes from.

---

### 7. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **$P(y \mid x)$** | What a classifier outputs | Logistic regression and softmax output $P(\text{class} \mid \text{features})$ |
| **Shrinking the world** | Segment analysis | Conversion rate *given* mobile vs desktop users |
| **$P(A\mid B) \neq P(B\mid A)$** | Interpreting model metrics | Precision $= P(\text{true}\mid\text{predicted})$ vs recall $= P(\text{predicted}\mid\text{true})$ |
| **Independence** | Naive Bayes assumption | Features assumed independent given the class (topic 12) |
| **Multiplication rule** | Language models | $P(\text{sentence}) = \prod_t P(w_t \mid w_{<t})$ |

---

### 8. Check Your Understanding

**Q1: Using the table above, compute $P(\text{dislikes candy} \mid \text{dislikes soda})$.**
<details>
<summary><b>Reveal Answer</b></summary>

Shrink to the "dislikes soda" column (60 people). Of those, 40 dislike candy:
$$ P(\text{no candy} \mid \text{no soda}) = \frac{40}{60} \approx 0.667 $$
</details>

**Q2: A spam filter flags 95% of spam, and 2% of all emails are flagged. Which of these is $P(\text{flagged} \mid \text{spam})$, and can you conclude $P(\text{spam} \mid \text{flagged}) = 0.95$?**
<details>
<summary><b>Reveal Answer</b></summary>

$P(\text{flagged} \mid \text{spam}) = 0.95$. You **cannot** conclude $P(\text{spam} \mid \text{flagged}) = 0.95$ — that reverses the condition. To get it you also need the base rate $P(\text{spam})$ and use Bayes' theorem:
$$ P(\text{spam}\mid\text{flagged}) = \frac{0.95 \cdot P(\text{spam})}{0.02} $$
If 1% of email is spam, this gives $0.475$ — less than half of flagged emails are actually spam.
</details>

**Q3: Show that if $P(A \mid B) = P(A)$, then $P(B \mid A) = P(B)$.**
<details>
<summary><b>Reveal Answer</b></summary>

From $P(A\mid B) = P(A)$ and the multiplication rule: $P(A \text{ and } B) = P(A\mid B)P(B) = P(A)P(B)$. Then
$$ P(B \mid A) = \frac{P(A \text{ and } B)}{P(A)} = \frac{P(A)P(B)}{P(A)} = P(B) \;\blacksquare $$
Independence is symmetric.
</details>

---

### 📺 Source

* **Video:** [Conditional Probability](https://youtu.be/_IgyaD7vOOA)

---

[⏮️ **Previous: 02 — Sampling from a Distribution**](02-sampling-from-a-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 04 — Bayes' Theorem** ⏭️](04-bayes-theorem.md)
