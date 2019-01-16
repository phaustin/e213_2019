# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Create Assignment
#   jupytext:
#     metadata_filter:
#       cells:
#         additional: all
#       notebook:
#         additional: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
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
#     version: 3.6.5
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

# %% [markdown] {"lines_to_next_cell": 0, "toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Mixing-calculations" data-toc-modified-id="Mixing-calculations-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Mixing calculations</a></span><ul class="toc-item"><li><span><a href="#ODEs-and-Euler’s-method**" data-toc-modified-id="ODEs-and-Euler’s-method**-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>ODEs and Euler’s method**</a></span></li><li><span><a href="#Problem-description-and-conceptual-model" data-toc-modified-id="Problem-description-and-conceptual-model-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Problem description and conceptual model</a></span></li><li><span><a href="#Identification-of-sulfate-sources" data-toc-modified-id="Identification-of-sulfate-sources-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Identification of sulfate sources</a></span><ul class="toc-item"><li><span><a href="#Parameters" data-toc-modified-id="Parameters-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Parameters</a></span></li></ul></li><li><span><a href="#Evolution-of-the-mass-of-water" data-toc-modified-id="Evolution-of-the-mass-of-water-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Evolution of the mass of water</a></span></li><li><span><a href="#Evolution-of-the-mass-of-sulfates" data-toc-modified-id="Evolution-of-the-mass-of-sulfates-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Evolution of the mass of sulfates</a></span></li><li><span><a href="#Mass-balance" data-toc-modified-id="Mass-balance-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Mass balance</a></span><ul class="toc-item"><li><span><a href="#Associated-ODE" data-toc-modified-id="Associated-ODE-1.6.1"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Associated ODE</a></span></li><li><span><a href="#Analytical-Solution" data-toc-modified-id="Analytical-Solution-1.6.2"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Analytical Solution</a></span></li><li><span><a href="#Error-estimation" data-toc-modified-id="Error-estimation-1.6.3"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>Error estimation</a></span></li></ul></li></ul></li><li><span><a href="#Plot-the-errors" data-toc-modified-id="Plot-the-errors-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Plot the errors</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Influence-of-the-timestep" data-toc-modified-id="Influence-of-the-timestep-2.0.1"><span class="toc-item-num">2.0.1&nbsp;&nbsp;</span>Influence of the timestep</a></span></li></ul></li></ul></li></ul></div>
# %% [markdown] {"lines_to_next_cell": 0}
# # Assignment
#
# ## Objectives and description**
#
# The objective of this assignment is to create a python program that
# computes the concentration of sulfate in time in the water in a tailings
# management facility (TMF) at a mine site.
#
# The goal is to describe the computational approach to the resolution of a typical "0D" problem. In the end, the goal is to understand how the computational approach corresponds to the resolution of an ODE. We will investigate that ODE and study its solutions. That will allow us to compare the accuracy of the numerical solution, because mathematics allowed us to know, in this particular case, the exact solution of a problem.
#
# This assignment is built so that the concepts of the accuracy of a solution are naturally introduced. In the end, you will realize that you will have implemented what is called the forward Euler approach. 
#
# ## Problem description and conceptual model
#
# Sulfate $SO_{4}^{2 -}$ is one of the “major” dissolved constituents in
# most terrestrial waters (the others being sodium, calcium, magnesium,
# bicarbonate and chloride). Sulfate is not poisonous, but much in the
# same way that too much salt makes water undrinkable, too much sulfate
# can be too and is thus an environmental concern.
#
# Furthermore, high sulfate concentrations are usually associated with acidic conditions (think about sulfuric acid producing sulfates). In acidic conditions, heavy metals (which are poisonous) might be released from rock dissolution, ... Therefore, monitoring and predicting the sulfate content in groundwater is an essential environmental concern.
#
# We will go back to the TMF problem, where we want to know and assess the sulfate concentration evolution through time.
#
# ## Identification of sulfate sources
#
# To compute the concentration of sulfate in the TMF water, we need to
# know where it is coming from and going to and use that knowledge to
# develop a conceptual model describing the fate of sulfate in our system. That conceptual model will be translated into a computational model.
#
# The figure below is a conceptual sketch of the main sources and losses
# of sulfate in the TMF water:
#
# ![](figures/tmf_box.png)
#
# 1)  From the pit. To keep the pit dry, water is constantly pumped out of
#     the pit and put into the TMF at a rate $Q_{\text{pit}}$
#     (L/s of water). The pit water has a sulfate concentration of
#     $c_{\text{pit}}$ in mg/L.
#
# 2)  From the mill. The tailings are pumped into the TMF as a slurry of
#     tailings particles (fine, sand-size ground rock) and water. Assume
#     that the water from the mill enters the TMF at a rate of
#     $Q_{\text{mill}}\ $ (L/s of water), with a sulfate
#     concentration of $c_{\text{mill}}$ (mg/L).
#
# 3)  Diffusing from the tailings porewater at the bottom of the TMF into
#     the water column above. Sulfate dissolves from the tailings
#     particles into the adjacent porewater by oxidation of the sulfide
#     minerals in the particles. Because the ratio of rock to water is
#     high in the tailings sediments at the bottom, the porewater sulfate
#     concentration in the tailings, $c_{\text{pore}}$, is always
#     higher than in the water in the TMF. Accordingly, sulfate tends to
#     diffuse into the TMF water from the bottom porewater at a rate
#     proportional to the difference in concentration between the
#     porewater concentration and the concentration in the TMF,
#     $c_{\text{TMF}}.$ That is, the flux of sulfate from the bottom can
#     be written (a positive quantity when sulfate is entering into the
#     TMF):
#
# $j_{\text{pore}} = k\left( c_{\text{pore}} - c_{\text{TMF}} \right)$
#
# where $j_{\text{pore}}\ mg/(s \cdot m^{2})$ is the flux rate of
# sulfate per unit area of the bottom of the TMF and $k$ is the flux
# coefficient with units of $L/(s \cdot m^{2})$ . To compute
# $J_{\text{pore}}$, the total mass flux rate for the whole TMF, with
# units of $\frac{\text{mg}}{s}$, we must multiply the rate per unit
# area $j_{\text{area}}$ by the total area of the TMF bottom
# $A_{\text{bottom}}\ $ in $m^{2}$:
#
# $J_{\text{pore}} = A_{\text{bottom}}{\times j}_{\text{pore}}$
#
# 4)  Leaving via the discharge ditch. Sulfate leaves the TMF with the
#     water that is discharged at a rate $Q_{\text{discharge}}$ (L/s)
#     from the TMF to the environment. SIMPLIFYING ASSUMPTION: if we
#     assume that the water in the TMF is well mixed at all times, then
#     the concentration in the TMF, $c_{\text{TMF}}$ is the same at all
#     points in the TMF, and therefore the water leaving the TMF has that
#     same concentration $c_{\text{TMF}}\ $.
#
# ### Parameters
#
# You will need these parameters for your
# model
#
# | Symbol                   | Symbol Units                | Description                                                  |&nbsp; &nbsp; &nbsp; &nbsp; Value                   |
# | ------------------------ | --------------------- | ------------------------------------------------------------ | ----------------------- |
# | $c_{\text{pit}}$       | $mg/L$              | Concentration of sulfate in pit water (assume constant)      | $50$                  |
# | $Q_{\text{pit}}$       | $L/s$           | Flow rate of water from the pit into TMF (assume constant)   | 30                   |
# | $c_{\text{mill}}$      | $mg/L$              | Concentration of sulfate in mill water (assume constant)     | $700$                 |
# | $Q_{\text{mill}}$      | $L/s$           | Flow rate of water from mill into TMF (assume constant)      | 14                   |
# | $Q_{\text{discharge}}$ | $L/s$           | Flow rate of water from TMF to environment (assume constant) | 44                   |
# | $c_{\text{pore}}$      | $mg/L$              | Concentration of sulfate in porewater at bottom of pond      | 2000                    |
# | $k$                    | $L/(s \cdot m^{2})$ | Flux coefficient from porewater to water column              | $2.5 \times 10^{- 5}$ |
# | $A_{\text{bottom}}$    | $m^{2}$             | Total area of TMF bottom                                     | $3 \times 10^{5}$     |
# | $V_{\text{TMF}}$       | $L$             | Volume of water in TMF at start of simulation                | $8.1 \times 10^{6}$   |
# | $c_{0}$                | $mg/L$              | Concentration of sulfate in TMF water at start of simulation | $93$                  |
#
#
#
# %% [markdown] {"lines_to_next_cell": 0}
# ## Evolution of the mass of water
#
# First, we will check the evolution of the volume of water in the TMF. Let us denote by $V(t)$ the volume of water in the TMF at every time step.
#
# The flux from the pit and the mill are positive source terms for the volume of water, while the discharge is a negative source term (a sink term).
#
# Over a certain time $\Delta t$, the amount of water (in L) which is coming in/out the TMF are denoted $S_{\text{pit}}$, $S_{\text{mill}}$, $S_{\text{dis}}$ and are equal to
#
# \begin{equation}
# \left\lbrace
# \begin{array}{lll}
# S_{\text{pit}} & = &  Q_{\text{pit}} \Delta t \\
# S_{\text{mill}} & = &  Q_{\text{mill}} \Delta t \\
# S_{\text{dis}} & = &  Q_{\text{dis}} \Delta t \\
# \end{array}
# \right.
# \end{equation}
#
# Therefore, the volume $V$ of water in the TMF over the period [$t$;$t+\Delta t]$ is:
#
# \begin{equation}
# \begin{array}{llll}
# & V(t+\Delta t) & = &  V(t) + S_{\text{pit}} + S_{\text{mill}} - S_{\text{dis}} \\
# \Longleftrightarrow & V(t+\Delta t) & = &  Q_{\text{pit}} \Delta t + Q_{\text{mill}} \Delta t - Q_{\text{dis}} \Delta t \\
# \Longleftrightarrow & \frac{V(t+\Delta t)-V(t)}{\Delta t} & = &  Q_{\text{pit}}  + Q_{\text{mill}}  - Q_{\text{dis}}  \\
# \end{array}
# \end{equation}
#
# How does the volume of water change with time?
#
#
# %%
from numpy.testing import assert_almost_equal

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "grade_id": "cell-a09bbce77de223da", "points": 1}}
Q_pit = 30
Q_mill = 14
Q_dis = 44
###BEGIN SOLUTION
Q_pit+Q_mill-Q_dis
###END SOLUTION

