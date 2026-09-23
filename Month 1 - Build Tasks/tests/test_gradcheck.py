import numpy as np

from mathkit.gradcheck import gradient_check, numerical_gradient, relative_error


def test_simple_quadratic():
    f = lambda x: np.sum(x ** 2)
    g = lambda x: 2 * x
    passed, err, *_ = gradient_check(f, g, np.array([1.0, -2.0, 3.0]))
    assert passed and err < 1e-9


def test_three_variable_function():
    # f(x, y, z) = x^2 y + sin(y z) + e^x
    f = lambda v: v[0] ** 2 * v[1] + np.sin(v[1] * v[2]) + np.exp(v[0])
    g = lambda v: np.array([2 * v[0] * v[1] + np.exp(v[0]),
                            v[0] ** 2 + v[2] * np.cos(v[1] * v[2]),
                            v[1] * np.cos(v[1] * v[2])])
    passed, err, *_ = gradient_check(f, g, np.array([0.5, -1.2, 2.0]))
    assert passed


def test_matrix_input_logistic_loss():
    rng = np.random.default_rng(0)
    X, y = rng.normal(size=(20, 3)), rng.integers(0, 2, 20)
    sig = lambda z: 1 / (1 + np.exp(-z))

    def loss(w):
        p = sig(X @ w)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

    grad = lambda w: X.T @ (sig(X @ w) - y) / len(y)
    passed, err, *_ = gradient_check(loss, grad, rng.normal(size=3))
    assert passed


def test_catches_a_wrong_gradient():
    f = lambda x: np.sum(x ** 3)
    wrong = lambda x: 3 * x          # forgot the square
    passed, err, *_ = gradient_check(f, wrong, np.array([1.0, 2.0]))
    assert not passed and err > 1e-2


def test_does_not_modify_input():
    x = np.array([1.0, 2.0])
    numerical_gradient(lambda v: np.sum(v ** 2), x)
    np.testing.assert_array_equal(x, [1.0, 2.0])


def test_works_on_matrices():
    W = np.arange(6, dtype=float).reshape(2, 3)
    g = numerical_gradient(lambda M: np.sum(M ** 2), W)
    assert g.shape == W.shape
    np.testing.assert_allclose(g, 2 * W, atol=1e-6)


def test_relative_error_zero_case():
    assert relative_error(np.zeros(3), np.zeros(3)) == 0.0
