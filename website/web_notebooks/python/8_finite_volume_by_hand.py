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
#       jupytext_version: 1.0.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.7
#   nbsphinx:
#     execute: never
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: true
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Learning-goals" data-toc-modified-id="Learning-goals-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Learning goals</a></span></li><li><span><a href="#The-problem" data-toc-modified-id="The-problem-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>The problem</a></span><ul class="toc-item"><li><span><a href="#2-D-discrete-approximation-stencil-for-steady-state-diffusion." data-toc-modified-id="2-D-discrete-approximation-stencil-for-steady-state-diffusion.-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>2-D discrete approximation stencil for steady-state diffusion.</a></span><ul class="toc-item"><li><span><a href="#2D-stencil" data-toc-modified-id="2D-stencil-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>2D stencil</a></span></li></ul></li><li><span><a href="#Q1-(2pts)-Write-your-2d-Stencil" data-toc-modified-id="Q1-(2pts)-Write-your-2d-Stencil-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Q1 (2pts) Write your 2d Stencil</a></span></li><li><span><a href="#The-equations-for-each-gridblock-in-the-mesh." data-toc-modified-id="The-equations-for-each-gridblock-in-the-mesh.-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>The equations for each gridblock in the mesh.</a></span><ul class="toc-item"><li><span><a href="#Row-major-numbering" data-toc-modified-id="Row-major-numbering-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Row-major numbering</a></span></li></ul></li><li><span><a href="#Q2-Writing-equations-for-each-gridblock" data-toc-modified-id="Q2-Writing-equations-for-each-gridblock-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Q2 Writing equations for each gridblock</a></span><ul class="toc-item"><li><span><a href="#Q2-(2pts)-entry-cell-below" data-toc-modified-id="Q2-(2pts)-entry-cell-below-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Q2 (2pts) entry cell below</a></span></li></ul></li><li><span><a href="#Q3-Put-your-equations-into-the-matrix" data-toc-modified-id="Q3-Put-your-equations-into-the-matrix-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Q3 Put your equations into the matrix</a></span><ul class="toc-item"><li><span><a href="#Q3-(4pts)-entry-cell-below" data-toc-modified-id="Q3-(4pts)-entry-cell-below-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>Q3 (4pts) entry cell below</a></span></li></ul></li><li><span><a href="#Q4-(4pts)-Solve-the-system-of-equations" data-toc-modified-id="Q4-(4pts)-Solve-the-system-of-equations-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Q4 (4pts) Solve the system of equations</a></span></li><li><span><a href="#Check-your-answer" data-toc-modified-id="Check-your-answer-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Check your answer</a></span></li></ul></li><li><span><a href="#Reflection" data-toc-modified-id="Reflection-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Reflection</a></span></li></ul></div>

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "d53663505c78682bf9ce40bde7af7800", "grade": false, "grade_id": "cell-de94433790126e19", "locked": true, "schema_version": 1, "solution": false}}
# # Assignment Finite volumes by hand

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "dfd95b893e8c483887e919fe49861eaa", "grade": false, "grade_id": "cell-7f386941cdae6573", "locked": true, "schema_version": 1, "solution": false}}
#
#
# ## Learning goals
# 1. Can apply the finite-volume stencil to a 2D steady-state problem, and generate the equations for each unknown in the mesh.
# 2. Can place the equations into a system matrix.
# 3. Can compute fluxes.
#
# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "be5a065707078be5674aee3a94aa1c17", "grade": false, "grade_id": "cell-ec69e54f103e4048", "locked": true, "schema_version": 1, "solution": false}}
# ## The problem
#
# Consider the two-dimensional diffusion problem below. There are zero-flux boundary conditions on the top and bottom of the domain, and prescribed concentration (more generally known as Dirichlet or first-type boundary conditions)on the to sides. Each gridblock is the same dimension $\Delta x = \Delta y = 200~m$, and $\Delta z= 3~m$ (out of the page).  The gridblock node is placed at Dirichlet (prescribed concentration) boundaries. The diffusion coefficient in each gridblock is as shown in the figure and the porosity is $\theta = 0.25$ is the same everywhere.
#
#
# <img src="figures/by_hand.png" alt="pic05" width="50%" >
#
# <br><br><br>
#
#
# ###  2-D discrete approximation stencil for steady-state diffusion. 
#
# Recall the 1D stencil looks like this.
#
# <br><br>
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) =0 \label{8fvbh1}\\
# \end{align}
#
# <br><br>
#
# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "ad76b08affaa31f70b918bbd70e5556a", "grade": false, "grade_id": "cell-11c64894ba08ce51", "locked": true, "schema_version": 1, "solution": false}}
# #### 2D stencil
#
# Change the following 1-D stencil to 2-D by adding the "N" and "S" terms.
#
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) =0 \label{8fvbh2}\\
# \end{align}
#
# You may also want to simplify your stencil for the case of constant diffusion coefficient and constant gridblock dimensions.

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "bab6a15f659657983dc0406085d9987a", "grade": false, "grade_id": "cell-aaeb99589e3d8757", "locked": true, "schema_version": 1, "solution": false}}
# ### Q1 (2pts) Write your 2d Stencil
#
# In the cell below, enter your stencil in markdown.

