# 🛠️ Month 1 — Build Tasks (the "What you build" part of the roadmap)

Every **"What you build"** task from Month 1 of the roadmap (Weeks 1–4), done as working code, tested against trusted libraries, with a notebook for each task that explains the maths in plain words.

> [!TIP]
> **How to learn from this folder (not just read it).** For each task: **(1)** read the notebook top to bottom, **(2)** close it, **(3)** open the matching file in `mathkit/`, delete the body of one function and rewrite it yourself, **(4)** run `pytest` — the tests tell you if your version is right. That's the roadmap's *Understand → Derive → Implement → Test → Explain* loop. Each notebook ends with a **"Your turn"** section and one **"Explain out loud"** prompt for your Saturday recording.

---

## 📋 Task map

| Week | Roadmap task | Notebook | Code (`mathkit/`) | Headline result |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Matrix multiplication with loops, then NumPy. Time both, record the ratio. | [01-matmul-loops-vs-numpy](Week%201%20-%20Linear%20Algebra/01-matmul-loops-vs-numpy.ipynb) | `linalg.py` | Loops ≈ **1,000–2,000× slower** than NumPy at n = 200 (re-run on *your* laptop and record your ratio) |
| **1** | Vector projection, checked against the geometric formula | [02-vector-projection](Week%201%20-%20Linear%20Algebra/02-vector-projection.ipynb) | `linalg.py` | Dot-product formula = pure-geometry formula to 1e-14 on 10,000 random pairs |
| **2** | A numerical gradient checker | [01-numerical-gradient-checker](Week%202%20-%20Calculus/01-numerical-gradient-checker.ipynb) | `gradcheck.py` | Catches a forgotten chain-rule factor and names the wrong entry |
| **2** | Gradient descent on a bowl; raise the learning rate until it explodes | [02-gradient-descent-and-explosion](Week%202%20-%20Calculus/02-gradient-descent-and-explosion.ipynb) | `optim.py` | Explosion predicted exactly by **η < 2 / λ_max** of the Hessian |
| **3** | Simulate each distribution vs the theoretical curve | [01-distributions-simulated](Week%203%20-%20Probability/01-distributions-simulated.ipynb) | `distributions.py` | Bernoulli → Binomial → Poisson → Exponential shown as one family |
| **3** | Prove the Central Limit Theorem to yourself | [02-central-limit-theorem](Week%203%20-%20Probability/02-central-limit-theorem.ipynb) | — | Spread matches σ/√n at every n; skewness falls like 1/√n; Cauchy breaks it |
| **3** | Monty Hall: simulate, then solve with Bayes (+ medical-test base rate) | [03-monty-hall-and-bayes](Week%203%20-%20Probability/03-monty-hall-and-bayes.ipynb) | — | Simulation 0.334 / 0.666 = Bayes 1/3 / 2/3; a *random* host makes it 1/2 |
| **3** | Naive Bayes text classifier | [04-naive-bayes-text-classifier](Week%203%20-%20Probability/04-naive-bayes-text-classifier.ipynb) | `naive_bayes.py` | Real SMS spam: **F1 0.95** vs 0.00 for "always ham"; matches scikit-learn to 1e-14 |
| **4** | Bootstrap confidence intervals from scratch, checked against SciPy | [01-bootstrap-confidence-intervals](Week%204%20-%20Statistics/01-bootstrap-confidence-intervals.ipynb) | `bootstrap.py` | Spam is ~97 chars longer (median), 95% CI [94, 99] |
| **4** | 1,000 experiments → count intervals containing the truth | [02-ci-coverage-1000-experiments](Week%204%20-%20Statistics/02-ci-coverage-1000-experiments.ipynb) | — | **954 / 1000** covered; small skewed samples under-cover (~85% at n = 10) |

Week 1's first two tasks (tool setup, creating the three repos) are things only you can do on your machine — see the checklist at the bottom.

---

## 🖼️ A few of the figures

