# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Transient-problem" data-toc-modified-id="Transient-problem-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Transient problem</a></span></li><li><span><a href="#Initial-conditions" data-toc-modified-id="Initial-conditions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Initial conditions</a></span><ul class="toc-item"><li><span><a href="#Save-these-into-a-dict-for-later-use" data-toc-modified-id="Save-these-into-a-dict-for-later-use-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Save these into a dict for later use</a></span></li></ul></li><li><span><a href="#Transient-behavior" data-toc-modified-id="Transient-behavior-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Transient behavior</a></span></li></ul></div>
# %% [markdown]
# # Introduction
# %% [markdown]
# Let us recall that $J_{EC}$ and $J_{WC}$ represent the flux of mass [M/T] towards the center. If these are positive, the mass in the center will increase. If there is a source of mass in the center, the mass will increase as well. Therefore, the steady-state equation writes:
#
# \begin{equation}
# J_{EC}+J_{WC} + Q = 0
# \end{equation}
#
# With Q being written in terms of mg/s (Q: [M/T]) . Therefore mass balance equation with a source term writes:
#
# \begin{equation}
# \left( -2  \frac{D\theta}{\Delta x} c_{\left[i\right]}  + \frac{D\theta}{\Delta x}c_{\left[i-1\right]} +   \frac{D\theta}{\Delta x} c_{\left[i+1\right]} \right) \Delta y \Delta z  + q  \Delta x \Delta y \Delta z = 0
# \end{equation}
#
# with $q$ being the volumetric source ([M/T/L$^3$])
#
# We can rearrange the latter equation as:
#
# \begin{equation}
# \left( 2\frac{D\theta}{\Delta x} c_{\left[i\right]}  - \frac{D\theta}{\Delta x}c_{\left[i-1\right]} -   \frac{D\theta}{\Delta x} c_{\left[i+1\right]} \right) \Delta y \Delta z  = q  \Delta x \Delta y \Delta z
# \end{equation}
#
# We can also divide everything by $\Delta x \Delta y \Delta z$:
#
# \begin{equation}
# \frac{1}{\Delta x} \left( 2\frac{D\theta}{\Delta x} c_{\left[i\right]}  - \frac{D\theta}{\Delta x}c_{\left[i-1\right]} -   \frac{D\theta}{\Delta x} c_{\left[i+1\right]} \right)   = q
# \end{equation}
#
# which gives
# \begin{equation}
# 2\frac{D\theta}{\Delta x^2} c_{\left[i\right]}  - \frac{D\theta}{\Delta x^2}c_{\left[i-1\right]} -   \frac{D\theta}{\Delta x} c_{\left[i+1\right]}  = q
# \end{equation}
# %%
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML

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
def Build_1D_Inhomo_Matrix_Source(bc_left, bc_right, n, D, Width, poro, q):
    """
    Constructs a coefficient matrix and an array with varying diffusion coefficient and a source term
    Parameters:
    --------------
    bc_left: (float)  left boundary condition
    bc_right: (float) right boundary conditions
    n (int): amounts of cells
    D (float array): values of the diffusion coefficient
    Width (float): Total phyiscal width of the domain
    poro (float): porosity value
    q (float array): volumetric source term (mg/L/s)
    Returns the matrix A, and the array b to solve the
    discretized 1D diffusion problem Ax = b

    ----------
    """
    Matrix = np.zeros((n, n))
    RHS = np.zeros(n)
    dx = Width / (n - 1)
    coef = poro / dx / dx
    for i in range(n):
        if i == 0:
            RHS[i] = bc_left
            Matrix[i][i] = 1
        elif i == n - 1:
            RHS[i] = bc_right
            Matrix[i, i] = 1
        else:
            RHS[i] = q[i]
            East = coef * avg(D[i], D[i + 1])
            West = coef * avg(D[i], D[i - 1])
            Matrix[i, i] = East + West
            Matrix[i, i + 1] = -East
            Matrix[i, i - 1] = -West
    return Matrix, RHS


# %%
c_left = 1
c_right = 0
n = 50
Diff = 2e-9
D = Diff * np.ones(n)
Q = np.zeros(n)
Q[int(n / 4) : int(n / 2)] = 5e-9  # mg/L/s
Width = 2
poro = 0.4

x = np.linspace(0, Width, n)
A, b = Build_1D_Inhomo_Matrix_Source(c_left, c_right, n, D, Width, poro, Q)

