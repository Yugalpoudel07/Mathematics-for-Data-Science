"""Week 2 - plain gradient descent that remembers where it walked.

In simple words
---------------
Stand on a hill in fog. Feel which way is uphill (the gradient). Step the
other way. Repeat.

    x_{t+1} = x_t - lr * grad f(x_t)
"""

from __future__ import annotations

import numpy as np


def gradient_descent(grad_f, x0, lr: float, n_steps: int = 100, f=None,
                     blowup: float = 1e6):
    """Run gradient descent and return the full path.

    Parameters
    ----------
    grad_f : callable   x -> gradient at x
    x0     : start point
    lr     : learning rate (step size)
    n_steps: maximum number of steps
    f      : optional loss function, so the loss at each step is recorded
    blowup : stop early once ||x|| exceeds this (the run has "exploded")

    Returns
    -------
    dict with
        path     : (T+1, d) array of every point visited
        losses   : list of f(x) values (empty if f is None)
        diverged : True if the run exploded
    """
    x = np.array(x0, dtype=float)
    path = [x.copy()]
    losses = [float(f(x))] if f is not None else []
    diverged = False

    for _ in range(n_steps):
        x = x - lr * np.asarray(grad_f(x), dtype=float)
        path.append(x.copy())
        if f is not None:
            losses.append(float(f(x)))
        if not np.all(np.isfinite(x)) or np.linalg.norm(x) > blowup:
            diverged = True
            break

    return {"path": np.array(path), "losses": losses, "diverged": diverged}
