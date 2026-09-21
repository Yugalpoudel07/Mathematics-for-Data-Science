[⏮️ **Previous: Chapter 05 — What's So Special About Euler's Number e?**](05-derivatives-exponentials.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 07 — Limits, L'Hôpital's Rule & Epsilon-Delta** ⏭️](07-limits.md)

---

# Chapter 06: Implicit Differentiation — What's Going On Here?

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Some curves cannot be written as $y = f(x)$. A circle fails the vertical line test; so does a folium, a lemniscate, or any level set of a messy expression. Implicit differentiation handles them with one clean reframing: stop thinking of $x$ and $y$ as input and output, and start thinking of them as **two quantities tied together by a constraint**. Nudging one forces the other to respond so the constraint stays satisfied. The derivative $\frac{dy}{dx}$ is simply the ratio of those two forced nudges — and the mechanical rule "differentiate everything, tack on $\frac{dy}{dx}$ whenever you touch a $y$" is really just the multivariable chain rule in disguise.

---

### 1. The Problem: Curves That Are Not Functions

Consider the unit circle:
$$ x^2 + y^2 = 5^2 $$

```text
   The circle x^2 + y^2 = 25:

            y
            ^
          5 |    ___---___
            |  /           \
            | |      .      |     A single x value (say x = 3)
     -------+-+------+------+------> x        corresponds to TWO
            | |      |      |                 y values: +4 and -4.
            |  \___  |  ___/
         -5 |      --+--
                     |
              x = 3 --+
```

This is **not a function** — the vertical line test fails everywhere except the two poles. Yet the curve clearly has a well-defined tangent line at every point, so a slope must exist.

#### The Clumsy Approach

Solve for $y$:
$$ y = \pm\sqrt{25 - x^2} $$
Then differentiate the branch you care about. This works for a circle, but it is ugly (two cases, awkward square roots), and for most implicit curves it is **impossible** — there is no closed form for $y$ at all.

$$ y^5 + x^2 y^3 = 1 + \cos(xy) \qquad \text{(good luck solving for } y \text{)} $$

---

### 2. The Reframing: A Constraint Between Two Quantities

> **The shift in perspective:** do not think "$x$ is the input, $y$ is the output." Think "$x$ and $y$ are **two values**, and they are **constrained** to satisfy an equation."

The concrete story: a ladder of length $5$ leans against a wall. Its foot is $x$ from the wall; its top is $y$ up the wall. Pythagoras forces $x^2 + y^2 = 25$ at all times.

```text
   The sliding ladder:

      |\                        |
      | \                       |\
      |  \  length 5            | \
    y |   \          ---->    y'|  \      As the foot slides OUT (dx > 0),
      |    \                    |   \     the top slides DOWN (dy < 0).
      |     \                   |    \
      +------+                  +-----+
         x                         x'

   The constraint x^2 + y^2 = 25 must hold at every instant.
```

Now the question becomes concrete and physical:

> **If the foot slides out by $dx$, how far must the top slide down ($dy$) so that the ladder stays length $5$?**

That ratio $\frac{dy}{dx}$ is the derivative we want — and notice that it is well defined even though $y$ is not a function of $x$ globally.

---

### 3. The Derivation

**Step 1 — Name the constrained quantity.** Let
$$ S(x, y) = x^2 + y^2 $$
The constraint says $S$ must **stay equal to $25$** as the point moves along the curve.

**Step 2 — State what "staying constant" means.**
If $S$ never changes, then the change in $S$ is zero:
$$ dS = 0 $$

**Step 3 — Compute $dS$ by accounting for both contributions.**
Nudging $x$ changes $S$; nudging $y$ also changes $S$. The total change is the sum:

$$ dS = \underbrace{2x\,dx}_{\text{from the } x^2 \text{ term}} + \underbrace{2y\,dy}_{\text{from the } y^2 \text{ term}} $$

```text
   Two contributions to the change in S:

        the x^2 term            the y^2 term
             |                       |
             v                       v
        dS = 2x dx      +       2y dy       =  0
             ^                       ^
             |                       |
     "how much S changes      "how much S changes
      per unit of x"           per unit of y"
```

**Step 4 — Set the total to zero and solve.**
$$ 2x\,dx + 2y\,dy = 0 \;\Longrightarrow\; \boxed{\frac{dy}{dx} = -\frac{x}{y}} $$

#### Verification at a Known Point

