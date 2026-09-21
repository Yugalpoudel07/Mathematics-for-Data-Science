[⏮️ **Previous: Chapter 07 — Limits, L'Hôpital's Rule & Epsilon-Delta**](07-limits.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 09 — What Does Area Have to Do With Slope?** ⏭️](09-area-and-slope.md)

---

# Chapter 08: Integration and the Fundamental Theorem of Calculus

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Integration is what you reach for whenever a quantity is built from **many tiny contributions**, each of the form $f(x)\,dx$. Adding infinitely many infinitesimal pieces sounds impossible — and computing it directly *is* impossible. The **Fundamental Theorem of Calculus** provides the escape: instead of summing, ask *"which function has $f$ as its derivative?"* Evaluate that antiderivative at the two endpoints, subtract, and you are done. A hopeless infinite sum collapses into one subtraction.

---

### 1. The Motivating Problem: Distance From Velocity

A car's velocity is $v(t) = t(8 - t)$ over the interval $0 \le t \le 8$. **How far does it travel?**

```text
   Velocity over time:

    v(t)
     ^
  16 +          ____
     |       _/      \_
     |     /            \
     |   /                \
     | /                    \
   0 +-+--------------------+---> t
     0                      8

   If velocity were CONSTANT, distance = v * t.  Easy.
   But velocity changes every instant. What now?
```

#### The Slicing Strategy

Chop the 8 seconds into tiny intervals of width $dt$. Over one such interval, the velocity is **approximately constant**:

$$ \text{distance in one interval} \approx v(t)\,dt $$

```text
   Approximating with rectangles:

    v(t)
     ^
     |          ____
     |       _/|||||\_
     |     / ||||||||| \
     |   /  |||||||||||  \
     | /   ||||||||||||||  \
   0 +-+---+-+-+-+-+-+-+---+---> t
     0    |dt|               8

   Each rectangle:  height v(t), width dt, area = v(t) dt
   Total distance  ~=  sum of all rectangle areas
                    =  AREA UNDER THE VELOCITY CURVE
```

$$ \text{Total distance} = \lim_{dt\to 0}\sum v(t)\,dt = \int_{0}^{8} v(t)\,dt $$

> **The general principle:** whenever a quantity is a sum of many products $f(x)\,dx$, it is the area under the graph of $f$.

---

### 2. Notation and the Riemann Sum

$$ \int_{a}^{b} f(x)\,dx $$

| Symbol | Meaning |
| :--- | :--- |
| $\int$ | Elongated "S" — a **sum** |
| $a$, $b$ | Lower and upper **bounds** of integration |
| $f(x)$ | **Height** of each sliver |
| $dx$ | **Width** of each sliver |

The rigorous underpinning is the **Riemann sum**:

$$ \int_a^b f(x)\,dx = \lim_{n \to \infty}\sum_{i=1}^{n} f(x_i)\,\Delta x, \qquad \Delta x = \frac{b-a}{n} $$

```text
   More rectangles -> better approximation:

    n = 4                n = 8                n -> infinity
      ___                  ___                    ___
    _|   |_              _|___|_                _/   \_
   |  |  | |            |||||||||              /       \
   |__|__|_|            |||||||||             /_________\

   crude                 better               exact
```

#### Signed Area

Below the axis, $f(x) < 0$, so the "area" contributes **negatively**.

```text
    f(x)
     ^
     |    ___
     |  /  +  \                  + counts positively
   0 +-/-------\-----/---> x
     |          \ - /            - counts negatively
     |           \_/

   The integral is the NET signed area.
```

For the car, negative velocity means reversing — and the integral correctly reports **net displacement**, not total distance travelled.

---

### 3. The Central Question

Summing infinitely many terms is not something you can do by hand. So we reframe:

> **Instead of computing the sum directly, study how the running total grows.**

Define the **area function** $A(T)$ = area under $f$ from the fixed start $a$ up to a variable endpoint $T$:

$$ A(T) = \int_{a}^{T} f(x)\,dx $$

```text
   The area accumulated so far:

    f(x)
     ^
     |     ______
     |   /|||||||| \
     | / ||||||||||  \
   0 +---+++++++++-----+---> x
     a   [ A(T) ]  T

   As T slides right, A(T) grows.
   QUESTION: at what RATE does it grow?
```

