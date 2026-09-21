[⏮️ **Previous: Chapter 04 — Visualizing the Chain Rule & Product Rule**](04-chain-rule-product-rule.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 06 — Implicit Differentiation** ⏭️](06-implicit-differentiation.md)

---

# Chapter 05: What's So Special About Euler's Number $e$?

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Exponential functions have a property no other family shares: **their rate of change is proportional to their current value**. Differentiate $2^t$ and you get $2^t$ times a constant. Differentiate $3^t$ and you get $3^t$ times a different constant. Somewhere between $2$ and $3$ sits the unique base where that constant is exactly $1$ — and that number is $e \approx 2.71828$. So $e$ is not a random decimal to memorize. It is **defined** by the property $\frac{d}{dt}e^t = e^t$, and that is why it appears in every growth process, every decay process, and half of machine learning.

---

### 1. The Defining Property of Exponentials

Take $M(t) = 2^t$ and compute its derivative from first principles.

$$ \frac{dM}{dt} = \frac{2^{t + dt} - 2^t}{dt} $$

**The crucial algebraic move** — use the exponent law $2^{t+dt} = 2^t \cdot 2^{dt}$:

$$ \frac{dM}{dt} = \frac{2^t \cdot 2^{dt} - 2^t}{dt} = 2^t \cdot \frac{2^{dt} - 1}{dt} $$

```text
   The structure that makes exponentials special:

        d(2^t)              (2^dt - 1)
        ------  =   2^t  *  ----------
          dt                    dt
                     ^              ^
                     |              |
              depends on t    does NOT depend on t
                                (a pure constant!)
```

> **The key observation:** the messy limit factors out completely. It contains no $t$ whatsoever. So the derivative of $2^t$ is **$2^t$ multiplied by some fixed number**.

Evaluating that limit numerically:

$$ \lim_{dt \to 0}\frac{2^{dt} - 1}{dt} \approx 0.6931 $$

$$ \frac{d}{dt}\left(2^t\right) \approx 0.6931 \cdot 2^t $$

#### Repeating for Other Bases

| Base $a$ | Constant $\displaystyle\lim_{dt\to 0}\frac{a^{dt}-1}{dt}$ | Derivative |
| :---: | :---: | :--- |
| $2$ | $0.6931\ldots$ | $0.6931 \cdot 2^t$ |
| $3$ | $1.0986\ldots$ | $1.0986 \cdot 3^t$ |
| $8$ | $2.0794\ldots$ | $2.0794 \cdot 8^t$ |
| $\mathbf{e \approx 2.71828}$ | $\mathbf{1.0000\ldots}$ | $\mathbf{1 \cdot e^t}$ |

```text
   The constant as a function of the base:

    constant
        ^
     1.5|                                  .3
        |                              .
     1.0|- - - - - - - - - -.e - - - - - - - - -
        |                .
     0.5|           .2
        |       .
      0 +---.---+-------+-------+-------> base a
        1   |   2       e       3
            |
        (at a = 1 the constant is 0: 1^t is flat)
```

Somewhere between $2$ and $3$, the constant passes through exactly $1$. **That crossing point defines $e$.**

---

### 2. Defining $e$ Properly

> **Definition:** $e$ is the unique real number such that
> $$ \lim_{dt \to 0}\frac{e^{dt} - 1}{dt} = 1 $$
> equivalently, the unique base for which
> $$ \boxed{\; \frac{d}{dt}\,e^{t} = e^{t} \;} $$

This is a **self-referential** definition in the best possible sense: $e^t$ is the function that is its own derivative.

```text
   e^t is its own slope, everywhere:

      y
      ^
      |                        /  e^t
      |                       /
    e +                     /|  <- at t=1, height = e, slope = e
      |                   /  |
      |                 /    |
    1 +---------------/      |  <- at t=0, height = 1, slope = 1
      |            _-'       |
      |      __--''          |
      +----------------------+------> t
      0                      1

   At every point, the HEIGHT of the curve equals the STEEPNESS.
```

#### Equivalent Characterizations of $e$

All of these describe the same number:

