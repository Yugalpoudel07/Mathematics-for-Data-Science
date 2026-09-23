"""Week 1 - linear algebra from scratch.

In simple words
---------------
* A matrix is a machine: vector in -> vector out.
* Multiplying two matrices chains two machines together.
* Projecting vector ``a`` onto vector ``b`` means: "drop a shadow of ``a``
  onto the line that ``b`` points along".
"""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------------
# Matrix multiplication
# ---------------------------------------------------------------------------
def matmul_loops(A, B):
    """Multiply two matrices with three plain Python ``for`` loops.

    Entry (i, j) of the result is the dot product of row i of A with
    column j of B:

        C[i][j] = sum_k A[i][k] * B[k][j]

    Works on nested lists or NumPy arrays and always returns a list of lists,
    so that NO NumPy speed-up sneaks in.
    """
    A = [list(row) for row in A]
    B = [list(row) for row in B]
    n, m = len(A), len(A[0])
    m2, p = len(B), len(B[0])
    if m != m2:
        raise ValueError(
            f"Shapes do not line up: A is {n}x{m}, B is {m2}x{p}. "
            "The number of columns of A must equal the number of rows of B."
        )

    C = [[0.0] * p for _ in range(n)]
    for i in range(n):            # every row of A
        for j in range(p):        # every column of B
            total = 0.0
            for k in range(m):    # walk along the shared dimension
                total += A[i][k] * B[k][j]
            C[i][j] = total
    return C


def matmul_row_dot(A, B):
    """Middle ground: one Python loop over rows, NumPy for each row.

    Shows how much speed you get back by vectorising only the innermost work.
    """
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"Shapes {A.shape} and {B.shape} do not line up.")
    C = np.empty((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        C[i] = A[i] @ B           # (m,) @ (m, p) -> (p,)
    return C


# ---------------------------------------------------------------------------
# Vector projection
# ---------------------------------------------------------------------------
def scalar_projection(a, b):
    """Signed length of the shadow of ``a`` on the line through ``b``.

        comp_b(a) = (a . b) / ||b||   =   ||a|| cos(theta)
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    nb = np.linalg.norm(b)
    if nb == 0:
        raise ValueError("Cannot project onto the zero vector.")
    return float(a @ b) / nb


def project(a, b):
    """Vector projection of ``a`` onto ``b``.

        proj_b(a) = (a . b) / (b . b) * b

    Derivation (do this on paper):
      1. The answer lies on the line through b, so it is c * b for some number c.
      2. The leftover  r = a - c b  must be perpendicular to b  (b . r = 0).
      3. b . (a - c b) = 0  ->  a . b - c (b . b) = 0  ->  c = (a . b)/(b . b).
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    bb = float(b @ b)
    if bb == 0:
        raise ValueError("Cannot project onto the zero vector.")
    return (float(a @ b) / bb) * b


def projection_matrix(b):
    """Matrix P with  P @ a == project(a, b)  for every a.

        P = b b^T / (b^T b)

    Properties worth checking: P is symmetric, and P @ P == P
    (projecting twice changes nothing), and rank(P) == 1.
    """
    b = np.asarray(b, dtype=float).reshape(-1, 1)
    return (b @ b.T) / (b.T @ b).item()


def project_geometric_2d(a, b):
    """Projection computed ONLY from lengths and angles - no dot product.

    Used to check ``project`` against the pure geometry:
        length of shadow = ||a|| cos(theta)
        direction        = unit vector along b
    where theta is found from each vector's angle with the x-axis (atan2).
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    theta = np.arctan2(a[1], a[0]) - np.arctan2(b[1], b[0])
    length_a = np.hypot(a[0], a[1])
    b_hat = b / np.hypot(b[0], b[1])
    return length_a * np.cos(theta) * b_hat
