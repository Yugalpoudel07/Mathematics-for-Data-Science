[⏮️ **Previous: Chapter 09 — What Does Area Have to Do With Slope?**](09-area-and-slope.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 11 — Taylor Series** ⏭️](11-taylor-series.md)

---

# Chapter 10: Higher Order Derivatives

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> If the first derivative is the **slope**, the second derivative is the **rate at which the slope changes** — geometrically, how much the graph **curves**. Positive second derivative means the curve bends upward like a valley; negative means it bends downward like a hill; zero means it is momentarily straight. In physics these are position, velocity, and **acceleration** — and acceleration is what you actually *feel*. In machine learning the second derivative is the **curvature of the loss landscape**, which is precisely what separates a slow optimizer from a fast one.

---

### 1. Derivatives of Derivatives

The derivative $f'(x)$ is itself a function. Nothing stops us from differentiating it again.

$$ f(x) \;\xrightarrow{\;d/dx\;}\; f'(x) \;\xrightarrow{\;d/dx\;}\; f''(x) \;\xrightarrow{\;d/dx\;}\; f'''(x) \;\to\; \cdots $$

#### Notation

| Order | Lagrange | Leibniz | Physics meaning |
| :---: | :--- | :--- | :--- |
| 0 | $f(x)$ | $f$ | Position |
| 1 | $f'(x)$ | $\dfrac{df}{dx}$ | Velocity |
| 2 | $f''(x)$ | $\dfrac{d^2f}{dx^2}$ | Acceleration |
| 3 | $f'''(x)$ | $\dfrac{d^3f}{dx^3}$ | Jerk |
| $n$ | $f^{(n)}(x)$ | $\dfrac{d^nf}{dx^n}$ | — |

> **Why $\frac{d^2 f}{dx^2}$ and not $\frac{d^2f}{d^2x}$?** Read it as $\frac{d}{dx}\left(\frac{df}{dx}\right)$ — the operator $\frac{d}{dx}$ applied twice. The "$2$" upstairs counts applications of $d$; the "$2$" downstairs counts factors of $dx$ in the denominator. The units confirm it: if $f$ is metres and $x$ is seconds, then $f''$ is $\text{m}/\text{s}^2$.

---

### 2. The Geometric Meaning: Curvature

```text
   The second derivative measures BENDING:

   f'' > 0                 f'' = 0                f'' < 0
   (concave up)            (straight)             (concave down)

      \         /             /                    __
       \       /             /                   /    \
        \     /             /                   /      \
         \___/             /                   /        \

   holds water           no bending          spills water
   "valley"                                  "hill"

   slope is INCREASING   slope is CONSTANT   slope is DECREASING
```

The second derivative answers: **"is the slope getting steeper or shallower?"**

| $f'$ | $f''$ | What the curve does |
| :---: | :---: | :--- |
| $+$ | $+$ | Rising, and rising ever faster |
| $+$ | $-$ | Rising, but levelling off |
| $-$ | $+$ | Falling, but flattening out |
| $-$ | $-$ | Falling, and falling ever faster |

An **inflection point** is where $f''$ changes sign — where the curve switches from bending one way to bending the other.

```text
   An inflection point:

      f(x)
       ^                    _____
       |                 __/
       |              __/          <- concave DOWN (f'' < 0)
       |           __/
       |        *                  <- INFLECTION POINT (f'' = 0)
       |     __/
       |   _/                      <- concave UP (f'' > 0)
       | _/
       +--------------------> x
```

---

### 3. The Physical Meaning: Acceleration Is What You Feel

Let $s(t)$ be a car's position.

| Quantity | Symbol | What it is | Can you sense it? |
| :--- | :--- | :--- | :--- |
| Position | $s(t)$ | Where you are | Only by looking out the window |
| Velocity | $s'(t)$ | How fast you are moving | No — a smooth 300 km/h feels like standing still |
| **Acceleration** | $s''(t)$ | How fast velocity changes | **Yes** — this is the push into your seat |
| Jerk | $s'''(t)$ | How fast acceleration changes | Yes — the lurch when brakes grab suddenly |

```text
   Position, velocity, acceleration for a car trip:

   s(t)  |        ______        <- distance, always increasing
         |     __/
         |   _/
         |__/
         +-------------------> t

   v(t)  |     ____             <- speeds up, cruises, slows down
         |   _/    \_
         | _/        \_
         |/            \
         +-------------------> t

   a(t)  |  __                  <- positive while speeding up,
         | |  |                    ZERO while cruising,
         +-+--+----+---+-----> t    negative while braking
         |          |___|
```

