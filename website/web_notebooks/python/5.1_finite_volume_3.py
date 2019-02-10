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
#     toc_position:
#       height: calc(100% - 180px)
#       left: 10px
#       top: 150px
#       width: 305.526px
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#One-dimensional-steady-state-finite-volume-approximation" data-toc-modified-id="One-dimensional-steady-state-finite-volume-approximation-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>One dimensional steady-state finite-volume approximation</a></span><ul class="toc-item"><li><span><a href="#Summary-to-this-point" data-toc-modified-id="Summary-to-this-point-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Summary to this point</a></span></li><li><span><a href="#Fick's-law-of-diffusion" data-toc-modified-id="Fick's-law-of-diffusion-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Fick's law of diffusion</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Fick's-law-of-diffusion-of-solutes-in-porous-media" data-toc-modified-id="Fick's-law-of-diffusion-of-solutes-in-porous-media-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Fick's law of diffusion of solutes in porous media</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Your turn</a></span><ul class="toc-item"><li><span><a href="#Aside:-Gradients-in-3-dimensions" data-toc-modified-id="Aside:-Gradients-in-3-dimensions-1.8.1"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>Aside: Gradients in 3 dimensions</a></span></li></ul></li><li><span><a href="#Gridblock-fluxes-in-terms-of-concentrations" data-toc-modified-id="Gridblock-fluxes-in-terms-of-concentrations-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Gridblock fluxes in terms of concentrations</a></span><ul class="toc-item"><li><span><a href="#1-Total-fluxes-as-specific-fluxes" data-toc-modified-id="1-Total-fluxes-as-specific-fluxes-1.9.1"><span class="toc-item-num">1.9.1&nbsp;&nbsp;</span>1 Total fluxes as specific fluxes</a></span></li></ul></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Your turn</a></span><ul class="toc-item"><li><span><a href="#2-Specific-fluxes-in-terms-of-Fick's-law" data-toc-modified-id="2-Specific-fluxes-in-terms-of-Fick's-law-1.11.1"><span class="toc-item-num">1.11.1&nbsp;&nbsp;</span>2 Specific fluxes in terms of Fick's law</a></span></li><li><span><a href="#3-Discrete-approximation-for-Fick's-law" data-toc-modified-id="3-Discrete-approximation-for-Fick's-law-1.11.2"><span class="toc-item-num">1.11.2&nbsp;&nbsp;</span>3 Discrete approximation for Fick's law</a></span></li><li><span><a href="#What-is-a-reasonable-way-to-do-this?" data-toc-modified-id="What-is-a-reasonable-way-to-do-this?-1.11.3"><span class="toc-item-num">1.11.3&nbsp;&nbsp;</span>What is a reasonable way to do this?</a></span></li></ul></li><li><span><a href="#Putting-it-all-together" data-toc-modified-id="Putting-it-all-together-1.12"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>Putting it all together</a></span></li><li><span><a href="#Reflection" data-toc-modified-id="Reflection-1.13"><span class="toc-item-num">1.13&nbsp;&nbsp;</span>Reflection</a></span></li></ul></li></ul></div>
# %% [markdown]
# ## One dimensional steady-state finite-volume approximation
#
# ### Summary to this point
#
# We have developed a 1-D stencil for a gridblock C to generate an steady-state equation for each interior gridblock:
# \begin{align*}
# \left(J_{EC}+J_{WC}\right) &= 0 \\
# \end{align*}
#
#
# <img src="figures/finite_volume_1d_uniform_noxyz.png" style="width: 190px;" >
#
# where the gridblocks are sized $\Delta x$, $\Delta y$, $\Delta z$
#
# <img src="figures/xyz_single_block.png" style="width: 132px;" >
#
# We use the stencil to generate the equations for a simple 5 - gridblock example:
#
#
# <img src="figures/5node-const-c-bc.png" style="height: 110px;" >
#
# We generated the following equations:
#
#  | Gridblock  | Equation      |
#   |:----------:|:--------------:|
#   | 1  | $$c_1 = 2000$$|
#   | 2  | $$\left(J_{12}+J_{32}\right) = 0$$|
#   | 3  | $$\left(J_{23}+J_{43}\right) = 0$$|
#   | 4  | $$\left(J_{34}+J_{54}\right) = 0$$|
#  | 5  | $$c_5 = 93$$|
#
#  Recall, the equations for gridblock 1 and 5 came from the boundary conditions.
#
#  **Next**: we need to represent the fluxes such as $J_{12}$ in terms of the dependent variable of interest - concentration. We do that with Fick's law of diffusion.
# %% [markdown]
# ### Fick's law of diffusion
#
# **Concept**: solutes (dissolved substances) move from areas of high concentration to areas of low concentration. (Why?)
#
# <img src="figures/diffusing.png" style="height: 110px;" >
#
# Intuition:
# * rate of diffusion is proportional to gradient in concentration
# * mass flows from high concentrations towards lower concentrations
#
#
# $$ flux \propto {dc\over dx}~\left[{M/L^3 \over L}\right]$$
#
# ***Fick's law*** (the x component)
#
# \begin{align*}
# j_x = - D {\partial c\over \partial x}\\
# \end{align*}
#
# where
# * $j_x~\left[{M\over L^2 T}\right]$ is the x-component of the **specific mass flux**,
# * $D$ is the **diffusion coefficient** and
# * $\partial c\over \partial x$ is the x-component of the gradient in concentration.
#
#
# ### Your turn
#
# Why the minus sign in Fick's law?
#
#
# %% [markdown]
# <div class="alert alert-info">
# Your answer here
# </div>
# %% [markdown]
# ### Your turn
# What are the dimensions of the diffusion coefficient?
# %% [markdown]
# <div class="alert alert-info">
# Your answer here
# </div>
# %% [markdown]
# ### Your turn
#
# What is the magnitude (value) of the concentration gradient?
#
# <img src="figures/diff_example_1d.png" style="width: 212px;" >
# %% [markdown]
# <div class="alert alert-info">
# Your answer here
# </div>
# %% [markdown]
# ### Your turn
#
# 1. What is the direction of the concentration gradient?
# 2. What is the direction in which solutes are diffusing?
# %% [markdown]
# <div class="alert alert-info">
# Your answer here
# </div>
# %% [markdown]
#
# ### Fick's law of diffusion of solutes in porous media
#
# We have to modify Fick's law slightly to apply to porous media. We need to introduce **porosity** to account for the fact that diffusion only occurs in the pore space.
#
# \begin{align*}
# j_x = - D \theta {\partial c \over \partial x}\\
# \end{align*}
#
# where
# * $\theta ~\left[{\cdot}\right]$ is the  **porosity** (dimensionless)
#
#
#
# %% [markdown]
# ### Your turn
#
# Now let's compute the flux. Consider the same problem as above, where the diffusion coefficient is $D=10^{-10}~m^2/s$, and the porosity is $\theta = 0.3$.
#
# If the area perpendicular to this flux direction is $4\times10^4~m^2$ (the area of the bottom of a modest tailings pond), how much mass is transported by diffusion in one day?
# <img src="figures/diff_example_1d.png" style="width: 106px;" >
#
# Recall, that the specific flux $j$ is the mass flux of solute per unit area per unit time and that $J=jA$, where $A$ is the area normal to (perpendicular to) the component of flux.
#
# <img src="figures/flux_normal-area.png" style="width: 100px;" >
#
# You can use the python cell below to compute the answer.
# %%
# here you can use python to compute the flux using the information given above
# %% [markdown]
# <div class="alert alert-warning">
#
# #### Aside: Gradients in 3 dimensions
#
# The gradient is a vector that points in the direction that a function is *increasing*. In Cartesian coordinates, it has $x$, $y$ and $z$ components. The diffusive flux is a vector that points in the direction that concentration is *decreasing*. Hence the minus sign in Fick's law. So the diffusive flux is also a vector:
# \begin{align}
# j_x &= - D\theta {\partial c \over \partial x}\\
# j_y &= - D\theta {\partial c\over \partial y}\\
# j_z &= - D\theta {\partial c\over \partial z}\\
# \end{align}
#
# We've switched to partial derivatives only to indicate that the concentration is a function of several independent variables ($x$, $y$, and $z$). We'll be pretty loose with our partials and non-partials (impartials??!), but it is almost always clear from the context what is meant.
#
#
# </div>
# %% [markdown]
# ### Gridblock fluxes in terms of concentrations
#
# We'll do this in three steps:
# 1. We'll write the total fluxes in terms of specific fluxes.
# 2. We'll write specific fluxes in terms of Fick's law.
# 3. We'll introduce a discrete approximation for Fick's law.
#
# ####  1 Total fluxes as specific fluxes
#
# Let's look at our stencil equation:
# $$
# J_{WC}+J_{EC} =0
# $$
#
# First, let's express the total fluxes in terms of specific fluxes:
#
# $$J_{WC}=j_{WC}A$$
#
# ### Your turn
#
# <img src="figures/jwc-numbers.png" style="width: 200px;" >
#
# What is the correct value of the area $A$ to write $J_{WC}$ in terms of $j_{WC}$ for this example?
#
# %% [markdown]
# <div class="alert alert-info">
# Your answer here
#
# $A=   $
#
# </div>
# %% [markdown]
# ### Your turn
#
#
# <img src="figures/jwc-general.png" style="width: 200px;" >
#
# What is the correct value of the area $A$ to write $J_{WC}$ in terms of $j_{WC}$ for the general case above?
#
# %% [markdown]
# <div class="alert alert-info">
# Your answer here
#
# $A=   $
#
#
# (remember to write $\Delta$, use `$\Delta $` - or don't bother with math type.
#
# </div>
#
# %% [markdown]
# #### 2 Specific fluxes in terms of Fick's law
#
# For a gridblock C oriented as below, what is the appropriate component of Fick's law?
#
# <img src="figures/jwc-general.png" style="width: 200px;" >
#
# Choose one of (erase the two that are incorrect):
# \begin{align}
# j_x &= - D\theta{\partial c \over \partial x}\\
# j_y &= - D \theta{\partial c\over \partial y}\\
# j_z &= - D\theta {\partial c\over \partial z}\\
# \end{align}
#
#
#
# %% [markdown]
# #### 3 Discrete approximation for Fick's law
#
# We need a way to approximate specific fluxes such as $j_x = - D\theta {\partial c \over \partial x}$ in terms of concentrations at nodal values in the centre of gridblocks as shown below.
#
# <img src="figures/1d_stencil_w_nodes.png" style="width: 200px;" >
#
# #### What is a reasonable way to do this?
# %% [markdown]
# Describe in words how you would approach this.
# %% [markdown]
# ### Putting it all together
#
# Can you use the three steps above to re-write the stencil
#
# $$
# J_{WC}+J_{EC} =0
# $$
#
# In terms of concentration? We'll reveal the answer next...
#
#
# ### Reflection
#
# What have you learned? What have you struggled with? Some thoughts below. Reflect on anything else you have learned or struggled with and write it here.
#
# %%