At $(3, 4)$ on the circle: $\frac{dy}{dx} = -\frac{3}{4}$.

This is exactly right — the tangent to a circle is **perpendicular to the radius**. The radius to $(3,4)$ has slope $\frac{4}{3}$; the negative reciprocal is $-\frac{3}{4}$. ✓

---

### 4. The Mechanical Rule

In practice you do not set up $S$ every time. The working procedure:

```text
   The implicit differentiation recipe:

   1. Differentiate BOTH SIDES of the equation with respect to x.

   2. Treat y as a FUNCTION OF x. So every time you differentiate
      a term containing y, the chain rule fires and you pick up
      a factor of dy/dx.

          d/dx [ x^3 ]  =  3x^2              (no y -> nothing extra)
          d/dx [ y^3 ]  =  3y^2 * dy/dx      (y present -> chain rule!)
          d/dx [ x*y  ]  =  1*y + x * dy/dx  (product rule + chain rule)

   3. Collect every term containing dy/dx on one side.

   4. Factor out dy/dx and solve for it algebraically.
```

> **Why the extra $\frac{dy}{dx}$ appears:** $y$ is secretly a function of $x$ (locally). So $y^3$ is really $\big(y(x)\big)^3$ — a composition. The chain rule demands the inner derivative $y'(x) = \frac{dy}{dx}$.

#### Worked Example — The Folium of Descartes

$$ x^3 + y^3 = 3xy $$

**Differentiate both sides with respect to $x$:**

* $\frac{d}{dx}x^3 = 3x^2$
* $\frac{d}{dx}y^3 = 3y^2\frac{dy}{dx}$ (chain rule)
* $\frac{d}{dx}(3xy) = 3\left(y + x\frac{dy}{dx}\right)$ (product rule, then chain rule on $y$)

$$ 3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx} $$

**Collect the $\frac{dy}{dx}$ terms:**
$$ 3y^2\frac{dy}{dx} - 3x\frac{dy}{dx} = 3y - 3x^2 $$

**Factor and solve:**
$$ \frac{dy}{dx}\left(3y^2 - 3x\right) = 3y - 3x^2 \;\Longrightarrow\; \boxed{\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}} $$

Note that we **never solved for $y$** — and could not have. The derivative is expressed in terms of *both* coordinates, which is perfectly usable: plug in any point on the curve to get the slope there.

---

### 5. Related Rates: The Same Idea With Time

A close cousin. Instead of relating $x$ and $y$ directly, relate both to a third variable — usually **time**.

**Problem:** the ladder's foot slides away from the wall at $1$ m/s. How fast is the top falling when the foot is $3$ m out?

**Step 1 — Write the constraint:**
$$ x^2 + y^2 = 25 $$

**Step 2 — Differentiate with respect to $t$** (both $x$ and $y$ now depend on time, so both pick up chain-rule factors):
$$ 2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0 $$

**Step 3 — Simplify:**
$$ \frac{dy}{dt} = -\frac{x}{y}\cdot\frac{dx}{dt} $$

**Step 4 — Substitute the known values.** When $x = 3$, the constraint gives $y = 4$, and $\frac{dx}{dt} = 1$:
$$ \frac{dy}{dt} = -\frac{3}{4}\cdot 1 = -0.75 \text{ m/s} $$

The top falls at $0.75$ m/s. The negative sign correctly reports *downward*.

```text
   The rate blows up as the ladder goes flat:

      x = 3, y = 4   ->  dy/dt = -0.75 m/s     (gentle)
      x = 4, y = 3   ->  dy/dt = -1.33 m/s     (faster)
      x = 4.9, y=1.0 ->  dy/dt = -4.9 m/s      (very fast!)
      x -> 5, y -> 0 ->  dy/dt -> -infinity    (vertical tangent)

   Physically: near the ground, a small outward slide of the foot
   requires an enormous drop of the top to preserve the length.
```

---

### 6. What Is Really Happening: A Preview of Multivariable Calculus

The formula $dS = 2x\,dx + 2y\,dy$ is the **total differential** of $S$, and it generalizes:

$$ dS = \frac{\partial S}{\partial x}dx + \frac{\partial S}{\partial y}dy $$

where $\frac{\partial S}{\partial x}$ (a **partial derivative**) asks: *"how much does $S$ change per unit of $x$, holding $y$ fixed?"*

