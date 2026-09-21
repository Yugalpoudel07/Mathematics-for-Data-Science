[⏮️ **Previous: Chapter 02 — The Paradox of the Derivative**](02-paradox-of-the-derivative.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 04 — Visualizing the Chain Rule & Product Rule** ⏭️](04-chain-rule-product-rule.md)

---

# Chapter 03: Derivative Formulas Through Geometry

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Every derivative formula in the standard table is a **picture in disguise**. $\frac{d}{dx}x^2 = 2x$ is a square gaining two strips. $\frac{d}{dx}\frac{1}{x} = -\frac{1}{x^2}$ is a rectangle of fixed area trading height for width. $\frac{d}{dx}\sin(\theta) = \cos(\theta)$ is a point sliding around the unit circle. Once you see the picture, the formula stops being something to memorize and becomes something you can **re-derive on demand**.

---

### 1. The Universal Method

For any function $f$, the derivative is found by the same three-step ritual:

```text
   The ritual:

   1. NUDGE     Change the input from x to (x + dx)
                     |
                     v
   2. MEASURE   Find df = f(x + dx) - f(x), keeping careful
                track of which terms are order dx and which
                are order (dx)^2 or smaller
                     |
                     v
   3. DIVIDE    Compute df / dx, then discard every term
      & LIMIT   that still contains a dx
```

The art is in step 2 — and geometry usually makes it effortless.

> **The governing principle:** terms of order $(dx)^2$ and higher **always** vanish. So when nudging a picture, you only need to find the parts that grow **proportionally to $dx$**.

---

### 2. The Power Rule, Seen Geometrically

#### A. $f(x) = x^2$ — A Growing Square

Interpret $x^2$ as the **area of a square with side $x$**. Nudge the side length by $dx$.

```text
        <--------- x --------><dx>

    ^   +---------------------+---+
    |   |                     |   |
    |   |                     |   |
    x   |      Area = x^2     |x*dx|   <- vertical strip
    |   |                     |   |
    |   |                     |   |
    v   +---------------------+---+
   dx   |       x * dx        |dx^2|   <- horizontal strip + corner
        +---------------------+---+
              (strip)          (corner: negligible)
```

The gained area is:
$$ d(x^2) = \underbrace{2 \cdot x\,dx}_{\text{two strips}} + \underbrace{(dx)^2}_{\text{corner}} $$

Divide by $dx$ and drop the vanishing term:
$$ \frac{d(x^2)}{dx} = 2x + dx \;\longrightarrow\; \boxed{2x} $$

#### B. $f(x) = x^3$ — A Growing Cube

Interpret $x^3$ as the **volume of a cube with side $x$**.

```text
   Growing a cube from side x to side (x + dx):

   +--------+           The new volume consists of:
   |        |
   |   x^3  |  ---->    * the original cube:        x^3
   |        |           * 3 face slabs:          3 x^2 dx   <- ORDER dx
   +--------+           * 3 edge bars:           3 x (dx)^2 <- negligible
                        * 1 corner cube:           (dx)^3   <- negligible

   Only the three flat slabs (one per visible face) matter.
```

$$ d(x^3) = 3x^2\,dx + 3x(dx)^2 + (dx)^3 \;\Longrightarrow\; \frac{d(x^3)}{dx} \to \boxed{3x^2} $$

#### C. The General Power Rule

The pattern is now visible. For $f(x) = x^n$, the binomial expansion gives:

$$ (x + dx)^n = x^n + n\,x^{n-1}\,dx + \binom{n}{2}x^{n-2}(dx)^2 + \cdots $$

Every term after the second carries $(dx)^2$ or higher and dies:

$$ \boxed{\; \frac{d}{dx}\left(x^n\right) = n\,x^{n-1} \;} $$

> **Geometric reading:** an $n$-dimensional hypercube of side $x$ has $n$ "faces" of size $x^{n-1}$. Nudging the side length adds one thin slab per face. Hence the factor of $n$ and the reduced exponent $n-1$.

| $f(x)$ | Geometric object | $f'(x)$ |
| :--- | :--- | :--- |
| $x^1$ | Length of a segment | $1$ |
| $x^2$ | Area of a square | $2x$ |
| $x^3$ | Volume of a cube | $3x^2$ |
| $x^n$ | Volume of an $n$-cube | $nx^{n-1}$ |