# %% [markdown]
# Considering the values given, we have:
#
# \begin{equation}
# \frac{V(t+\Delta t)-V(t)}{\Delta t} = 30 + 14 - 44 = 0 \Longleftrightarrow V(t) = V_0
# \end{equation}
#
# Indicating that the volume of water is constant through time!
#
# Let's assigne a variable whose value is the volume of water in the TMF:

# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-113d07a78f5dd226"}}
V0 = 0
#  Change the value of V0 to match the given data

###BEGIN SOLUTION
V0 = 8.1e9  # volume of water in L
###END SOLUTION


# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-ebe77652bfd42a8e"}}
assert_almost_equal(V0,8.1e9,decimal=1)

# %% [markdown]
# ## Evolution of the mass of sulfates
#
# We have 4 main processes impacting the quantity of sulfates in the TMF. We will compute the evolution of this mass over time. First, initialize the required variable (initial mass, and the different input parameters).
#
#
#

# %% {"lines_to_next_cell": 2}
c0 = 93  # initial concentration

c_pit = 50
c_pore = 2000
c_mill = 700

k = 2.5e-5
Area = 3e5


# %% [markdown]
# What is the initial mass of sulfates? (in mg)

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-2372ba7e97931ee6"}}
m0 = 0
# Change the value of m0 so that it corresponds to the initial mass (in mg) of sulfates in the TMF.
###BEGIN SOLUTION
m0 = c0 * V0
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-bf5d8ad9924f2552"}}
assert_almost_equal(m0,7.533e11,decimal=1)

