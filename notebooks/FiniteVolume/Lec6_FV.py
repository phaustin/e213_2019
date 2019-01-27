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
#       jupytext_version: 1.0.0-dev
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
# %% [markdown] {"toc": "true"}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-to-finite-volume-methods" data-toc-modified-id="Introduction-to-finite-volume-methods-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to finite-volume methods</a></span><ul class="toc-item"><li><span><a href="#Context" data-toc-modified-id="Context-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Context</a></span></li><li><span><a href="#Link-to-the-TMF-problem" data-toc-modified-id="Link-to-the-TMF-problem-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Link to the TMF problem</a></span></li><li><span><a href="#General-idea-between" data-toc-modified-id="General-idea-between-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>General idea between</a></span></li><li><span><a href="#Continuity-equation" data-toc-modified-id="Continuity-equation-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Continuity equation</a></span><ul class="toc-item"><li><span><a href="#The-continuity-equation" data-toc-modified-id="The-continuity-equation-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>The continuity equation</a></span></li><li><span><a href="#Physical-interpretation-of-the-divergence" data-toc-modified-id="Physical-interpretation-of-the-divergence-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Physical interpretation of the divergence</a></span></li></ul></li></ul></li></ul></div>
# %% [markdown]
# # Introduction to finite-volume methods
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
#
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
# %%