Setting $dS = 0$ and solving gives the general implicit-differentiation formula:

$$ \boxed{\; \frac{dy}{dx} = -\frac{\partial S/\partial x}{\partial S/\partial y} \;} $$

#### The Geometric Picture: Level Curves and Gradients

```text
   S(x, y) = x^2 + y^2 viewed as a surface over the plane:

        Level curves (contours of constant S):

              y
              ^
              |    ___---___          S = 36
              |  /  ___---_  \
              | | /  _---_ \ |        S = 25   <- our circle
              | || /  ___ \ ||
        ------+-||-|--(o)-|-||------> x        S = 16
              | || \ \___/ / ||
              | | \  -----  / |
              |  \  -------  /
              |    ---------

    * Walking ALONG a level curve keeps S constant  -> dS = 0
    * The gradient (dS/dx, dS/dy) points PERPENDICULAR
      to the level curve, in the direction of steepest increase.
```

> **The deep statement:** implicit differentiation finds the direction you can move **without changing $S$** — the direction perpendicular to the gradient. This single idea reappears as Lagrange multipliers, as constrained optimization, and as the geometry of loss surfaces in machine learning.

---

### 7. A Bonus: Deriving $\frac{d}{dx}\ln(x)$ Implicitly

Implicit differentiation gives a slick route to inverse-function derivatives.

$$ y = \ln(x) \;\Longleftrightarrow\; e^y = x $$

**Differentiate both sides with respect to $x$:**
$$ e^y \frac{dy}{dx} = 1 $$

**Solve and substitute $e^y = x$:**
$$ \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x} \;\checkmark $$

The same trick handles all inverse functions:

| Inverse function | Implicit form | Derivative |
| :--- | :--- | :--- |
| $y = \ln x$ | $e^y = x$ | $\dfrac{1}{x}$ |
| $y = \arcsin x$ | $\sin y = x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
| $y = \arctan x$ | $\tan y = x$ | $\dfrac{1}{1+x^2}$ |
| $y = \sqrt[n]{x}$ | $y^n = x$ | $\dfrac{1}{n}x^{1/n - 1}$ |

---

### 8. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Level sets and gradients** | The geometry of every loss landscape | Contour plots of $L(\theta)$; gradient descent always moves perpendicular to the local contour |
| **Constrained optimization** | Lagrange multipliers | Hard-margin SVM: minimize $\|w\|^2$ subject to $y_i(w^Tx_i + b) \ge 1$ |
| **Total differential** $dS = \sum \frac{\partial S}{\partial x_i}dx_i$ | The multivariable chain rule behind autodiff | Every framework's backward pass accumulates $\frac{\partial L}{\partial x_i}$ contributions this way |
| **Implicit function theorem** | Implicit layers and equilibrium models | Deep Equilibrium Models (DEQ) and Neural ODEs differentiate through a fixed point $z = f(z, x)$ without unrolling it |
| **Related rates** | Monitoring coupled training quantities | How fast validation loss changes as training loss falls; tracking the gradient-norm-to-weight-norm ratio |
| **Inverse function derivatives** | Normalizing flows and change of variables | Invertible transforms need $\frac{dx}{dz}$, computed from $\frac{dz}{dx}$ via the same reciprocal trick |
| **Curves that are not functions** | Decision boundaries | A classifier boundary $\{x : f(x) = 0\}$ is a level set, not a graph; its geometry is studied implicitly |

#### The Implicit Function Theorem in Deep Learning

A Deep Equilibrium Model defines its output as the solution $z^\star$ of $z = f_\theta(z, x)$. Backpropagating through hundreds of solver iterations would be ruinous. Instead, differentiate the constraint implicitly:

$$ \frac{\partial z^\star}{\partial \theta} = \left(I - \frac{\partial f}{\partial z}\right)^{-1}\frac{\partial f}{\partial \theta} $$

**Constant memory, regardless of how many iterations the forward solver took.** This is Section 3's reasoning applied to a modern architecture.

---

### 9. Check Your Understanding

**Q1: Find $\frac{dy}{dx}$ for the ellipse $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$, and find the slope at the point $\left(\tfrac{3}{\sqrt{2}}, \sqrt{2}\right)$.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Differentiate both sides with respect to $x$:**
   $$ \frac{2x}{9} + \frac{2y}{4}\frac{dy}{dx} = 0 $$
