import numpy as np
import pytest

from mathkit import distributions as d

stats = pytest.importorskip("scipy.stats")


def test_bernoulli():
    np.testing.assert_allclose(d.bernoulli_pmf([0, 1], 0.3), stats.bernoulli.pmf([0, 1], 0.3))


def test_binomial():
    k = np.arange(0, 21)
    np.testing.assert_allclose(d.binomial_pmf(k, 20, 0.35), stats.binom.pmf(k, 20, 0.35), atol=1e-14)


def test_poisson():
    k = np.arange(0, 60)
    np.testing.assert_allclose(d.poisson_pmf(k, 12.5), stats.poisson.pmf(k, 12.5), atol=1e-14)


def test_normal():
    x = np.linspace(-5, 9, 200)
    np.testing.assert_allclose(d.normal_pdf(x, 2, 1.5), stats.norm.pdf(x, 2, 1.5), atol=1e-14)


def test_exponential():
    x = np.linspace(-1, 10, 200)
    np.testing.assert_allclose(d.exponential_pdf(x, 0.7), stats.expon.pdf(x, scale=1 / 0.7), atol=1e-14)


def test_inverse_transform_sampler():
    rng = np.random.default_rng(0)
    s = d.exponential_via_inverse_transform(2.0, 200_000, rng)
    assert s.mean() == pytest.approx(0.5, rel=0.01)
    assert s.var() == pytest.approx(0.25, rel=0.03)
    # Kolmogorov-Smirnov test: should NOT reject the exponential distribution
    assert stats.kstest(s[:5000], "expon", args=(0, 0.5)).pvalue > 0.01
