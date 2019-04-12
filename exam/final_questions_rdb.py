# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
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
# <div class="toc"><ul class="toc-item"></ul></div>

# %% [markdown]
# I'd like to test their abilities across the math/conceptual spectrum, from the simple box models to PDEs.
# <br><br>
#
# Leaning goal to be tested
#
# - Can write a mathematical model (i.e. the appropriate equations) that describes how a conserved quantity such as mass, volume (if the material in incompressible), energy, in a single, discrete control volume, (for example the TMF problem) changes through time.
# - Can represent fluxes, sources and sinks in the conservation equation with the correct dimensions (eg, stuff per mass per time, stuff per volume per time, stuff per time, etc).
# - can represent a model for a discrete control volume as either a difference equation or a differential equation.

# %% [markdown]
# **Acidity** is is an important water-quality parameter at mine sites. It describes the moles of a base (typically carbonate) required to raise a water's pH to a prescribed value. Acidity is a **conserved quantity**. In practice, the units are moles of acidity per litre of water $[M/L^3]$. Acidity is usually generated from the oxidation of pyrite (iron sulfide), which produces acid.  
#
# In this question, you will develop a model (equations) that describe the change in acidity over time in a tailings management facility (TMF or tailings pond), under these assumptions:
# <br>
# 1. the TMF has a total volume of $V(t)~[L^3]$, that changes in time in response to in- and outflows of water.
# * drainage from the pit flows into the TMF at a rate $Q_{pit}(t)~[L^3/T]$ with an acidity concentration of $c_{pit}~[M/L^3]$, measured in units of moles acidity per litre.
# * precipitation with zero acidity $c_{precip} = 0~ moles/l$ enters the TMF as precipitation on the surface of the TMF. Assume that the precipitation rate is given from data and can be represented in your model equations as $P(t),~[L/T]$ with units of $mm/day$. Assume that the surface area of the TMF is $A~[L^2]$ with units of $m^2$. Assume that area **does not change** as the volume in the TMF changes (an approximation that is valid for small changes in volume). 
# * evaporation removes water from the TMF at a rate that can be represented in your equation as $ET(t)~[L/T]$ with units of $mm/day$. 
# * the TMF is well stirred, such that the concentration of acidity in the TMF, $c_{TMF}~[M/L^3]$, measured in units of moles acidity per litre of water, is the same at all points in the pond at each instant in time.
#
# * water is discharged from the TMF at a rate $Q_{dis}(t)~[L^3/T]$ with an acidity concentration of $c_{TMF}$.
# * assume all other sources and sinks of water are negligible and can be ignored.
#
# | Variable    |    Description    |Dimension| 
# |----------   |      -------------|   ---------|
# | $V(t)$          | Volume in the TMF| $[L^3]$|
# | $Q_{pit}(t)$    | Rate of flow from pit into TMF| $[L^3/T]$|
# | $c_{pit}(t)$    | Concentration of acidity in pit water| $[M/L^3]$|
# | $P(t)$          | Precipitation rate                    | $[L/T]$ |
# | $ET(t)$         | Evaporation rate                    | $[L/T]$  |
# | $A$             | Surface area of the TMF m           | $[L^2]$  |
# | $c_{TMF}(t)$       | Concentration of acidity in the TMF | $[M/L^3]$ |
# | $Q_{dis}(t)$  | Rate of discharge out of TMF      | $[L^3/T]$|
#
#
#
#
# Question a.
#
# Write an expression that describes how the volume of water in the TMF changes over a time interval from time $t$ to time $t+\Delta t$. That is complete this equation:
#
# $$ V(t+\Delta t) - V(t) =$$
#
# where $V$ is given in units of litres. 
#
# Question b.
#
# Write the expression as a differential equation governing the rate of change of the water volume in the TMF. That is, complete this equation:
#
# $${dV\over dt}=$$
#
# Question c.
#
# Let $ACID(t)~[M]$ be the total mass of acidity in the TMF at time t, with units of moles. Write an expression for the change in acidity in the TMF over the time interval from time $t$ to time $t+\Delta t$. That is, complete this equation:
#
# $$ACID(t+\Delta t) - ACID(t) = $$
#
# Question d.
#
# Write a differential equation, or differential equations for the **concentration** of acidity in the TMF $c_{TMF}(t)$.
#
# Question e.
#
# Acidity can be generated from oxidation of pyrite in the tailings at the bottom of the pond. If the acidity flux per unit area of TMF bottom  $j_{acid}~[M/(L^2 T)]$ is given by $j_{acid} = k c_{TMF} + b$. What are the dimensions of the parameters $k$ and $b$?
#
