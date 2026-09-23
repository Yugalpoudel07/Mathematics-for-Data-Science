"""mathkit - small, from-scratch implementations built during Month 1.

Every function here is written with plain Python / NumPy so you can read
exactly what it does. Each one is checked against a trusted library
(NumPy, SciPy or scikit-learn) in the ``tests/`` folder.

Modules
-------
linalg        matrix multiplication with loops, vector projection      (Week 1)
gradcheck     numerical gradient checker                               (Week 2)
optim         plain gradient descent that records its path             (Week 2)
distributions PMFs / PDFs written by hand                              (Week 3)
naive_bayes   multinomial naive Bayes text classifier                  (Week 3)
bootstrap     bootstrap confidence intervals                           (Week 4)
"""

__all__ = [
    "linalg",
    "gradcheck",
    "optim",
    "distributions",
    "naive_bayes",
    "bootstrap",
]
