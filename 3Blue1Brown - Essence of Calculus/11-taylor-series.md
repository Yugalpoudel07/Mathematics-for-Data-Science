[⏮️ **Previous: Chapter 10 — Higher Order Derivatives**](10-higher-order-derivatives.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 12 — What They Won't Teach You in Calculus** ⏭️](12-what-they-wont-teach-you.md)

---

# Chapter 11: Taylor Series

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Polynomials are the only functions we can really compute — addition and multiplication is all a machine can do. $\cos(x)$, $e^x$, and $\ln(x)$ are none of those things. **Taylor series** bridge the gap: they translate any smooth function into a polynomial by **matching every derivative at a single point**. Know the value, slope, curvature, rate-of-change-of-curvature, and so on at one location, and you can reconstruct the function near that location. The factorials that appear are not decoration — they are exactly the bookkeeping needed to make each derivative come out right.

---

### 1. Why Polynomials?

| Property | Why it matters |
| :--- | :--- |
| **Easy to evaluate** | Only addition and multiplication — a CPU's native operations |
| **Easy to differentiate** | The power rule, term by term |
| **Easy to integrate** | Reverse the power rule, term by term |
| **Easy to add and multiply** | The family is closed under both |

Compare with $\cos(x)$. What *is* $\cos(1.3)$? There is no finite arithmetic recipe. Your calculator does not "know" cosine — **it evaluates a polynomial approximation**.

```text
   The strategy:

     hard function                        easy polynomial
        cos(x)         ---approximate-->   1 - x^2/2 + x^4/24 - ...
     (transcendental)                      (pure arithmetic)
```

---

### 2. Building the Approximation, One Derivative at a Time

**Goal:** approximate $\cos(x)$ near $x = 0$ with a polynomial $P(x) = c_0 + c_1x + c_2x^2 + \cdots$

**The strategy:** force $P$ to agree with $\cos$ in as many derivatives as possible **at the single point $x=0$**.

#### Order 0 — Match the value

$$ P(0) = \cos(0) = 1 \;\Longrightarrow\; c_0 = 1 $$

```text
     cos(x)                        P(x) = 1
       ^                             ^
     1 +---___                     1 +---------------
       |      \___                   |
     0 +----------\______> x       0 +---------------> x

   Agrees at x=0. Terrible everywhere else.
```

#### Order 1 — Match the slope

$$ P'(x) = c_1 + 2c_2x + \cdots \;\Longrightarrow\; P'(0) = c_1 $$
Since $\frac{d}{dx}\cos(x) = -\sin(x)$ and $-\sin(0) = 0$:
$$ c_1 = 0 $$

#### Order 2 — Match the curvature

$$ P''(x) = 2c_2 + 6c_3x + \cdots \;\Longrightarrow\; P''(0) = 2c_2 $$
Since $\frac{d^2}{dx^2}\cos(x) = -\cos(x)$ and $-\cos(0) = -1$:
$$ 2c_2 = -1 \;\Longrightarrow\; c_2 = -\frac{1}{2} $$

$$ P(x) = 1 - \frac{x^2}{2} $$

```text
   The quadratic approximation:

       ^
     1 +---*---
       |  / \                    Now the parabola HUGS the cosine
       | /   \                   curve near zero — same height,
     0 +/-----\-------> x        same slope, same curvature.
       |       \
       |        \    <- but it diverges further out
```

#### Order 4 — Keep going

$$ P^{(4)}(0) = 24c_4 = \cos(0) = 1 \;\Longrightarrow\; c_4 = \frac{1}{24} $$

$$ P(x) = 1 - \frac{x^2}{2} + \frac{x^4}{24} $$

```text
   Successive approximations to cos(x):

       ^
     1 +####
       |    ###                   ---- cos(x)         (true)
       |       ##                 .... 1 - x^2/2      (order 2)
     0 +---------##-------> x     ____ 1 - x^2/2 + x^4/24 (order 4)
       |           ##
       |             ###

   Each new term extends the region where the polynomial
   is indistinguishable from the real thing.
```

---

### 3. Where the Factorials Come From

This is the step that makes the whole formula click.

**The problem:** differentiating $c_n x^n$ repeatedly generates a pile of constants.

```text
   Differentiating x^4 four times:

      x^4
       |  d/dx
       v
      4x^3
       |  d/dx
       v
      12x^2        =  4 * 3 * x^2
       |  d/dx
       v
      24x          =  4 * 3 * 2 * x
       |  d/dx
       v
      24           =  4 * 3 * 2 * 1  =  4!    <- a pure number

   So the n-th derivative of c_n x^n, evaluated at 0, is  c_n * n!
```

**The fix:** to make the $n$-th derivative of the polynomial come out to exactly $f^{(n)}(a)$, **divide by $n!$**:

$$ c_n = \frac{f^{(n)}(a)}{n!} $$

> **Why every other term dies at $x=0$:** taking the $n$-th derivative kills all terms of degree $< n$ (they differentiate to zero), and every term of degree $> n$ still carries a factor of $x$, which vanishes at $x=0$. Only the $n$-th term survives — cleanly isolated. **This is why Taylor coefficients can be read off one at a time.**

---

### 4. The Taylor Series Formula

$$ \boxed{\; f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n \;} $$

Written out:

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots $$

**When $a = 0$** this is called a **Maclaurin series**:

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots $$

#### What Each Term Contributes

```text
   Progressive refinement of the local picture:

   term 0:  f(a)                 pins the HEIGHT
   term 1:  f'(a)(x-a)           pins the TILT
   term 2:  f''(a)/2 (x-a)^2     pins the CURVATURE
   term 3:  f'''(a)/6 (x-a)^3    pins the ASYMMETRY of the curvature
   term n:  ...                  pins the n-th order wiggle

   Each term corrects the error left by all the previous ones.
```

---

### 5. The Essential Series

| Function | Taylor series about $0$ | Converges for |
| :--- | :--- | :--- |
| $e^x$ | $\displaystyle 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=0}^\infty \frac{x^n}{n!}$ | All $x$ |
| $\sin x$ | $\displaystyle x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | All $x$ |
| $\cos x$ | $\displaystyle 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | All $x$ |
| $\dfrac{1}{1-x}$ | $\displaystyle 1 + x + x^2 + x^3 + \cdots$ | $\lvert x\rvert < 1$ |
| $\ln(1+x)$ | $\displaystyle x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ | $-1 < x \le 1$ |
| $(1+x)^\alpha$ | $\displaystyle 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \cdots$ | $\lvert x\rvert < 1$ |

