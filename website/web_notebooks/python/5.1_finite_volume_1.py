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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-to-finite-volume-methods-and-partial-differential-equations" data-toc-modified-id="Introduction-to-finite-volume-methods-and-partial-differential-equations-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to finite-volume methods and partial differential equations</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Roadmap" data-toc-modified-id="Roadmap-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>Roadmap</a></span></li><li><span><a href="#Conservation-principles" data-toc-modified-id="Conservation-principles-1.0.2"><span class="toc-item-num">1.0.2&nbsp;&nbsp;</span>Conservation principles</a></span></li><li><span><a href="#A-note-about-notation" data-toc-modified-id="A-note-about-notation-1.0.3"><span class="toc-item-num">1.0.3&nbsp;&nbsp;</span>A note about notation</a></span></li></ul></li><li><span><a href="#Learning-goals" data-toc-modified-id="Learning-goals-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Learning goals</a></span></li><li><span><a href="#Conservation-principles-revisited" data-toc-modified-id="Conservation-principles-revisited-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Conservation principles revisited</a></span><ul class="toc-item"><li><span><a href="#Simplest-conservation-statement" data-toc-modified-id="Simplest-conservation-statement-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Simplest conservation statement</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Sign-conventions" data-toc-modified-id="Sign-conventions-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Sign conventions</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Instantaneousness" data-toc-modified-id="Instantaneousness-1.2.5"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>Instantaneousness</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.6"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.7"><span class="toc-item-num">1.2.7&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Connected-volumes---specific-case" data-toc-modified-id="Connected-volumes---specific-case-1.2.8"><span class="toc-item-num">1.2.8&nbsp;&nbsp;</span>Connected volumes - specific case</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.9"><span class="toc-item-num">1.2.9&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Connected-volumes---general-case" data-toc-modified-id="Connected-volumes---general-case-1.2.10"><span class="toc-item-num">1.2.10&nbsp;&nbsp;</span>Connected volumes - general case</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.11"><span class="toc-item-num">1.2.11&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-1.2.12"><span class="toc-item-num">1.2.12&nbsp;&nbsp;</span>Your turn</a></span></li></ul></li><li><span><a href="#Reflection" data-toc-modified-id="Reflection-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Reflection</a></span></li><li><span><a href="#On-to-finite-volumes!" data-toc-modified-id="On-to-finite-volumes!-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>On to finite volumes!</a></span></li></ul></li></ul></div>
# %% [markdown]
# # Introduction to finite-volume methods and partial differential equations
#
# We are ready to do some fun stuff! We are going to show you the fundamental principles of many of the numerical models used in the earth sciences such as
# * heat flow
# * contaminant transport
# * fluid flow
#     * groundwater
#     * river (surface water)
#     * the atmosphere (climate and weather)
#
#     <img src="figures/gcm_grid_creat_commons.png" style="width: 354px;">
#     Figure from creative commons.
#
# ### Roadmap
#
# We are going to develop a numerical model to compute the steady-state sulfate concentration profile with depth in the top two meters of tailings at the bottom of the TMF. We will assume for this problem that:
#
# * the TMF pond has a large surface area, and we are computing the profile in the middle of the TMF away from the edge.
# * the concentration in the water in the TMF pond does not change in time and is fixed at $c=93~mg/L$
# * the concentration at $2~m$ depth in the sediments does not change in time and is fixed at $c=2000~mg/L$
# * sulfate is not produced in the top $2~m$ of the tailings.
# * sulfate moves by diffusion only.
#
# <img src="figures/tailings_diffusion.png" style="width: 456px;" >
#
# This is a simplification of reality - we can introduce more complexity later.
#
# ### Conservation principles
# You will see that these models are based on the same general approach: divide a region of interest into
# connected volumes (often called gridblocks), and track how a quantity such as energy or a contaminant moves from
# one volume to the next (the flux of the quantity) and how it is produced or consumed inside each volume.
# Tracking flux into and production/consumption within the volume through
# time allows us to determine how the amount of the quantity is changing within the volume through time. This is the **conservation principle**.
#
# We can apply the conservation principle to:
#
#
#   | Quantity  | Flux |
#   |:----------:|:--------:|
#   | Thermal energy | heat|
#  |electrical charge | electrical current |
#    | mass | chemical flux|
#   | water | water flux |
#
#
# We've already done this for water and sulfate - both examples of the conservation of mass. We'll show you how the
# conservation principle can be written as *algebraic*, *differential* and *integral* expressions, and how these expressions
# are fundamentally the same thing.
#
#
# %% [markdown]
# ### A note about notation
# A common roadblock that students encounter is mathematical notation. You'll need
# to recognize and read some new mathematical notation that we'll be introducing. It is complex but not difficult.
# And while the conservation statements may look daunting in differential or integral notations, their essense is the same as that in the
# simple TMF model.
#
#
#
#
# ## Learning goals
# 1. Be able to identify the components of a conservation statement.
# 2. Be able to write a general conservation equation for a single defined volume (control volume) in terms of:
#  * the flux of a quantity across the boundary into a volume,
#  * the rate at which the quantity is produced or consumed internal to the volume;
#  * the rate at which the amount of the quantity is changing in the volume.
# 3. Be able to write a conservation equation for a group of connected volumes in terms of:
#  * the flux of a quantity across the boundary into each volume,
#  * the rate at which the quantity is produced or consumed internal to the volume;
#  * the rate at which the amount of the quantity is changing in the volume.
# 4. Be able to recognize conservation expressions written in algebraic, integral and differntial notations.
# 5. Be able to develop a finite-volume stencil for a one-dimensional conservation law.
# 6. Be able to derive the differential equation from the finite-volume stencil by taking the limit of the volume to a point.
# 7. Be able to use the finite-volume stencil to develop a discrete approximation for a spatially distributed conservation
# problem defined on a grid of connected finite volumes.
#
#
# %% [markdown]
# ## Conservation principles revisited
#
# We used the principle of conservation mass  to compute the volume of water in the TMF:
#
# <img src="figures/tmf_water.png" style="width: 402px;" >
#
#
#
# %% [markdown]
# In the cell below, enter *in words* a statement about the **conservation of mass** over a time period $\Delta t$ for the TMF:
#
# %% [markdown]
# Enter your statement in words here (edit the cell):
#
# %% [markdown]
# ### Simplest conservation statement
#
# If we define $\Delta m$ $\left[{M}\right]$ as the change in mass in the TMF over time $\Delta t$ $\left[{T}\right]$, and $m_{in}$ $\left[{M}\right]$, $m_{out}$ $\left[{M}\right]$ as the masses that entered and exited the TMF over $\Delta t$, then an expression for the conservation of mass over time $\Delta t$ is
#
# \begin{align}
# \Delta m  &= m_{in} - m_{out} \label{eq1} \\
# \end{align}
#
# #### Dimensions
# Recall the square brackets notation $\left[ \cdot \right]$ is used to indicate the dimension of the term preceding it.
# The basic dimensions are mass $M$, time $T$, length $L$ and temperature $\Theta$. It is permissible to compare, equate, add or subtract only those physical quantities that have the same dimensions. In other words, every term in an expression describing a physical system must have the same dimesions.
#
# #### Fluxes
#
# In equation $\ref{eq1}$, each term is a **mass**. To take this concept further, it is useful to rewrite equation $\ref{eq1}$ in terms of **fluxes** and **rates**. What the flux?
#
# A **flux** is something that flows through a surface or substance.  In our example, we can conceive of the water (or sulfate) as flowing across the boundary of the TMF (our control volume). The rate at which the mass flows across the boundary is a **mass flux**.
#
# Fluxes are typically defined in two ways:
#
# * as a **total flux**, which is the rate that the total amount of a quantity enters a volume.
# * as a **specific flux**, which is the rate per unit area of boundary that a quantity enters a volume.
#
# **Example**: mass is entering a volume at the rate of $30~kg/s$. The area of the boundary that is crossed to enter the volume is $10~m^2$. Then:
# * the total flux $J=30~kg/s$.
# * the specific flux $j=3~kg/(s\cdot m^2)$.
#
# More generally, $J= {j A}$, where $A$ is the area normal to the direction that a quantity enters the volume:
#
# <img src="figures/flux_normal-area.png" style="width: 200px;" >
#
#
# So if over the time period $\Delta t$ a mass of $m_{in}$ flowed into the TMF,
# the **total mass flux**, $J_{m~{in}} ~ \left[{M\over T}\right] $ is
#
# \begin{align}
# J_{m~in} &= {\Delta m_{in}\over \Delta t} \label{eq2}\\
# \end{align}
#
# ##### Notation nation
#
# * ${J}$ is notation for the total flux.
# * $j$ is notation for a specific flux.
# * ${J_m}$ is notation for a total *mass* flux.
# * $J_{m~in}$ is notation for the total *mass flux in*.
# * $\left[{M\over T}\right]$ is notation that can be read to say *the dimensions of the term(s) preceding this are mass, $M$, over time, $T$*.
#
#
# ### Your turn
# In the next cell, write the TMF mass conservation equation $\ref{eq1}$ in terms of total mass fluxes $J$. Hint: divide the equation by $\Delta t$.
#
#
#
# %% [markdown]
# Write your equation in this cell (double click to edit the cell).
#
# Markdown help: to get $J_{m~in}$, and $\Delta t$ you write `$J_{m~in}$` and `$\Delta t$` in markdown.
# %% [markdown]
# ### Sign conventions
#
# As will be clearer later, fluxes, unlike mass, have magnitude and direction - they are vectors. The sign of the flux is used to indicate its direction.
#
# When we write our conservation expressions, we will use these conventions:
# * mass flux **entering** the control volume is **positive**;
# * mass flux **leaving** the volume is **negative**.
#
# Using this convention, we can write the conservation statement for a TMF as:
#
# \begin{align}
# {\Delta m\over \Delta t}  &= \sum_{i=1}^n J_{i} \label{eq3}\\
# \end{align}
#
# Where the notation $\sum_{i=1}^n$ means *"sum over mass fluxes  $i=1,2,\ldots, n$"*. For example, we could decide to label the flux from the pit into the TMF $J_1$ and flux at the discharge structure $J_2$. Because mass is entering the TMF from the pit, $J_1$ will be greater than or equal to zero ($J_1\ge0$), and because mass is leaving at the discharge structure, $J_2$ will be less than or equal to zero ($J_2\le0$).
#
# ### Your turn
#
# The flow into the TMF from the pit is $0.03~ m^3/s$, and the flow out of the discharge structure is $0.035~m^3/s$. What is the change in volume in the TMF over one day ($1~d = 86400~s$)? Enter your answer below as `dvol =`.
#
# %%
# %% [markdown]
# ### Instantaneousness
#
# The simple conservation statement above applies over time period $\Delta t$. **Does it apply at every *instant* in time?**
# That is, what does the above equation become as $\Delta t\rightarrow 0$
#
#
#
# ### Your turn
# Replace the ??? below with the correct term for the equation ${\Delta m\over \Delta t}  = \sum_{i=1}^n J_{i}$  when $\Delta t\rightarrow 0$.
# %% [markdown]
#
# \begin{align}
# ?? &= \sum_{i=1}^n J_{i} \label{eqfv4} \\
# \end{align}
#
# %% [markdown]
# ### Your turn
#
# In this cell, write a statement in words that describes the behavior of the system when:
# 1. $\sum_{i=1}^n J_{i}=0$ (the net flux entering the control volume is zero)
# 2. $\sum_{i=1}^n J_{i}<0$ (the net flux entering the control volume is less than zero)
# 3. $\sum_{i=1}^n J_{i}>0$ (the net flux entering the control volume is greater than zero)
#
# %% [markdown]
# ### Connected volumes - specific case
#
# Consider three large tanks (control volumes) connected by pipes. The instantaneous volume of water in each tank, and instantaneous total flux of water through each pipe is indicated in the figure. The flow direction is indicated with a arrow above each pipe.
#
# <img src="figures/three_tanks_numbers.png" style="width: 1248px;" >
#
# ### Your turn
#
# 1. Compute the instantaneous rate of change of water volume in tanks 1, 2, 3, by writing a conservation of volume equation
# for each tank (Note: we can use volume, if we assume water density is constant).
#
#
# %% [markdown]
# ### Connected volumes - general case
#
# Consider three large tanks (control volumes) connected by pipes. The instantaneous volume of water in each tank, and instantaneous total volumetric flux of water $J~\left[L^3\over T\right]$ through each pipe is indicated with variable names
# as indicated in the figure.
#
# <img src="figures/three_tanks_general.png" style="width: 1248px;" >
#
# ### Your turn
#
# 1. Write a general conservation of mass (volume, since we will assume water density is constant) equation for tanks 1, 2, and 3 in terms of the variables in the figure. Be consistent with the signs of the fluxes used in the equations.
#
# %% [markdown]
# ### Your turn
#
# Can you write the conservation equation for tank 2 that must hold if the volume in the tank is not changing with time? This is called the steady-state equation.
# %% [markdown]
# ## Reflection
#
# What have you learned? What have you struggled with? Some thoughts below. Reflect on anything else you have learned or struggled with and write it here.
#
# * defined the term flux
# * to write conservation expressions in terms of fluxes
# * defined steady-state and non-steady (also called transient) conditions, and their corresponding conservation equations.
#
#
#
# ## On to finite volumes!
