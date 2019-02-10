# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb
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
#     version: 3.6.7
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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Assignment" data-toc-modified-id="Assignment-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Assignment</a></span><ul class="toc-item"><li><span><a href="#Objectives-and-description**" data-toc-modified-id="Objectives-and-description**-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Objectives and description**</a></span></li><li><span><a href="#Problem-description-and-conceptual-model" data-toc-modified-id="Problem-description-and-conceptual-model-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Problem description and conceptual model</a></span></li><li><span><a href="#Identification-of-sulfate-sources" data-toc-modified-id="Identification-of-sulfate-sources-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Identification of sulfate sources</a></span><ul class="toc-item"><li><span><a href="#Parameters" data-toc-modified-id="Parameters-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Parameters</a></span></li></ul></li><li><span><a href="#Evolution-of-the-mass-of-water" data-toc-modified-id="Evolution-of-the-mass-of-water-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Evolution of the mass of water</a></span></li><li><span><a href="#Evolution-of-the-mass-of-sulfates" data-toc-modified-id="Evolution-of-the-mass-of-sulfates-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Evolution of the mass of sulfates</a></span></li><li><span><a href="#Mass-balance" data-toc-modified-id="Mass-balance-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Mass balance</a></span><ul class="toc-item"><li><span><a href="#Associated-ODE" data-toc-modified-id="Associated-ODE-1.6.1"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Associated ODE</a></span></li><li><span><a href="#Influence-of-the-timestep" data-toc-modified-id="Influence-of-the-timestep-1.6.2"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Influence of the timestep</a></span></li></ul></li></ul></li></ul></div>
# %% [markdown]
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
# %% [markdown]
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

Q_pit = 30
Q_mill = 14
Q_dis = 44
# %% {"deletable": false, "nbgrader": {"checksum": "ce2fa2dc080110310937d49e1616b156", "grade": true, "grade_id": "cell-a09bbce77de223da", "locked": false, "points": 1, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

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
# %%
V0 = 0
#  Change the value of V0 to match the given data
# %% {"deletable": false, "nbgrader": {"checksum": "61c0d80c72c243406544a3ecc38ce77a", "grade": false, "grade_id": "cell-113d07a78f5dd226", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "d9222a56f5fc34b98580b4540e34beec", "grade": true, "grade_id": "cell-ebe77652bfd42a8e", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
assert_almost_equal(V0, 8.1e9, decimal=1)

# %% [markdown]
# ## Evolution of the mass of sulfates
#
# We have 4 main processes impacting the quantity of sulfates in the TMF. We will compute the evolution of this mass over time. First, initialize the required variable (initial mass, and the different input parameters).
#
#
#

# %%
c0 = 93  # initial concentration

c_pit = 50
c_pore = 2000
c_mill = 700

k = 2.5e-5
Area = 3e5


# %% [markdown]
# What is the initial mass of sulfates? (in mg)
# %%
m0 = 0
# Change the value of m0 so that it corresponds to the initial mass (in mg) of sulfates in the TMF.
# %% {"deletable": false, "nbgrader": {"checksum": "d2a8d9e0c449ec3a003bda0b28e9fc2c", "grade": false, "grade_id": "cell-2372ba7e97931ee6", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "8a757e5acd0e5a31549e469d03f15843", "grade": true, "grade_id": "cell-bf5d8ad9924f2552", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
assert_almost_equal(m0, 7.533e11, decimal=1)

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
# %%
dt = 1  # day
Seconds_in_a_day = 24 * 3600
S_pit = 0
# %% {"deletable": false, "nbgrader": {"checksum": "dc41bfa6d057d79ba795408282bd74a6", "grade": false, "grade_id": "cell-be9d32b64825de70", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "7921d15075b542ee6bfc3552405968a1", "grade": true, "grade_id": "cell-b0f765e9007b556b", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
assert_almost_equal(S_pit, 129600000, decimal=1)