2. **Step 2 — Isolate the derivative term:**
   $$ \frac{y}{2}\frac{dy}{dx} = -\frac{2x}{9} $$
3. **Step 3 — Solve:**
   $$ \frac{dy}{dx} = -\frac{4x}{9y} $$
4. **Step 4 — Evaluate at $\left(\tfrac{3}{\sqrt{2}}, \sqrt{2}\right)$:**
   $$ \frac{dy}{dx} = -\frac{4 \cdot \frac{3}{\sqrt 2}}{9\sqrt 2} = -\frac{\frac{12}{\sqrt 2}}{9\sqrt 2} = -\frac{12}{9 \cdot 2} = -\frac{2}{3} $$

* **Result:** $\frac{dy}{dx} = -\frac{4x}{9y}$, and the slope at that point is $-\frac{2}{3}$.

**Sanity check:** the point is in the first quadrant on the upper-right arc, where the ellipse descends — a negative slope is correct.
</details>

**Q2: A spherical balloon is inflated at $100\ \text{cm}^3/\text{s}$. How fast is its radius growing when $r = 10$ cm?**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Write the constraint relating the two quantities:**
   $$ V = \frac{4}{3}\pi r^3 $$
2. **Step 2 — Differentiate both sides with respect to time** (both $V$ and $r$ change, so the chain rule fires on $r^3$):
   $$ \frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt} $$
   *(Note: $\frac{dV}{dr} = 4\pi r^2$ is the surface area — exactly the shell-slicing result from Chapter 01.)*
3. **Step 3 — Solve for the unknown rate:**
   $$ \frac{dr}{dt} = \frac{1}{4\pi r^2}\cdot\frac{dV}{dt} $$
4. **Step 4 — Substitute $r = 10$, $\frac{dV}{dt} = 100$:**
   $$ \frac{dr}{dt} = \frac{100}{4\pi(100)} = \frac{1}{4\pi} \approx 0.0796\ \text{cm/s} $$

* **Result:** about $0.08$ cm/s.

**Physical insight:** as the balloon grows, $\frac{dr}{dt} \propto \frac{1}{r^2}$. At $r = 20$ the radius grows four times more slowly, even at the same air-pumping rate — the surface area over which the new volume spreads has quadrupled.
</details>

**Q3: Explain *why* differentiating a $y$ term produces an extra factor of $\frac{dy}{dx}$, connecting it to the chain rule from Chapter 04.**
<details>
<summary><b>Reveal Answer &amp; Explanation</b></summary>

**The setup.** Along the curve, $y$ is locally a function of $x$ — write it as $y(x)$ to make this explicit. Then a term like $y^3$ is really the **composition** $\big(y(x)\big)^3$.

**Apply the chain rule** with outer function $g(u) = u^3$ and inner function $u = y(x)$:
$$ \frac{d}{dx}\big(y(x)\big)^3 = \underbrace{3\big(y(x)\big)^2}_{g'(\text{inner})} \cdot \underbrace{y'(x)}_{\text{inner derivative}} = 3y^2\frac{dy}{dx} $$

**Compare with an $x$ term:**
$$ \frac{d}{dx}x^3 = 3x^2 \cdot \underbrace{\frac{dx}{dx}}_{= \; 1} = 3x^2 $$

The factor is *always* there — it is just invisible for $x$ terms because $\frac{dx}{dx} = 1$.

**The unified statement.** Differentiating any expression $F(x, y)$ with respect to $x$ gives:
$$ \frac{dF}{dx} = \frac{\partial F}{\partial x} + \frac{\partial F}{\partial y}\frac{dy}{dx} $$
Setting $\frac{dF}{dx} = 0$ (because $F$ is pinned to a constant along the curve) and solving recovers the formula from Section 6.

**The takeaway:** implicit differentiation is not a separate technique with its own rules. It is the ordinary chain rule, applied honestly to a variable that happens to depend on $x$ without us having a formula for it.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 6 — Implicit differentiation, what's going on here?](https://www.youtube.com/watch?v=qb40J4N1fa4)
* **Lesson page:** [3blue1brown.com — Implicit differentiation](https://www.3blue1brown.com/lessons/implicit-differentiation)

---

[⏮️ **Previous: Chapter 05 — What's So Special About Euler's Number e?**](05-derivatives-exponentials.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 07 — Limits, L'Hôpital's Rule & Epsilon-Delta** ⏭️](07-limits.md)
