import numpy as np
import pytest

from mathkit.bootstrap import _normal_quantile, bootstrap_ci, bootstrap_distribution, bootstrap_se


def test_normal_quantile():
    assert _normal_quantile(0.975) == pytest.approx(1.959964, abs=1e-5)


def test_bootstrap_se_of_mean_matches_formula():
    rng = np.random.default_rng(0)
    x = rng.normal(10, 3, size=400)
    formula = x.std(ddof=0) / np.sqrt(len(x))     # plug-in SE of the mean
    assert bootstrap_se(x, n_boot=20_000, rng=1) == pytest.approx(formula, rel=0.03)


def test_percentile_ci_matches_scipy():
    stats = pytest.importorskip("scipy.stats")
    rng = np.random.default_rng(42)
    x = rng.exponential(2.0, size=200)
    mine = bootstrap_ci(x, np.median, n_boot=20_000, method="percentile", rng=7)
    ref = stats.bootstrap((x,), np.median, n_resamples=20_000, method="percentile",
                          random_state=7).confidence_interval
    # different random draws, so allow Monte-Carlo wiggle
    assert mine[0] == pytest.approx(ref.low, rel=0.03)
    assert mine[1] == pytest.approx(ref.high, rel=0.03)


def test_basic_ci_matches_scipy():
    stats = pytest.importorskip("scipy.stats")
    rng = np.random.default_rng(3)
    x = rng.normal(5, 2, size=150)
    mine = bootstrap_ci(x, np.mean, n_boot=20_000, method="basic", rng=0)
    ref = stats.bootstrap((x,), np.mean, n_resamples=20_000, method="basic",
                          random_state=0).confidence_interval
    assert mine[0] == pytest.approx(ref.low, rel=0.01)
    assert mine[1] == pytest.approx(ref.high, rel=0.01)


def test_mean_ci_close_to_t_interval():
    stats = pytest.importorskip("scipy.stats")
    rng = np.random.default_rng(5)
    x = rng.normal(0, 1, size=500)
    lo, hi = bootstrap_ci(x, np.mean, n_boot=20_000, rng=2)
    t_lo, t_hi = stats.t.interval(0.95, len(x) - 1, loc=x.mean(), scale=stats.sem(x))
    assert lo == pytest.approx(t_lo, abs=0.01) and hi == pytest.approx(t_hi, abs=0.01)


def test_statistic_without_axis_argument():
    x = np.arange(20.0)
    reps = bootstrap_distribution(x, lambda s: np.percentile(s, 90), n_boot=50, rng=0)
    assert reps.shape == (50,)