# %% [markdown]
# 1. Advective flux from the pit and the mill
#
# We have a source of sulfates from the pit. Over a certain time $\Delta t$, the volume of water coming from the pit is $S_{\text{pit}} = Q_{\text{pit}} \Delta t$. This volume of water has a sulfate concentration corresponding to the pit concentration. So, the total mass of sulfate from the pit which arrived in the pit over the same period, $M_{\text{pit}}$ is simply:
# \begin{equation}
# M_{\text{pit}} = S_{\text{pit}}  c_{\text{pit}} = Q_{\text{pit}}  c_{\text{pit}} \Delta t
# \end{equation}
#
# You can always check the units:
# \begin{equation}
# \overbrace{M_{\text{pit}}}^{mg} = \overbrace{Q_{\text{pit}}}^{L/s}  \, \overbrace{c_{\text{pit}}}^{mg/L} \, \overbrace{\Delta t}^{s}
# \end{equation}
#
#
# Compute the mass of sulfates after 1 day if the pit is the only source of sulfate. Create a variable S_pit corresponding to the mass (mg) of sulfates brought by the pit in one day.
#
#

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-be9d32b64825de70"}}
dt = 1  # day
Seconds_in_a_day = 24 * 3600
S_pit = 0

###BEGIN SOLUTION
S_pit = Q_pit * c_pit * dt * Seconds_in_a_day
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-b0f765e9007b556b"}}
assert_almost_equal(S_pit,129600000,decimal=1)