**The rule extends beyond positive integers** — to negative and fractional exponents — even though the "hypercube" picture stops applying. The next two examples show why.

---

### 3. $f(x) = \dfrac{1}{x}$ — The Constant-Area Rectangle

Rewrite as $x^{-1}$. The power rule *predicts* $-1 \cdot x^{-2} = -\frac{1}{x^2}$. Let us see the picture that confirms it.

**The setup:** let $y = \frac{1}{x}$. Then $xy = 1$ always — so $x$ and $y$ are the sides of a **rectangle of fixed area $1$**.

```text
   A rectangle of area exactly 1, reshaping as x grows:

        <-- x -->               <----- x + dx ----->
      +-----------+           +---------------------+
    y |           |     ->    |                     | y + dy
      |  Area = 1 |           |      Area = 1       |
      +-----------+           +---------------------+

   Widening by dx ADDS a strip of area  y * dx  on the right.
   To keep the total area at 1, an equal area must be REMOVED
   from the top:  x * (-dy)  must equal  y * dx.
```

Setting the gained and lost areas equal:
$$ y\,dx + x\,dy = 0 \quad\Longrightarrow\quad \frac{dy}{dx} = -\frac{y}{x} $$

Substitute $y = \frac{1}{x}$:
$$ \boxed{\; \frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1/x}{x} = -\frac{1}{x^2} \;} $$

The **negative sign is geometric**, not algebraic bookkeeping: making the rectangle wider forces it to get shorter.

---

### 4. $f(x) = \sqrt{x}$ — A Square With Controlled Area

Write $y = \sqrt{x}$, so $y^2 = x$. Now $y$ is the **side** of a square whose **area** is $x$.

```text
   A square whose AREA is the input x:

        <--- y --->            Nudging the area by dx
      +------------+           adds a thin border of
      |            |           total width 2y:
    y |  Area = x  |
      |            |              dx = 2y * dy
      +------------+
```

From $dx = 2y\,dy$:
$$ \frac{dy}{dx} = \frac{1}{2y} = \boxed{\frac{1}{2\sqrt{x}}} $$

This matches the power rule with $n = \tfrac{1}{2}$:
$$ \frac{d}{dx}\left(x^{1/2}\right) = \tfrac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}} $$

> **Notice:** as $x \to 0^+$, the derivative blows up to $+\infty$ — the graph of $\sqrt{x}$ has a **vertical tangent** at the origin. The picture explains why: when the square is tiny, its border is tiny, so a fixed change in area demands a huge change in side length.

---

### 5. Trigonometric Derivatives From the Unit Circle

#### The Circle Picture

On the **unit circle**, a point at angle $\theta$ has coordinates $(\cos\theta, \sin\theta)$. The angle $\theta$ equals the **arc length** travelled along the circle (that is what radians mean).

```text
   The unit circle, nudged by d(theta):

              y
              ^          . (cos(t+dt), sin(t+dt))
              |        .'|
              |      .'  |  d(sin) = cos(t) * dt   <- vertical rise
              |    .'    |
              |  .'------+
              |.'  d(cos) = -sin(t) * dt  <- horizontal run (leftward!)
              |
        ------+--------------------> x
              0

   The nudge arc has length dt. The little triangle formed by
   the arc is SIMILAR to the radius triangle, but ROTATED 90 degrees.
```

#### The Derivation

Walking a tiny arc-length $d\theta$ along the circle moves the point in a direction **perpendicular to the radius**. Decomposing that tiny step:

* Vertical component: $d(\sin\theta) = \cos\theta \; d\theta$
* Horizontal component: $d(\cos\theta) = -\sin\theta \; d\theta$

$$ \boxed{\; \frac{d}{d\theta}\sin(\theta) = \cos(\theta) \qquad \frac{d}{d\theta}\cos(\theta) = -\sin(\theta) \;} $$

#### Sanity-Checking Against the Graphs

