"""Week 4 - the bootstrap, from scratch.

In simple words
---------------
You have ONE sample. You would love to collect the data again 10,000 times
and see how much your statistic (mean, median, ...) wobbles - but you can't.

The bootstrap pretends your sample IS the population: draw n values from it
*with replacement*, recompute the statistic, repeat thousands of times. The
spread of those recomputed values estimates how much the real statistic
would wobble. No formula needed - it works for medians, ratios, correlations,
anything you can compute.
"""

from __future__ import annotations

import numpy as np
from math import erf, sqrt


def bootstrap_distribution(data, statistic=np.mean, n_boot: int = 10_000, rng=None):
    """Return ``n_boot`` bootstrap replicates of ``statistic(data)``.

    Vectorised: draws an (n_boot, n) matrix of indices in one go, then applies
    the statistic along axis=1 when it supports ``axis`` (mean, median, std...).
    """
    rng = np.random.default_rng(rng)
    data = np.asarray(data)
    n = len(data)
    idx = rng.integers(0, n, size=(n_boot, n))       # sampling WITH replacement
    samples = data[idx]
    try:
        reps = statistic(samples, axis=1)
    except TypeError:                                  # statistic has no axis argument
        reps = np.array([statistic(s) for s in samples])
    return np.asarray(reps, dtype=float)


def bootstrap_se(data, statistic=np.mean, n_boot: int = 10_000, rng=None) -> float:
    """Bootstrap standard error = standard deviation of the replicates."""
    return float(np.std(bootstrap_distribution(data, statistic, n_boot, rng), ddof=1))


def bootstrap_ci(data, statistic=np.mean, confidence: float = 0.95,
                 n_boot: int = 10_000, method: str = "percentile", rng=None):
    """Bootstrap confidence interval.

    method = "percentile":  [q_(a/2), q_(1-a/2)] of the replicates.
                           Simple, and what most people mean by "bootstrap CI".
    method = "basic":       [2*theta_hat - q_(1-a/2), 2*theta_hat - q_(a/2)]
                           ("reverse percentile") - corrects for a shifted
                           bootstrap distribution.
    method = "normal":      theta_hat +/- z * bootstrap SE.
    """
    data = np.asarray(data)
    alpha = 1 - confidence
    theta_hat = float(statistic(data))
    reps = bootstrap_distribution(data, statistic, n_boot, rng)
    lo_q, hi_q = np.quantile(reps, [alpha / 2, 1 - alpha / 2])

    if method == "percentile":
        return float(lo_q), float(hi_q)
    if method == "basic":
        return float(2 * theta_hat - hi_q), float(2 * theta_hat - lo_q)
    if method == "normal":
        z = _normal_quantile(1 - alpha / 2)
        se = float(np.std(reps, ddof=1))
        return theta_hat - z * se, theta_hat + z * se
    raise ValueError(f"unknown method {method!r}")


def _normal_quantile(p: float) -> float:
    """Inverse of the standard normal CDF by bisection (keeps this file SciPy-free)."""
    lo, hi = -10.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if 0.5 * (1 + erf(mid / sqrt(2))) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
