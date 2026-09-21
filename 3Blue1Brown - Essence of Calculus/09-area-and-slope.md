[⏮️ **Previous: Chapter 08 — Integration & the Fundamental Theorem**](08-integration-fundamental-theorem.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 10 — Higher Order Derivatives** ⏭️](10-higher-order-derivatives.md)

---

# Chapter 09: What Does Area Have to Do With Slope?

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Area and slope seem to have nothing in common — one is about *accumulating*, the other about *steepness*. The bridge is the **average value of a continuous function**. Averaging finitely many numbers means summing and dividing by the count; averaging a continuum means **integrating and dividing by the length**. And once you write that down, the Fundamental Theorem turns it into $\frac{F(b)-F(a)}{b-a}$ — which is literally the **slope of a secant line** on the antiderivative's graph. Area and slope are two views of one object.

---

### 1. The Motivating Question

> **What is the average value of $\sin(x)$ over $[0, \pi]$?**

This is not an idle puzzle. It is the shape of countless real questions:

* What is the average height of a randomly chosen point on a hill?
* What is the average power delivered by an alternating current?
* What is the average loss of a model over a continuous data distribution?

```text
   The average of a SMOOTH curve:

     sin(x)
       ^
     1 +        ___
       |     _/     \_
       |   /           \       There are INFINITELY many
       |  /             \      values between 0 and pi.
       | /               \     Which do we "average"?
     0 +/-----------------\---> x
       0                  pi
```

The difficulty is structural: the usual recipe "add up the values and divide by how many there are" asks us to divide infinity by infinity.

---

### 2. Finite Averages, Then a Limit

Start with something you can do. Sample $n$ evenly spaced points and average them.

```text
   Sampling finitely many heights:

     sin(x)
       ^
     1 +        ___
       |     _/|||\_
       |   / |||||| \
       |  / ||||||||  \
       | / ||||||||||  \
     0 +/--+--+--+--+---\---> x
       0   x1 x2 x3 x4   pi

   Average = ( sin(x1) + sin(x2) + ... + sin(xn) ) / n
```

$$ \text{Average}_n = \frac{1}{n}\sum_{i=1}^{n} f(x_i) $$

**The trick — manufacture a $\Delta x$.** With $n$ samples across $[a,b]$, the spacing is
$$ \Delta x = \frac{b-a}{n} \quad\Longrightarrow\quad \frac{1}{n} = \frac{\Delta x}{b-a} $$

Substituting:

$$ \text{Average}_n = \frac{1}{b-a}\sum_{i=1}^{n} f(x_i)\,\Delta x $$

```text
   What just happened:

        1                          Delta x
       --- * sum f(x_i)     =     --------- * sum f(x_i)
        n                          (b - a)

                              =      1        ______________
                                  -------  *  \  f(x_i) dx      <- a RIEMANN SUM!
                                  (b - a)     /
```

Now take $n \to \infty$. The sum becomes an integral:

$$ \boxed{\; \bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx \;} $$

> **The conceptual move:** dividing by $n$ was blocking us, because $n \to \infty$. Converting $\frac{1}{n}$ into $\frac{\Delta x}{b-a}$ moved the problematic infinity *inside* the sum, where it is exactly what an integral is designed to handle.

---

### 3. The Geometric Meaning of the Average

```text
   The average value flattens the curve without changing the area:

     f(x)
      ^
      |        ___
      |     _/    \_
  fbar+----/--------\-----+
      |   /          \    |      Rectangle area = (b-a) * fbar
      |  /   SAME     \   |      Curve area     = integral
      | /    AREA      \  |
    0 +/----------------\-+---> x
      a                  b

   The horizontal line sits at exactly the height where the
   "hills" above it fill the "valleys" below it.
```

Equivalently: $\bar{f}$ is the height of the rectangle with the same base and the same area as the region under the curve.

---

### 4. Worked Example: The Average of $\sin(x)$

