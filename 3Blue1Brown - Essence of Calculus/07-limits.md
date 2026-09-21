[⏮️ **Previous: Chapter 06 — Implicit Differentiation**](06-implicit-differentiation.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 08 — Integration & the Fundamental Theorem** ⏭️](08-integration-fundamental-theorem.md)

---

# Chapter 07: Limits, L'Hôpital's Rule, and Epsilon-Delta Definitions

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Everything so far has leaned on the phrase "as $dx$ approaches zero." **Limits** are the rigorous machinery that makes that phrase mean something. The formal $\epsilon$-$\delta$ definition is not academic pedantry — it is a precise answer to "how do you prove a quantity approaches a value it never actually reaches?" And once limits are on solid ground, a beautiful bonus falls out: **L'Hôpital's rule**, which turns indeterminate $\frac{0}{0}$ expressions into ordinary derivative computations.

---

### 1. Why Limits Are Needed At All

Recall the derivative definition:

$$ \frac{df}{dx} = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h} $$

At $h = 0$ exactly, this expression is $\frac{0}{0}$ — meaningless. The whole enterprise depends on asking what happens **near** $h = 0$ without ever setting $h = 0$.

```text
   The expression is undefined AT the point,
   but perfectly well-behaved AROUND it:

      value
        ^
        |
      2 |. . . . . . o . . . . . .     <- the HOLE at h = 0
        |         .     .
        |       .         .
        |     .             .
        +---------+-----------------> h
                  0

   Sampling nearer and nearer to 0 from both sides,
   the values home in on 2 — even though h = 0 itself
   gives nothing at all.
```

> **The limit answers:** "what value is this expression *heading toward*?" — a question that makes sense even when the destination is never reached.

---

### 2. The Informal Definition and Its Weakness

**Informal:** $\lim_{x \to c}f(x) = L$ means "$f(x)$ gets arbitrarily close to $L$ as $x$ gets arbitrarily close to $c$."

The weasel word is **"close."** Close to within what? A millimetre? A nanometre? Mathematics cannot build on a vague adjective, and the vagueness caused genuine confusion for nearly two centuries after Newton and Leibniz.

---

### 3. The Epsilon-Delta Definition

> **Formal definition.** $\displaystyle\lim_{x\to c} f(x) = L$ means:
> for **every** $\epsilon > 0$, there **exists** a $\delta > 0$ such that
> $$ 0 < |x - c| < \delta \;\implies\; |f(x) - L| < \epsilon $$

#### Reading It as a Game

The definition is best understood as a **challenge–response game** between two players.

```text
   The epsilon-delta game:

   CHALLENGER: "I bet you cannot get the output within
                epsilon = 0.01 of L."
                        |
                        v
   YOU:        "Watch me. Restrict the input to within
                delta = 0.003 of c, and every output
                lands inside your band."
                        |
                        v
   CHALLENGER: "Fine. Now epsilon = 0.0000001."
                        |
                        v
   YOU:        "Then delta = 0.00000002. Still works."

   You WIN the limit if you have a winning response to
   EVERY challenge, no matter how small.
```

#### The Picture

```text
              y
              ^
              |
      L + eps +- - - - -+-------------+- - - -     <- output band
              |         |    ___/     |               (the challenge)
          L   +- - - - -|-_-/- - - - -|- - - -
              |     ___/|             |
      L - eps +- -/- - -+-------------+- - - -
              |  /      |             |
              +---------+------+------+---------> x
                     c - del   c   c + del

                        <---- input window ---->
                             (your response)

   WIN CONDITION: every x inside the input window (except
   possibly c itself) must produce a y inside the output band.
```

#### Why the Order of Quantifiers Matters

**"For all $\epsilon$, there exists $\delta$"** — this order is not negotiable.

* $\epsilon$ is chosen **first** (by the adversary) and can be arbitrarily tiny.
* $\delta$ is chosen **second**, and is **allowed to depend on $\epsilon$**.

Reversing the order ("there exists $\delta$ such that for all $\epsilon$...") would demand one window that works for every tolerance simultaneously — impossible unless $f$ is constant.

