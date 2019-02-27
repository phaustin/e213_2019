import pdb

import numpy as np
from numpy.random import rand


def bmatrix(a, eqno=False, precision=3):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError("bmatrix can at most display two dimensions")

    lines = (
        np.array2string(a, precision=precision)
        .replace("[", "")
        .replace("]", "")
        .splitlines()
    )
    rv = [r"\begin{align*}", r"\begin{bmatrix}"]
    rv += ["  " + " & ".join(l.split()) + r"\\" for l in lines]
    tail = [r"\end{bmatrix}", r"\end{align*}"]
    rv.extend(tail)
    return "\n".join(rv)


if __name__ == "__main__":

    A = rand(10, 10)
    print(bmatrix(A))

    A = np.array([[12, 5, 2], [20, 4, 8], [2, 4, 3], [7, 1, 10]])
    print(bmatrix(A))

    B = np.array([[1.2], [3.7], [0.2]])
    print(bmatrix(B))

    C = np.array([1.2, 9.3, 0.6, -2.1])
    print(bmatrix(C))