> **The everyday insight:** a physics-engine developer, a roller-coaster designer, and an autonomous-vehicle engineer all care more about $s''$ and $s'''$ than about $s$. Comfort is a statement about higher-order derivatives.

---

### 4. Finding Maxima and Minima: The Second Derivative Test

The first derivative finds **candidate** extrema. The second derivative **classifies** them.

```text
   Critical points (f' = 0) come in three flavours:

      MINIMUM              MAXIMUM            SADDLE / INFLECTION
      f'' > 0              f'' < 0                 f'' = 0

        \   /                _____                      __/
         \_/                /     \                  __/
                           /       \               _/

    curve opens up      curve opens down      test is inconclusive
```

> **The Second Derivative Test.** At a point $c$ with $f'(c) = 0$:
> * $f''(c) > 0 \Rightarrow$ **local minimum**
> * $f''(c) < 0 \Rightarrow$ **local maximum**
> * $f''(c) = 0 \Rightarrow$ **inconclusive** — must investigate further

#### Why the Inconclusive Case Is Genuinely Ambiguous

At $x = 0$, all three of these have $f' = f'' = 0$, yet behave completely differently:

| Function | Behaviour at $0$ |
| :--- | :--- |
| $x^4$ | Local **minimum** |
| $-x^4$ | Local **maximum** |
| $x^3$ | Neither — an **inflection point** |

The test fails because the function is *too flat* at that point for second-order information to decide. You must look at $f'''$, $f^{(4)}$, or examine the sign of $f'$ on either side.

#### Worked Example

$$ f(x) = x^3 - 3x^2 + 1 $$

**Step 1 — Find critical points:**
$$ f'(x) = 3x^2 - 6x = 3x(x-2) = 0 \;\Longrightarrow\; x = 0,\; x = 2 $$

**Step 2 — Compute the second derivative:**
$$ f''(x) = 6x - 6 $$

**Step 3 — Classify:**

* $f''(0) = -6 < 0$ → **local maximum** at $x=0$, value $f(0) = 1$
* $f''(2) = 6 > 0$ → **local minimum** at $x=2$, value $f(2) = 8 - 12 + 1 = -3$

**Step 4 — Locate the inflection point:**
$$ f''(x) = 0 \;\Longrightarrow\; x = 1 $$
The curve switches from concave down to concave up at $x = 1$.

```text
   The resulting shape:

      f(x)
        ^
      1 +*                         /
        | \                       /
        |  \                    _/
      0 +---\-----+------------/--------> x
        |0   \     1          /  3
        |     \_        _____/
     -3 +       \______*
        |              2
        max at 0    min at 2,  inflection at 1
```

---

### 5. Why Higher Derivatives Matter: A Preview of Taylor Series

Each derivative order captures a finer feature of a curve's local shape:

```text
   Building up a local picture of a function at a point:

   ORDER 0:  f(a)          "the curve passes through HERE"
                  *

   ORDER 1:  f'(a)         "...and it is TILTED like this"
                  *
                 /

   ORDER 2:  f''(a)        "...and it CURVES like this"
                  *
                 /
                /
               (

   ORDER 3:  f'''(a)       "...and the curvature itself CHANGES like this"
```

The **Taylor polynomial** assembles them all into a single approximation (Chapter 11):

$$ f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots $$

Each additional derivative buys one more order of accuracy near $a$.

| Approximation order | Geometric object | Matches |
| :---: | :--- | :--- |
| 0 | A horizontal line | Value |
| 1 | The tangent line | Value + slope |
| 2 | The osculating parabola | Value + slope + curvature |
| $n$ | Degree-$n$ polynomial | Derivatives up to order $n$ |

---

### 6. Higher Derivatives in Many Variables: The Hessian

For a function of several variables $f(x_1, \ldots, x_n)$, there are many second derivatives — one for each pair of directions. They assemble into a matrix:

$$ H = \nabla^2 f = \begin{bmatrix} \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots \\[8pt] \dfrac{\partial^2 f}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots \\[8pt] \vdots & \vdots & \ddots \end{bmatrix} $$

This is where **Essence of Calculus meets Essence of Linear Algebra**. The Hessian is symmetric (for nice functions), so it has real eigenvalues and orthogonal eigenvectors — and those tell you everything about the local shape:

| Eigenvalues of $H$ | Local shape | Optimization meaning |
| :--- | :--- | :--- |
| All **positive** | Bowl (convex) | Local **minimum** |
| All **negative** | Dome (concave) | Local **maximum** |
| **Mixed signs** | Saddle | Neither — a pass between valleys |
| Some **zero** | Flat direction | Degenerate; plateau |