```text
   sin(theta) and its slope:

   sin  +1 |    ___                     slope: 0 at the peak
           |  /     \                          max positive at 0
         0 +-/-------\------/---> t            negative going down
           |/         \    /
        -1 |           \__/

   cos  +1 |\           __                cos is exactly that
           | \         /  \               pattern of slopes
         0 +--\-------/----\--> t
           |   \     /
        -1 |    \___/
```

At $\theta = 0$ the sine curve is rising at its steepest — and $\cos(0) = 1$, the maximum. At $\theta = \pi/2$ the sine curve is flat at its peak — and $\cos(\pi/2) = 0$. The formula and the picture agree everywhere.

> **Crucial caveat:** these formulas hold **only in radians**. In degrees, $\frac{d}{d\theta}\sin(\theta^\circ) = \frac{\pi}{180}\cos(\theta^\circ)$, because arc length no longer equals the angle measure. Radians exist precisely to make this factor equal to $1$.

---

### 6. The Complete Geometric Table

| Function | Geometric picture | Derivative |
| :--- | :--- | :--- |
| $c$ (constant) | A flat, unchanging horizontal line | $0$ |
| $x$ | A segment growing at unit rate | $1$ |
| $x^2$ | A square gaining two strips | $2x$ |
| $x^3$ | A cube gaining three slabs | $3x^2$ |
| $x^n$ | An $n$-cube gaining $n$ slabs | $nx^{n-1}$ |
| $\dfrac{1}{x}$ | Fixed-area rectangle trading width for height | $-\dfrac{1}{x^2}$ |
| $\sqrt{x}$ | Square whose *area* is the input | $\dfrac{1}{2\sqrt{x}}$ |
| $\sin\theta$ | Vertical motion of a point on the unit circle | $\cos\theta$ |
| $\cos\theta$ | Horizontal motion of a point on the unit circle | $-\sin\theta$ |

---

### 7. Two Structural Rules That Follow Immediately

#### A. The Sum Rule

$$ \frac{d}{dx}\big[f(x) + g(x)\big] = f'(x) + g'(x) $$

**Why:** nudging the input nudges each function independently; the total change is the sum of the individual changes. Nothing interacts.

#### B. The Constant Multiple Rule

$$ \frac{d}{dx}\big[c \cdot f(x)\big] = c \cdot f'(x) $$

**Why:** scaling a function vertically by $c$ scales every rise by $c$ while leaving every run alone, so every slope scales by $c$.

Together these say the derivative is a **linear operator** — a fact that will matter enormously when we reach Taylor series and, in machine learning, when we reach backpropagation.

$$ \frac{d}{dx}\big[a f(x) + b g(x)\big] = a f'(x) + b g'(x) $$

> **Warning:** there is *no* such simple rule for products or compositions. $\frac{d}{dx}[f \cdot g] \neq f' \cdot g'$. Those cases need the product rule and chain rule — the subject of Chapter 04.

---

### 8. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Power rule** $\frac{d}{dx}x^n = nx^{n-1}$ | Differentiating squared-error losses | $\frac{\partial}{\partial \hat{y}}(y - \hat{y})^2 = -2(y - \hat{y})$ — the residual, which is why MSE gradients are so clean |
| **Derivative of $1/x$** | Gradients of normalization layers | BatchNorm and LayerNorm divide by a standard deviation that itself depends on the parameters |
| **Derivative of $\sqrt{x}$** | Adaptive optimizers | Adam and RMSProp divide by $\sqrt{v_t}$; the $\frac{1}{2\sqrt{x}}$ blow-up near zero is why they add an $\epsilon$ term |
| **Trigonometric derivatives** | Positional encodings and signal models | Transformer sinusoidal position embeddings; Fourier features in implicit neural representations (SIREN, NeRF) |
| **Linearity of the derivative** | Why loss terms can be combined freely | $L = L_{\text{task}} + \lambda L_{\text{reg}} \Rightarrow \nabla L = \nabla L_{\text{task}} + \lambda \nabla L_{\text{reg}}$ |
| **Sum rule over a dataset** | Why mini-batching is valid | $\nabla \sum_i \ell_i = \sum_i \nabla \ell_i$ — gradients of a batch are the sum of per-example gradients |
| **Geometric re-derivation over memorization** | Debugging custom layers | When you write a custom backward pass, the picture tells you whether your formula is plausible |

---

### 9. Check Your Understanding

