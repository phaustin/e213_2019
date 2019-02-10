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
#   nbsphinx:
#     execute: never
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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Putting-it-all-together" data-toc-modified-id="Putting-it-all-together-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Putting it all together</a></span><ul class="toc-item"><li><span><a href="#1-D-steady---state-diffusion-stencil-(aligned-in-the-x-direction)" data-toc-modified-id="1-D-steady---state-diffusion-stencil-(aligned-in-the-x-direction)-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>1-D steady - state diffusion stencil (aligned in the x direction)</a></span></li></ul></li><li><span><a href="#5---gridblock-example" data-toc-modified-id="5---gridblock-example-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>5 - gridblock example</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Gridblock-1" data-toc-modified-id="Gridblock-1-2.0.1"><span class="toc-item-num">2.0.1&nbsp;&nbsp;</span>Gridblock 1</a></span></li><li><span><a href="#Gridblock-2" data-toc-modified-id="Gridblock-2-2.0.2"><span class="toc-item-num">2.0.2&nbsp;&nbsp;</span>Gridblock 2</a></span></li><li><span><a href="#Gridblock-3" data-toc-modified-id="Gridblock-3-2.0.3"><span class="toc-item-num">2.0.3&nbsp;&nbsp;</span>Gridblock 3</a></span></li><li><span><a href="#Gridblock-4" data-toc-modified-id="Gridblock-4-2.0.4"><span class="toc-item-num">2.0.4&nbsp;&nbsp;</span>Gridblock 4</a></span></li><li><span><a href="#Gridblock-5" data-toc-modified-id="Gridblock-5-2.0.5"><span class="toc-item-num">2.0.5&nbsp;&nbsp;</span>Gridblock 5</a></span></li><li><span><a href="#Collecting-all-equations" data-toc-modified-id="Collecting-all-equations-2.0.6"><span class="toc-item-num">2.0.6&nbsp;&nbsp;</span>Collecting all equations</a></span></li></ul></li><li><span><a href="#Simplify" data-toc-modified-id="Simplify-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Simplify</a></span></li><li><span><a href="#Equations-for-unknown-concentrations" data-toc-modified-id="Equations-for-unknown-concentrations-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Equations for unknown concentrations</a></span></li></ul></li><li><span><a href="#Solve-the-system-of-equations" data-toc-modified-id="Solve-the-system-of-equations-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Solve the system of equations</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Your-answer-here:" data-toc-modified-id="Your-answer-here:-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>Your answer here:</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-3.0.2"><span class="toc-item-num">3.0.2&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-3.0.3"><span class="toc-item-num">3.0.3&nbsp;&nbsp;</span>Your turn</a></span></li></ul></li></ul></li><li><span><a href="#Summary" data-toc-modified-id="Summary-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Summary</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-4.0.1"><span class="toc-item-num">4.0.1&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Boundary-value-problem-checklist" data-toc-modified-id="Boundary-value-problem-checklist-4.0.2"><span class="toc-item-num">4.0.2&nbsp;&nbsp;</span>Boundary value problem checklist</a></span></li></ul></li></ul></li><li><span><a href="#Context" data-toc-modified-id="Context-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Context</a></span></li><li><span><a href="#Link-to-the-TMF-problem" data-toc-modified-id="Link-to-the-TMF-problem-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Link to the TMF problem</a></span></li><li><span><a href="#General-idea-between" data-toc-modified-id="General-idea-between-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>General idea between</a></span></li><li><span><a href="#Continuity-equation" data-toc-modified-id="Continuity-equation-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Continuity equation</a></span><ul class="toc-item"><li><span><a href="#The-continuity-equation" data-toc-modified-id="The-continuity-equation-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>The continuity equation</a></span></li><li><span><a href="#Physical-interpretation-of-the-divergence" data-toc-modified-id="Physical-interpretation-of-the-divergence-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Physical interpretation of the divergence</a></span></li></ul></li></ul></div>
# %% [markdown]
# <div class="alert alert-warning">
#
# ## Putting it all together
#
# Recall our approach:
# 1. Write a discrete approximation for mass conservation for gridblock C. This equation is the fundamental stencil.
# 2. Apply this stencil to each gridblock in the grid to generate a unique equation for each gridblock in the grid.
#
# For n gridblocks, we can generate n equations.
# </div>
# %% [markdown]
#
# We just developed the fundamental stencil for 1-D steady-state diffusion in terms of concentrations in gridblocks as:
#
# ### 1-D steady - state diffusion stencil (aligned in the x direction)
#
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) = 0 \label{eq651}\\
# \end{align}
#
# It is convenient to rearrange the stencil and collect terms that multiply $c_E$, $c_C$ and $c_W$:
#
# \begin{align}
# &\left(D\theta {\Delta y \Delta z \over \Delta x}\right) c_E - \left(2 D\theta {\Delta y \Delta z \over \Delta x}\right) c_C + \left(D\theta {\Delta y \Delta z \over \Delta x}\right) c_W  = 0 \label{eq652}\\
# \end{align}
#
# If each gridblock is the same size, and porosity and the diffusion coefficient are everywhere the same (spatially homogeneous) then the stencil simplifies to:
#
# \begin{align}
# & c_E -  2   c_C +  c_W  = 0 \label{eq653}\\
# \end{align}
#
#
#
#
#
#
# %% [markdown]
# ## 5 - gridblock example
#
# Let's write the equations for the 5-gridblock example from before, now in terms of concentrations.
#
# <img src="figures/5node-const-c-bc.png" style="height: 200px;" >
#
# The total length of the domain is $2~m$ in the $x$ direction, each gridblock is the same size and porosity and diffusion coefficient are spatially homogeneous:
# * $\Delta x=0.5 m$
# * $\Delta y=0.3 m$
# * $\Delta z=0.5 m$
# * $D=2\times 10^{-10}~m^2/s$
# * $\theta = 0.25$
#
# Note that the *nodes* of gridblock 1 and 5 are located on the boundary.
#
# #### Gridblock 1
#
# The node is on the boundary where the concentration is prescribed, so the equation is simply
#
# \begin{align}
# c_1&= 2000 \label{eq654}\\
# \end{align}
#
# #### Gridblock 2
#
# <img src="figures/block2_eq.png" style="height: 110px;" >
#
# Because each gridblock is the same size and $D$ and $\theta$ are spatially homogeneous, we can use the stencil in its simplest form \ref{eq653} and the equation for gridblock 2 becomes:
#
#
# \begin{align}
# c_1 -2c_2 + c_3 &= 0 \label{eq655}\\
# \end{align}
#
#
# #### Gridblock 3
#
# <img src="figures/block3_eq.png" style="height: 110px;" >
#
# The equation for gridblock 3:
#
# \begin{align}
# c_2 -2c_3 + c_4 &= 0 \label{eq656}\\
# \end{align}
#
# #### Gridblock 4
#
# <img src="figures/block4_eq.png" style="height: 110px;" >
#
# The equation for gridblock 4:
#
#
# \begin{align}
# c_3 -2c_4 + c_5  &= 0 \label{eq657}\\
# \end{align}
#
# #### Gridblock 5
#
# The node is on the boundary where the concentration is prescribed, so the equation is simply
#
# \begin{align}
# c_5&= 93 \label{eq658}\\
# \end{align}
#
# #### Collecting all equations
#
#
#
#
#   | Gridblock  | Equation      |
#   |:----------:|:--------------:|
#   | 1  | $$c_1 = 2000$$|
#   | 2  | $$c_1 -2c_2 + c_3 = 0$$|
#   | 3  | $$c_2 -2c_3 + c_4 = 0$$|
#   | 4  | $$c_3 -2c_4 + c_5  = 0 $$|
#   | 5  | $$c_5 = 93$$|
#
# ### Simplify
#
# We can use the equation for gridblock 1 to simplify the equation for gridblock 2 by substituting the known value of $c_1$ into equation 2:
#
# $2000 -2c_2 + c_3 = 0$ or, bringing the known value to the right hand side,
#
# \begin{align}
# -2c_2 + c_3 &= -2000 \label{eq659}\\
# \end{align}
#
# Similarly for equation 4,
#
#
# \begin{align}
# c_3 -2c_4&= -93 \label{eq6510}\\
# \end{align}
#
#
# %% [markdown]
# ### Equations for unknown concentrations
#
# Finally collecting all the equations for the unknown concentrations  $c_2$, $c_3$, $c_4$ together:
#
#
#   | Gridblock  | Equation      |
#   |:----------:|:--------------:|
#   | 2  | $$-2c_2 + c_3 =-2000$$|
#   | 3  | $$c_2 + c_4 -2c_3= 0$$|
#   | 4  | $$c_3 -2c_4 = -93 $$|
#
# %% [markdown]
# ## Solve the system of equations
#
# Solve the equations and plot the concentration versus $x$.
#
# %% [markdown]
# <div class="alert alert-info">
#
# #### Your answer here:
#
# </div>
# %% [markdown]
# <div class="alert alert-info">
#
# #### Your turn
#
# The approximation for $j_{EC}$ is given above in equation \ref{eq5148}.
#
# Write the corresponding discrete approximation for $j_{WC}$ in terms of $D\theta$, $c_W$, $c_C$ and $\Delta x$, $\Delta y$, and $\Delta z$.
#
# </div>
# %% [markdown]
# <div class="alert alert-info">
#
# #### Your turn
# \begin{align}
# j_{WC} &\approx {????} \label{eq5148}\\
# \end{align}
#
# 1. Is the sign of the flux $j_{WC}$ computed using your expression positive for flux entering gridblock C?
# 2. Give an example.
#
# </div>
# %% [markdown]
# ## Summary
#
# Bringing it all together, the 1-D steady-state diffusion stencil
#
# \begin{align*}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) = 0 \\
# \end{align*}
#
# becomes (replace $j_{WC}$ in the expression below with your expression from above):
#
# #### Your turn
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   j_{WC}   \right) (\Delta y) (\Delta z) = 0 \label{eq5144}\\
# \end{align}
#
#
#
# Consider a three gridblocks W, C, E, where $c_W=28~mg/L$, $c_C=20~mg/L$ and $c_E= 15 mg/L$, the diffusion coeffient is $D=2\times 10^{-10}~m^2/s$, and the porosity is $\theta = 0.25$. Write the python code to compute:
# 1. $j_{EC}$ and $j_{WC}$
# 2. $J_{EC}$ and $J_{WC}$
# %% [markdown]
#
# #### Boundary value problem checklist
# To solve a boundary value problem requires:
# 1. knowledge of the equations that govern the dependent variable.
# 2. specification of the problem domain.
# 3. specification of properties of the problem domain.
# 4. the value of the dependent variable or its derivatives on the boundary.
#
# Let's go through the checklist for our problem.
# 1. we have not developed these yet, but we are going to use conservation of mass and an expression for diffusion to develop the equations that govern concentration.
#
#
#
#
# %% [markdown]
# Why go to the trouble with the fancy math? Couple of reasons:
# * it is the most succinct and unambiguous way to state a physical principle. In that sense, mathematics is a  language with a grammar and rules that allow one to make precise statements. We use the *language* of mathematics to write
# *literature*: precise descriptions of physical systems .
# * once we have a mathematical description, we can use the grammar rules of mathematics and manipulate the expressions to, for example, simplify them, or use calculus to derive solutions to our expressions.
#
#
# %% [markdown]
#
#
# ## Context
#
# So far we have solved 0 dimensional problems:
#
# - we have considered the mass of water to be given by one value
# - we have considered that the concentration of sulfates was given by one value and that this value was the same at any point in the TMF.
#
# In reality, the concentration of sulfates is not necessarily the same everywhere, and the spatial distribution or evolution of the contaminant is important to know.
#
# Consider a factory releasing a contaminant: this contaminant will be transported in space and time.
#
# - if the factory releases this contaminant in a river, it will follow the river current
# - if it is released in the atmosphere, it will follow windspeed
# - if is is released in the groundwater, it will follow the groundwater flow
#
# But the windspeed, the river current, the groundwater flow are not the same everywhere (they are not uniform). If we want to be able to predict where the contaminant goes, we need to understand which processes are responsible for its movement.
#
# In a 3 dimensional space, the concentration can be different at every point in space. But also, the concentration at each point in space can evolve in time. In general, the concentration will be described by a function $c(x,y,z,t)$ which represents the concentration at each point of coordinates $(x,y,z)$ for each time $t$.
#
# When we have developped Euler's approaches, we have divided into small intervals. We are going to do the same with space. This is called **discretization**. It is the idea of splitting a variable who can take any value on a real axis into subdomains where this variable is supposed to be constant.
#
# <img src="figures/figDisc.png">
#
# Without a discretization, we would have to solve a problem for each possible $(x,y,z)$, which would be impossible.
#
# %% [markdown]
# ## Link to the TMF problem
#
# To introduce this spatial behaviour, let us go back to the TMF problem. The conceptual model could be expressed like this:
# <img src="figures/figTMF.png" alt="drawing" width ="400">
#
# This "spatial" view of the method we have applied corresponds precisely to the finite volume - difference method we will use. In our problem, we were only interested in one "point" in space, the TMF. This "point" representation of this TMF actually arises from a discretization of space.
#
# We have computed the evolution the mass/concentration of sulfates in that "point" by computing the fluxes which were going in and out of this "point".
#
# What if the amount of sulfates in the pit/mill was not "infinite" (constant in all time)? Well, that would mean that $c_{\text{pit}}$ would decrease during time, and the flux incoming from the pit would decrease as well. If that is the case, we now need to add another equation to compute the evolution of the concentration in the pit, and also a formulation which links the flux between the pit/mill towards the TMF.
#
# That is the central idea for the resolution of any transient (not steady) problem including spatial variation. The evolution of the concentration at each point of interest during a certain time is computed by
#
# - summing all the fluxes going in - all the fluxes going out
# - considering these fluxes are constant in time during that period of time ( // Euler's method).
#
# So what we need, is to be able to compute these fluxes.
#
# Watch out, in physics, flux is usually defined as the amount (of matter, energy, ...) which goes through a surface per unit of time. A mass flux is described in kg/m$^2$/s. Above, we have described a "flux" in mg/s. In the following, flux $\phi$ will be denoted in units of Mass per unit of surface per unit of time.
# %% [markdown]
# ## General idea between
# If we focus on the central volume here, it might exchange fluxes $\phi$ with its neighbouring volumes. In a 2D space, central volume $i$ has 4 neighbours: North-East-South-West, with whom it can exchange matter (or energy, ...).
#
# <img src="figures/figFV.png" alt="drawing" width="400">
#
#
#
# So, if we know the mass-flux between volume $i$ and volume North, $\phi_{i\rightarrow \text{North}}$, that means that the mass in volume $i$ is evolving by the amount:
#
# \begin{equation}
# \frac{dM}{dt} = \sum_j \phi_{j\rightarrow i} S_{ij}
# \end{equation}
#
# where $j$ represents the set of every neighbour (here North, East, South, West). In 1D, there are 2 neighbours, in 3D, there are 6 neighbours.
#
# Where S is the surface (in m$^2$) of the interface between volumes i and North. So, to compute the evolution of mass in volume $i$, we only need to find the values of the different fluxes.
#
# The idea behind the space discretization is that, in each "volume", the concentration is uniform and has only one value. That also means that, on every surface separating two volumes, the fluxes are uniform.
# %% [markdown]
# ## Continuity equation
#
# ### The continuity equation
#
# Multiplying both ends by the volume of water $V_0$ yields:
#
# So, if the concentration is uniform in the volume $V$, that means that the mass can be obtained by:
#
# \begin{equation}
# M = \int_V c dV = c \int_V dV = cV
# \end{equation}
#
# The evolution of the mass arises from the different fluxes
#
# \begin{equation}
# \frac{\Delta M}{\Delta t} = \sum_j \phi_{j\rightarrow i} S_{ij} = -R
# \end{equation}
#
# The rate of matter evolution $R$ (mg/s) through any surface is usually given by the integral of the flux over the surface:
# \begin{equation}
# R = \oint_S \overrightarrow{\phi}d\overrightarrow{S}
# \end{equation}
#
# where $d\overrightarrow{S}$ represents the unit normal vector oriented towards the outside of the closed surface. So, $R$ is positive when matters is going out ot the volume. This surface integral can be decomposed, in our cases, as the sum over the 4 straight lines delimiting our volume. And, since the flux is uniform through these straight lines, this integral becomes straightforward to compute:
#
# \begin{equation}
# \begin{array}{lll}
# R & = & \displaystyle{ \oint_S \overrightarrow{\phi}d\overrightarrow{S}} \\
#   & = & \int_{S_{\textrm{North}}} \phi_{\textrm{North}} dS + \int_{S_{\textrm{East}}} \phi_{\textrm{East}} dS + ... \\
#   & = & \phi_{\textrm{North}} \int_{S_{\textrm{North}}}  dS + \phi_{\textrm{East}} \int_{S_{\textrm{East}}}  dS + ... \\
#   & = & \phi_{\textrm{North}}S_{\textrm{North}} + \phi_{\textrm{East}}S_{\textrm{East}} + \phi_{\textrm{South}}S_{\textrm{South}} + \phi_{\textrm{West}}S_{\textrm{West}}   \\
#   & = & \sum_j \phi_{i\rightarrow j} S_{ij}
# \end{array}
# \end{equation}
#
# But there is a math theorem (Green-Ostrogradski) which also states that
#
# The rate of matter evolution $R$ (mg/s) through any surface is usually given by the integral of the flux over the surface:
# \begin{equation}
# \oint_{S(V)} \overrightarrow{\phi}d\overrightarrow{S} = \int_V \mathrm{div} \overrightarrow{\phi}
# \end{equation}
#
# This is the "divergence" theorem. The divergence operator is defined as:
#
# \begin{equation}
# \mathrm{div} \overrightarrow{\phi} = \overrightarrow{\nabla} \cdot \overrightarrow{\phi}
# \end{equation}
#
# So, combining the different equation together, we get
#
# \begin{equation}
# \begin{array}{llll}
#  & \frac{dm}{dt} & = & \sum_j \phi_{j\rightarrow i} S_{ij} \\
# \Longleftrightarrow & \displaystyle{\frac{d}{dt} \int_V c dV} & = & \displaystyle{ - \oint_S \overrightarrow{\phi}d\overrightarrow{S}} \\
# \Longleftrightarrow & \displaystyle{\frac{d}{dt} \int_V c dV} & = & \displaystyle{ - \int_V \mathrm{div} \overrightarrow{\phi} dV}
# \end{array}
# \end{equation}
#
# And, since the integral over the same volume $V$ has to be equal on both sides, that means that what is inside the integrals have to be equal, which gives the divergence equation:
#
# \begin{equation}
# \frac{dc}{dt} + \mathrm{div} \overrightarrow{\phi} = 0
# \end{equation}
#
# This is known as the **continuity equation**, which is used in many areas of physics (quantum mechanics, fluid mechanics, energy, mass balance, ...).
# %% [markdown]
# ### Physical interpretation of the divergence
#
# The divergence theorem states that, for any given volume, the integral of the flux (mg/m$^2$/s) over the surface which defines that volume (mg/s) corresponds to the integral over the volume of the "divergence" of the flux.
# \begin{equation}
# \oint_{S(V)} \overrightarrow{\phi}d\overrightarrow{S} = \int_V \mathrm{div} \overrightarrow{\phi}
# \end{equation}
#
# Remember Maxwell's law of electromagnetism? If you look at a magnet, the lines describing the magnetic field always goes from the north to the south "pole". And over one line,  the value of the magnetic field $B$ (in Tesla), is constant.
#
# <img src="figures/B.png">
#
# That means that, if you define a volume $V$ whatsoever, delimited by a closed surface $S(V)$, everything that is coming in, is going to come out. Maxwell's law  for that is
#
# \begin{equation}
# \mathrm{div} \overrightarrow{B} = 0
# \end{equation}
#
# This is not the case for the electric field.
#
# <img src="figures/E.png">
#
# In this case, the presence of one electric charge will generate electric field lines. So if you take any volume, whose incorporates that electric charge, the integral of the flux will be positive (for a positive charge). Maxwell's law states, with $\rho$ being the charge density:
#
# \begin{equation}
# \mathrm{div} \overrightarrow{E} = \frac{\rho}{\epsilon_0}
# \end{equation}
#
# Here in our case, the divergence of a vector field $\rightarrow{q}$ will basically indicate:
# \begin{equation}
# \mathrm{q} \propto \textrm{What goes out} - \textrm{What goes in}
# \end{equation}
#
# So, the continuity equation:
#
# \begin{equation}
# \frac{dc}{dt} = - \mathrm{div} \overrightarrow{\phi} \propto \textrm{What goes in} - \textrm{What goes out}
# \end{equation}
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# %%