```text
   The eigenvalue picture (see Essence of Linear Algebra, Ch. 14):

   All positive           Mixed signs            Very different magnitudes
   (bowl)                 (saddle)               (ill-conditioned ravine)

      \       /             \   /                  \_____________/
       \     /               \ /                    \___________/
        \___/                 X                      \_________/
                             / \                   narrow in one direction,
                            /   \                  flat in the other
```

> **The condition number** $\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$ measures how stretched the bowl is. A large $\kappa$ means gradient descent zig-zags across a narrow ravine instead of heading straight for the bottom — the single most common reason training is slow.

---

### 7. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Second derivative = curvature** | The geometry of the loss landscape | Sharp minima vs. flat minima; flat minima generalize better (a widely observed empirical finding) |
| **Hessian matrix** | Second-order optimization | Newton's method: $\theta \leftarrow \theta - H^{-1}\nabla L$ — uses curvature to pick the step size automatically |
| **Eigenvalues of the Hessian** | Diagnosing and setting learning rates | Stability requires $\eta < \frac{2}{\lambda_{\max}}$; convergence speed is governed by $\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$ |
| **Saddle points** | The real obstacle in deep learning | In high dimensions, critical points are overwhelmingly saddles, not local minima — which is why SGD noise helps escape them |
| **Second derivative test** | Verifying convergence | A converged model should sit where $\nabla L \approx 0$ **and** $H \succeq 0$ |
| **Inflection points** | Reading training curves | Where the loss curve stops accelerating downward and begins to plateau |
| **Jerk (third derivative)** | Smooth control and scheduling | Trajectory planning in robotics and self-driving; smooth learning-rate warmup schedules |

#### Why Full Newton's Method Is Rarely Used

For $n$ parameters, the Hessian has $n^2$ entries and inverting it costs $O(n^3)$. With $n = 10^9$ parameters, both are absurd. The practical compromises:

| Method | Approximation to $H$ | Cost |
| :--- | :--- | :--- |
| **L-BFGS** | Low-rank update built from recent gradients | $O(mn)$ for memory $m$ |
| **Adam / RMSProp** | Diagonal only, estimated from $\mathbb{E}[g^2]$ | $O(n)$ |
| **K-FAC** | Kronecker-factored block structure | $O(n^{1.5})$-ish |
| **Gauss-Newton** | $J^TJ$, dropping second-order residual terms | Cheaper, always PSD |
| **Hessian-vector products** | Never form $H$; compute $Hv$ by autodiff | $O(n)$ per product |

> **The key insight behind adaptive optimizers:** Adam's per-parameter step size $\frac{\eta}{\sqrt{\hat{v}_t}+\epsilon}$ is a crude estimate of dividing by curvature. It is a diagonal, gradient-based stand-in for $H^{-1}$ — cheap second-order information smuggled into a first-order method.

---

### 8. Check Your Understanding

**Q1: For $f(x) = x^4 - 4x^3$, find all critical points, classify them, and locate all inflection points.**
<details>
<summary><b>Reveal Answer &amp; Full Analysis</b></summary>

1. **Step 1 — First derivative and critical points:**
   $$ f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3) = 0 \;\Longrightarrow\; x = 0 \;(\text{double}),\; x = 3 $$
2. **Step 2 — Second derivative:**
   $$ f''(x) = 12x^2 - 24x = 12x(x-2) $$
3. **Step 3 — Classify each critical point:**
   * $f''(3) = 12(3)(1) = 36 > 0$ → **local minimum** at $x=3$, value $f(3) = 81 - 108 = -27$.
   * $f''(0) = 0$ → **test inconclusive.** Investigate the sign of $f'$ around $0$:
     - $f'(-1) = 4(1)(-4) = -16 < 0$ (decreasing)
     - $f'(1) = 4(1)(-2) = -8 < 0$ (still decreasing)
     The slope is negative on **both** sides, so $x=0$ is **not an extremum** — it is a point where the curve momentarily flattens while continuing downward (a *saddle* in 1D).
4. **Step 4 — Inflection points:** set $f''(x) = 0$:
   $$ 12x(x-2) = 0 \;\Longrightarrow\; x = 0,\; x = 2 $$
   Check that concavity actually flips:
   * $f''(-1) = 36 > 0$ (concave up)
   * $f''(1) = -12 < 0$ (concave down) → sign change at $x=0$ ✓
   * $f''(3) = 36 > 0$ (concave up) → sign change at $x=2$ ✓

* **Summary:** local minimum at $(3, -27)$; inflection points at $x=0$ and $x=2$; no local maximum.

