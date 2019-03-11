# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,python//py:percent
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "cell-2ad2c23f9a0a820a", "locked": true, "schema_version": 1, "solution": false}, "toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#2D-transient-diffusion-in-homogeneous-media" data-toc-modified-id="2D-transient-diffusion-in-homogeneous-media-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>2D transient diffusion in homogeneous media</a></span><ul class="toc-item"><li><span><a href="#Q5-(10)-Solve-for-the-2D-concentration-as-a-function-of-time" data-toc-modified-id="Q5-(10)-Solve-for-the-2D-concentration-as-a-function-of-time-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Q5 (10) Solve for the 2D concentration as a function of time</a></span></li></ul></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Conclusions</a></span></li></ul></div>
# %% {"nbgrader": {"grade": false, "grade_id": "cell-e58a84ffce31f93a", "locked": true, "schema_version": 1, "solution": false}}
import time

import matplotlib.cm as cmap
import matplotlib.pyplot as plt
import numpy as np
from module_2D import Boundary_Def
from module_2D import build_2D_matrix
from module_2D import mat2vec
from module_2D import Problem_Def
from module_2D import vec2mat
from mpl_toolkits.axes_grid1 import AxesGrid
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


# %%
c0 = 1  # mg/L

# %% {"nbgrader": {"grade": false, "grade_id": "cell-f97ab996f12bd2f2", "locked": true, "schema_version": 1, "solution": false}}
# Here we create 4 boundaries, west has a constant concentration at c0, east has a constant boundary at 0;
west = Boundary_Def("const", val=c0)
east = Boundary_Def("const", val=0)

# For 1D problem, the used boundaries are west and east.

# The other south and north boundaries have a zero flux (impermeable)

north = Boundary_Def("flux", val=0)
south = Boundary_Def("flux", val=0)

# %% {"nbgrader": {"grade": false, "grade_id": "cell-ea536fa5b54285e2", "locked": true, "schema_version": 1, "solution": false}}
bc_dict = {"west": west, "north": north, "east": east, "south": south}
# The latter array bc_dict will be sent to the different functions

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "cell-7bfb0e282680103b", "locked": true, "schema_version": 1, "solution": false}}
# ## 2D transient diffusion in homogeneous media
#
# Going from 1 to 2 dimensions changes nothing conceptually. There are, however a couple of changes required for the coding perspective. Indeed, whether the problem is 1D or 2D or 3D, the stucture of the system of equation Ac = b is the same. Matrix $A$ will always be a $n \times n$ matrix, while $c$ and $b$ will always be column vector of size $n$. In 2D, $n = n_x \times n_y$, while in 3D, it will be $n = n_x \times n_y \times n_z$.  The individual equation for a cell still
# produces a single row in the A and b matrices, but in 2D that cell has 4 neighbours instead
# of 2, and 3D it has 6 neighbors intead of 4.
#
# However, the fact is that in every case, the solution is stored in one vector, representing either a 1/2/3D solution. For these higher dimension problems, a two-way conversion between vector and matrix is required. To plot the 2D result, for example, we will use colourmap plots, which require the solution to be plotted to be represented as a 2D array (matrix).
#
# The function vec2mat(...) (specifically $vector\ to\ matrix$) does this: it converts a vector into the relevant 2D matrix, using n_x and n_y.
#
# The reverse function is usually required to initialize the initial condition. It is mac2vec(...). These two functions are defined here below.

# %%
decreasing_factor = 0.1  # Feel free to change if you want to see the impact
# (you can go higher than 1 ... But be careful, if diffusion speeds up significantly,
# the accuracy with respect to the chosen timestep might not be so good if you speed things up! )
# Initial value is 0.01

# %% {"nbgrader": {"grade": false, "grade_id": "cell-42d47ff484f9a502", "locked": true, "schema_version": 1, "solution": false}}
Diff = 2e-9 * 100 * 24 * 3600  # dm²/day


# %% {"nbgrader": {"grade": false, "grade_id": "cell-b9bd7eaf90619a64", "locked": true, "schema_version": 1, "solution": false}}
# Here we define the initial condition, and the diffusion matrix for the 2D problem


def make_D_matrix(the_problem, Diff, decreasing_factor):
    Diff_low = Diff * decreasing_factor
    n_x, n_y = the_problem.nx, the_problem.ny
    width_x, width_y = the_problem.wx, the_problem.wy
    D_matrix = Diff * np.ones((n_y, n_x))

    c_init = np.zeros((n_y, n_x))

    x = np.linspace(0, width_x, n_x)
    y = np.linspace(0, width_y, n_y)

    for i in range(n_y):
        for j in range(n_x):
            if j == 0:
                c_init[i, j] = c0  # Initial condition
    #
    # overwrite the center of the image with a low diffusivity
    #

    for i in range(n_y):
        for j in range(n_x):
            if (
                abs(x[j] - width_x / 2) <= 0.2 * width_x
                and abs(y[i] - width_y / 2) <= 0.2 * width_y
            ):
                D_matrix[i, j] = Diff_low
                # here we define a square of low diffusivity in the middle
    return x, y, D_matrix, c_init


width_x = 10  # dm
width_y = 10  # dm
n_x = 21
n_y = n_x
poro = 0.4

the_prob = Problem_Def(n_x, n_y, poro, width_x, width_y)
x, y, D_matrix, c_init = make_D_matrix(the_prob, Diff, decreasing_factor)
fig, ax = plt.subplots()
# This generates a colormap of diffusion.
cm = cmap.get_cmap("magma")
plt.contourf(x, y, D_matrix, cmap=cm)
plt.colorbar()

# "magma" refers to a colormap example. You can chose other ones
# https://matplotlib.org/examples/color/colormaps_reference.html