# %% [markdown] {"deletable": false, "nbgrader": {"checksum": "6ff2c308059342dd0bc69905833a7390", "grade": true, "grade_id": "cell-a0eeb6eaec166609", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
# YOUR ANSWER HERE

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "b822389ee3f2d32ad5dbc38d8cc8a60a", "grade": false, "grade_id": "cell-da52f03fa9ac85b8", "locked": true, "schema_version": 1, "solution": false}}
# ### The equations for each gridblock in the mesh.
# <br><br>
# How many unknowns are there? In the 2-d problem above, we have 3 rows and 4 columns so **12 unknowns** in total.
# <br><br>
# **Problem** now our mesh is two dimensional - how can we number our gridblocks and unknowns? In 1-D, we just numbered one gridblock after another:
# <br><br>
# <img src="figures/1d-numbered-grid.png" alt="pic05" width="50%" >
# <br><br>
# We eventually want to put the system of equations into a matrix that looks like this (for a 5-gridblock 1-D problem with two boundary concentrations $bc_1$ and $bc_5$)
#
# \begin{align*}
# \mathbf{Ac}&=\mathbf{b}\\
# {\begin{bmatrix} 
# 1 & 0 & 0 & 0 & 0 \\ 
# 1 & -2 & 1 & 0 & 0\\ 
# 0 & 1 & -2 & 1 & 0\\ 
# 0 & 0 & 1 & -2 & 1\\ 
# 0 & 0 & 0 & 0 & 1\\ 
# \end{bmatrix}}
# \begin{bmatrix} 
# c_1\\ 
# c_2\\ 
# c_3\\ 
# c_4\\ 
# c_5\\ 
# \end{bmatrix}
# &=\begin{bmatrix} 
# bc_1\\ 
# 0\\ 
# 0\\ 
# 0\\ 
# bc_5\\ 
# \end{bmatrix}
# \end{align*}
#
# We will have a similar matrix structure for a 2, 3 or n-dimensional problem. For a multidimensional problem, the key is to number the gridblocks in an organized way. 
# <br><br>
# #### Row-major numbering
# Python is organized so that so-called **row-major** numbering is the most efficient. That means we should number our gridblocks as shown here:
# <img src="figures/by_hand_numbered.png" alt="pic05" width="50%" >
#
# <br><br>
# Where we used the python style and gave the first gridblock the index 0. This numbering can be considered a mapping of the row, column structure to a sequential, 1-D vector of indices.
# <br><br>
# In the 2-D code you were given, we used the following function to map a gridblock index into row and column index that we used to assemble the equations in the algorithm.

# %%
import numpy as np
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


# %% [markdown]
# Let's see if it returns the proper indices for our situation where `nrows = 3` and `ncol = 4`. According to the figure, the gridblock number 6 should be in python row 1, python column 2 (a python row or column begins with index 0): 

# %%
ind = 6
nrows = 3
ncols = 4
row, column = index_to_row_col(ind, nrows, ncols)
print(f"The gridblock {ind} is in python row {row} and python column {column}")