# %% [markdown]
# 2. Advective flux from the mill
#
# If we only consider the mill as a sulfate source, how will the mass of sulfates evolve in one day. Assign this value in variable named S_mill (in mg).
#
#

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-fc68eb0af7e61cfa"}}
S_mill = 0
###BEGIN SOLUTION
S_mill = Q_mill * c_mill * dt * Seconds_in_a_day
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "grade_id": "cell-7584745de7a3187e", "points": 1}}
#assert that S_mill = 846720000
assert_almost_equal(S_mill,846720000,decimal=1)

# %% [markdown]
# 3. Discharge flux from the TMF
#
# The same development can be performed for the discharge of water. The volume of water leaving the TMF over a certain period $\Delta t$ is $S_{\text{dis}} = Q_{\text{dis}} \Delta t$. The concentration of sulfates in this volume corresponds to the concentration of sulfates in the TMF $c_{\text{TMF}}$, so that we can write:
#
# \begin{equation}
# M_{\text{dis}} = Q_{\text{dis}}  c_{\text{TMF}} \Delta t
# \end{equation}
#
# How will the discharge change the mass of sulfates over one day? Create a variable called S_dis which stores that value (in mg).
#

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-43706ee6c2fba2a1"}}
S_dis = 0
###BEGIN SOLUTION
S_dis = Q_dis * c0 * dt * Seconds_in_a_day
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-e29825a21bf3f2e8"}}

assert_almost_equal(S_dis,353548800,decimal=1)

# %% [markdown]
# 4. First order mass transfer
#
# The mass flux was written as:
# \begin{equation}
# J_{\text{pore}} = \overbrace{A_{\text{bottom}}}^{m^2} \overbrace{k}^{L . s^{-1} . m^{-2}}  \left( \overbrace{c_{\text{pore}} - c_{\text{TMF}}}^{mg . L^{-1}} \right)
# \end{equation}
# which is in the units of mg/s. If this flux is constant over time, the added mass of sulfates over a certain time $\Delta t$ corresponds to the latter quantity multiplied by the the quantity $J_{\text{pore}}$ multiplied by $\Delta t$:
#
# \begin{equation}
# M_{\text{pore}} = A_{\text{bottom}} k \left( c_{\text{pore}} - c_{\text{TMF}}  \right) \Delta t
# \end{equation}
#
# How will this mass transfer impact the mass of sulfate? Create a variable S_pore which stores the value (in mg) of the sulfate brought by this first order mass transfer.
#

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-9bff3ecfa902f301"}}
S_pore = 0
###BEGIN SOLUTION
S_pore = Area * k * (c_pore - c0) * dt * Seconds_in_a_day
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-c83065e1b82a3abe"}}
#ASSERT THAT S_PORE = 1235736000.0
assert_almost_equal(S_pore,1235736000,decimal=1)

# %% [markdown]
# Now, compute the total evolution of the mass of sulfates after one day, and print its value and how it has changed. Store that value (in mg) in a variable called m1.
#

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-6077ebff299ad1b0"}}
m1 = 0
###BEGIN SOLUTION
m1 = m0 + S_pore + S_pit + S_mill - S_dis
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-7af99e25848e170f"}}
#assert that m1=7.5516e11
assert_almost_equal(m1,755158507200,decimal=1)

# %% [markdown]
# This is the mass after 1 day (in mg). What is the concentration after one day? Store that value in a variable called c1 (in mg/L).

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-eed606a5f5b25f6f"}}
c1 = 0
###BEGIN SOLUTION
c1 = m1 / V0
###END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-bb3d1f8b92cdfc0c"}}
#assert that c1=93.2294453333
assert_almost_equal(c1,93.2294453333,decimal=3)