---

### 4. The Fundamental Theorem, Derived

Nudge the endpoint from $T$ to $T + dT$. The extra area is a thin sliver:

```text
   The sliver gained:

    f(x)
     ^
     |          |#|   <- new sliver
     |    ______|#|
     |  /       |#|
     |/         |#|
   0 +----------+-+---> x
     a          T |
                 T+dT

   The sliver is (very nearly) a rectangle:
       height = f(T)
       width  = dT
       area   = f(T) dT
```

$$ dA \approx f(T)\,dT $$

The error is the small curved wedge on top, of order $(dT)^2$ — negligible (the Chapter 01 argument, again). Dividing:

$$ \boxed{\; \frac{dA}{dT} = f(T) \;}$$

> **The Fundamental Theorem of Calculus, Part 1:** the derivative of the area function **is the original function**.

$$ \frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x) $$

#### The Practical Consequence (Part 2)

Turn it around. To find the area, look for a function $F$ whose derivative is $f$ — an **antiderivative**:

$$ F'(x) = f(x) $$

Then:

$$ \boxed{\; \int_a^b f(x)\,dx = F(b) - F(a) \;} $$

```text
   Why the subtraction works:

   F(x) tracks the total accumulated from some reference point.

        F(b) = everything accumulated up to b
      - F(a) = everything accumulated up to a
      --------
       F(b) - F(a) = exactly what accumulated BETWEEN a and b

   Whatever arbitrary starting offset F carries cancels out.
```

This is why the constant $+C$ in the indefinite integral does not matter for definite integrals — it appears in both terms and subtracts away.

---

### 5. Worked Example: The Car

$$ \int_0^8 t(8-t)\,dt = \int_0^8 \left(8t - t^2\right)dt $$

**Step 1 — Find an antiderivative.** Reverse the power rule ($\frac{d}{dt}t^n = nt^{n-1}$ means going backwards adds one to the exponent and divides by it):
$$ F(t) = 4t^2 - \frac{t^3}{3} $$

**Verify:** $F'(t) = 8t - t^2$ ✓

**Step 2 — Evaluate at the bounds.**
$$ F(8) = 4(64) - \frac{512}{3} = 256 - \frac{512}{3} = \frac{768 - 512}{3} = \frac{256}{3} $$
$$ F(0) = 0 $$

**Step 3 — Subtract.**
$$ \int_0^8 t(8-t)\,dt = \frac{256}{3} - 0 = \frac{256}{3} \approx 85.33 $$

The car travels about $85.33$ metres.

> **Pause on what just happened.** An infinite sum of infinitesimal products was replaced by: *guess a function, differentiate it to check, plug in two numbers, subtract.* This is the single most consequential labour-saving device in mathematics.

---

### 6. Antiderivatives and the $+C$

Because the derivative of a constant is zero, antiderivatives are never unique:

$$ \frac{d}{dx}\left(x^2\right) = 2x \qquad \frac{d}{dx}\left(x^2 + 7\right) = 2x \qquad \frac{d}{dx}\left(x^2 - 100\right) = 2x $$

```text
   A family of curves, all with identical slopes:

      y
      ^        /   /   /
      |      /   /   /      x^2 + 7
      |    /   /   /        x^2
      |  /   /   /          x^2 - 5
      +---------------> x

   Vertical shifts change nothing about slope.
```

$$ \int f(x)\,dx = F(x) + C \qquad \text{(indefinite integral)} $$

| | Definite integral | Indefinite integral |
| :--- | :--- | :--- |
| **Notation** | $\int_a^b f(x)dx$ | $\int f(x)dx$ |
| **Result** | A **number** | A **family of functions** |
| **Meaning** | Net signed area over $[a,b]$ | All antiderivatives of $f$ |
| **$+C$?** | Cancels in the subtraction | Must be written |

---

### 7. Common Antiderivatives (The Derivative Table, Reversed)