# %% {"nbgrader": {"grade": false, "grade_id": "cell-3f0b9e511535468c", "locked": true, "schema_version": 1, "solution": false}}
# Here we plot the initial condition using the colormap again
fig, ax = plt.subplots()
# This generates a colormap of diffusion.
cm = cmap.get_cmap("RdGy_r")
plt.contourf(x, y, c_init, cmap=cm)
plt.colorbar()


# %% {"nbgrader": {"grade": false, "grade_id": "cell-bbb5e477a2fcd825", "locked": true, "schema_version": 1, "solution": false}}
# Here we give you the asymptotic solution to the problem
# we are using everything we have done before

### Asymptotic behavior

Qsource = np.zeros((n_y, n_x))
A, b = build_2D_matrix(bc_dict, the_prob, D_matrix, Qsource)
v = np.linalg.solve(A, b)
n = n_x * n_y
# array v contains the solution
# we convert it in a matrix:

c = vec2mat(v, n_y, n_x)

# and we plot the matrix
plt.contourf(x, y, c, 20, cmap=cm)
plt.colorbar()

# %%
# Here we give you the asymptotic solution to the problem
# we are using everything we have done before

### Asymptotic behavior

poro = 0.4
prob = Problem_Def(n_x, n_y, poro, width_x, width_y)
Qsource = np.zeros((n_y, n_x))
A, b = build_2D_matrix(bc_dict, prob, D_matrix, Qsource)
A = csr_matrix(A, copy=True)

v = spsolve(A, b)
n = n_x * n_y
# # array v contains the solution
# # we convert it in a matrix:

c = vec2mat(v, n_y, n_x)

# # and we plot the matrix
plt.contourf(x, y, c, 20, cmap=cm)
plt.colorbar()

# %% {"nbgrader": {"grade": false, "grade_id": "cell-e8a4fef275e77cec", "locked": true, "schema_version": 1, "solution": false}}
dt = 1.0
Tf = 2000.0
number_of_fig = 9
plot_times = np.linspace(0, Tf, number_of_fig, dtype=np.int, endpoint=True)
plot_timesteps = (plot_times / dt).astype(np.int)
nTstp = int(Tf / dt)  # number of timesteps

# %% [markdown]
# ### Q5 (10) Solve for the 2D concentration as a function of time

# %%
width_x = 10  # dm
width_y = 10  # dm
n_x = 25
n_y = n_x
n = n_x * n_y
poro = 0.4

the_prob = Problem_Def(n_x, n_y, poro, width_x, width_y)
x, y, D_matrix, c_init = make_D_matrix(the_prob, Diff, decreasing_factor)
Qsource = np.zeros((n_y, n_x))
A, b = build_2D_matrix(bc_dict, the_prob, D_matrix, Qsource)

# %% {"nbgrader": {"grade": true, "grade_id": "cell-80a44bbf4fb48e87", "locked": false, "points": 10, "schema_version": 1, "solution": true}}
try_sparse = False
v = mat2vec(c_init, n_y, n_x)
Adelta = np.zeros((n, n))
for i in range(n):
    Adelta[i, i] = poro / dt
Aa = A + Adelta
Bdelta = np.zeros(n)
if try_sparse:
    Aa = csr_matrix(Aa, copy=True)

save_figs = list()

clock_start = time.time()
fig_timesteps = []
fig_count = 0
for t in range(nTstp):
    capture_time = plot_timesteps[fig_count]
    for i in range(n):
        Bdelta[i] = v[i] * poro / dt
    bb = b + Bdelta
    if try_sparse:
        v = spsolve(Aa, bb)
    else:
        v = np.linalg.solve(Aa, bb)

    if t > capture_time:
        save_figs.append(vec2mat(v, n_y, n_x))
        fig_count += 1

clock_stop = time.time()
print(f"with try_sparse={try_sparse}, elapsed time is {clock_stop - clock_start}")


# %% {"nbgrader": {"grade": false, "grade_id": "cell-be8acbb200b99a1f", "locked": true, "schema_version": 1, "solution": false}}
# https://jdhao.github.io/2017/06/11/mpl_multiplot_one_colorbar/
# https://matplotlib.org/tutorials/toolkits/axes_grid.html

automated_plot = True  # set that to False if you don't want the automated 9 plots
if automated_plot:
    fig = plt.figure(figsize=(10, 10))

    grid = AxesGrid(
        fig,
        111,
        nrows_ncols=(3, 3),
        axes_pad=0.40,
        cbar_mode="single",
        cbar_location="right",
        cbar_pad=0.1,
    )

    for fig_num, the_ax in enumerate(grid):
        the_ax.axis("equal")
        try:
            time_step = plot_times[fig_num]
            conc = save_figs[fig_num]
            im = the_ax.contourf(x, y, conc, 20, cmap=cm)
            the_ax.set_title(f"timestep {time_step} days")
        except IndexError:
            fig.delaxes(the_ax)

    cbar = grid.cbar_axes[0].colorbar(im)
    cbar.set_label_text("Concentration (mg/L)", rotation=270, size=20, va="bottom")
    fig.suptitle(
        "Evolution of the concentration through time", y=0.9, size=25, va="bottom"
    )
    fig.savefig("evolution.png")

# %% [markdown]
# ##  Conclusions
#
# What you may have noticed, is that, even for small simple 2d transient problems like the one you have just solved, the computation times are already becoming significant...
#
# This is partly because we are dealing with big matrix which are filled with zeros. It is a complete waste of time and memory to deal with all of these 0 values. There are other ways to make our calculation way faster. We will probably dedicate a lecture to understand how we can improve this.