# %% [markdown]
# We can see that concentration has increased by only 0.2%.
#
# We have computed the evolution of the mass of sulfates in the TMF after one day. How would you do that after another day?
#
# We will use a loop to do that calculation, to compute the evolution of the concentration over a large period of time (10 years, for example), using daily timesteps again. 
#
# At the end, we want to plot the evolution of the concentration, so we have to store its values in an array, whose size corresponds to the amount of timesteps required. 
#
# Using daily timesteps, what size would that array need to be if we want to monitor the concentration for 10 years. That size is an integer called n.
#
#

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": false, "locked": false, "grade_id": "cell-1fd7b979fdedb3f6"}}
Tf = 10 #years

### BEGIN SOLUTION
n = int(1+365*Tf/dt)
### END SOLUTION

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-7a3c87c2eac1fad5"}}
# Assert that n = 3651
assert_almost_equal(n,3651,decimal=1)

# %%
import matplotlib.pyplot as plt
import numpy as np

# Let us assign some arrays to describe our problem
m = np.zeros(n, float) # represents the mass of sulfates (mg) at each time
c = np.zeros(n, float) # represents the concentration of sultates (mg/L) at each time
Spit = np.zeros(n, float) # represents at each time, the amount of sulfates (in kg) brought by the pit
Smill = np.zeros(n, float) # represents at each time, the amount of sulfates (in kg) brought by the mill
Sdis = np.zeros(n, float) # represents at each time, the amount of sulfates (in kg) discharged
Spore = np.zeros(n, float) # represents at each time, the amount of sulfates (in kg) brought by the tailing
time = np.zeros(n, float) # represents the time at each timestep
discharge = np.zeros(n, float) # represents the cumulative discharge of sulfates (in kg)

# %% [markdown]
# First, we initialize the initial mass and concentrations.
#

# %% {"lines_to_next_cell": 2}
m[0] = m0
c[0] = c0


# %% [markdown]
# Then, we need to compute these terms at every timesteps, by looping over the different times
#

# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "points": 5, "grade_id": "cell-02c577db8f512061"}}
###BEGIN SOLUTION
for i in range(n - 1):
    S_pit = Q_pit * c_pit
    S_mill = Q_mill * c_mill
    S_dis = Q_dis * c[i]
    S_pore = Area * k * (c_pore - c[i])
    
    Spit[i + 1] = S_pit * dt  * Seconds_in_a_day/ 1e6
    Smill[i + 1] = S_mill * dt  * Seconds_in_a_day/ 1e6
    Sdis[i + 1] = S_dis * dt  * Seconds_in_a_day/ 1e6
    Spore[i + 1] = S_pore * dt  * Seconds_in_a_day/ 1e6

    m[i + 1] = m[i] + (S_pore + S_pit + S_mill - S_dis) * dt  * Seconds_in_a_day
    discharge[i + 1] = discharge[i]  + S_dis * dt  * Seconds_in_a_day / 1e6
    c[i + 1] = m[i + 1] / V0
    time[i + 1] = (i+1) / 365  # time in years
###END SOLUTION


# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 5, "grade_id": "cell-b329fb3c5008055f"}}
assert_almost_equal(c[n-1],454.46947737053875,decimal=0)
### CHECK THAT THE LAST VALUE OF c is between 500-520 mg/L
### CHECK that last discharge value is around m(n-1) is between  4.4e6 and 4.6e6

# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 0, "grade_id": "cell-e9da3dd3143069f1"}}
assert_almost_equal(discharge[n-1],4.584599422624083e+06,decimal=1)

# %% [markdown]
# The calculation is now performed, let us look at the results using matplotlib.
# Design 3 vertically stacked plots
# 1. The first should show the evolution of the concentration over time
# 2. The second should show the relative importance of the different sources/sinks
# 3. The third should show the cumulative discharge (in kg) of sulfates

# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "points": 5, "grade_id": "cell-46d08bddb2fe7b38"}}
# call a figure with two plots, vertically stacked, sharing x(time) axis

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# First plot is the evolution of concentration

ax1.plot(time, c, label="Concentration")
ax1.set(xlabel="Time (years)", ylabel="Concentration (mg/L)")


# Second plot is the relative contribution to the concentration

ax2.plot(time, Spit, label="Source (mg/L) from the pit")
ax2.plot(time, Smill, label="Source (mg/L) from the mill")
ax2.plot(time, Spore, label="Source (mg/L) from the underground")
ax2.plot(time, Sdis, label="Sink (mg/L) towards the discharge")
ax2.set(xlabel="Time (years)", ylabel="Different Contribution (kg)")
ax2.legend(loc="upper center", bbox_to_anchor=(1.3, 1))