$$ \bar{f} = \frac{1}{\pi - 0}\int_0^\pi \sin(x)\,dx $$

**Step 1 — Antiderivative:** $F(x) = -\cos(x)$.

**Step 2 — Evaluate:**
$$ \int_0^\pi \sin x\,dx = \big[-\cos x\big]_0^\pi = -\cos(\pi) - \big(-\cos(0)\big) = 1 + 1 = 2 $$

**Step 3 — Divide by the length:**
$$ \bar{f} = \frac{2}{\pi} \approx 0.6366 $$

```text
   Checking the answer for plausibility:

     1 +        ___
       |     _/     \_
  0.64 +---/-----------\----     <- 2/pi, a bit below the midpoint
       |  /             \           of 0 and 1 — correct, since
       | /               \          the curve spends more time
     0 +/-----------------\--> x    near the ends than at the peak
       0                  pi
```

The answer sits sensibly between $0$ and $1$, slightly below $\frac{1}{2}\cdot 1 + \frac{1}{2}\cdot 0$ weighted toward the tails. ✓

---

### 5. The Punchline: Average Value **Is** Average Slope

Here is the connection the chapter is named for. Apply the Fundamental Theorem to the average-value formula:

$$ \bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx = \frac{F(b) - F(a)}{b - a} $$

where $F$ is any antiderivative of $f$.

**Look at what that right-hand side is.** $\frac{F(b)-F(a)}{b-a}$ is $\frac{\text{rise}}{\text{run}}$ — the **slope of the secant line** joining the two endpoints of $F$'s graph.

```text
   Two graphs, one fact:

   The function f (heights)            Its antiderivative F (slopes)

     f(x)                                F(x)
      ^                                   ^              * F(b)
      |     ___                           |            /|
      |   _/|||\_                         |         _/  |
  fbar+--/-|||||\--+                      |      _/     | rise = F(b)-F(a)
      | / |||||||\ |                      |   _/        |
      |/  |||||||| \                      | */----------+
    0 +---+++++++++-+---> x               |  F(a)  run = b-a
      a           b                       +------------------> x
                                          a            b

   The AVERAGE HEIGHT of f      ==      the SLOPE of the secant
   over [a, b]                          on F over [a, b]
```

> **The statement in words:** the **average value of a function** equals the **average rate of change of its antiderivative**. Area under $f$ and slope on $F$ are the same information, read off two different graphs.

#### The Mean Value Theorem Falls Out

Since $F' = f$, this says the secant slope of $F$ equals the *average* of $F$'s instantaneous slopes. If $f$ is continuous, it must actually **attain** that average somewhere:

$$ \exists\, c \in (a,b) \;\text{ such that }\; F'(c) = \frac{F(b)-F(a)}{b-a} $$

```text
   The Mean Value Theorem:

     F(x)
      ^                    * F(b)
      |                  /|
      |          _____ /  |     Somewhere in between, the TANGENT
      |        /     /    |     is exactly PARALLEL to the secant.
      |      /     /      |
      |    /  <--tangent at c
      |  */
      | F(a)
      +--+------+---------+---> x
         a      c         b
```

**The everyday version:** if you average 60 mph over a journey, then at some instant your speedometer read *exactly* 60.

---

### 6. Why the Average Value Formula Matters

| Question | The integral that answers it |
| :--- | :--- |
| Average temperature over a day | $\frac{1}{24}\int_0^{24}T(t)\,dt$ |
| Root-mean-square voltage of AC | $\sqrt{\frac{1}{T}\int_0^T V(t)^2 dt}$ |
| Centre of mass of a rod | $\frac{\int x\,\rho(x)dx}{\int \rho(x)dx}$ |
| Expected value of a random variable | $\int x\,p(x)\,dx$ |
| Expected loss over a data distribution | $\int \ell(f(x),y)\,p(x,y)\,dx\,dy$ |

