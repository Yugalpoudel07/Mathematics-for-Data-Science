import numpy as np

from mathkit.optim import gradient_descent


def bowl(v):
    return v[0] ** 2 + 10 * v[1] ** 2


def bowl_grad(v):
    return np.array([2 * v[0], 20 * v[1]])


def test_converges_to_minimum_with_small_lr():
    out = gradient_descent(bowl_grad, [3.0, 2.0], lr=0.05, n_steps=500, f=bowl)
    assert not out["diverged"]
    np.testing.assert_allclose(out["path"][-1], [0, 0], atol=1e-8)
    assert out["losses"][-1] < out["losses"][0]


def test_explodes_above_theory_threshold():
    # Hessian eigenvalues are 2 and 20 -> stable only if lr < 2 / 20 = 0.1
    stable = gradient_descent(bowl_grad, [3.0, 2.0], lr=0.099, n_steps=2000)
    exploded = gradient_descent(bowl_grad, [3.0, 2.0], lr=0.101, n_steps=2000)
    assert not stable["diverged"]
    assert exploded["diverged"]