ax3.plot(time, discharge, label="Discharge")
ax3.set(xlabel="Time (years)", ylabel="discharge (kg)")

# %% [markdown]
#
# ## Mass balance
#
# ### Associated ODE
#
# We can (and you will!) show that this problem can be described by a linear non-homogeneous 1st order ODE. We can (and you will) verify that the solution to this ODE is given by:
#
# \begin{equation}
# c_{\text{TMF}}(t) = \frac{Q}{\lambda} + A \mathrm{exp}(-\lambda t)
# \end{equation}
#
# where
# \begin{equation}
# \left\lbrace
# \begin{array}{lll}
# Q & = & \frac{Q_{\text{pit}}c_{\text{pit}} + Q_{\text{mill}}c_{\text{mill}}+ A_{\text{bottom}}kc_{\text{p}}}{V_0} \\ 
# \lambda & = & \frac{A_{\text{bottom}}k+Q_{\text{dis}}}{V_0} 
# \end{array}
# \right.
# \end{equation}
#
# Find the value of A so that the initial condition is satisfied.
#

# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 0, "grade_id": "cell-6f7dd8352a1c8c86"}}
A = 0
# Assign A to its real value so that the previous solution matches the initial ccondition of the problem
###BEGIN SOLUTION
c_inf = (Q_pit * c_pit + Q_mill * c_mill + Area * k * c_pore) / (Q_dis + Area * k)
A = c0 - c_inf
###END SOLUTION


# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 2, "grade_id": "cell-0093877e19c5c0c6"}}
#check that A is between -417 and -418
assert_almost_equal(A,-417.6796,decimal=0)

# %% [markdown] {"lines_to_next_cell": 2}
# Again, we want a triple vertical plots (with time as x-axis).
# 1. The first plot shows the computed solution vs the analytical solution
# 2. The second plot shows the absolute error (computed_solution - real solution)
# 3. The third plot shows the relative error (computed_solution-real_solution)/real_solution
#
# To do that, you need to compute the real solution and store it in an array. You also have to compute the error and relative error. The next cell should contain the analytical calculation of the real solution and every plot material.


# %% {"nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "points": 5, "grade_id": "cell-7566713fe04d3d02"}}
###BEGIN SOLUTION
c_real = np.zeros(n, float)
error = np.zeros(n, float)
rel_error = np.zeros(n, float)
rel_error[0] = 0
error[0] = 0
c_real[0] = c0
lam = (Area * k + Q_dis) / V0
for i in range(n - 1):
    c_real[i + 1] = c_inf + (c0 - c_inf) * np.exp(-lam * time[i + 1] * 24 * 3600 * 365)
    error[i + 1] = c[i + 1] - c_real[i + 1]
    rel_error[i + 1] = (c[i + 1] - c_real[i + 1]) / c_real[i + 1]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# First plot is the evolution of concentration

ax1.plot(time, c, label="Concentration")
ax1.plot(time, c_real, label="Real solution")
ax1.set(xlabel="Time (years)", ylabel="Concentration (mg/L)")
ax1.legend()

# Second plot is the evolution of the error

ax2.plot(time, error, label="Absolute error")
ax2.set(xlabel="Time (years)", ylabel="Error (mg/L)")
ax2.legend()

# Third plot is the relative error
ax3.plot(time, rel_error, label="Relative error")
ax3.set(xlabel="Time (years)", ylabel="Error (-)")
ax3.legend()

###END SOLUTION

# %% [markdown]
# ### Influence of the timestep
#
# The error is arising from the timestepping approach we have used. During one timestep, we have computed the discharge flux and the source-term from the "pore" as if the concentration $c_{\text{TMF}}$ was constant through the timestep. This is actually not true. So, the bigger the timesteps, the bigger the error.
#
# Try the same methods used above for different timesteps (0.1 day, 1 day, 10 days, 50 days) and compare each of these solutions to the real solution and comment on the error.

# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "points": 5, "grade_id": "cell-2fec890573e90a1b"}}
###BEGIN SOLUTION
# First timestep = 0.1 day
n = 1 + 10 * 365 * Tf
dt = 0.1 * Seconds_in_a_day
m1 = np.zeros(n, float)
c1 = np.zeros(n, float)
time1 = np.zeros(n, float)
error1 = np.zeros(n, float)
m1[0] = m0
c1[0] = c0