# %% [markdown]
# 2. Advective flux from the mill
#
# If we only consider the mill as a sulfate source, how will the mass of sulfates evolve in one day. Assign this value in variable named S_mill (in mg).
#
#
# %%
S_mill = 0
# %% {"deletable": false, "nbgrader": {"checksum": "304e34e7e76508399502176cea00e7cd", "grade": false, "grade_id": "cell-fc68eb0af7e61cfa", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "0fe72418d9dc6c56e7414077fbb5ba88", "grade": true, "grade_id": "cell-7584745de7a3187e", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
# assert that S_mill = 846720000
assert_almost_equal(S_mill, 846720000, decimal=1)

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
# %%
S_dis = 0
# %% {"deletable": false, "nbgrader": {"checksum": "93199e58de3c0eb91b10834355c95d9d", "grade": false, "grade_id": "cell-43706ee6c2fba2a1", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "508d95c7203c1141dcbb1aef7fae98b5", "grade": true, "grade_id": "cell-e29825a21bf3f2e8", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
assert_almost_equal(S_dis, 353548800, decimal=1)

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
# %%
S_pore = 0
# %% {"deletable": false, "nbgrader": {"checksum": "30c062c41a8a433f4749c58b92e3145b", "grade": false, "grade_id": "cell-9bff3ecfa902f301", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "e1de40d68e02708a0bd924015c8b27c8", "grade": true, "grade_id": "cell-c83065e1b82a3abe", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
# ASSERT THAT S_PORE = 1235736000.0
assert_almost_equal(S_pore, 1235736000, decimal=1)

# %% [markdown]
# Now, compute the total evolution of the mass of sulfates after one day, and print its value and how it has changed. Store that value (in mg) in a variable called m1.
#
# %%
m1 = 0
# %% {"deletable": false, "nbgrader": {"checksum": "4a01f3031b515507b63df859ea11989c", "grade": false, "grade_id": "cell-6077ebff299ad1b0", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "d3b3555ded14083db7edb2c4e713bfae", "grade": true, "grade_id": "cell-7af99e25848e170f", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
assert_almost_equal(m1, 755158507200, decimal=1)

# %% [markdown]
# This is the mass after 1 day (in mg). What is the concentration after one day? Store that value in a variable called c1 (in mg/L).
# %%
c1 = 0
# %% {"deletable": false, "nbgrader": {"checksum": "42ba143dd9f7d9c7b7303b5ef0deb59d", "grade": false, "grade_id": "cell-eed606a5f5b25f6f", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "559deac450d76b3c38e76c1b92b40061", "grade": true, "grade_id": "cell-bb3d1f8b92cdfc0c", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
# assert that c1=93.2294453333
assert_almost_equal(c1, 93.2294453333, decimal=3)

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
# %%
Tf = 10  # years
# %% {"deletable": false, "nbgrader": {"checksum": "e88e4890c63b05d04aab6b9adcababfc", "grade": false, "grade_id": "cell-1fd7b979fdedb3f6", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "40d8d857ebea8b8af041edfbc806b79f", "grade": true, "grade_id": "cell-7a3c87c2eac1fad5", "locked": true, "points": 1, "schema_version": 1, "solution": false}}
assert_almost_equal(n, 3651, decimal=1)

# %%
import matplotlib.pyplot as plt
import numpy as np

# Let us assign some arrays to describe our problem
m = np.zeros(n, float)  # represents the mass of sulfates (mg) at each time
c = np.zeros(n, float)  # represents the concentration of sultates (mg/L) at each time
Spit = np.zeros(
    n, float
)  # represents at each time, the amount of sulfates (in kg) brought by the pit
Smill = np.zeros(
    n, float
)  # represents at each time, the amount of sulfates (in kg) brought by the mill
Sdis = np.zeros(
    n, float
)  # represents at each time, the amount of sulfates (in kg) discharged
Spore = np.zeros(
    n, float
)  # represents at each time, the amount of sulfates (in kg) brought by the tailing
time = np.zeros(n, float)  # represents the time at each timestep
discharge = np.zeros(
    n, float
)  # represents the cumulative discharge of sulfates (in kg)

