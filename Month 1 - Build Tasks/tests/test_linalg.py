import numpy as np
import pytest

from mathkit.linalg import (matmul_loops, matmul_row_dot, project, project_geometric_2d,
                            projection_matrix, scalar_projection)


@pytest.mark.parametrize("shape", [(1, 1, 1), (2, 3, 4), (5, 5, 5), (7, 1, 3)])
def test_matmul_loops_matches_numpy(shape):
    n, m, p = shape
    rng = np.random.default_rng(0)
    A, B = rng.normal(size=(n, m)), rng.normal(size=(m, p))
    np.testing.assert_allclose(np.array(matmul_loops(A, B)), A @ B, atol=1e-12)
    np.testing.assert_allclose(matmul_row_dot(A, B), A @ B, atol=1e-12)


def test_matmul_shape_mismatch_raises():
    with pytest.raises(ValueError):
        matmul_loops(np.ones((2, 3)), np.ones((2, 3)))


def test_matmul_is_composition():
    rng = np.random.default_rng(1)
    A, B, x = rng.normal(size=(3, 3)), rng.normal(size=(3, 3)), rng.normal(size=3)
    AB = np.array(matmul_loops(A, B))
    np.testing.assert_allclose(AB @ x, A @ (B @ x), atol=1e-12)   # (AB)x == A(Bx)


def test_projection_matches_geometry_2d():
    rng = np.random.default_rng(2)
    for _ in range(200):
        a, b = rng.normal(size=2), rng.normal(size=2)
        np.testing.assert_allclose(project(a, b), project_geometric_2d(a, b), atol=1e-12)


def test_projection_residual_is_perpendicular_and_shortest():
    rng = np.random.default_rng(3)
    a, b = rng.normal(size=5), rng.normal(size=5)
    p = project(a, b)
    assert abs((a - p) @ b) < 1e-12
    # any other point on the line c*b is further away from a
    for c in np.linspace(-3, 3, 61):
        assert np.linalg.norm(a - p) <= np.linalg.norm(a - c * b) + 1e-12


def test_projection_matrix_properties():
    b = np.array([1.0, 2.0, 2.0])
    P = projection_matrix(b)
    np.testing.assert_allclose(P, P.T)
    np.testing.assert_allclose(P @ P, P, atol=1e-12)
    assert np.linalg.matrix_rank(P) == 1
    a = np.array([3.0, -1.0, 4.0])
    np.testing.assert_allclose(P @ a, project(a, b))
    assert scalar_projection(a, b) == pytest.approx((a @ b) / 3.0)


def test_zero_vector_raises():
    with pytest.raises(ValueError):
        project([1, 2], [0, 0])