#### Structural Observations Worth Noticing

* $e^x$ contains **every** power — it is the "densest" of the elementary series, and its $\frac{1}{n!}$ coefficients are why it converges everywhere.
* $\sin$ has only **odd** powers (it is an odd function); $\cos$ has only **even** powers (it is even). The series *knows* the symmetry.
* Differentiating the $\sin$ series term by term produces the $\cos$ series exactly. The series respect calculus.
* Setting $x = i\theta$ in the $e^x$ series and separating real from imaginary parts produces **Euler's formula**:
  $$ e^{i\theta} = \cos\theta + i\sin\theta $$
  The three most important series in mathematics turn out to be one series.

---

### 6. Convergence and the Radius of Convergence

A crucial caveat: **a Taylor series does not always equal the function it came from.**

```text
   The geometric series 1/(1-x) = 1 + x + x^2 + ...

   At x = 0.5:   1 + 0.5 + 0.25 + 0.125 + ...  =  2        = 1/(1-0.5)  OK
   At x = 2:     1 + 2 + 4 + 8 + 16 + ...      =  infinity
                 but 1/(1-2) = -1               <- the series LIES

   The series is only valid inside |x| < 1.
```

> **Radius of convergence $R$:** the series converges for $|x - a| < R$ and diverges for $|x-a| > R$.

```text
   The convergence disc:

      ----------(=================)---------- x
              a-R        a       a+R

      diverges  |   converges    |  diverges
```

| Function | $R$ about $0$ | Why |
| :--- | :---: | :--- |
| $e^x$, $\sin x$, $\cos x$ | $\infty$ | Factorials crush the growth of $x^n$ |
| $\frac{1}{1-x}$ | $1$ | There is a pole at $x=1$ |
| $\ln(1+x)$ | $1$ | Singularity at $x=-1$ |
| $\frac{1}{1+x^2}$ | $1$ | Surprising! No real singularity — but there are **complex** poles at $\pm i$ |

> **The beautiful subtlety:** $\frac{1}{1+x^2}$ is perfectly smooth for all real $x$, yet its Taylor series breaks down beyond $|x| = 1$. The reason is invisible on the real line: the function has poles at $x = \pm i$ in the complex plane, exactly distance $1$ from the origin. **The radius of convergence is the distance to the nearest singularity in the complex plane** — a fact that explains real-valued behaviour only by leaving the real numbers.

---

### 7. The Practical Payoff: Truncation and Error

In practice we use a **Taylor polynomial** — a truncation — plus an error bound.

$$ f(x) = \underbrace{\sum_{n=0}^{N}\frac{f^{(n)}(a)}{n!}(x-a)^n}_{\text{Taylor polynomial}} + \underbrace{R_N(x)}_{\text{remainder}} $$