# %% [markdown]
# First, we initialize the initial mass and concentrations.
#

# %%
m[0] = m0
c[0] = c0


# %% [markdown]
# Then, we need to compute these terms at every timesteps, by looping over the different times
#

# %% {"deletable": false, "nbgrader": {"checksum": "8ebe18f8759402c7c4a9bf985535a7b0", "grade": true, "grade_id": "cell-02c577db8f512061", "locked": false, "points": 5, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "b787e4bb171a06028d795ffca83a992f", "grade": true, "grade_id": "cell-b329fb3c5008055f", "locked": true, "points": 5, "schema_version": 1, "solution": false}}
assert_almost_equal(c[n - 1], 454.46947737053875, decimal=0)

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "d30a2bf6faebd3689d6c059afebf7f74", "grade": true, "grade_id": "cell-e9da3dd3143069f1", "locked": true, "points": 0, "schema_version": 1, "solution": false}}
assert_almost_equal(discharge[n - 1], 4.584599422624083e06, decimal=1)

# %% [markdown]
# The calculation is now performed, let us look at the results using matplotlib.
# Design 3 vertically stacked plots
# 1. The first should show the evolution of the concentration over time
# 2. The second should show the relative importance of the different sources/sinks
# 3. The third should show the cumulative discharge (in kg) of sulfates

# %% {"deletable": false, "nbgrader": {"checksum": "658f539be87f5a2b14570bae69957f79", "grade": true, "grade_id": "cell-46d08bddb2fe7b38", "locked": false, "points": 5, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

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
# %
# A = 0
# Assign A to its real value so that the previous solution matches the initial ccondition of the problem
# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "7919f4ae83f46e65df4357d06328d4cf", "grade": true, "grade_id": "cell-6f7dd8352a1c8c86", "locked": true, "points": 2, "schema_version": 1, "solution": false}}


# %% {"deletable": false, "nbgrader": {"checksum": "609b0e16b5294c5fd70a7daf46fff2c1", "grade": false, "grade_id": "cell-0093877e19c5c0c6", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% [markdown]
# Again, we want a triple vertical plots (with time as x-axis).
# 1. The first plot shows the computed solution vs the analytical solution
# 2. The second plot shows the absolute error (computed_solution - real solution)
# 3. The third plot shows the relative error (computed_solution-real_solution)/real_solution
#
# To do that, you need to compute the real solution and store it in an array. You also have to compute the error and relative error. The next cell should contain the analytical calculation of the real solution and every plot material.


# %% {"deletable": false, "nbgrader": {"checksum": "96bd347400fdf890fdf8ab2249265bbb", "grade": true, "grade_id": "cell-7566713fe04d3d02", "locked": false, "points": 5, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% [markdown]
# ### Influence of the timestep
#
# The error is arising from the timestepping approach we have used. During one timestep, we have computed the discharge flux and the source-term from the "pore" as if the concentration $c_{\text{TMF}}$ was constant through the timestep. This is actually not true. So, the bigger the timesteps, the bigger the error.
#
# Try the same methods used above for different timesteps (0.1 day, 1 day, 10 days, 50 days) and compare each of these solutions to the real solution and comment on the error.

# %% {"deletable": false, "nbgrader": {"checksum": "6fdc73f03a2af6958fc0e64b44654f21", "grade": true, "grade_id": "cell-2fec890573e90a1b", "locked": false, "points": 5, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% [markdown]
# How would you change the method if the volume of water was not constant?


# %% {"deletable": false, "nbgrader": {"checksum": "1f983f73c4c31f143a687045ffdb3818", "grade": true, "grade_id": "cell-1b62e4a53dbbbe2c", "locked": false, "points": 3, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %%