for i in range(n - 1):
    S_pit = Q_pit * c_pit
    S_mill = Q_mill * c_mill
    S_dis = Q_dis * c1[i]
    S_pore = Area * k * (c_pore - c1[i])

    m1[i + 1] = m1[i] + (S_pore + S_pit + S_mill - S_dis) * dt
    c1[i + 1] = m1[i + 1] / V0
    time1[i + 1] = i * 0.1 / 365  # time in years
    c_real_t = c_inf + (c0 - c_inf) * np.exp(-lam * time1[i + 1] * 24 * 3600 * 365)
    error1[i + 1] = (c1[i + 1] - c_real_t) / c_real_t

## Second timestep = 10 day
n = 1 + int(365 / 10 * Tf)
dt = 10 * Seconds_in_a_day
m2 = np.zeros(n, float)
c2 = np.zeros(n, float)
error2 = np.zeros(n, float)
time2 = np.zeros(n, float)
m2[0] = m0
c2[0] = c0

for i in range(n - 1):
    S_pit = Q_pit * c_pit
    S_mill = Q_mill * c_mill
    S_dis = Q_dis * c2[i]
    S_pore = Area * k * (c_pore - c2[i])

    m2[i + 1] = m2[i] + (S_pore + S_pit + S_mill - S_dis) * dt
    c2[i + 1] = m2[i + 1] / V0
    time2[i + 1] = i * 10 / 365  # time in years
    c_real_t = c_inf + (c0 - c_inf) * np.exp(-lam * time2[i + 1] * 24 * 3600 * 365)
    error2[i + 1] = (c2[i + 1] - c_real_t) / c_real_t

## Third timestep = 50 day
n = 1+int(365 / 50 * Tf)
dt = 50 * Seconds_in_a_day
m3 = np.zeros(n, float)
c3 = np.zeros(n, float)
time3 = np.zeros(n, float)
error3 = np.zeros(n, float)
m3[0] = m0
c3[0] = c0

for i in range(n - 1):
    S_pit = Q_pit * c_pit
    S_mill = Q_mill * c_mill
    S_dis = Q_dis * c3[i]
    S_pore = Area * k * (c_pore - c3[i])

    m3[i + 1] = m3[i] + (S_pore + S_pit + S_mill - S_dis) * dt
    c3[i + 1] = m3[i + 1] / V0
    time3[i + 1] = i * 50 / 365  # time in years
    c_real_t = c_inf + (c0 - c_inf) * np.exp(-lam * time3[i + 1] * 24 * 3600 * 365)
    error3[i + 1] = (c3[i + 1] - c_real_t) / c_real_t

## Plot the different

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# First plot is the evolution of concentration

ax1.plot(time1, c1, label="Concentration - tstep = 0.1 day")
ax1.plot(time, c, label="Concentration - tstep = 1 day")
ax1.plot(time2, c2, label="Concentration - tstep = 10 days")
ax1.plot(time3, c3, label="Concentration - tstep = 50 days")
ax1.plot(time, c_real, label="Real solution")
ax1.set(xlabel="Time (years)", ylabel="Concentration (mg/L)")
ax1.legend(loc="upper center", bbox_to_anchor=(1.3, 1))

# Second plot is the evolution of the error

ax2.plot(time1, 100 * error1, label="Rel error - tstep = 0.1 day")
ax2.plot(time, 100 * rel_error, label="Rel error - tstep = 1 day")
ax2.plot(time2, 100 * error2, label="Rel error - tstep = 10 days")
ax2.plot(time3, 100 * error3, label="Rel error - tstep = 50 days")
ax2.set(xlabel="Time (years)", ylabel="Error (%)")
ax2.legend()

###END SOLUTION


# %% [markdown] {"lines_to_next_cell": 2, "trusted": false}
# How would you change the method if the volume of water was not constant? 


# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "points": 3, "grade_id": "cell-1b62e4a53dbbbe2c"}}
# I WANT THEM TO SAY THAT AFTER EACH TIMESTEP, THEY WOULD HAVE TO COMPUTE V, 
# the volume of water, and use that value to divide the mass to obtain the concentration. 
# But we might not have an analytical solution then!


# %%