Notice the last two. **Expected value is a weighted average**, and the weighting function is the probability density:

$$ \mathbb{E}[X] = \int_{-\infty}^{\infty} x\,p(x)\,dx $$

Compare with the unweighted average $\frac{1}{b-a}\int_a^b x\,dx$: the uniform distribution on $[a,b]$ has $p(x) = \frac{1}{b-a}$, so **the plain average is the expected value under a uniform distribution.** The two formulas were never different ideas.

---

### 7. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Average value as an integral** | The definition of **expected risk** | $R(f) = \mathbb{E}_{(x,y)\sim p}\big[\ell(f(x),y)\big] = \int \ell\,p\,dx\,dy$ — the quantity you actually want to minimize |
| **Finite average → integral** | Why **empirical risk minimization** works | $\hat{R} = \frac{1}{N}\sum_i \ell_i$ is the Riemann/Monte Carlo estimate of $R$; the gap is the *generalization gap* |
| **$\frac{1}{n} \to \frac{\Delta x}{b-a}$ trick** | Importance sampling and reweighting | $\mathbb{E}_p[f] = \mathbb{E}_q\!\left[f\frac{p}{q}\right]$ — the same "manufacture the right weight" manoeuvre |
| **Average value = average slope** | Interpreting loss curves | Average improvement per epoch is the secant slope of the cumulative loss curve |
| **Mean Value Theorem** | Convergence guarantees in optimization | Bounds of the form $f(y) - f(x) = \nabla f(c)^T(y-x)$ underpin nearly every descent-lemma proof |
| **Weighted averages** | Attention, ensembling, moving averages | $\text{attention}(Q,K,V) = \sum_i \alpha_i v_i$ is a weighted average with learned weights $\alpha$ |
| **RMS (average of squares)** | Adaptive optimizer state | RMSProp tracks $\mathbb{E}[g^2]$; Adam tracks both $\mathbb{E}[g]$ and $\mathbb{E}[g^2]$ |

#### The Deepest Link: Why Mini-Batches Work

The full objective is an integral over the data distribution:

$$ R(\theta) = \int \ell(\theta; x)\,p(x)\,dx $$

A mini-batch of size $B$ drawn i.i.d. from $p$ gives:

$$ \hat{R}_B(\theta) = \frac{1}{B}\sum_{i=1}^{B}\ell(\theta; x_i) $$

This is **exactly the Section 2 construction** — a finite average approximating a continuous one — with two properties that make SGD viable:

* **Unbiased:** $\mathbb{E}[\hat{R}_B] = R$, so the gradient estimate points the right way *on average*.
* **Variance $\propto \frac{1}{B}$:** noise shrinks as $\sqrt{B}$, which is why batch size trades compute against gradient quality.

> The entire practice of stochastic optimization rests on the claim that a finite sample average converges to an integral — the claim this chapter proves.

---

### 8. Check Your Understanding

**Q1: Find the average value of $f(x) = x^2$ over $[0, 3]$, and find the point $c$ where $f(c)$ equals that average.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Antiderivative:** $F(x) = \dfrac{x^3}{3}$
2. **Step 2 — Definite integral:**
   $$ \int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = 9 - 0 = 9 $$
3. **Step 3 — Divide by the interval length:**
   $$ \bar{f} = \frac{1}{3 - 0}\cdot 9 = 3 $$
4. **Step 4 — Solve $f(c) = 3$:**
   $$ c^2 = 3 \;\Longrightarrow\; c = \sqrt{3} \approx 1.732 $$
   (We take the positive root since $c$ must lie in $[0,3]$.)

* **Result:** $\bar{f} = 3$, attained at $c = \sqrt{3}$.

**Note where $c$ sits:** at $1.73$, not at the midpoint $1.5$. Because $x^2$ grows faster on the right half of the interval, the average height is reached later than the midpoint. This is the Mean Value Theorem for Integrals in action.
</details>