| $f(x)$ | $\int f(x)\,dx$ | Check by differentiating |
| :--- | :--- | :--- |
| $x^n$ ($n \neq -1$) | $\dfrac{x^{n+1}}{n+1} + C$ | $\frac{(n+1)x^n}{n+1} = x^n$ ✓ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert + C$ | $\frac{1}{x}$ ✓ (the case the power rule misses) |
| $e^x$ | $e^x + C$ | $e^x$ ✓ |
| $e^{cx}$ | $\dfrac{e^{cx}}{c} + C$ | $e^{cx}$ ✓ |
| $\cos x$ | $\sin x + C$ | $\cos x$ ✓ |
| $\sin x$ | $-\cos x + C$ | $\sin x$ ✓ |
| $\dfrac{1}{1+x^2}$ | $\arctan x + C$ | ✓ |

> **A sobering fact:** differentiation is **mechanical** — any elementary function can be differentiated by rules. Integration is **not**. Many perfectly innocent functions have no elementary antiderivative at all. The most famous:
> $$ \int e^{-x^2}\,dx $$
> This is the Gaussian — the heart of the normal distribution. No combination of polynomials, exponentials, logarithms, or trig functions gives it. Statisticians define $\text{erf}(x)$ precisely to name this missing antiderivative, and normal-distribution tables exist because the integral must be evaluated **numerically**.

---

### 8. The Average Value of a Function

A natural companion question: what is the **average** of a function over an interval?

Averaging finitely many values means summing and dividing by the count. For a continuum, sum with an integral and divide by the *length*:

$$ \boxed{\; \bar{f} = \frac{1}{b-a}\int_a^b f(x)\,dx \;} $$

```text
   The average value, visually:

    f(x)
     ^
     |     ___
     |   /     \
  fbar+--/-------\----+       The horizontal line at fbar
     | /         \    |       encloses the SAME AREA as
     |/           \___|       the curve does.
   0 +----------------+--> x
     a                b

   Area of rectangle (b-a) * fbar  =  Area under curve
```

For the car: $\bar{v} = \frac{1}{8}\cdot\frac{256}{3} = \frac{32}{3} \approx 10.67$ m/s — the constant speed that would cover the same distance in the same time.

---

### 9. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Integral as accumulated total** | Expected values over continuous distributions | $\mathbb{E}[X] = \int x\,p(x)\,dx$; expected risk $\int \ell\,p\,dx$ |
| **Riemann sums** | Why mini-batch training is a valid estimator | A batch average is a Monte Carlo estimate of the population integral |
| **Fundamental Theorem** | CDF and PDF are derivative/integral partners | $F(x) = \int_{-\infty}^x p(t)dt$; inverse-transform sampling inverts $F$ |
| **Signed area** | Evaluation metrics as integrals | ROC-AUC $= \int_0^1 \text{TPR}\,d(\text{FPR})$; Average Precision |
| **Average value of a function** | The definition of every loss you minimize | $L = \frac{1}{N}\sum_i \ell_i \to \mathbb{E}_{p}[\ell]$ as $N \to \infty$ |
| **Non-elementary integrals** | Why numerical and variational methods dominate | The Gaussian CDF, partition functions $Z = \int e^{-E(x)}dx$, Bayesian evidence $\int p(D\vert\theta)p(\theta)d\theta$ |
| **Antiderivative families ($+C$)** | Energy-based and score-based models | A score function $\nabla_x \log p(x)$ determines $p$ only up to a normalizing constant — the same ambiguity |

#### Where Integration Really Bites: Intractable Posteriors

Bayesian inference needs the evidence:

$$ p(D) = \int p(D\mid\theta)\,p(\theta)\,d\theta $$

In high dimensions this integral is analytically hopeless and numerically exponential. The entire fields of **variational inference** (replace the integral with an optimization problem) and **MCMC** (replace it with sampling) exist because of this single unsolvable integral.

| Approach | Strategy |
| :--- | :--- |
| **Monte Carlo** | $\int f p\,dx \approx \frac{1}{N}\sum f(x_i)$, $x_i \sim p$ — a randomized Riemann sum |
| **Variational inference** | Optimize a lower bound (ELBO) instead of integrating |
| **Normalizing flows** | Engineer the density so the integral is tractable by construction |
| **Quadrature** | Deterministic weighted sums — exact for low dimensions, useless above ~10 |

---

### 10. Check Your Understanding

