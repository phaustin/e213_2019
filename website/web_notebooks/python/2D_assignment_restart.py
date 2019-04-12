# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Import-the-state-from-the-original-notebook" data-toc-modified-id="Import-the-state-from-the-original-notebook-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Import the state from the original notebook</a></span></li></ul></div>

# %% [markdown]
# # Import the state from the original notebook

# %%
import numpy as np
values = np.load('savestate.npz')
print(list(values.keys()))


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
        dx = problem.wx / (problem.ny - 1)
        dy = problem.wy / (problem.nx - 1)
        coef_x = problem.poro / dx / dx
        coef_y = problem.poro / dy / dy

    for ind in range(n):
        if is1D:
            j = ind
            i = -1
        else:
            i, j = index_to_row_col(ind, number_of_rows, number_of_cols)
        if j == 0:  # WEST BOUNDARY
            if bc_dict["west"].btype == "const":
                rhs[ind] = bc_dict["west"].val
                the_matrix[ind, ind] = 1
            else:  # flux boundary condition
                the_matrix[ind, ind] = 1
                the_matrix[ind, ind + 1] = -1
                rhs[ind] = bc_dict["west"].val / dx

        elif j == number_of_cols - 1:  # EAST BOUNDARY
            if bc_dict["east"].btype == "const":
                rhs[ind] = bc_dict["east"].val
                the_matrix[ind, ind] = 1
            else:  # flux boundary condition
                the_matrix[ind, ind] = 1
                the_matrix[ind, ind - 1] = -1
                rhs[ind] = bc_dict["east"].val / dx
        elif i == 0 and problem.ny > 1:  # SOUTH BOUNDARY
            if bc_dict["south"].btype == "const":
                rhs[ind] = bc_dict["south"].val
                the_matrix[ind, ind] = 1
            else:  # flux boundary condition
                the_matrix[ind, ind] = 1
                the_matrix[ind, ind + number_of_cols] = -1
                rhs[ind] = bc_dict["south"].val / dy

        elif i == number_of_rows - 1 and problem.ny > 1:  # NORTH BOUNDARY
            if bc_dict["north"].btype == "const":
                rhs[ind] = bc_dict["west"].val
                the_matrix[ind, ind] = 1
            else:  # flux boundary condition
                the_matrix[ind, ind] = 1
                the_matrix[ind, ind - number_of_cols] = -1
                rhs[ind] = bc_dict["north"].val / dy
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
def avg(Di, Dj):
    """
    Computes the harmonic average between two values Di and Dj
    Returns 0 if either of them is zero
    """
    if (Di * Dj) == 0:
        return 0
    else:
        return 2 / (1 / Di + 1 / Dj)


# %% [markdown]
# # User defined types
#
# In python, a user can create new types, that are coequal citizens with
# the basic python types like list or dict
#
# See:  the first few sections of
#
# https://www.diveinto.org/python3/iterators.html
#

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
    poro: float
    wx: float
    wy: float

    def __init__(self, nx, ny, poro, wx, wy):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy


# %%
c0 = 1  # mg/L

# %%
# Here we create 4 boundaries, west has a constant concentration at c0, east has a constant boundary at 0;
west = Boundary_Def("const", val=c0)
east = Boundary_Def("const", val=0)

# For 1D problem, the used boundaries are west and east.

# The other south and north boundaries have a zero flux (impermeable)

north = Boundary_Def("flux", val=0)
south = Boundary_Def("flux", val=0)

# %%
bc_dict = {"west": west, "north": north, "east": east, "south": south}
# The latter array bc_dict will be sent to the different functions

# %%
n_x = 51
n_y = 1 # 1D -- x only
c0 = 1  # mg/L
Diff = 2e-9 * 100 * 24 * 3600  # dm²/day
width_x = 10  # dm
width_y = 0
n = n_x * n_y
x = np.linspace(0, width_x, n_x)
c_init = np.zeros(n_x)
c_init[0] = c0
D_matrix = Diff * np.ones(n)
poro = 0.4
prob = Problem_Def(n_x, n_y, poro, width_x, width_y)
Qsource = np.zeros(n)
A, b = build_2D_matrix(bc_dict, prob, D_matrix, Qsource)