**Q2: Show that the average value of $f$ over $[a,b]$ equals the secant slope of any antiderivative $F$, and explain why the choice of antiderivative does not matter.**
<details>
<summary><b>Reveal Answer &amp; Proof</b></summary>

**Step 1 — Start from the average value formula:**
$$ \bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx $$

**Step 2 — Apply the Fundamental Theorem** with any antiderivative $F$ (so $F' = f$):
$$ \int_a^b f(x)\,dx = F(b) - F(a) $$

**Step 3 — Substitute:**
$$ \bar{f} = \frac{F(b) - F(a)}{b - a} $$
which is precisely $\frac{\text{rise}}{\text{run}}$ for the secant line through $\big(a, F(a)\big)$ and $\big(b, F(b)\big)$. ∎

**Why the choice of $F$ is irrelevant:** any two antiderivatives of $f$ differ by a constant, $G(x) = F(x) + C$. Then:
$$ \frac{G(b) - G(a)}{b-a} = \frac{\big(F(b)+C\big) - \big(F(a)+C\big)}{b-a} = \frac{F(b)-F(a)}{b-a} $$
The constant cancels. **Geometrically:** adding $C$ shifts the whole graph of $F$ vertically, which moves both endpoints by the same amount and therefore leaves every secant slope unchanged.
</details>

**Q3: A model's training loss over 100 epochs is $L(t) = 2e^{-t/20} + 0.1$. What is its average loss over the full run, and how does that compare to the final loss? What does the gap tell you?**
<details>
<summary><b>Reveal Answer &amp; Analysis</b></summary>

1. **Step 1 — Set up the average:**
   $$ \bar{L} = \frac{1}{100}\int_0^{100}\left(2e^{-t/20} + 0.1\right)dt $$
2. **Step 2 — Antiderivative** (recall $\int e^{ct}dt = \frac{e^{ct}}{c}$, here $c = -\frac{1}{20}$):
   $$ F(t) = 2 \cdot \frac{e^{-t/20}}{-1/20} + 0.1t = -40e^{-t/20} + 0.1t $$
3. **Step 3 — Evaluate:**
   $$ F(100) = -40e^{-5} + 10 \approx -40(0.006738) + 10 \approx 9.7305 $$
   $$ F(0) = -40(1) + 0 = -40 $$
   $$ \int_0^{100} = 9.7305 - (-40) = 49.7305 $$
4. **Step 4 — Divide:**
   $$ \bar{L} = \frac{49.7305}{100} \approx 0.497 $$
5. **Step 5 — Compare with the final loss:**
   $$ L(100) = 2e^{-5} + 0.1 \approx 0.1135 $$

* **Result:** average loss $\approx 0.497$; final loss $\approx 0.114$. The average is roughly **4.4 times** the final value.

**What the gap means:**

* Most of the "area under the loss curve" was accumulated **early**, during the steep initial descent. The model spent the bulk of its training already near its final performance.
* The time constant is $20$ epochs ($\frac{1}{20}$ in the exponent): after about $3$ time constants — 60 epochs — the model is within 5% of its floor. **Epochs 60–100 contributed almost nothing.** This is exactly the signal early stopping looks for.
* The asymptote $0.1$ is the **irreducible loss** — label noise or model-capacity limits. No amount of further training removes it.
* A large average-to-final ratio is characteristic of healthy, fast convergence. A ratio near $1$ would mean the loss barely moved — either the learning rate is far too small or the model is not learning at all.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 9 — What does area have to do with slope?](https://www.youtube.com/watch?v=FnJqaIESC2s)
* **Lesson page:** [3blue1brown.com — What does area have to do with slope?](https://www.3blue1brown.com/lessons/area-and-slope)

---

[⏮️ **Previous: Chapter 08 — Integration & the Fundamental Theorem**](08-integration-fundamental-theorem.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 10 — Higher Order Derivatives** ⏭️](10-higher-order-derivatives.md)
