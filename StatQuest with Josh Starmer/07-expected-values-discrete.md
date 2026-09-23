[⏮️ **Previous: 06 — The Normal Distribution**](06-normal-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 08 — Expected Values (Continuous)** ⏭️](08-expected-values-continuous.md)

---

# 07: Expected Values, Part 1 (Discrete)

**StatQuest with Josh Starmer**

> [!TIP]
> **Core Intuition:**
> The expected value is the **long-run average** — what you'd get on average per trial if you repeated something many, many times. For a discrete variable, it's each possible outcome **weighted by how likely it is**, all added up. It doesn't have to be a value you can actually observe (the expected number of children per family can be 2.3), and it's the right number for decisions you make repeatedly: bets, insurance, pricing, and — in ML — losses.

> ✍️ **My one line (write after watching, no peeking):**

---

### 1. From an Average to an Expected Value

Suppose a game pays: \$0 with probability 0.5, \$1 with probability 0.3, \$10 with probability 0.2. Play 100 times and you'd expect roughly:

```text
   50 games paying $0   ->   $0
   30 games paying $1   ->   $30
   20 games paying $10  ->   $200
                            -----
   total                     $230   over 100 games  =  $2.30 per game
```

Dividing by 100 turns the counts into probabilities:

$$ \mathbb{E}[X] = 0(0.5) + 1(0.3) + 10(0.2) = 0 + 0.3 + 2.0 = 2.30 $$

---

### 2. The Formula

$$ \boxed{\; \mathbb{E}[X] = \sum_{x} x \cdot P(X = x) \;} $$

**Weighted average:** each outcome counts in proportion to its probability.

```text
   Expected value = the balance point of the distribution

      P(x)
       ^
   0.5 +  ###
       |  ###
   0.3 +  ###   ###
   0.2 +  ###   ###                       ###
       |  ###   ###                       ###
     0 +--###---###-----------------------###---> x
          0     1        ^                 10
                         |
                     E[X] = 2.3   <- where the "seesaw" balances
```

If you placed weights equal to the probabilities at each value on a seesaw, it would balance at the expected value.

---

### 3. Should You Play? Using Expected Value for Decisions

If the game costs \$3 to play, your expected **profit** is $2.30 - 3 = -0.70$ per game. Over many games you lose ~70 cents each time. Casinos, lotteries and insurance companies all price so that your expected value is negative (their expected value is positive).

> **Caveat:** expected value is the right guide for **repeated** decisions. For a one-shot decision with catastrophic downside, the spread (variance) and worst case matter too — that's why people buy insurance despite its negative expected value.

---

### 4. Useful Properties

| Property | Formula | In words |
| :--- | :--- | :--- |
| **Linearity** | $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ | Scale and shift pass straight through |
| **Sum rule** | $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ | **Always** true — even if $X, Y$ are dependent |
| **Function of $X$** | $\mathbb{E}[g(X)] = \sum_x g(x)\,P(X=x)$ | Weight $g(x)$, not $x$ |
| **Not for products (in general)** | $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ **only if independent** | |
| **Not for nonlinear functions** | $\mathbb{E}[X^2] \neq (\mathbb{E}[X])^2$ in general | The gap is the variance |

#### Variance Is an Expected Value Too

$$ \text{Var}(X) = \mathbb{E}\big[(X - \mathbb{E}[X])^2\big] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 $$

The average squared distance from the mean.

---

### 5. Connection to Machine Learning & Data Science

| Idea | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Expected value** | The definition of the objective | Expected loss (risk) $= \mathbb{E}[\ell(\hat{y}, y)]$ is what training minimizes |
| **Weighted average** | Cross-entropy | $-\sum_k y_k \log \hat{y}_k$ is an expectation over the true label distribution |
| **Linearity** | Splitting losses | $\mathbb{E}[L_1 + L_2] = \mathbb{E}[L_1] + \mathbb{E}[L_2]$ — why batch losses average cleanly |
| **Expected value for decisions** | Cost-sensitive classification | Choose the threshold that minimizes expected cost, not errors |
| **Expected return** | Reinforcement learning | RL agents maximize $\mathbb{E}[\sum_t \gamma^t r_t]$ |

---

### 6. Check Your Understanding

**Q1: A fair six-sided die. Compute $\mathbb{E}[X]$ and $\text{Var}(X)$.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

1. $\mathbb{E}[X] = \frac{1}{6}(1+2+3+4+5+6) = \frac{21}{6} = 3.5$
2. $\mathbb{E}[X^2] = \frac{1}{6}(1+4+9+16+25+36) = \frac{91}{6} \approx 15.167$
3. $\text{Var}(X) = 15.167 - 3.5^2 = 15.167 - 12.25 \approx 2.917$

Note: 3.5 is never actually rolled — expected values need not be possible outcomes.
</details>

**Q2: A fraud model flags a transaction. Investigating costs \$5. If it's fraud (probability 0.1) you save \$200; otherwise you save nothing. Should you investigate?**
<details>
<summary><b>Reveal Answer</b></summary>

$\mathbb{E}[\text{benefit}] = 0.1 \times 200 - 5 = 20 - 5 = \$15 > 0$. Yes — on average each investigation gains \$15. You'd investigate whenever $P(\text{fraud}) \times 200 > 5$, i.e. $P(\text{fraud}) > 0.025$. That's how expected value sets a **decision threshold**.
</details>

---

### 📺 Source

* **Video:** [Expected Values, Part 1](https://youtu.be/KLs_7b7SKi4)

---

[⏮️ **Previous: 06 — The Normal Distribution**](06-normal-distribution.md) &nbsp;•&nbsp; [📚 **StatQuest Index**](README.md) &nbsp;•&nbsp; [**Next: 08 — Expected Values (Continuous)** ⏭️](08-expected-values-continuous.md)
