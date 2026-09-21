[⏮️ **Previous: Chapter 03 — Derivative Formulas Through Geometry**](03-derivative-formulas-geometry.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 05 — What's So Special About Euler's Number e?** ⏭️](05-derivatives-exponentials.md)

---

# Chapter 04: Visualizing the Chain Rule and Product Rule

**Essence of Calculus — 3Blue1Brown**

> [!TIP]
> **Core Intuition:**
> Chapter 03 gave us derivatives of *simple* functions. Real functions are built by **combining** simple ones — adding, multiplying, and nesting them. Three rules cover every combination. Addition is trivial. **Multiplication** is a rectangle gaining two strips: *left d-right plus right d-left*. **Composition** is a chain of nudges rippling through a pipeline, where the sensitivities **multiply**. The chain rule is, without exaggeration, the single most important formula in modern machine learning — backpropagation is nothing but the chain rule applied systematically.

---

### 1. The Three Ways to Build Functions

| Construction | Example | Rule needed |
| :--- | :--- | :--- |
| **Sum** | $\sin(x) + x^2$ | Sum rule (trivial) |
| **Product** | $\sin(x) \cdot x^2$ | **Product rule** |
| **Composition** | $\sin(x^2)$ | **Chain rule** |

> Read the notation carefully: $\sin(x)x^2$ is a *product*, $\sin(x^2)$ is a *composition*. They look almost identical on the page and behave completely differently.

---

### 2. The Sum Rule (Warm-Up)

$$ \frac{d}{dx}\big[g(x) + h(x)\big] = \frac{dg}{dx} + \frac{dh}{dx} $$

```text
   Stacking two graphs vertically:

     g + h  |          ___/           The total rise over a run dx
            |      ___/               is just the rise of g plus
            |  ___/                   the rise of h.
            |_/
            +----------------> x

     dx nudges both functions at once; the changes simply add.
```

Nothing interacts, so nothing complicated happens. This is the easy case — and its simplicity is exactly why the next two rules feel surprising.

---

### 3. The Product Rule — A Rectangle Gaining Two Strips

Let $f(x) = g(x) \cdot h(x)$. Draw a **rectangle** whose width is $g(x)$ and whose height is $h(x)$. Its area is $f(x)$.

```text
        <------------ g(x) ------------><--- dg --->

    ^   +-------------------------------+-----------+
    |   |                               |           |
    |   |                               |           |
  h(x)  |          Area = g * h         |  h * dg   |  <- right strip
    |   |                               |           |
    |   |                               |           |
    v   +-------------------------------+-----------+
   dh   |            g * dh             | dg * dh   |  <- top strip + corner
        +-------------------------------+-----------+
                  (top strip)             (corner:
                                          NEGLIGIBLE)
```

The area gained when both sides are nudged:

$$ df = \underbrace{h \cdot dg}_{\text{right strip}} + \underbrace{g \cdot dh}_{\text{top strip}} + \underbrace{dg \cdot dh}_{\text{corner} \;\to\; 0} $$

Divide by $dx$ and discard the corner (it is a product of two small quantities — order $(dx)^2$):

$$ \boxed{\; \frac{d}{dx}\big[g \cdot h\big] = \frac{dg}{dx}\,h \;+\; g\,\frac{dh}{dx} \;} $$

#### The Mnemonic

> **"Left d-Right, plus Right d-Left."**
> $$ (gh)' = g'h + gh' $$

**Why the asymmetry disappears:** each factor gets a turn at being differentiated while the other is held fixed. That is exactly what the two strips represent — one strip from widening, one from heightening.

#### Worked Example