> **Why $0 < |x-c|$:** the strict inequality deliberately **excludes $x = c$ itself**. This is the entire point. The limit describes the approach, not the arrival — which is exactly what we need for $\frac{0}{0}$ expressions like the difference quotient.

---

### 4. Reformulating the Derivative

With limits made precise, the derivative definition is now fully rigorous:

$$ f'(x) = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h} $$

Every "$dx$ shrinks to zero" hand-wave in Chapters 01–06 can now be replaced by an honest limit statement. The intuition was never wrong — it just needed a foundation.

| Chapter 01–06 phrasing | Rigorous replacement |
| :--- | :--- |
| "$dx$ is infinitely small" | $\lim_{dx \to 0}$ |
| "discard terms with $(dx)^2$" | those terms vanish in the limit |
| "the sum of infinitely many slivers" | $\lim_{n\to\infty}$ of a finite Riemann sum |
| "the secant becomes the tangent" | the limit of secant slopes exists |

---

### 5. L'Hôpital's Rule

Limits of the form $\frac{0}{0}$ appear constantly. There is a beautiful shortcut, and its derivation is pure geometry.

#### The Motivating Example

$$ \lim_{x \to 1}\frac{\sin(\pi x)}{x^2 - 1} $$

At $x = 1$: numerator $\sin(\pi) = 0$, denominator $1 - 1 = 0$. Indeterminate.

#### The Geometric Derivation

Zoom in very close to $x = 1$. Both functions are approximately **linear** near a point (that is what differentiability means):

```text
   Near x = 1, both curves look like straight lines through zero:

      value
        ^
        |            /  numerator: rises with slope f'(1)
        |          /
        |        /
      0 +------*--------------------------> x
        |     /|  1
        |   /  |
        | /    |  denominator: falls with slope g'(1)
        |/     |

   Nudge the input by dx away from 1:
      numerator   ~=  f'(1) * dx
      denominator ~=  g'(1) * dx

   Their ratio:
      f'(1) * dx        f'(1)
      ----------  =     -----      <- the dx's cancel exactly!
      g'(1) * dx        g'(1)
```

$$ \boxed{\; \lim_{x \to c}\frac{f(x)}{g(x)} = \lim_{x \to c}\frac{f'(x)}{g'(x)} \quad \text{when } f(c) = g(c) = 0 \;} $$

#### Applying It

$$ \lim_{x\to 1}\frac{\sin(\pi x)}{x^2 - 1} = \lim_{x\to 1}\frac{\pi\cos(\pi x)}{2x} = \frac{\pi\cos(\pi)}{2} = \frac{-\pi}{2} $$

#### Conditions and Cautions

| Requirement | Why |
| :--- | :--- |
| The form must be $\frac{0}{0}$ or $\frac{\infty}{\infty}$ | Otherwise the linear approximations do not both pass through the same point |
| $f$ and $g$ must be differentiable near $c$ | The linear approximation must exist |
| $g'(c) \neq 0$ (or apply again) | Otherwise the new ratio is itself indeterminate |
| You may apply it **repeatedly** | $\lim \frac{1-\cos x}{x^2} = \lim\frac{\sin x}{2x} = \lim\frac{\cos x}{2} = \frac{1}{2}$ |

> **The most common error:** applying the rule to a form that is *not* indeterminate. $\lim_{x\to 0}\frac{x+1}{x+2} = \frac{1}{2}$ by direct substitution; differentiating top and bottom would wrongly give $\frac{1}{1} = 1$. **Always check the form first.**

---

### 6. When Limits Fail to Exist

```text
   Three ways a limit can fail:

   1. JUMP                2. OSCILLATION        3. BLOW-UP
      (different                (no settling)         (unbounded)
       one-sided limits)

        ___                   /\  /\  /\               |
       |                     /  \/  \/  \              |
    ___|                    sin(1/x) near 0          __|

   left != right         values never converge    grows without bound
```

| Failure mode | Example | What happens |
| :--- | :--- | :--- |
| **One-sided limits disagree** | $\frac{|x|}{x}$ at $0$ | Left gives $-1$, right gives $+1$ |
| **Unbounded oscillation** | $\sin\!\left(\frac{1}{x}\right)$ at $0$ | Values cycle forever, never settling |
| **Divergence to infinity** | $\frac{1}{x^2}$ at $0$ | No finite $L$ exists (though we write $\to +\infty$) |