$$ e = \lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^{n} \qquad e = \sum_{k=0}^{\infty}\frac{1}{k!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \cdots $$

$$ e = \text{the unique } a \text{ with } \frac{d}{dt}a^t = a^t \qquad e = \text{the unique } a \text{ with } \int_1^a \frac{1}{x}\,dx = 1 $$

The third is the one this chapter is built on, and it is the reason $e$ shows up in calculus at all.

---

### 3. Where the Mystery Constants Come From: The Natural Logarithm

The constants in the table above — $0.6931$, $1.0986$, $2.0794$ — are not arbitrary. Rewrite any base in terms of $e$.

**Step 1 — Every positive number is a power of $e$:**
$$ a = e^{\ln(a)} $$
where $\ln$ (the **natural logarithm**) answers: *"$e$ raised to what power gives $a$?"*

**Step 2 — Rewrite the exponential:**
$$ a^t = \left(e^{\ln a}\right)^t = e^{(\ln a) \cdot t} $$

**Step 3 — Differentiate using the chain rule:**

* Outer: $\frac{d}{du}e^u = e^u$
* Inner: $\frac{d}{dt}\big[(\ln a)\,t\big] = \ln a$

$$ \boxed{\; \frac{d}{dt}\left(a^t\right) = \ln(a) \cdot a^t \;} $$

**The mystery is solved:**

| Constant | Its true identity | Value |
| :--- | :--- | :---: |
| $0.6931\ldots$ | $\ln(2)$ | $0.693147\ldots$ |
| $1.0986\ldots$ | $\ln(3)$ | $1.098612\ldots$ |
| $2.0794\ldots$ | $\ln(8) = 3\ln 2$ | $2.079441\ldots$ |
| $1.0000\ldots$ | $\ln(e)$ | $1$ |

> **Why mathematicians always write $e^{ct}$ instead of $a^t$:** the form $e^{ct}$ puts the growth rate $c$ **right there in the exponent**, where it is visible and meaningful. Writing $2^t$ hides the rate $0.693$ inside the base.

---

### 4. The Real Meaning: Rate Proportional to Amount

Any function of the form $M(t) = e^{ct}$ satisfies:

$$ \frac{dM}{dt} = c \cdot e^{ct} = c \cdot M(t) $$

$$ \boxed{\; \frac{dM}{dt} = c\,M \;} $$

> **In words:** the rate of change is **proportional to the current amount**. The constant $c$ is the **proportionality constant** — the fractional growth rate per unit time.

This differential equation is arguably the most important in all of applied mathematics.

```text
   Rate proportional to amount:

   c > 0  (growth)              c < 0  (decay)

      M                            M
      ^        /                   ^\
      |       /                    | \
      |      /                     |  \
      |    _/                      |   \__
      |  _/                        |      \____
      +-/---------> t              +-----------\--> t

   The bigger it gets, the         The more that's left, the
   faster it grows.                faster it disappears.
```

#### Where This Equation Appears

| Phenomenon | Equation | Meaning of $c$ |
| :--- | :--- | :--- |
| Population growth | $\frac{dP}{dt} = cP$ | Birth rate minus death rate |
| Radioactive decay | $\frac{dN}{dt} = -\lambda N$ | Decay constant ($\lambda > 0$) |
| Compound interest | $\frac{dA}{dt} = rA$ | Interest rate |
| Capacitor discharge | $\frac{dQ}{dt} = -\frac{Q}{RC}$ | Inverse time constant |
| Newton's law of cooling | $\frac{dT}{dt} = -k(T - T_{\text{env}})$ | Heat transfer rate |
| Learning-rate decay | $\frac{d\eta}{dt} = -\lambda\eta$ | Decay schedule |
| Weight decay in training | $\frac{dw}{dt} = -\lambda w$ | $L_2$ regularization strength |

**The unifying reason these all use $e$:** the solution to $\frac{dM}{dt} = cM$ is *always* $M(t) = M_0 e^{ct}$. The exponential is the only function family that solves it.

---

### 5. The Natural Logarithm and Its Derivative

Since $\ln$ is the inverse of $e^x$, its derivative follows from the chain rule.

**Setup:** let $y = \ln(x)$. By definition of the inverse, $e^y = x$.

**Differentiate both sides with respect to $x$:**
$$ \frac{d}{dx}\left(e^y\right) = \frac{d}{dx}(x) $$
$$ e^y \cdot \frac{dy}{dx} = 1 $$

**Solve, then substitute $e^y = x$:**
$$ \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x} $$

$$ \boxed{\; \frac{d}{dx}\ln(x) = \frac{1}{x} \;} $$