**Lagrange form of the remainder:**
$$ R_N(x) = \frac{f^{(N+1)}(\xi)}{(N+1)!}(x-a)^{N+1} \quad \text{for some } \xi \text{ between } a \text{ and } x $$

**Two things shrink the error:**

1. **$(x-a)^{N+1}$** — the approximation is excellent **near $a$** and degrades as you move away.
2. **$(N+1)!$** — factorial growth in the denominator makes extra terms extremely effective.

#### The Small-Angle Approximation

The most used truncation in all of physics and engineering:

$$ \sin(\theta) \approx \theta \qquad \text{for small } \theta $$

**Error bound:** the next nonzero term is $\frac{\theta^3}{6}$.

| $\theta$ | $\sin\theta$ | $\theta$ | Relative error |
| :---: | :---: | :---: | :---: |
| $0.1$ | $0.099833$ | $0.1$ | $0.17\%$ |
| $0.5$ | $0.479426$ | $0.5$ | $4.3\%$ |
| $1.0$ | $0.841471$ | $1.0$ | $18.8\%$ |

This single approximation is what makes the pendulum equation solvable, and it is the reason clocks worked for three centuries.

---

### 8. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **First-order Taylor expansion** | The justification for gradient descent | $L(\theta + \Delta) \approx L(\theta) + \nabla L^T\Delta$ — stepping against $\nabla L$ decreases the linear model of the loss |
| **Second-order expansion** | Newton's method and trust regions | $L(\theta+\Delta) \approx L + \nabla L^T\Delta + \frac{1}{2}\Delta^T H\Delta$; minimizing gives $\Delta = -H^{-1}\nabla L$ |
| **Truncation error $O(\|\Delta\|^2)$** | Why the learning rate must be bounded | Large steps exit the region where the expansion is valid — the mathematical reason for divergence |
| **Series for $e^x$** | Numerically stable softmax | Overflow is avoided by subtracting the max logit; series reasoning explains the conditioning |
| **$\ln(1+x) \approx x$** | Stable log-probability arithmetic | `log1p` / `expm1`; used throughout likelihood computation and in `log(1+exp(z))` softplus |
| **Local polynomial approximation** | Surrogate and response-surface models | Bayesian optimization fits local quadratics; LIME explains a black box with a local linear model |
| **Taylor expansion of the network itself** | Neural Tangent Kernel theory | An infinitely wide network's training dynamics are governed by its first-order expansion around initialization |
| **Padé / series acceleration** | Efficient activation and attention kernels | Polynomial approximations to GELU, exp, and softmax in quantized and low-precision inference |

#### Every Optimizer Is a Taylor Expansion Choice

```text
   How much of the expansion do you keep?

   L(theta + d)  =  L  +  grad^T d  +  (1/2) d^T H d  +  ...
                    |       |              |
                    |       |              |
                  order 0  order 1      order 2

   SGD             : keep through order 1, fixed step
   Momentum        : order 1, with a smoothed gradient estimate
   Adam / RMSProp  : order 1, plus a DIAGONAL estimate of order 2
   L-BFGS          : order 1, plus a LOW-RANK estimate of order 2
   Newton          : full order 2, exactly
```

> **The unifying view:** every optimizer builds a local polynomial model of the loss, minimizes that model, and takes the resulting step. They differ only in **how much of the Taylor expansion they can afford to compute.**

---

### 9. Check Your Understanding

**Q1: Find the Taylor series of $f(x) = e^{x}$ about $a = 0$, and use the first four terms to estimate $e^{0.5}$.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Compute the derivatives.** Every derivative of $e^x$ is $e^x$, so:
   $$ f^{(n)}(0) = e^0 = 1 \quad \text{for all } n $$
2. **Step 2 — Apply the formula $c_n = \frac{f^{(n)}(0)}{n!}$:**
   $$ c_n = \frac{1}{n!} $$
3. **Step 3 — Write the series:**
   $$ e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots $$
4. **Step 4 — Estimate $e^{0.5}$ with four terms:**
   $$ 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.020833 = 1.645833 $$

* **True value:** $e^{0.5} = 1.648721\ldots$
* **Error:** $0.0029$, about $0.18\%$.

**Error check against the remainder bound:** the next term is $\frac{0.5^4}{24} = \frac{0.0625}{24} \approx 0.0026$ — matching the observed error almost exactly. For a series with rapidly shrinking terms, **the first omitted term is an excellent error estimate.**
</details>

**Q2: Derive the second-order Taylor expansion of a loss $L(\theta)$ and show that Newton's method minimizes it exactly.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