> **Connection to Chapter 02:** a function is **differentiable** at a point exactly when the limit of its difference quotients exists. ReLU fails at $x=0$ by failure mode 1 — the left slope is $0$, the right slope is $1$.

---

### 7. Continuity, Stated With Limits

$$ f \text{ is continuous at } c \iff \lim_{x\to c}f(x) = f(c) $$

This compact statement packs three separate requirements:

1. $f(c)$ must be **defined**.
2. The limit must **exist**.
3. They must be **equal**.

```text
   Three ways continuity breaks:

   f(c) undefined        limit missing         they disagree
                                                    o  <- f(c)
      ---o   o---          ---o
                              |___              ---*---
                                                (limit is here)
```

**And the chain of implications:**
$$ \text{differentiable} \implies \text{continuous} \implies \text{limit exists} $$

None of the arrows reverse: $|x|$ is continuous at $0$ but not differentiable there.

---

### 8. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Limits underpinning derivatives** | Every gradient in every framework | Finite-difference gradient checking approximates the limit with a small finite $h$ |
| **$\epsilon$-$\delta$ style reasoning** | Convergence proofs for optimizers | "For any tolerance $\epsilon$, SGD reaches $\|\nabla L\| < \epsilon$ within $O(1/\epsilon^2)$ steps" |
| **L'Hôpital's rule** | Analyzing limiting behaviour of losses | Behaviour of $\frac{\log(1+e^{-z})}{z}$ as $z \to 0$; softmax temperature limits $T \to 0$ and $T\to\infty$ |
| **Continuity** | Requirement for gradient-based training | Discrete/argmax operations are discontinuous, hence Gumbel-Softmax and straight-through estimators |
| **Non-differentiable points** | Subgradients and optimizer conventions | ReLU at $0$, $L_1$ penalty at $0$, hinge loss at the margin — all use subgradient conventions |
| **Numerical vs. analytical limits** | Choosing $h$ in finite differences | Too large: truncation error $O(h)$. Too small: catastrophic floating-point cancellation. Optimal $h \approx \sqrt{\epsilon_{\text{machine}}}$ |
| **Oscillation without convergence** | Diagnosing training failure | A loss that oscillates instead of settling means the learning rate exceeds the stability limit $2/\lambda_{\max}$ |

#### The Practical Face of Limits: Gradient Checking

Every autodiff implementation is validated by comparing against a numerical limit:

$$ \frac{\partial L}{\partial \theta_i} \approx \frac{L(\theta + h\,e_i) - L(\theta - h\,e_i)}{2h} $$

The **central** difference is used rather than the forward difference because its error is $O(h^2)$ instead of $O(h)$ — a direct consequence of the Taylor expansion (Chapter 11). Typical choice: $h = 10^{-5}$ for `float64`.

---

### 9. Check Your Understanding

**Q1: Evaluate $\displaystyle\lim_{x\to 0}\frac{e^x - 1 - x}{x^2}$.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Check the form.** At $x=0$: numerator $= 1 - 1 - 0 = 0$; denominator $= 0$. Indeterminate $\frac{0}{0}$. ✓
2. **Step 2 — Apply L'Hôpital once:**
   $$ \lim_{x\to 0}\frac{e^x - 1}{2x} $$
3. **Step 3 — Check the form again.** Numerator $= 0$, denominator $= 0$. Still $\frac{0}{0}$, so apply again:
   $$ \lim_{x\to 0}\frac{e^x}{2} = \frac{1}{2} $$

* **Result:** $\frac{1}{2}$.

**Cross-check with the Taylor series** (Chapter 11): $e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$, so
$$ \frac{e^x - 1 - x}{x^2} = \frac{\frac{x^2}{2} + \frac{x^3}{6} + \cdots}{x^2} = \frac{1}{2} + \frac{x}{6} + \cdots \to \frac{1}{2} \;\checkmark $$
</details>

