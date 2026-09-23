"""Week 3 - the five distributions that actually show up, written by hand.

Each function is the textbook formula and nothing else, so you can read it.
They are checked against ``scipy.stats`` in tests/test_distributions.py.

| name        | what it counts / measures                         | mean      | variance        |
|-------------|---------------------------------------------------|-----------|-----------------|
| Bernoulli   | one yes/no trial, P(yes) = p                      | p         | p(1-p)          |
| Binomial    | number of yes in n independent trials             | n p       | n p (1-p)       |
| Poisson     | number of events in a fixed window, rate lam      | lam       | lam             |
| Normal      | sum of many small independent effects             | mu        | sigma^2         |
| Exponential | waiting time until the next Poisson event         | 1/lam     | 1/lam^2         |
"""

from __future__ import annotations

import math

import numpy as np


def bernoulli_pmf(k, p):
    k = np.asarray(k)
    return np.where(k == 1, p, np.where(k == 0, 1 - p, 0.0))


def binomial_pmf(k, n, p):
    """P(K = k) = C(n, k) p^k (1-p)^(n-k)"""
    k = np.atleast_1d(np.asarray(k, dtype=int))
    out = np.array([
        math.comb(n, int(ki)) * p ** ki * (1 - p) ** (n - ki) if 0 <= ki <= n else 0.0
        for ki in k
    ])
    return out


def poisson_pmf(k, lam):
    """P(K = k) = lam^k e^(-lam) / k!   (computed in log space so it never overflows)"""
    k = np.atleast_1d(np.asarray(k, dtype=int))
    out = np.array([
        math.exp(ki * math.log(lam) - lam - math.lgamma(ki + 1)) if ki >= 0 else 0.0
        for ki in k
    ])
    return out


def normal_pdf(x, mu=0.0, sigma=1.0):
    """f(x) = 1 / (sigma sqrt(2 pi)) * exp(-(x - mu)^2 / (2 sigma^2))"""
    x = np.asarray(x, dtype=float)
    z = (x - mu) / sigma
    return np.exp(-0.5 * z ** 2) / (sigma * math.sqrt(2 * math.pi))


def exponential_pdf(x, lam=1.0):
    """f(x) = lam e^(-lam x) for x >= 0, else 0"""
    x = np.asarray(x, dtype=float)
    return np.where(x >= 0, lam * np.exp(-lam * np.clip(x, 0, None)), 0.0)


def exponential_via_inverse_transform(lam, size, rng):
    """Turn uniform random numbers into exponential ones.

    If U ~ Uniform(0, 1) then X = -ln(1 - U) / lam  has the Exponential(lam)
    distribution, because P(X <= x) = P(U <= 1 - e^(-lam x)) = 1 - e^(-lam x),
    which is exactly the exponential CDF. This trick ("inverse transform
    sampling") works for ANY distribution whose CDF you can invert.
    """
    u = rng.random(size)
    return -np.log1p(-u) / lam