**Q1: Evaluate $\displaystyle\int_1^3 \left(x^2 - 2x + 1\right)dx$.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Find an antiderivative term by term:**
   $$ F(x) = \frac{x^3}{3} - x^2 + x $$
   **Verify:** $F'(x) = x^2 - 2x + 1$ ✓
2. **Step 2 — Evaluate at the upper bound:**
   $$ F(3) = \frac{27}{3} - 9 + 3 = 9 - 9 + 3 = 3 $$
3. **Step 3 — Evaluate at the lower bound:**
   $$ F(1) = \frac{1}{3} - 1 + 1 = \frac{1}{3} $$
4. **Step 4 — Subtract:**
   $$ \int_1^3 = 3 - \frac{1}{3} = \frac{8}{3} \approx 2.667 $$

**Sanity check:** the integrand is $(x-1)^2 \ge 0$, so the answer must be positive — and it is. Over $[1,3]$ the function rises from $0$ to $4$, so a value between $0$ and $2\times 4 = 8$ is plausible. ✓
</details>

**Q2: Find the average value of $f(x) = \sin(x)$ over $[0, \pi]$, and explain why the answer over $[0, 2\pi]$ is different.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

**Over $[0, \pi]$:**

1. **Antiderivative:** $F(x) = -\cos(x)$
2. **Definite integral:**
   $$ \int_0^\pi \sin x\,dx = \left[-\cos x\right]_0^\pi = -\cos(\pi) + \cos(0) = 1 + 1 = 2 $$
3. **Divide by the interval length:**
   $$ \bar{f} = \frac{1}{\pi - 0}\cdot 2 = \frac{2}{\pi} \approx 0.6366 $$

**Over $[0, 2\pi]$:**
$$ \int_0^{2\pi}\sin x\,dx = \left[-\cos x\right]_0^{2\pi} = -1 + 1 = 0 \;\Longrightarrow\; \bar{f} = 0 $$

**Why the difference:** over $[0,\pi]$ the sine curve is entirely **above** the axis, so all contributions are positive. Over $[0,2\pi]$ the second half is entirely **below** the axis, contributing exactly the negative of the first half. The signed areas cancel.

**ML relevance:** this is precisely why a **signed** average (mean gradient) can be near zero while the **magnitude** is large. Optimizers such as Adam track $\mathbb{E}[g]$ and $\mathbb{E}[g^2]$ separately for exactly this reason — the second moment survives cancellation.
</details>

**Q3: Explain why $\int_a^b f(x)\,dx = F(b) - F(a)$, referring to the meaning of the area function.**
<details>
<summary><b>Reveal Answer &amp; Explanation</b></summary>

**Step 1 — Define the accumulation function.** Let $A(x) = \int_a^x f(t)\,dt$ — the area collected from the fixed start $a$ to the sliding endpoint $x$. By FTC Part 1, $A'(x) = f(x)$, so $A$ **is** an antiderivative of $f$. Also, by construction, $A(a) = 0$.

**Step 2 — Relate an arbitrary antiderivative to $A$.** Suppose $F$ is any other antiderivative of $f$. Then $(F - A)' = f - f = 0$, and a function with zero derivative everywhere on an interval is constant. So:
$$ F(x) = A(x) + C \quad\text{for some constant } C $$

**Step 3 — Subtract at the two endpoints.**
$$ F(b) - F(a) = \big(A(b) + C\big) - \big(A(a) + C\big) = A(b) - A(a) $$
The unknown constant $C$ **cancels**.

**Step 4 — Use $A(a) = 0$.**
$$ F(b) - F(a) = A(b) - 0 = A(b) = \int_a^b f(x)\,dx \;\blacksquare $$

**The intuition in one line:** $F$ is an odometer whose zero point was set arbitrarily. To find how far you travelled *between* two moments, read the odometer twice and subtract — whatever offset it started with is irrelevant.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 8 — Integration and the fundamental theorem of calculus](https://www.youtube.com/watch?v=rfG8ce4nNh0)
* **Lesson page:** [3blue1brown.com — Integration and the fundamental theorem of calculus](https://www.3blue1brown.com/lessons/integration)

---

[⏮️ **Previous: Chapter 07 — Limits, L'Hôpital's Rule & Epsilon-Delta**](07-limits.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 09 — What Does Area Have to Do With Slope?** ⏭️](09-area-and-slope.md)