**Q2: Using the $\epsilon$-$\delta$ definition, prove that $\lim_{x\to 3}(2x + 1) = 7$.**
<details>
<summary><b>Reveal Answer &amp; Full Proof</b></summary>

**Goal.** Given any $\epsilon > 0$, produce a $\delta > 0$ such that $0 < |x - 3| < \delta \implies |(2x+1) - 7| < \epsilon$.

**Step 1 — Work backwards from the conclusion.**
$$ |(2x + 1) - 7| = |2x - 6| = 2|x - 3| $$

**Step 2 — Demand this be less than $\epsilon$.**
$$ 2|x-3| < \epsilon \iff |x - 3| < \frac{\epsilon}{2} $$

**Step 3 — Read off the required $\delta$.** Choose $\delta = \dfrac{\epsilon}{2}$.

**Step 4 — Write the proof forwards.**
Let $\epsilon > 0$ be arbitrary. Set $\delta = \frac{\epsilon}{2} > 0$. Suppose $0 < |x-3| < \delta$. Then:
$$ |(2x+1) - 7| = 2|x-3| < 2\delta = 2\cdot\frac{\epsilon}{2} = \epsilon \;\blacksquare $$

**What made this easy:** the function is linear, so $\delta$ scales linearly with $\epsilon$ — here by the factor $\frac{1}{2}$, which is the reciprocal of the slope. For a steeper line, you would need a *smaller* $\delta$ to keep outputs in the same band. For nonlinear functions, $\delta$ depends on $\epsilon$ in more complicated ways, and often on $c$ too.
</details>

**Q3: You implement a custom layer and want to gradient-check it. You try $h = 10^{-15}$ and get wildly wrong answers, even though smaller $h$ should mean a better limit approximation. Explain.**
<details>
<summary><b>Reveal Answer &amp; Analysis</b></summary>

**The mathematical limit and the numerical computation disagree, because floating-point arithmetic has finite precision.**

Two competing error sources:

1. **Truncation error** — the approximation error from using a finite $h$ rather than the true limit. For a central difference this is $O(h^2)$. It **shrinks** as $h$ shrinks.
2. **Round-off error** — with `float64` carrying about 16 significant digits, computing $L(\theta+h) - L(\theta-h)$ for tiny $h$ subtracts two nearly identical numbers. This is **catastrophic cancellation**: the leading digits cancel, leaving only noise. Dividing that noise by a tiny $h$ **amplifies** it, so this error **grows** as $h$ shrinks, roughly like $\frac{\epsilon_{\text{machine}}}{h}$.

```text
   total
   error
     ^
     |  \                              /
     |   \  round-off               /  truncation
     |    \  ~ eps/h              /    ~ h^2
     |     \                    /
     |      \                 /
     |       \____       ____/
     |            \_____/
     +---------------+-----------------> h
                 optimal h

   At h = 1e-15 you are deep in the round-off regime.
```

**The fix.** Choose $h$ near the minimum of the combined curve:

* Central difference, `float64`: $h \approx 10^{-5}$ to $10^{-6}$.
* Forward difference: $h \approx \sqrt{\epsilon_{\text{machine}}} \approx 10^{-8}$.
* Always use the **central** difference — its $O(h^2)$ truncation error buys several digits for free.
* Compare with **relative** error, not absolute: $\frac{|g_{\text{analytic}} - g_{\text{numeric}}|}{\max(|g_{\text{analytic}}|, |g_{\text{numeric}}|, 10^{-8})} < 10^{-7}$.
* Gradient-check in `float64`, never `float32`.

**The lesson:** the limit $h \to 0$ is a statement about real numbers. Computers do not have real numbers.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 7 — Limits, L'Hôpital's rule, and epsilon delta definitions](https://www.youtube.com/watch?v=kfF40MiS7zA)
* **Lesson page:** [3blue1brown.com — Limits, L'Hôpital's rule, and epsilon delta definitions](https://www.3blue1brown.com/lessons/limits)

---

[⏮️ **Previous: Chapter 06 — Implicit Differentiation**](06-implicit-differentiation.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 08 — Integration & the Fundamental Theorem** ⏭️](08-integration-fundamental-theorem.md)