| Matrix multiplication = composition | Learning-rate cliff predicted by eigenvalues |
| :---: | :---: |
| ![composition](Week%201%20-%20Linear%20Algebra/figures/w1_composition.png) | ![lr cliff](Week%202%20-%20Calculus/figures/w2_lr_cliff.png) |
| **The Central Limit Theorem appearing** | **100 confidence intervals, ~5 miss** |
| ![clt](Week%203%20-%20Probability/figures/w3_clt.png) | ![coverage](Week%204%20-%20Statistics/figures/w4_ci_coverage_100.png) |

---

## 📂 Folder layout

```text
Month 1 - Build Tasks/
├── README.md                     # this file
├── requirements.txt              # numpy, scipy, matplotlib, pandas, scikit-learn, pytest, jupyterlab
├── pytest.ini                    # lets `pytest` find the mathkit package
├── mathkit/                      # from-scratch implementations (plain NumPy, heavily commented)
│   ├── linalg.py                 #   matmul with loops, projection, projection matrix
│   ├── gradcheck.py              #   numerical gradient checker  <- you'll reuse this in Weeks 11, 19, 26
│   ├── optim.py                  #   gradient descent that records its path
│   ├── distributions.py          #   PMFs / PDFs by hand + inverse-transform sampling
│   ├── naive_bayes.py            #   multinomial naive Bayes text classifier
│   └── bootstrap.py              #   bootstrap distribution, SE, percentile / basic / normal CIs
├── tests/                        # 36 tests: each implementation vs NumPy / SciPy / scikit-learn
├── data/sms_spam.tsv             # SMS Spam Collection (UCI, CC BY 4.0) - used in Weeks 3 & 4
├── Week 1 - Linear Algebra/      # notebooks + figures/
├── Week 2 - Calculus/
├── Week 3 - Probability/
└── Week 4 - Statistics/
```

---

## ▶️ How to run it

```bash
cd "Month 1 - Build Tasks"
pip install -r requirements.txt       # or: uv pip install -r requirements.txt
pytest                                # all 36 tests should pass
jupyter lab                           # open any notebook and "Run All"
```

Every notebook is saved **with its outputs**, so you can read it on GitHub without running anything. Notebooks import `mathkit` from the parent folder, so open them from inside their week folder (Jupyter does this by default).

---

## 🎯 Gate 1 — where each question is practised

| Gate 1 question | Practised in |
| :--- | :--- |
| 1. Chain rule for a 3-function composition | Week 2 · gradient checker, §5 (derived and checked numerically) |
| 2. Matrix multiplication as combining transformations; 3×3 by hand | Week 1 · matmul, §1–2 (shear-then-rotate picture, 3×3 example) |
| 3. Derive Bayes' theorem; solve a base-rate problem | Week 3 · Monty Hall & Bayes, §1–2 |
| 4. Correct vs wrong meaning of a 95% CI | Week 4 · coverage, §3 and §6 (answer card) |
| 5. Why the gradient points uphill | Week 2 · gradient descent, §1 (proof + 360-direction check) |

The gate is closed-book: use these to *study*, then sit it on a blank page.

---

## ✅ End-of-Month-1 checklist (from the roadmap)

- [ ] Toolchain working: git (practise a branch + merge + a deliberate conflict), Python via `uv` or conda, `ruff`, `pytest`, JupyterLab, VS Code — *`pytest` passing in this folder is a good first check*
- [ ] Three public repos created: `lab-notebook`, `ml-from-scratch`, `ds-projects` (you can move `mathkit/gradcheck.py` into `ml-from-scratch` — it's meant to be reused)
- [x] Numerical gradient checker, tested
- [x] Central Limit Theorem demonstration notebook
- [x] Bootstrap implemented from scratch
- [x] Naive Bayes text classifier
- [ ] ~130 mathematics problems logged (Khan Academy)
- [ ] **Gate 1 passed, honestly scored**
- [ ] 4 lab-notebook entries

---

*Data credit: Almeida, T.A., Gómez Hidalgo, J.M., Yamakami, A. (2011). SMS Spam Collection. UCI Machine Learning Repository. CC BY 4.0.*