**The lesson:** a critical point where $f''=0$ demands further investigation. Here the double root of $f'$ was the tell — it signals a flattening, not a turning.
</details>

**Q2: A loss function near its minimum behaves like $L(\theta) = \frac{1}{2}\lambda\theta^2$. Show that gradient descent converges only if $\eta < \frac{2}{\lambda}$.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

1. **Step 1 — Compute the gradient:**
   $$ \frac{dL}{d\theta} = \lambda\theta $$
   (And note $L'' = \lambda$ — the curvature is exactly $\lambda$.)
2. **Step 2 — Write the gradient-descent update:**
   $$ \theta_{t+1} = \theta_t - \eta\lambda\theta_t = (1 - \eta\lambda)\theta_t $$
3. **Step 3 — Recognize a geometric sequence:**
   $$ \theta_t = (1-\eta\lambda)^t\,\theta_0 $$
4. **Step 4 — Impose convergence.** This tends to $0$ if and only if the multiplier has magnitude less than $1$:
   $$ |1 - \eta\lambda| < 1 \;\Longleftrightarrow\; -1 < 1 - \eta\lambda < 1 \;\Longleftrightarrow\; 0 < \eta\lambda < 2 $$
   $$ \boxed{\eta < \frac{2}{\lambda}} $$

**Behaviour in each regime:**

| Learning rate | Multiplier $1-\eta\lambda$ | Behaviour |
| :--- | :--- | :--- |
| $\eta = \frac{1}{\lambda}$ | $0$ | **Optimal** — converges in a single step (this is Newton's method!) |
| $0 < \eta < \frac{1}{\lambda}$ | in $(0,1)$ | Monotone convergence |
| $\frac{1}{\lambda} < \eta < \frac{2}{\lambda}$ | in $(-1,0)$ | Oscillating but converging |
| $\eta > \frac{2}{\lambda}$ | magnitude $> 1$ | **Divergence** |

**In multiple dimensions** the same analysis applies per eigendirection of the Hessian. Stability is dictated by the *largest* eigenvalue ($\eta < \frac{2}{\lambda_{\max}}$), while convergence *speed* is dictated by the *smallest*. The ratio $\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$ is therefore the fundamental difficulty measure — and this is exactly why normalization layers, which shrink $\kappa$, speed up training so dramatically.
</details>

**Q3: Why are saddle points, rather than local minima, considered the main obstacle in high-dimensional deep learning?**
<details>
<summary><b>Reveal Answer &amp; Explanation</b></summary>

**The counting argument.** At any critical point ($\nabla L = 0$), the Hessian has $n$ eigenvalues. The point is a local minimum only if **all $n$** are positive.

If we model the eigenvalue signs as roughly independent coin flips, the probability that all $n$ are positive is about $2^{-n}$. For a network with $n = 10^6$ parameters, that probability is $2^{-1{,}000{,}000}$ — indistinguishable from zero. **Almost every critical point has at least one negative eigenvalue, making it a saddle.**

```text
   In 2D a saddle is easy to picture:

              up
               |
      down ----+---- down       Along one axis it looks like
               |                a minimum; along another,
              up                a maximum.

   In a million dimensions, finding ALL directions curving
   upward is astronomically unlikely.
```

**Why saddles slow training down:** near a saddle the gradient is small in every direction, so progress crawls. The loss plateaus and the run *looks* converged — but it is merely stuck on a pass, not at a bottom.

**Why they are ultimately escapable:**

* A saddle has at least one direction of **negative curvature**. Any perturbation with a component along it grows exponentially.
* **SGD noise** supplies exactly such perturbations for free — the stochasticity of mini-batches is a feature, not a bug.
* **Momentum** accumulates velocity across the flat region and carries the iterate through.
* Saddles are **unstable** equilibria: unlike a local minimum, you cannot stay at one under noise.

**The practical upshot.** The classical worry — "gradient descent will get trapped in a bad local minimum" — turns out to be largely misplaced for deep networks. Empirically, most local minima in these landscapes have similar loss values. The real enemies are saddle-point plateaus and ill-conditioning ($\kappa \gg 1$), both of which are statements about the **second derivative**.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 10 — Higher order derivatives](https://www.youtube.com/watch?v=BLkz5LGWihw)
* **Lesson page:** [3blue1brown.com — Higher order derivatives](https://www.3blue1brown.com/lessons/higher-order-derivatives)

---

[⏮️ **Previous: Chapter 09 — What Does Area Have to Do With Slope?**](09-area-and-slope.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 11 — Taylor Series** ⏭️](11-taylor-series.md)
