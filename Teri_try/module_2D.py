# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>
# %%
import numpy as np
from numpy.testing import assert_allclose

module_name = __name__
if module_name == "module_2D":
    print(
        (
            "It looks like I've been imported by another python script\n"
            f"My file location is: \n{__file__}\n"
        )
    )
else:
    print(
        (
            "It looks like I am being run as a main program\n"
            f"My name is {__name__}\n\n"
        )
    )

# %%


def avg(Di, Dj):
    """
    Computes the harmonic average between two values Di and Dj
    Returns 0 if either of them is zero
    """
    if (Di * Dj) == 0:
        return 0
    else:
        return 2 / (1 / Di + 1 / Dj)


# %%
def index_to_row_col(ind, nrows, ncol):
    """
    in a 2D array, returns the row and column value
    associated with a 1D index
    Bottom left is index is zero (0-th row, 0-th column)
    while index one is the 0-th row and 1st column
    """
    if ind > nrows * ncol - 1:
        return 0

    row = int(np.floor(ind / ncol))
    col = int(ind - row * ncol)
    return row, col


# %%
def build_2D_matrix(bc_dict, problem, D_matrix, Qsource):
    """
    Constructs a coefficient matrix A and an array b corresponding to the system Ac = b
    This system corresponds either to a 1D or 2D problem

    Parameters
    ----------
    bc_dict: dict
       dictionary with Boundary_Def objects defining the boundary conditions
    D_matrix: (float vector if 1D or matrix if 2D)
        values of the diffusion coefficient at each grid point(dm^2/day)
        if 2D, dimension is [problem.ny, problem.nx]
    width_x: (float)
        x-extent of the domain (dm)
    width_y: (float)
        y-extent of the domain (dm)
    poro (float)
        porosity value
    Qsource: (float array)
      volumetric source term (mg/L/day)

    Returns
    -------

    the_matrix, rhs: tuple
       where the_matrix=A and rhs =b
       in the discretized diffusion problem
       Ax=b
    """
   
    number_of_rows = problem.ny
    number_of_cols = problem.nx
    n = problem.nx * problem.ny
    is1D = False
    if number_of_rows == 1 or number_of_cols == 1:
        is1D = True
        number_of_cols = n
    the_matrix = np.zeros((n, n))
    rhs = np.zeros(n)

    if is1D:
        dx = max(problem.wx, problem.wy) / (max(problem.ny, problem.nx) - 1)
        coef_x = problem.poro / dx / dx
    else:
        dx = problem.wx / (problem.nx - 1)
        dy = problem.wy / (problem.ny - 1)
        coef_x = 1 / dx / dx
        coef_y = 1 / dy / dy

    for ind in range(n):
        if is1D:
            j = ind
            i = -1
        else:
            i, j = index_to_row_col(ind, number_of_rows, number_of_cols)
            if i == 0 and problem.ny > 1:  # SOUTH BOUNDARY
                if bc_dict["south"].btype == "const":
                    rhs[ind] = bc_dict["south"].val
                    the_matrix[ind, ind] = 1
                else:  # flux boundary condition
                    the_matrix[ind, ind] = 1
                    the_matrix[ind, ind + number_of_cols] = -1
                    rhs[ind] = bc_dict["south"].val / dy
            elif j == 0:  # WEST BOUNDARY
                if bc_dict["west"].btype == "const":
                    rhs[ind] = bc_dict["west"].val
                    the_matrix[ind, ind] = 1
                else:  # flux boundary condition
                    the_matrix[ind, ind] = 1
                    the_matrix[ind, ind + 1] = -1
                    rhs[ind] = bc_dict["west"].val / dx
            elif i == number_of_rows - 1 and problem.ny > 1:  # NORTH BOUNDARY
                if bc_dict["north"].btype == "const":
                    rhs[ind] = bc_dict["north"].val
                    the_matrix[ind, ind] = 1
                else:  # flux boundary condition
                    the_matrix[ind, ind] = 1
                    the_matrix[ind, ind - number_of_cols] = -1
                    rhs[ind] =bc_dict["north"].val / dy
            elif j == number_of_cols - 1:  # EAST BOUNDARY
                #for j in range(len(y_p)):
                if bc_dict["east"].btype == "const":
                    rhs[ind] = bc_dict["east"].val #y_p[j]
                    the_matrix[ind, ind] = 1
                else:  # flux boundary condition
                    the_matrix[ind, ind] = 1
                    the_matrix[ind, ind - 1] = -1
                    bc_dict["west"].val / dx
            
            else:
                if is1D:
                    north = 0
                    south = 0
                    rhs[ind] = Qsource[ind]
                    east = coef_x * avg(D_matrix[ind + 1], D_matrix[ind])
                    west = coef_x * avg(D_matrix[ind - 1], D_matrix[ind])
                else:
                    north = coef_y * avg(D_matrix[i, j], D_matrix[i + 1, j])
                    south = coef_y * avg(D_matrix[i, j], D_matrix[i - 1, j])
                    east = coef_x * avg(D_matrix[i, j], D_matrix[i, j + 1])
                    west = coef_x * avg(D_matrix[i, j], D_matrix[i, j - 1])
                    the_matrix[ind, ind + number_of_cols] = -north
                    the_matrix[ind, ind - number_of_cols] = -south
                    rhs[ind] = Qsource[i, j]

                the_matrix[ind, ind] = east + west + north + south
                the_matrix[ind, ind + 1] = -east
                the_matrix[ind, ind - 1] = -west

    return the_matrix, rhs


# %%
class Boundary_Def:
    """
    this class holds the boundary type btype ('flux' or 'const')
    and the value of the boundary condition (derivitive of the concentration if 'flux'
    value of the concentration if 'const')
    """

    btype: str
    val: float

    def __init__(self, btype, val):
        self.btype = btype
        self.val = val


# %%
class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    nx: int
    ny: int
    K: float
    wx: float
    wy: float

    def __init__(self, nx, ny, K, wx, wy):
        self.nx = nx
        self.ny = ny
        self.K = K
        self.wx = wx
        self.wy = wy


# %%
def mat2vec(c, nrow, ncol):
    #
    # flatten a 2-dimensional concentration array
    # to one dimension, so it can be solved
    # with a matrix equation of the form A*x=b
    #
    n = nrow * ncol
    v = np.zeros(n)
    for ind in range(n):
        i, j = index_to_row_col(ind, nrow, ncol)
        v[ind] = c[i, j]

    return v


# %%
def vec2mat(v, nrow, ncol):
    #
    # return a flattened concentration matrix
    # to its 2-dimensional form for plotting
    #
    n = 0
    c = np.zeros((nrow, ncol))
    for i in range(nrow):
        for j in range(ncol):
            c[i, j] = v[n]
            n = n + 1
    return c


def test_vec():
    """
    test vec2mat using a vector of length
    30 containing the numbers 0 to 29 inclusive
    Note that the second test fails
    """
    v = np.arange(0, 30, 1)
    c = vec2mat(v, 3, 10)
    assert_allclose(c[1, 1], 11.0)
    assert_allclose(c[2, 7], 25.0)


if __name__ == "__main__":
    test_vec()