c_final = np.linalg.solve(A, b)
plt.plot(x, c_final, label="Concentration")
plt.xlabel("x-axis (m)")
plt.ylabel("Concentration (mg/L)")

# %% [markdown]
# # Transient problem
#
# The transient problem will solve the evolution of the concentration until it reaches the steady-state solved before. We have to define first initial conditions (let's say concentration  is zero everywhere).

# %% [markdown]
# # Initial conditions

# %%
c_left = 1
c_right = 0
n = 50
Diff = 2e-9
D = Diff * np.ones(n)
q = np.zeros(n)
q[int(n / 4) : int(n / 2)] = 5e-9  # mg/L/s
Width = 2
poro = 0.4
nTstp = 200
dt = 1.0e7

c_init = np.zeros((nTstp, n))


# %% [markdown]
# ## Save these into a dict for later use

# %%
init_dict = dict(
    c_left=c_left,
    c_right=c_right,
    c_init=c_init,
    n=n,
    Diff=Diff,
    D=D,
    q=q,
    Width=Width,
    poro=poro,
    nTstp=nTstp,
    dt=dt,
)


# %% [markdown]
# The transient behavior that we have discussed in the previous notebook simply adds these terms to the previous equation.
#
# \begin{equation}
# J_{EC}+J_{WC} + Q = \frac{dm}{dt}
# \end{equation}
#
# Using the same developements expressed before, using
#
# \begin{equation}
# \frac{d\theta c}{dt} = \theta \frac{c(t+\Delta t) - c(t)}{\Delta t}
# \end{equation}
#
# \begin{equation}
# \frac{\theta c_{\left[i\right]}}{\Delta t} + 2\frac{D\theta}{\Delta x^2} c_{\left[i\right]}  - \frac{D\theta}{\Delta x^2}c_{\left[i-1\right]} -   \frac{D\theta}{\Delta x} c_{\left[i+1\right]}  = q + \frac{\theta c_{\left[i\right]}(old)}{\Delta t}
# \end{equation}
#
# So we can solve this problem by using the same matrixes used before, but we need to add extra terms.

# %%
x = np.linspace(0, Width, n)
A, b = Build_1D_Inhomo_Matrix_Source(c_left, c_right, n, D, Width, poro, Q)

c_final = np.linalg.solve(A, b)
plt.plot(x, c_final, label="Concentration")
plt.xlabel("x-axis (m)")
plt.ylabel("Concentration (mg/L)")


# %% [markdown]
# # Transient behavior

# %%
def calc_conc(
    Diff=None,
    D=None,
    Width=None,
    c_left=None,
    c_right=None,
    poro=None,
    q=None,
    c_init=None,
    n=None,
    nTstp=None,
    dt=None,
):

    x = np.linspace(0, Width, n)
    A, b = Build_1D_Inhomo_Matrix_Source(c_left, c_right, n, D, Width, poro, q)

    c = c_init
    Abis = np.zeros((n, n))
    Bbis = np.zeros(n)
    for t in range(nTstp - 1):
        for i in range(n):
            Abis[i][i] = 0
            Bbis[i] = 0
        Aa = A + Abis
        bb = b + Bbis
        cnew = np.linalg.solve(Aa, bb)
        c[t + 1][:] = cnew
    return x, c


x, c = calc_conc(**init_dict)

plt.plot(x, c_final, label="Asymptotic concentration")
plt.plot(x, c[0][:], label="Initial concentration")
plt.plot(x, c[10][:], label="Concentration after 10 timestep")
plt.plot(x, c[30][:], label="Concentration after 30 timesteps")
plt.plot(x, c[60][:], label="Concentration after 60 timesteps")
plt.plot(x, c[nTstp - 1][:], label="Concentration after 100 timesteps")
plt.xlabel("x-axis (m)")
plt.ylabel("Concentration (mg/L)")
plt.legend()


# %%
def make_animation(init_dict):
    image_list = []
    x, c = calc_conc(**init_dict)
    fig, ax = plt.subplots()
    ax.set_xlim((0, 2.0))
    ax.set_ylim((0, 2.0))
    nsteps, nvals = c.shape
    for index in range(nsteps):
        line = ax.plot(x, c[index, :], "r-", lw=2)
        image_list.append(line)
    return fig, image_list


fig, image_list = make_animation(init_dict)


# %%

anim = animation.ArtistAnimation(
    fig, image_list, interval=50, blit=True, repeat_delay=1000
)

# %%
HTML(anim.to_html5_video())

# %%