```text
   Why the logarithm and 1/x are linked:

      ln(x)                        1/x
        ^                           ^
        |      _____                |\
        |   __/                     | \
      0 +--/---------> x          0 +--\_______> x
        | /|                         |  1
        |/ 1                         |
        |                            |
   Slope is steep near 0,      ...which is exactly the
   flattening as x grows...    shape of 1 / x.
```

> **A remarkable consequence:** the power rule $\frac{d}{dx}x^n = nx^{n-1}$ produces every power *except* $x^{-1}$ (you would need $n = 0$, which gives $0$). The "missing" antiderivative of $\frac{1}{x}$ is exactly $\ln|x|$. The logarithm plugs the one hole in the power rule.

---

### 6. Summary Table

| Function | Derivative | Why |
| :--- | :--- | :--- |
| $e^x$ | $e^x$ | The defining property of $e$ |
| $e^{cx}$ | $c\,e^{cx}$ | Chain rule, inner derivative $c$ |
| $a^x$ | $\ln(a)\,a^x$ | Rewrite as $e^{(\ln a)x}$ |
| $\ln(x)$ | $\dfrac{1}{x}$ | Inverse function of $e^x$ |
| $\log_a(x)$ | $\dfrac{1}{x\ln a}$ | Change of base: $\log_a x = \frac{\ln x}{\ln a}$ |
| $e^{f(x)}$ | $f'(x)\,e^{f(x)}$ | Chain rule |
| $\ln(f(x))$ | $\dfrac{f'(x)}{f(x)}$ | Chain rule — the "logarithmic derivative" |

---

### 7. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| $\frac{d}{dx}e^x = e^x$ | Makes softmax and sigmoid gradients elegant | $\sigma'(z) = \sigma(z)(1 - \sigma(z))$ — a derivative expressible in terms of the function itself |
| **Rate proportional to amount** | Exponential learning-rate schedules | $\eta_t = \eta_0 e^{-\lambda t}$; also exponential moving averages in Adam, momentum, and BatchNorm statistics |
| $\frac{d}{dx}\ln x = \frac{1}{x}$ | Cross-entropy loss gradients | $L = -\sum y_i \ln \hat{y}_i \Rightarrow \frac{\partial L}{\partial \hat{y}_i} = -\frac{y_i}{\hat{y}_i}$ |
| **$\ln$ turns products into sums** | Log-likelihood maximization | $\ln \prod_i p(x_i) = \sum_i \ln p(x_i)$ — avoids numerical underflow across thousands of samples |
| **Exponential decay** | Weight decay and regularization | $L_2$ penalty produces $w \leftarrow (1 - \eta\lambda)w$, an exponential shrink toward zero |
| **Softmax** | Converting scores into probabilities | $\text{softmax}(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$ — chosen because its log-gradient is simply $\hat{y} - y$ |
| **Logarithmic derivative $\frac{f'}{f}$** | The REINFORCE / score-function estimator | $\nabla_\theta \mathbb{E}[R] = \mathbb{E}[R \nabla_\theta \ln p_\theta]$ — the backbone of policy-gradient RL |

#### The Softmax + Cross-Entropy Miracle

The single most-used pairing in classification. Its gradient collapses to something beautiful:

$$ \frac{\partial L}{\partial z_i} = \hat{y}_i - y_i $$

**Why it is so clean:** the $\ln$ in cross-entropy and the $e$ in softmax are exact inverses. They cancel, leaving nothing but the prediction error. The entire deep-learning stack is built on this coincidence — which is, of course, not a coincidence at all.

---

### 8. Check Your Understanding

**Q1: Differentiate $f(t) = 5 \cdot 3^{2t}$.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

**Method 1 — Convert to base $e$ (recommended):**

1. Rewrite: $3^{2t} = e^{(\ln 3)(2t)} = e^{2\ln(3)\,t}$
2. So $f(t) = 5e^{2\ln(3)t}$
3. Chain rule, inner derivative $2\ln 3$:
   $$ f'(t) = 5 \cdot 2\ln(3) \cdot e^{2\ln(3)t} = 10\ln(3) \cdot 3^{2t} $$

**Method 2 — Direct rule $\frac{d}{dt}a^u = \ln(a)a^u u'$:**
$$ f'(t) = 5 \cdot \ln(3) \cdot 3^{2t} \cdot 2 = 10\ln(3)\,3^{2t} $$

* **Result:** $f'(t) = 10\ln(3)\,3^{2t} \approx 10.986 \cdot 3^{2t}$.
</details>

**Q2: Prove that $\sigma'(z) = \sigma(z)(1 - \sigma(z))$ for the sigmoid $\sigma(z) = \dfrac{1}{1 + e^{-z}}$.**
<details>
<summary><b>Reveal Answer &amp; Full Derivation</b></summary>

1. **Step 1 — Rewrite with a negative exponent:**
   $$ \sigma(z) = \left(1 + e^{-z}\right)^{-1} $$
2. **Step 2 — Chain rule, outer layer (power rule with $n = -1$):**
   $$ \sigma'(z) = -\left(1 + e^{-z}\right)^{-2} \cdot \frac{d}{dz}\left(1 + e^{-z}\right) $$
3. **Step 3 — Inner derivative** ($\frac{d}{dz}e^{-z} = -e^{-z}$):
   $$ \sigma'(z) = -\left(1 + e^{-z}\right)^{-2} \cdot \left(-e^{-z}\right) = \frac{e^{-z}}{\left(1 + e^{-z}\right)^2} $$
4. **Step 4 — Split the fraction cleverly:**
   $$ \sigma'(z) = \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}} $$
5. **Step 5 — Recognize the second factor:**
   $$ 1 - \sigma(z) = 1 - \frac{1}{1+e^{-z}} = \frac{(1 + e^{-z}) - 1}{1 + e^{-z}} = \frac{e^{-z}}{1 + e^{-z}} $$
6. **Conclusion:**
   $$ \boxed{\sigma'(z) = \sigma(z)\big(1 - \sigma(z)\big)} $$

**Why this matters practically:**

* The forward pass already computed $\sigma(z)$, so the backward pass costs **one multiply** — no exponentials needed.
* The maximum is at $z = 0$: $\sigma'(0) = 0.5 \times 0.5 = 0.25$. This is the hard ceiling that produces vanishing gradients in deep sigmoid networks (Chapter 04, Q3).
* As $|z| \to \infty$, $\sigma' \to 0$ — the **saturation** problem that motivated ReLU.
</details>

**Q3: A model's learning rate decays as $\eta(t) = \eta_0 e^{-\lambda t}$. Derive the half-life of the learning rate, and find $\lambda$ if you want the rate to halve every 10 epochs.**
<details>
<summary><b>Reveal Answer &amp; Derivation</b></summary>

1. **Step 1 — Set up the half-life condition.** Find $t_{1/2}$ such that $\eta(t_{1/2}) = \frac{\eta_0}{2}$:
   $$ \eta_0 e^{-\lambda t_{1/2}} = \frac{\eta_0}{2} \;\Longrightarrow\; e^{-\lambda t_{1/2}} = \frac{1}{2} $$
2. **Step 2 — Take the natural log of both sides:**
   $$ -\lambda t_{1/2} = \ln\!\left(\tfrac{1}{2}\right) = -\ln 2 $$
3. **Step 3 — Solve for the half-life:**
   $$ \boxed{t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}} $$
4. **Step 4 — Solve for $\lambda$ given $t_{1/2} = 10$:**
   $$ \lambda = \frac{\ln 2}{10} \approx 0.0693 $$

**Sanity check at $t = 20$:**
$$ \eta(20) = \eta_0 e^{-0.0693 \times 20} = \eta_0 e^{-1.386} \approx 0.25\,\eta_0 \;\checkmark $$
Two half-lives, one quarter of the rate.

**Note the recurring $0.693$:** it is $\ln 2$, the same constant that appeared as the derivative coefficient of $2^t$ at the very start of this chapter. Half-life problems and base-2 exponentials are the same mathematics wearing different clothes.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 5 — What's so special about Euler's number e?](https://www.youtube.com/watch?v=m2MIpDrF7Es)
* **Lesson page:** [3blue1brown.com — What's so special about Euler's number e?](https://www.3blue1brown.com/lessons/eulers-number)

---

[⏮️ **Previous: Chapter 04 — Visualizing the Chain Rule & Product Rule**](04-chain-rule-product-rule.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 06 — Implicit Differentiation** ⏭️](06-implicit-differentiation.md)