1. **Step 1 — Expand to second order** about the current point $\theta$, with step $\Delta$:
   $$ L(\theta + \Delta) \approx L(\theta) + \nabla L(\theta)^T\Delta + \frac{1}{2}\Delta^T H \Delta $$
   where $H = \nabla^2 L(\theta)$ is the Hessian (Chapter 10).
2. **Step 2 — Treat the right-hand side as a quadratic in $\Delta$ and minimize it.** Differentiate with respect to $\Delta$ and set to zero:
   $$ \nabla_\Delta\left[\nabla L^T\Delta + \tfrac{1}{2}\Delta^T H\Delta\right] = \nabla L + H\Delta = 0 $$
3. **Step 3 — Solve:**
   $$ \Delta = -H^{-1}\nabla L $$
4. **Step 4 — The update rule:**
   $$ \boxed{\theta_{t+1} = \theta_t - H^{-1}\nabla L(\theta_t)} $$

**Why Newton's method converges so fast:** if $L$ is *exactly* quadratic, the second-order model is exact and Newton's method lands on the minimum **in one step**. Near a minimum, any smooth loss is approximately quadratic, which gives **quadratic convergence** — the number of correct digits roughly doubles per iteration.

**Why it is nonetheless impractical at scale:**

* Forming $H$ costs $O(n^2)$ memory; inverting it costs $O(n^3)$ time. For $n = 10^9$, both are impossible.
* $H$ must be **positive definite** for the step to point downhill. Near a saddle it is not, and Newton's method can step *toward* the saddle.
* Fixes: trust regions, damping ($H + \lambda I$), Gauss-Newton ($J^TJ$, always PSD), or quasi-Newton approximations (L-BFGS).

**The connection to Chapter 10's Q2:** in one dimension, $H = \lambda$ and the Newton step is $\eta = \frac{1}{\lambda}$ — which we showed converges in exactly one iteration. Newton's method is "gradient descent with the perfect per-direction learning rate."
</details>

**Q3: The softmax function $\sigma(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$ overflows for large logits. Explain the problem and the standard fix, using series reasoning.**
<details>
<summary><b>Reveal Answer &amp; Analysis</b></summary>

**The problem.** In `float32`, the maximum representable value is about $3.4 \times 10^{38}$. Since $e^{89} \approx 4.5\times 10^{38}$, any logit above roughly $88$ produces `inf`. The subsequent division gives `inf/inf` = `nan`, and the `nan` propagates through the entire backward pass, destroying the run.

**The fix — subtract the maximum logit.** Let $m = \max_j z_j$ and note the exact identity:
$$ \frac{e^{z_i}}{\sum_j e^{z_j}} = \frac{e^{z_i - m}\,e^{m}}{e^{m}\sum_j e^{z_j - m}} = \frac{e^{z_i - m}}{\sum_j e^{z_j - m}} $$

The factor $e^m$ cancels **exactly** — this is algebra, not approximation, so the result is mathematically identical.

**Why it is numerically safe:** every shifted logit satisfies $z_i - m \le 0$, so every exponential lies in $(0, 1]$. The largest term is exactly $1$. No overflow is possible.

**What about underflow?** Very negative shifted logits give $e^{z_i - m} \approx 0$. This is **benign** — those classes genuinely have negligible probability, and rounding them to zero loses nothing that matters.

**The series connection.** The companion function is the **log-sum-exp**:
$$ \log\sum_j e^{z_j} = m + \log\sum_j e^{z_j - m} $$
Combined with $\log(1+x) \approx x - \frac{x^2}{2} + \cdots$ for small $x$ (the Taylor series from Section 5), this is what `log1p` exploits: computing $\log(1+x)$ directly loses precision when $x$ is tiny, because $1+x$ rounds to $1$. Evaluating the series instead preserves every significant digit.

**The same reasoning appears in:**

* `softplus(z)` $= \log(1+e^z)$, computed as $\max(z,0) + \log(1+e^{-|z|})$.
* `logsumexp` in every probabilistic library.
* Log-likelihood accumulation, where products of thousands of small probabilities would underflow to zero.

**The general principle:** numerical stability is achieved by rewriting a formula into a mathematically equivalent form whose intermediate values stay in a well-conditioned range — and Taylor series are the tool for knowing when a direct evaluation is losing precision.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 11 — Taylor series](https://www.youtube.com/watch?v=3d6DsjIBzJ4)
* **Lesson page:** [3blue1brown.com — Taylor series](https://www.3blue1brown.com/lessons/taylor-series)

---

[⏮️ **Previous: Chapter 10 — Higher Order Derivatives**](10-higher-order-derivatives.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 12 — What They Won't Teach You in Calculus** ⏭️](12-what-they-wont-teach-you.md)