$$ f(x) = \sin(x)\,x^2 $$
$$ f'(x) = \underbrace{\cos(x) \cdot x^2}_{g'h} \;+\; \underbrace{\sin(x) \cdot 2x}_{gh'} \;=\; x^2\cos(x) + 2x\sin(x) $$

#### Extending to Three Factors

$$ \frac{d}{dx}\big[fgh\big] = f'gh + fg'h + fgh' $$

**Pattern:** differentiate one factor at a time, leave the rest alone, and sum. Geometrically this is a **box gaining three slabs** — the same picture as the $x^3$ derivation in Chapter 03, which is just the special case $f = g = h = x$:
$$ \frac{d}{dx}\big[x \cdot x \cdot x\big] = 1\cdot x \cdot x + x \cdot 1 \cdot x + x \cdot x \cdot 1 = 3x^2 \;\checkmark $$

---

### 4. The Chain Rule — A Pipeline of Nudges

Now consider **composition**: $f(x) = g(h(x))$. The input flows through $h$ first, and that output flows into $g$.

```text
   The pipeline view:

      x  ---->  [ h ]  ---->  h(x)  ---->  [ g ]  ---->  g(h(x))
      |                        |                           |
     dx                       dh                          dg

   A nudge dx at the input causes a nudge dh in the middle,
   which in turn causes a nudge dg at the output.
```

#### Three Number Lines

The clearest visualization uses **three stacked number lines**, one per stage:

```text
   Input line (x):
   ----+--------+----------------------------------> x
       x      x+dx
       |<-dx->|
          |
          | h maps this interval to...
          v
   Middle line (h):
   --------+-----------+--------------------------> h
          h(x)     h(x+dx)
           |<---dh--->|          dh = h'(x) * dx
               |
               | g maps THAT interval to...
               v
   Output line (g):
   ---+-------------------------+------------------> g
    g(h(x))              g(h(x)+dh)
      |<---------dg----------->|   dg = g'(h(x)) * dh
```

#### The Derivation

Each stage multiplies the size of the nudge by its own local sensitivity:

$$ dh = h'(x)\,dx \qquad\text{and}\qquad dg = g'(h(x))\,dh $$

Substituting the first into the second:

$$ dg = g'(h(x)) \cdot h'(x) \cdot dx $$

Divide by $dx$:

$$ \boxed{\; \frac{d}{dx}\,g(h(x)) \;=\; g'\big(h(x)\big) \cdot h'(x) \;} $$

#### The Leibniz Form — Why It Looks Like Cancellation

Write $u = h(x)$. Then:

$$ \frac{dg}{dx} = \frac{dg}{du} \cdot \frac{du}{dx} $$

```text
        dg       dg     du
       ---- =   ---- * ----
        dx       du     dx
                  \     /
                   \   /
                 the du's "cancel"
```

> **A critical caveat:** the $du$ terms are not literally cancelling — these are limits, not fractions. But the notation was *designed* so that the bookkeeping would look like cancellation, and that design is why Leibniz notation dominates in physics, engineering, and machine learning.

#### The Interpretation That Matters

> **The chain rule says sensitivities multiply.** If nudging $x$ moves $u$ three times as much, and nudging $u$ moves $g$ five times as much, then nudging $x$ moves $g$ **fifteen** times as much.

#### Worked Example

$$ f(x) = \sin(x^2) $$

* Outer function: $g(u) = \sin(u)$, so $g'(u) = \cos(u)$.
* Inner function: $h(x) = x^2$, so $h'(x) = 2x$.

$$ f'(x) = \cos(x^2) \cdot 2x = 2x\cos(x^2) $$

> **The most common mistake:** writing $\cos(2x)$. The outer derivative must be evaluated **at the inner function's output**, not at $x$. The argument of $\cos$ stays $x^2$.

---

### 5. Extending the Chain Rule to Deep Compositions

Composition nests arbitrarily deep, and the rule extends by simple repetition:

$$ \frac{d}{dx}\,f\big(g(h(x))\big) = f'\big(g(h(x))\big) \cdot g'\big(h(x)\big) \cdot h'(x) $$

```text
   A deep pipeline (this IS a neural network):

    x --> [h] --> [g] --> [f] --> output

   Forward pass:  compute h(x), then g(h(x)), then f(g(h(x)))

   Backward pass: multiply the local sensitivities in reverse

        df/dx  =  f'  x  g'  x  h'
                  ^      ^      ^
                  |      |      |
              last   middle   first
              layer   layer   layer
```

For an $L$-layer composition:

$$ \frac{\partial \text{output}}{\partial \text{input}} = \prod_{\ell=1}^{L} \frac{\partial (\text{layer } \ell \text{ output})}{\partial (\text{layer } \ell \text{ input})} $$

**This product is literally backpropagation.** It is also the origin of the two great pathologies of deep learning:

| Pathology | Cause | Consequence |
| :--- | :--- | :--- |
| **Vanishing gradients** | Many factors each $< 1$ multiply together | $0.5^{50} \approx 10^{-15}$ — early layers stop learning |
| **Exploding gradients** | Many factors each $> 1$ multiply together | $1.5^{50} \approx 6 \times 10^{8}$ — training diverges |

Residual connections, careful weight initialization, normalization layers, and gradient clipping all exist to keep this product near $1$.

---

### 6. Combining All Three Rules

Real expressions mix all three constructions. The strategy: **peel from the outside in.**

#### Worked Example

$$ f(x) = x^2 \sin\!\left(\sqrt{x}\right) $$

**Step 1 — Identify the outermost structure.** This is a **product** of $u = x^2$ and $v = \sin(\sqrt{x})$.

**Step 2 — Apply the product rule.**
$$ f'(x) = 2x \cdot \sin(\sqrt{x}) + x^2 \cdot \frac{d}{dx}\sin(\sqrt{x}) $$

**Step 3 — The remaining derivative is a composition — chain rule.**
$$ \frac{d}{dx}\sin(\sqrt{x}) = \cos(\sqrt{x}) \cdot \frac{d}{dx}\sqrt{x} = \cos(\sqrt{x}) \cdot \frac{1}{2\sqrt{x}} $$

**Step 4 — Assemble.**
$$ f'(x) = 2x\sin(\sqrt{x}) + \frac{x^2\cos(\sqrt{x})}{2\sqrt{x}} = 2x\sin(\sqrt{x}) + \frac{x^{3/2}\cos(\sqrt{x})}{2} $$

```text
   Decision procedure for any expression:

   Look at the OUTERMOST operation:
       |
       +-- Is it a sum?          -> Sum rule, handle each term
       |
       +-- Is it a product?      -> Product rule, then recurse
       |                            into each factor
       |
       +-- Is it a composition?  -> Chain rule, then recurse
       |                            into the inner function
       |
       +-- Is it elementary?     -> Look up the picture (Ch. 03)
```

---

### 7. The Quotient Rule (A Corollary, Not a New Idea)

$$ \frac{d}{dx}\left[\frac{g}{h}\right] = \frac{g'h - gh'}{h^2} $$

**Derivation:** write $\frac{g}{h} = g \cdot h^{-1}$ and apply the product rule plus the chain rule:
$$ \frac{d}{dx}\left[g \cdot h^{-1}\right] = g'h^{-1} + g\cdot(-1)h^{-2}h' = \frac{g'}{h} - \frac{gh'}{h^2} = \frac{g'h - gh'}{h^2} $$

> There is no need to memorize this separately. It falls out of the two rules you already have.

---

### 8. Connection to Machine Learning & Data Science

| Calculus Idea from This Chapter | Role in ML / Data Science | Concrete Example |
| :--- | :--- | :--- |
| **Chain rule** | **Backpropagation** — the entire training algorithm for neural networks | $\frac{\partial L}{\partial W^{(1)}} = \frac{\partial L}{\partial a^{(3)}}\frac{\partial a^{(3)}}{\partial a^{(2)}}\frac{\partial a^{(2)}}{\partial W^{(1)}}$ |
| **Sensitivities multiply** | Explains vanishing and exploding gradients | Sigmoid saturates with $\sigma' \le 0.25$; 20 stacked layers give $0.25^{20} \approx 10^{-12}$ |
| **Product rule** | Gradients of gated and attention architectures | LSTM gates ($f_t \odot c_{t-1}$), attention weights times values ($\text{softmax}(QK^T)V$) |
| **Deep composition** | The mathematical definition of "deep" learning | A network *is* $f_L \circ f_{L-1} \circ \cdots \circ f_1$ |
| **Leibniz cancellation form** | Reparameterization and change of variables | VAE reparameterization trick; normalizing flows use $\frac{dz}{dx}$ chains |
| **Outer-derivative-at-inner-value** | The most common bug in hand-written backward passes | Evaluating $\sigma'$ at the pre-activation $z$, not the activation $a$ |
| **Reverse-mode accumulation** | Why autodiff runs backwards | Computing the product right-to-left costs $O(1)$ passes for many parameters; left-to-right would cost one pass *per parameter* |

#### The Backprop Connection, Explicitly

For a two-layer network $\hat{y} = W_2\,\sigma(W_1 x)$ with loss $L$:

$$ \frac{\partial L}{\partial W_1} = \underbrace{\frac{\partial L}{\partial \hat{y}}}_{\text{loss grad}} \cdot \underbrace{\frac{\partial \hat{y}}{\partial \sigma}}_{W_2} \cdot \underbrace{\frac{\partial \sigma}{\partial z}}_{\sigma'(z)} \cdot \underbrace{\frac{\partial z}{\partial W_1}}_{x} $$

Every term is a local derivative from Chapter 03; the chain rule is what glues them into a training signal.

---

### 9. Check Your Understanding

**Q1: Differentiate $f(x) = (3x^2 + 1)^5$.**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

1. **Step 1 — Identify the composition:**
   * Outer: $g(u) = u^5 \Rightarrow g'(u) = 5u^4$
   * Inner: $h(x) = 3x^2 + 1 \Rightarrow h'(x) = 6x$
2. **Step 2 — Apply the chain rule (outer derivative evaluated at the inner value):**
   $$ f'(x) = 5\left(3x^2 + 1\right)^4 \cdot 6x $$
3. **Step 3 — Simplify:**
   $$ f'(x) = 30x\left(3x^2 + 1\right)^4 $$

* **Sanity check:** expanding $(3x^2+1)^5$ would give a degree-10 polynomial; its derivative should have degree 9. Our answer has degree $1 + 8 = 9$. ✓
</details>

**Q2: Differentiate $f(x) = \dfrac{e^{2x}\sin(x)}{x^2}$. (Use $\frac{d}{dx}e^x = e^x$, proved in Chapter 05.)**
<details>
<summary><b>Reveal Answer &amp; Step-by-Step Derivation</b></summary>

Rewrite as a product to avoid the quotient rule: $f(x) = e^{2x}\sin(x)\,x^{-2}$.

Apply the three-factor product rule, differentiating one factor at a time:

1. **Differentiate $e^{2x}$** (chain rule, inner derivative $2$):
   $$ 2e^{2x}\sin(x)x^{-2} $$
2. **Differentiate $\sin(x)$:**
   $$ e^{2x}\cos(x)x^{-2} $$
3. **Differentiate $x^{-2}$** (power rule):
   $$ e^{2x}\sin(x)\cdot(-2x^{-3}) $$

**Sum the three:**
$$ f'(x) = \frac{2e^{2x}\sin(x)}{x^2} + \frac{e^{2x}\cos(x)}{x^2} - \frac{2e^{2x}\sin(x)}{x^3} $$

**Factored form:**
$$ f'(x) = \frac{e^{2x}}{x^3}\Big[2x\sin(x) + x\cos(x) - 2\sin(x)\Big] $$
</details>

**Q3: A 30-layer network uses sigmoid activations. The maximum value of $\sigma'(z)$ is $0.25$. Estimate the largest possible gradient magnitude reaching layer 1, and explain what this means for training.**
<details>
<summary><b>Reveal Answer &amp; Analysis</b></summary>

1. **Step 1 — The chain rule gives a product of 30 activation derivatives:**
   $$ \left|\frac{\partial L}{\partial W^{(1)}}\right| \;\lesssim\; \prod_{\ell=1}^{30} \left|\sigma'(z_\ell)\right| \cdot \prod_\ell \|W^{(\ell)}\| $$
2. **Step 2 — Bound the activation term (ignoring weights, i.e. the best case for the activations alone):**
   $$ (0.25)^{30} = 2^{-60} \approx 8.7 \times 10^{-19} $$
3. **Step 3 — Interpret:**
   * This is far below the resolution of `float32` (about $10^{-7}$ relative precision), so the gradient is numerically **zero**.
   * Layer 1 receives no learning signal at all. The early layers — which learn the most general features — never update.
   * And $0.25$ is the **maximum**; typical sigmoid inputs are off-center, where $\sigma'$ is far smaller.

**How practitioners fix this:**

* **ReLU** activations ($\sigma' = 1$ on the positive side) keep the factors at exactly $1$.
* **Residual connections** ($x + f(x)$) contribute a derivative of $1 + f'$, so the product has a "highway" of $1$s.
* **Normalization layers** keep pre-activations in the high-gradient region.
* **Careful initialization** (He, Xavier) sets weight scales so the product of layer Jacobians stays near $1$.

Every one of these is an engineering response to a plain consequence of the chain rule.
</details>

---

### 📺 Source

* **Video:** [Essence of calculus, chapter 4 — Visualizing the chain rule and product rule](https://www.youtube.com/watch?v=YG15m2VwSjA)
* **Lesson page:** [3blue1brown.com — Visualizing the chain rule and product rule](https://www.3blue1brown.com/lessons/chain-rule-and-product-rule)

---

[⏮️ **Previous: Chapter 03 — Derivative Formulas Through Geometry**](03-derivative-formulas-geometry.md) &nbsp;•&nbsp; [📚 **Essence of Calculus Index**](README.md) &nbsp;•&nbsp; [**Next: Chapter 05 — What's So Special About Euler's Number e?** ⏭️](05-derivatives-exponentials.md)