# %% [markdown]
# ### Q2 Writing equations for each gridblock
#
# Now, write your equations using your stencil, the gridblock dimensions, diffusion coefficient and boundary conditions.
# I'll write a few (but not all) of the simple equations at the Dirichlet (specified concentration) boundaries:
#
# \begin{align*}
# &c_0 = 64\\
# &c_4 = 64\\
# &c_3= 125\\
# &c_7 = 125\\
# \end{align*}
#
# Use your stencil and write the other equations here in markdown.
# <br><br>
# **Zero-flux boundaries** 
#
# Hint: the 2-D stencil is basically just $J_{WC}+J_{EC}+J_{SC} + J_{NC}=0$. When the C gridblock is adjacent to a zero-flux boundary, one of the terms in the stencil is set to zero. For example in gridblock 1 above, we have this mapping of the stencil $\rightarrow$ gridblock index: C $\rightarrow$ 1, W $\rightarrow$ 0, N $\rightarrow$ 5, but to the S we have a zero-flux boundary. Accordingly, in the stencil for gridblock with index 1, $J_{SC}=0$ and the stencil simplifies to $J_{WC}+J_{EC}+ J_{NC}=0$.

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "ba6cd056fcde0ee3dabb99ce0099ffab", "grade": false, "grade_id": "cell-2c42cc4bc6a65d4d", "locked": true, "schema_version": 1, "solution": false}}
# #### Q2 (2pts) entry cell below

# %% [markdown] {"deletable": false, "nbgrader": {"checksum": "aa80b2001517ee6b67c38ed43baffa70", "grade": true, "grade_id": "cell-5697ad62cf1545ae", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
# YOUR ANSWER HERE

# %% [markdown]
# ### Q3 Put your equations into the matrix
#
# I've put some of the easy ones in. You do the rest by replacing the zeros in the markdown array 
# below with the correct coefficients from your equations.  Double click on this cell to get the
# raw latex formatting, then copy it below into the answer box and edit.
#
# \begin{align*} \mathbf{Ac} &= \mathbf{b}\\ 
# {\begin{bmatrix} 
# 1 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0\\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 1 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 1 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &1 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# 0 & 0 & 0 & 0 & 0 &0 &0 &0 &0 &0 &0 &0 \\
# \end{bmatrix}} 
# \begin{bmatrix} 
# c_0\\ 
# c_1\\ 
# c_2\\ 
# c_3\\ 
# c_4\\ 
# c_5\\ 
# c_6\\ 
# c_7\\ 
# c_8\\ 
# c_9\\ 
# c_{10}\\ 
# c_{11}\\
# \end{bmatrix} 
# &= \begin{bmatrix} 
# 64\\ 
# 0\\ 
# 0\\ 
# 125\\ 
# 64\\ 
# 0\\ 
# 0\\
# 125\\ 
# 0\\ 
# 0\\ 
# 0\\ 
# 0\\ 
# \end{bmatrix} \end{align*}
# <br><br>

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "1488183aa8d35e1ead5864cf56fb4f1b", "grade": false, "grade_id": "cell-054ca779a158a743", "locked": true, "schema_version": 1, "solution": false}}
# #### Q3 (4pts) entry cell below

# %% [markdown] {"deletable": false, "nbgrader": {"checksum": "7ff53e7859b58982baf8799410bd7c08", "grade": true, "grade_id": "cell-a67b164bea144ab7", "locked": false, "points": 4, "schema_version": 1, "solution": true}}
# YOUR ANSWER HERE

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "8030a7425e0b8af6fe460d3e2e32ac47", "grade": false, "grade_id": "cell-d244a601d6dfbef6", "locked": true, "schema_version": 1, "solution": false}}
# ### Q4 (4pts) Solve the system of equations
#
# You have a few options here:
# 1. Guess the answer and check if the equations are satisfied.
# 2. Use python. See how the code uses the statement `c = np.linalg.solve(A, b)`. The trick is to put your equations into numpy arrays `A` and `b`.
# <br><br> 
# To check that you have solved the equations, we ask that you report the concentrations in gridblocks 5 and 6 for autograding in the cell below. 

# %% {"deletable": false, "nbgrader": {"checksum": "12bdc96d1e4cc8792cef2c65718c4bcf", "grade": false, "grade_id": "cell-a82414d1b2a6dfdb", "locked": false, "schema_version": 1, "solution": true}}
# replace -9999 with the values of the concentration in gridblocks 5 and 6 below
# c5 = -9999
# c6 = -9999
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "8f735371eff3135b3a8a0d0b0a67fb52", "grade": true, "grade_id": "cell-d059da85a25864e9", "locked": true, "points": 4, "schema_version": 1, "solution": false}}
# Hidden test follows here.

# %% [markdown]
# ### Check your answer
#
# Take the equation for any gridblock and substitute in the concentrations you computed. Is the equation satisfied?

# %% [markdown]
# ## Reflection
# 1. Each row in the coefficient matrix has only a few non-zero coefficients. Why?
# 2. What would this system matrix look like for a 3-d discretization?
# 3. How would the python function `index_to_row_col` change for a 3-d discretization, where we now have row, columns and layers?
