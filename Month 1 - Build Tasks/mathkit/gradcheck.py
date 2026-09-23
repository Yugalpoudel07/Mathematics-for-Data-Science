"""Week 2 - a numerical gradient checker.

In simple words
---------------
You derive a gradient by hand (or write code for it). How do you know it is
right? Nudge each input a tiny bit up and a tiny bit down, see how much the
output changes, and divide. That is the *definition* of a derivative, so it
cannot be "wrong" - it can only be a little imprecise. If your hand-derived
gradient disagrees with it, your derivation has a bug.

    df/dx_i  ~=  [ f(x + eps e_i) - f(x - eps e_i) ] / (2 eps)

This is the *centred* difference. Its error shrinks like eps**2, while the
one-sided version [f(x+eps) - f(x)] / eps only shrinks like eps.

You will reuse this in Week 11 (logistic regression), Week 19 (backprop)
and Week 26 (attention).
"""

from __future__ import annotations

import numpy as np


def numerical_gradient(f, x, eps: float = 1e-5):
    """Centred-difference gradient of scalar function ``f`` at ``x``.

    ``x`` may be a scalar, vector or matrix - the gradient has the same shape.
    ``x`` itself is never modified.
    """
    x = np.array(x, dtype=float)          # private copy
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=["multi_index"])
    while not it.finished:
        idx = it.multi_index
        original = x[idx]

        x[idx] = original + eps
        f_plus = float(f(x))
        x[idx] = original - eps
        f_minus = float(f(x))
        x[idx] = original                 # put it back!

        grad[idx] = (f_plus - f_minus) / (2 * eps)
        it.iternext()
    return grad


def relative_error(a, b) -> float:
    """||a - b|| / (||a|| + ||b||)  - scale-free, so 1e-7 means the same thing
    whether gradients are tiny or huge. Returns 0.0 when both are zero."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    denom = np.linalg.norm(a) + np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.linalg.norm(a - b) / denom)


def gradient_check(f, grad_f, x, eps: float = 1e-5, tol: float = 1e-6, verbose: bool = False):
    """Compare an analytic gradient ``grad_f`` with the numerical one.

    Returns
    -------
    passed : bool
    rel_err : float
    numeric, analytic : ndarray

    Rule of thumb for the relative error (double precision, eps = 1e-5):
        < 1e-7   : correct
        1e-7..1e-4 : suspicious - look closer (kinks like ReLU/abs can cause this)
        > 1e-4   : almost certainly a bug
    """
    x = np.array(x, dtype=float)
    numeric = numerical_gradient(f, x, eps=eps)
    analytic = np.asarray(grad_f(x.copy()), dtype=float).reshape(numeric.shape)
    err = relative_error(numeric, analytic)
    passed = err < tol
    if verbose:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] relative error = {err:.3e}  (tol = {tol:.0e})")
        if not passed:
            worst = tuple(int(i) for i in np.unravel_index(np.argmax(np.abs(numeric - analytic)), numeric.shape))
            print(f"        worst entry {worst}: numeric={numeric[worst]:.6g}, analytic={analytic[worst]:.6g}")
    return passed, err, numeric, analytic
