# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ''
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0-rc2
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
#     version: 3.6.8
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#One-dimensional-steady-state-finite-volume-approximation" data-toc-modified-id="One-dimensional-steady-state-finite-volume-approximation-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>One dimensional steady-state finite-volume approximation</a></span><ul class="toc-item"><li><span><a href="#Problem" data-toc-modified-id="Problem-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Problem</a></span><ul class="toc-item"><li><span><a href="#Boundary-value-problem-(BVP)" data-toc-modified-id="Boundary-value-problem-(BVP)-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Boundary-value problem (BVP)</a></span></li></ul></li><li><span><a href="#Number-of-equations-=-number-of-unknowns." data-toc-modified-id="Number-of-equations-=-number-of-unknowns.-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Number of equations = number of unknowns.</a></span></li></ul></li><li><span><a href="#Gridblock-conservation-equation" data-toc-modified-id="Gridblock-conservation-equation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Gridblock conservation equation</a></span><ul class="toc-item"><li><span><a href="#One---dimensional-flux" data-toc-modified-id="One---dimensional-flux-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>One - dimensional flux</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Gridblock-with-two-neighbours" data-toc-modified-id="Gridblock-with-two-neighbours-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Gridblock with two neighbours</a></span><ul class="toc-item"><li><span><a href="#Mass-in-gridblock" data-toc-modified-id="Mass-in-gridblock-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Mass in gridblock</a></span></li><li><span><a href="#Fluxes" data-toc-modified-id="Fluxes-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Fluxes</a></span></li></ul></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Approach-to-generate-an-equation-for-each-gridblock-in-the-mesh" data-toc-modified-id="Approach-to-generate-an-equation-for-each-gridblock-in-the-mesh-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Approach to generate an equation for each gridblock in the mesh</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Example</a></span><ul class="toc-item"><li><span><a href="#Gridblock-2:" data-toc-modified-id="Gridblock-2:-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>Gridblock 2:</a></span></li></ul></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Your turn</a></span><ul class="toc-item"><li><span><a href="#Gridblock-3:" data-toc-modified-id="Gridblock-3:-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>Gridblock 3:</a></span></li><li><span><a href="#Gridblock-4:" data-toc-modified-id="Gridblock-4:-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Gridblock 4:</a></span></li></ul></li></ul></li><li><span><a href="#Boundary-gridblocks" data-toc-modified-id="Boundary-gridblocks-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Boundary gridblocks</a></span><ul class="toc-item"><li><span><a href="#Boundary-conditions" data-toc-modified-id="Boundary-conditions-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Boundary conditions</a></span><ul class="toc-item"><li><span><a href="#Prescribed-concentration-boundary-condition" data-toc-modified-id="Prescribed-concentration-boundary-condition-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Prescribed concentration boundary condition</a></span></li><li><span><a href="#Number-of-equations-=-number-of-unknowns?" data-toc-modified-id="Number-of-equations-=-number-of-unknowns?-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Number of equations = number of unknowns?</a></span></li></ul></li></ul></li><li><span><a href="#Reflection" data-toc-modified-id="Reflection-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Reflection</a></span></li><li><span><a href="#Next-steps" data-toc-modified-id="Next-steps-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Next steps</a></span></li></ul></div>
# %% [markdown]
# ## One dimensional steady-state finite-volume approximation
#
#
# ### Problem
#
# Recall that our problem is to compute the steady-state sulfate concentration profile with depth in the top two meters of tailings at the bottom of the TMF under the assumptions that:
#
# * the TMF pond has a large surface area, and we are computing the profile in the middle of the TMF away from the edge.
# * the concentration in the water in the TMF pond does not change in time and is fixed at $c=93~mg/L$
# * the concentration at $2~m$ depth in the sediments does not change in time and is fixed at $c=2000~mg/L$
# * sulfate is not produced in the top $2~m$ of the tailings.
# * sulfate moves by diffusion only.
#
# We are going to compute a discrete approximation using a set of gridblocks aligned in the vertical direction. We will compute the concentration of sulfate at the center of each gridblock. Then we can interpolate between points to give us an approximate value at any point in the vertical direction.
#
# <img src="figures/tailings_diffusion_w_grid.png" style="width: 456px;" >
#
# #### Boundary-value problem (BVP)
#
# Can we even solve this problem? Our diffusion problem is an example of a class of problems called **boundary value problems** where the goal is to determine the value of the dependent variable (here, concentration) inside the problem domain when we know the dependent variable  or its derivative(s) on the boundary of the domain. We'll revisit this later when we relate the discrete approximation to a partial differential equation.
#
#
# ### Number of equations = number of unknowns.
#
# Common sense tell us that if our grid contains $n$ unknown values of concentration, one at the center of each gridblock (sometimes called nodes, or gridpoints), then we need $n$ equations to uniquely determine those $n$ unknown values. How? You probably guessed, it must have something to do with conservation principles.
#
# We will number each gridblock and each concentration in the grid: $c_1$ will be the concentration at the node in gridblock 1, $c_2$,
# will be the concentration at the node in gridblock 2, $\ldots$, $c_n$ will be the concentration at the node in gridblock n.
#
#
#
# ## Gridblock conservation equation
#
# We start by considering a single gridblock of size $\Delta x$, $\Delta y$ and $\Delta z$
#
# <img src="figures/xyz_single_block.png" style="width: 263px;" >
#
# ### One - dimensional flux
#
# Let's consider the case where mass (like sulfate) is moving into and out of the gridblock on the "E" and "W" faces only as shown below:
#
#
# <img src="figures/single_block_flux.png" style="width: 300px;" >
#
#
#
# Let's define $J_{E}~\left[M\over T\right]$ as the total mass flux on the "E" side  and  $J_{W}~\left[M\over T\right]$ as the total mass flux on the "W" side. Let $m_C(t)~\left[M\right]$ be the mass inside the gridblock "C" at time $t$ (**remember, our convention is that fluxes are positive for flux into the volume**).
#
#
#
# ### Your turn
# Write in words the meaning of the following equation
#
# \begin{align}
# \Delta m_C = m_C(t+\Delta t) - m_C(t) & = (J_E+J_W)\Delta t \label{1dcons}\\
# \end{align}
#
#
#
#
# %% [markdown]
# Your answer here
# %% [markdown]
# ### Your turn
#
# What is the equation if the mass in the gridblock is not changing in time?
# %% [markdown]
# Your answer here
# %% [markdown]
# In words, if the mass in the gridblock is not changing in time, them the **net** rate at which mass is flowing into the gridblock must equal zero.
#
# ### Gridblock with two neighbours
#
# Now let's look a small section of a 1-D grid, where gridblock "C" is connected to gridblock "E" and "W" as shown here
# <img src="figures/finite_volume_1d_uniform_noxyz.png" style="width: 380px;" >
#
# #### Mass in gridblock
# * $m_W$ is the mass in gridblock W ("West")
# * $m_C$ is the mass in gridblock C ("Center")
# * $m_E$ is the mass in gridblock E ("East")
#
# #### Fluxes
# Define fluxes:
# * $J_{WC}~\left[M\over T\right]$ as the total mass flux between the W and C gridblocks (positive if mass is entering C).
# * $J_{EC}~\left[M\over T\right]$ as the total mass flux between the E and C gridblock (positive if mass is entering C).
#
# The mass conservation statement for gridblock C over time period $\Delta t$ is then
#
# \begin{align*}
# m_C(t+\Delta t) - m_C(t) & = \left(J_{EC}+J_{WC}\right)\Delta t \\
# \end{align*}
#
#
#
#
# ### Your turn
# Write the **steady-state** mass conservation equation for gridblock C. How does this compare to the equation for the three tanks?
# %% [markdown]
# Your answer here
# %% [markdown]
# ### Approach to generate an equation for each gridblock in the mesh
#
# 1. Write a discrete approximation for mass conservation for gridblock C. This equation is the fundamental stencil.
# 2. Apply this stencil to each gridblock in the grid to generate a unique equation for each gridblock in the grid.
#
# For n gridblocks, we can generate n equations.
#
# <img src="figures/1d-numbered-grid.png" style="width: 380px;" >
#
# ### Example
#
# Consider a grid with 5 gridblocks. From your answer above, the steady-state 1-d finite volume equation for gridblock C is $J_{WC}+J_{EC}=0$.
#
# We can apply the stencil to the interior gridblocks of our 5 - gridblock example. Let's start with gridblock 2. We align the stencil so that C corresponds to gridblock 2:
#
# <img src="figures/block2_eq.png" style="height: 110px;" >
#
# You see then that in the stencil equation $J_{WC}+J_{EC}=0$, we replace C with 2, W with 1 and E with 3, so we have:
# #### Gridblock 2:
#
# \begin{align}
# J_{12} + J_{32} = 0\\
# \end{align}
#
# ### Your turn
#
# Replace the steady-state finite volume stencil equation for gridblock C with the correct equation for gridblock 3, and gridblock 4.
#
#
# %% [markdown]
# #### Gridblock 3:
# <img src="figures/block3_eq.png" style="height: 110px;">
#
# Change the following stencil equation to the correct equation for gridblock 3.
# $$
# J_{WC}+J_{EC} =0
# $$
#
# %% [markdown]
# #### Gridblock 4:
# <img src="figures/block4_eq.png" style="height: 110px;" >
#
# Change the following stencil equation to the correct equation for gridblock 4.
# $$
# J_{WC}+J_{EC} =0
# $$
#
# %% [markdown]
# ## Boundary gridblocks
#
# We now have generated one equation for the interior gridblocks 2, 3 and 4. But for a grid with 5 gridblocks don't we need 5 equations? What about the boundary gridblocks 1 and 5?
#
# ### Boundary conditions
#
# There are two types of boundary conditions associated with diffusion problems:
# 1. The concentration is known at the boundary. This is called a prescribed concentration boundary condition.
# 2. The flux is known at the boundary. This is called a prescribed flux boundary.
#
# We'll deal with prescribed concentration boundary conditions here, and revisit prescribed flux later.
#
# #### Prescribed concentration boundary condition
#
# Say we know the concentration at the two boundaries. Since gridblocks 1 and 5 lie on the boundary, the concentrations in those gridblocks have to be the same as the boundary condition concentrations.
# <img src="figures/5node-const-c-bc.png" style="height: 110px;" >
#
# That is, the concentrations in gridblocks 1, and 5 are known.
#
# #### Number of equations = number of unknowns?
#
# How many equations do we have? How many unknowns?
#
# %% [markdown]
# ## Reflection
# What have you learned? What have you struggled with? Some thoughts below. Reflect on anything else you have learned or struggled with and write it here.
# * we can write a finite-volume expression for the instantaneous change in mass in a gridblock
# * we developed a stencil for 1-d steady-state finite volume
# * we used the stencil to develop one equation for each interior gridblock in the grid
# * we used specified concentration boundary conditions to determine the concentrations in the boundary gridblocks
# * we have not yet learned how to use specified flux boundary conditions
# * our equations for interior gridblocks are in terms of fluxes, $J$, not concentrations.
#
# ## Next steps
# We will next use the principles of diffusion to replace fluxes such as $J_{12}$ with expressions in terms of concentrations in gridblocks. To do that, we need to look at Fick's law of diffusion, which we will do next.
#