**Q1: Use the geometric method to derive $\frac{d}{dx}\left(\frac{1}{x^2}\right)$. Verify with the power rule.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

**Method 1 — Power rule.** Write $\frac{1}{x^2} = x^{-2}$:
$$ \frac{d}{dx}\left(x^{-2}\right) = -2x^{-3} = -\frac{2}{x^3} $$

**Method 2 — From first principles.** Let $y = \frac{1}{x^2}$, so $y x^2 = 1$ (a "box" of fixed volume with a square base of side $x$ and height $y$). Nudge:
$$ (y + dy)(x + dx)^2 = 1 $$
Expand, keeping only terms of order $dx$ and $dy$:
$$ y x^2 + 2xy\,dx + x^2\,dy + O(\text{higher}) = 1 $$
Since $yx^2 = 1$, the leading terms cancel:
$$ 2xy\,dx + x^2\,dy = 0 \;\Longrightarrow\; \frac{dy}{dx} = -\frac{2y}{x} $$
Substituting $y = \frac{1}{x^2}$:
$$ \frac{dy}{dx} = -\frac{2}{x^3} $$

* **Result:** Both methods give $-\dfrac{2}{x^3}$. The negative sign again says: widen the base and the height must drop to preserve the fixed volume.
</details>

**Q2: Differentiate $f(x) = 5x^4 - 3\sqrt{x} + \frac{7}{x} - 2\sin(x) + 11$.**
<details>
<summary><b>Reveal Answer &amp; Term-by-Term Derivation</b></summary>

Apply linearity (sum rule + constant multiple rule) and handle each term with its own picture:

| Term | Rewrite | Derivative |
| :--- | :--- | :--- |
| $5x^4$ | — | $5 \cdot 4x^3 = 20x^3$ |
| $-3\sqrt{x}$ | $-3x^{1/2}$ | $-3 \cdot \tfrac{1}{2}x^{-1/2} = -\dfrac{3}{2\sqrt{x}}$ |
| $\dfrac{7}{x}$ | $7x^{-1}$ | $7 \cdot (-1)x^{-2} = -\dfrac{7}{x^2}$ |
| $-2\sin(x)$ | — | $-2\cos(x)$ |
| $11$ | constant | $0$ |

* **Result:**
  $$ f'(x) = 20x^3 - \frac{3}{2\sqrt{x}} - \frac{7}{x^2} - 2\cos(x) $$

Note that the constant $11$ contributes nothing — shifting a graph vertically never changes any slope.
</details>

**Q3: Why do the formulas $\frac{d}{d\theta}\sin\theta = \cos\theta$ and $\frac{d}{d\theta}\cos\theta = -\sin\theta$ require radians? What changes in degrees?**
<details>
<summary><b>Reveal Answer &amp; Explanation</b></summary>

**The reason:** the derivation relies on the fact that a small change $d\theta$ in the angle corresponds to an **arc length of exactly $d\theta$** on the unit circle. That identity — *angle equals arc length* — is the definition of a radian.

**In degrees:** one degree of angle corresponds to an arc length of $\frac{\pi}{180}$ on the unit circle, not $1$. So the tiny step along the circle is scaled down by $\frac{\pi}{180}$, and every derivative picks up that factor:
$$ \frac{d}{d\theta}\sin(\theta^\circ) = \frac{\pi}{180}\cos(\theta^\circ) $$

**Why this matters practically:** radians are not an arbitrary convention chosen to annoy students. They are the **unique** angle unit in which the calculus of trigonometric functions is clean. Every other choice injects a conversion constant into every derivative, every Taylor series, and every differential equation. This is the same reason $e$ is the unique base with a clean exponential derivative — a theme Chapter 05 develops in full.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 3 — Derivative formulas through geometry](https://www.youtube.com/watch?v=S0_qX4VJhMQ)
* **Lesson page:** [3blue1brown.com — Derivative formulas through geometry](https://www.3blue1brown.com/lessons/derivative-formulas-geometrically)

---

[⏮️ **Previous: Chapter 02 — The Paradox of the Derivative**](02-paradox-of-the-derivative.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 04 — Visualizing the Chain Rule & Product Rule** ⏭️](04-chain-rule-product-rule.md)
