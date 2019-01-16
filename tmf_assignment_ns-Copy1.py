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
# <div class="toc"><ul class="toc-item"></ul></div>
# %% [markdown]
# **EOSC 213**
#
# **Mixing calculations**
#
# **ODEs and Euler’s method**
#
# The objective of this assignment is to create a python program that
# computes the concentration of sulfate in time in the water in a tailings
# management facility (TMF) at a mine site.
#
# **Problem description and conceptual model**
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
# **Identification of sulfate sources**
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
# **Parameters**
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
# **Evolution of the mass of water**
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
# \Longleftrightarrow & V(t+\Delta t)-V(t) & = &  Q_{\text{pit}} \Delta t + Q_{\text{mill}} \Delta t - Q_{\text{dis}} \Delta t \\
# \Longleftrightarrow & \frac{V(t+\Delta t)-V(t)}{\Delta t} & = &  Q_{\text{pit}}  + Q_{\text{mill}}  - Q_{\text{dis}}  \\
# \end{array}
# \end{equation}
#
# Considering the values given, we have:
#
# \begin{equation}
# \frac{V(t+\Delta t)-V(t)}{\Delta t} = 30 + 14 - 44 = 0 \Longleftrightarrow V(t) = V_0
# \end{equation}
#
# Indicating that the volume of water is constant through time.
#
# Let's assigne a variable $V_0$ whose value is the volume of water in the TMF:

# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "grade_id": "cell-74e6147961a870b0", "points": 1}}
V0 = 0
#Change the value of V0 to the one provided in the data (in L)

### BEGIN SOLUTION
V0 = 8.1e9 # volume of water in L
### END SOLUTION


# %% {"nbgrader": {"schema_version": 1, "solution": false, "grade": true, "locked": true, "points": 1, "grade_id": "cell-51e38c4e99635e26"}}
# Need to provide a test 
#assert that V0 = 8.1e9

# %% [markdown]
# **Evolution of the mass of sulfates**
#
# We have 4 main processes impacting the quantity of sulfates in the TMF. We will compute the evolution of this mass over time. First, initialize the required variable (initial mass, and the different input parameters).
#
#
#

# %% {"lines_to_next_cell": 2, "nbgrader": {"schema_version": 1, "solution": true, "grade": true, "locked": false, "points": 1, "grade_id": "cell-29bf1d749a2f8415"}}
c0 = 93 # initial concentration
Q_pit = 30
Q_mill = 14
Q_dis = 44

c_pit = 50
c_pore = 2000
c_mill = 700

k = 2.5e-5
Area = 3e5

#Initial mass of sulfates = Volume of water * c0
#Compute the initial mass of sulfates based on the previous variables
m0 = 0
### BEGIN SOLUTION
m0 = c0*V0
### END SOLUTION



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
# Compute the mass of sulfates after 1 day if the pit is the only source of sulfate. Create a variable S_pit corresponding to the mass of sulfates brought by the pit.
#
#

# %%
dt = 1 # day
Seconds_in_a_day = 24*3600
dt = dt*Seconds_in_a_day
m = m0 + Q_pit*c_pit*dt
S_pit = Q_pit*c_pit*dt

S_pit

# %% [markdown]
# 2. Advective flux from the mill
#
# Do the same if we only consider the mill as a sulfate source. (name of the variable = S_mill)
#
#

# %%
m = m0 + Q_mill*c_mill*dt
S_mill = Q_mill*c_mill*dt
S_mill

# %% [markdown]
# 3. Discharge flux from the TMF
#
# The same development can be performed for the discharge of water. The volume of water leaving the TMF over a certain period $\Delta t$ is $S_{\text{dis}} = Q_{\text{dis}} \Delta t$. The concentration of sulfates in this volume corresponds to the concentration of sulfates in the TMF $c_{\text{TMF}}$, so that we can write:
#
# \begin{equation}
# M_{\text{dis}} = Q_{\text{dis}}  c_{\text{TMF}} \Delta t
# \end{equation}
#
# How will the discharge change the mass of sulfates over one day? Create a variable called S_dis which stores that value.
#

# %%
m = m0 - Q_dis*c0*dt
S_dis = Q_dis*c0*dt
S_dis

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
# How will this mass transfer impact the mass of sulfate? Create a variable S_pore which stores the value of the sulfate brought by this first order mass transfer
#

# %%
m = m0 + Area * k * (c_pore-c0) * dt
S_pore = Area * k * (c_pore-c0) * dt
print(S_pore)

# %% [markdown]
# Now, compute the total evolution of the mass of sulfates after one day, and print its value and how it has changed.
#

# %%
m = m0 + S_pore + S_pit + S_mill - S_dis
print(S_pore)
print(S_pit)
print(S_mill)
print(S_dis)
S_pore + S_pit + S_mill - S_dis

# %% [markdown]
# This is the mass, to compute the new concentration, we have to divide by the mass of water. 

# %%
c = m/V0
c

# %% [markdown]
# We can see that concentration has increased by only 0.2%.

# %% {"lines_to_next_cell": 2}






# %% [markdown]
# We have computed the evolution of the mass of sulfates in the TMF after one day. Let us apply the same method over a large period of time, using daily timesteps again. Let's say we want to model the evolution of the mass over a period of 10 years. Create and initialize the required arrays.
#

# %%
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% [markdown]
# Before setting an array, it is better to know its size.
#

# %%
Tf = 10 # years
n = 365*Tf # 1 calculation per day, for Tf years

m = np.zeros(n, float)
c = np.zeros(n, float)
Spit = np.zeros(n,float)
Smill = np.zeros(n,float)
Sdis = np.zeros(n,float)
Spore = np.zeros(n,float)
time = np.zeros(n,float)
discharge = np.zeros(n,float)

# %% [markdown]
# Then, let us initialize the initial values.
#

# %% {"lines_to_next_cell": 2}
m[0] = m0
c[0] = c0


# %% [markdown]
# Then, we need to compute these terms at every timesteps, by looping over the different times
#

# %%
for i in range(n - 1):
    S_pit = Q_pit*c_pit
    S_mill = Q_mill*c_mill
    S_dis = Q_dis*c[i]
    S_pore = Area*k*(c_pore-c[i])
    
    Spit[i+1] = S_pit*dt/1e6
    Smill[i+1] = S_mill*dt/1e6
    Sdis[i+1] = S_dis*dt/1e6
    Spore[i+1] = S_pore*dt/1e6
    
    m[i+1] = m[i] + (S_pore + S_pit + S_mill - S_dis)*dt
    discharge[i+1] = discharge[i] + (S_pore + S_pit + S_mill - S_dis)*dt/1e6
    c[i+1] = m[i+1]/V0
    time[i+1] = i/365 #time in years
    
    

# %% [markdown]
# The calculation is now performed, let us look at the results using matplotlib.

# %%
# call a figure with two plots, vertically stacked, sharing x(time) axis

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# First plot is the evolution of concentration

ax1.plot(time, c, label="Concentration")
ax1.set(xlabel="Time (years)",ylabel="Concentration (mg/L)")


# Second plot is the relative contribution to the concentration

ax2.plot(time, Spit, label="Source (mg/L) from the pit")
ax2.plot(time, Smill, label="Source (mg/L) from the mill")
ax2.plot(time, Spore, label="Source (mg/L) from the underground")
ax2.plot(time, Sdis, label="Sink (mg/L) towards the discharge")
ax2.set(xlabel="Time (years)", ylabel="Different Contribution (kg)")
ax2.legend(loc='upper center', bbox_to_anchor=(1.3, 1));

ax3.plot(time, discharge, label="Discharge")
ax3.set(xlabel="Time (years)",ylabel="discharge (kg)")

# %% [markdown]
#

# %% [markdown]
# **Mass balance**
#
# ** Associated ODE **
#
# Therefore, if the mass of sulfates at a certain time $t_0$ $m(t)$ is $m(t_0) = m_0$, the mass of sulfates at $t+\Delta t$ is:
# \begin{equation}
# \begin{array}{llll}
# & m(t_0 + \Delta t) & = & m(t_0) + M_{\text{pit}} + M_{\text{mill}} + M_{\text{pore}} - M_{\text{dis}} \\
# \Longleftrightarrow & m(t_0 + \Delta t) & = & m(t_0) + \left(Q_{\text{pit}}  c_{\text{pit}} + Q_{\text{mill}}  c_{\text{mill}} + A_{\text{bottom}} k \left( c_{\text{pore}} - c_{\text{TMF}}  \right)    -Q_{\text{dis}} c_{\text{TMF}}\right) \Delta t \\
# \Longleftrightarrow & \frac{m(t_0 + \Delta t)-m(t_0)}{\Delta t} & = &  Q_{\text{pit}}  c_{\text{pit}} + Q_{\text{mill}}  c_{\text{mill}} + A_{\text{bottom}} k \left( c_{\text{pore}} - c_{\text{TMF}}  \right)    -Q_{\text{dis}} c_{\text{TMF}}  \\
# \end{array}
# \end{equation}
#
# The link between concentration and mass of sulfates is the volume of water
# \begin{equation}
# c_{\text{TMF}}(t) = \frac{m(t)}{V(t)}
# \end{equation}
#
# But, since the volume of water is constant, we have:
# \begin{equation}
# c_{\text{TMF}}(t) = \frac{m(t)}{V_0}
# \end{equation}
#
# Therefore, if we divide the latter equation by $V_0$, we have:
# \begin{equation}
# \frac{c_{\text{TMF}}(t_0 + \Delta t)-c_{\text{TMF}}(t_0)}{\Delta t} =  \frac{Q_{\text{pit}}  c_{\text{pit}} + Q_{\text{mill}}  c_{\text{mill}} + A_{\text{bottom}} k \left( c_{\text{pore}} - c_{\text{TMF}}  \right)    -Q_{\text{dis}} c_{\text{TMF}}}{V_0}
# \end{equation}
#
# Going to the limit $\Delta t \rightarrow 0$ (i.e. $\Delta t= dt$), this becomes:
# \begin{equation}
# \frac{dc_{\text{TMF}}}{dt} =  \frac{Q_{\text{pit}}  c_{\text{pit}} + Q_{\text{mill}}  c_{\text{mill}} + A_{\text{bottom}} k \left( c_{\text{pore}} - c_{\text{TMF}}  \right)    -Q_{\text{dis}} c_{\text{TMF}}}{V_0}
# \end{equation}
# which is a 1$^{st}$ order linear ODE.
#
# The latter can be rewritten in the following way:
#
# \begin{equation}
# \frac{dc_{\text{TMF}}}{dt} + \lambda c_{\text{TMF}} = Q
# \end{equation}
#
# ** Analytical Solution **
#
# Check that the solution of the homogeneous problem is
# \begin{equation}
# c_H(t) = A \mathrm{exp}(-\lambda t)
# \end{equation}
# Check that the solution of the particular problem is
# \begin{equation}
# c_p(t) = \frac{Q}{\lambda}
# \end{equation}
#
# So that the general solution to the ODE is:
# \begin{equation}
# c_{\text{TMF}}(t) = \frac{Q}{\lambda} + A \mathrm{exp}(-\lambda t)
# \end{equation}
#
# Find the value of A so that the initial condition is satisfied.
#

# %% {"lines_to_next_cell": 3}
# Assign a value of A so that function c_tmf is the analytical solution to the differential problem
c_inf = (Q_pit*c_pit+Q_mill*c_mill+Area*k*c_pore)/(Q_dis+Area*k)
A = c0 - c_inf







# %% [markdown]
# Plot the real analytical solution vs the computed solution.

# %%
#Since we need an exponential function, we need some mathematical features
import math

# %%
# code here the plots
c_real = np.zeros(n,float)
error = np.zeros(n,float)
rel_error = np.zeros(n,float)
rel_error[0] = 0
error[0] = 0 
c_real[0] = c0
lam = (Area*k+Q_dis)/V0
for i in range(n - 1):
    c_real[i+1] = c_inf + (c0-c_inf)*math.exp(-lam*time[i+1]*24*3600*365)
    error[i+1] = c[i+1] - c_real[i+1]
    rel_error[i+1] = (c[i+1]-c_real[i+1])/c_real[i+1]

fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize=(8, 12))

# First plot is the evolution of concentration

ax1.plot(time, c, label="Concentration")
ax1.plot(time, c_real, label="Real solution")
ax1.set(xlabel="Time (years)",ylabel="Concentration (mg/L)")
ax1.legend();

# Second plot is the evolution of the error

ax2.plot(time, error, label="Absolute error")
ax2.set(xlabel="Time (years)",ylabel="Error (mg/L)")
ax2.legend();

# Third plot is the relative error
ax3.plot(time, rel_error, label="Relative error")
ax3.set(xlabel="Time (years)",ylabel="Error (-)")
ax3.legend();

# %% [markdown]
# **Error estimation**
#
# Now that we know the real solution to the problem, we can assess the error we have made.
# Plot the absolute error, the relative error that we did through time.

# %%
# Plot the errors

# %% [markdown]
# **Influence of the timestep**
#
# The error is arising from the timestepping approach we have used. During one timestep, we have computed the discharge flux and the source-term from the "pore" as if the concentration $c_{\text{TMF}}$ was constant through the timestep. This is actually not true. So, the bigger the timesteps, the bigger the error.
#
# Try the same methods used above for different timesteps (0.1 day, 1 day, 10 days, 50 days) and compare each of these solutions to the real solution and comment on the error.

# %%
## First timestep = 0.1 day
n = 10*365*Tf
dt = 0.1*Seconds_in_a_day
m1 = np.zeros(n, float)
c1 = np.zeros(n, float)
time1 = np.zeros(n,float)
error1 = np.zeros(n,float)
m1[0] = m0
c1[0] = c0

for i in range(n - 1):
    S_pit = Q_pit*c_pit
    S_mill = Q_mill*c_mill
    S_dis = Q_dis*c1[i]
    S_pore = Area*k*(c_pore-c1[i])
    
    m1[i+1] = m1[i] + (S_pore + S_pit + S_mill - S_dis)*dt
    c1[i+1] = m1[i+1]/V0
    time1[i+1] = i*0.1/365 #time in years
    c_real_t = c_inf + (c0-c_inf)*math.exp(-lam*time1[i+1]*24*3600*365)
    error1[i+1] = (c1[i+1]-c_real_t)/c_real_t
    
## Second timestep = 10 day
n = int(365/10*Tf)
dt = 10*Seconds_in_a_day
m2 = np.zeros(n, float)
c2 = np.zeros(n, float)
error2 = np.zeros(n,float)
time2 = np.zeros(n,float)
m2[0] = m0
c2[0] = c0

for i in range(n - 1):
    S_pit = Q_pit*c_pit
    S_mill = Q_mill*c_mill
    S_dis = Q_dis*c2[i]
    S_pore = Area*k*(c_pore-c2[i])
    
    m2[i+1] = m2[i] + (S_pore + S_pit + S_mill - S_dis)*dt
    c2[i+1] = m2[i+1]/V0
    time2[i+1] = i*10/365 #time in years
    c_real_t = c_inf + (c0-c_inf)*math.exp(-lam*time2[i+1]*24*3600*365)
    error2[i+1] = (c2[i+1]-c_real_t)/c_real_t
    
## Third timestep = 50 day
n = int(365/50*Tf)
dt = 50*Seconds_in_a_day
m3 = np.zeros(n, float)
c3 = np.zeros(n, float)
time3 = np.zeros(n,float)
error3 = np.zeros(n,float)
m3[0] = m0
c3[0] = c0

for i in range(n - 1):
    S_pit = Q_pit*c_pit
    S_mill = Q_mill*c_mill
    S_dis = Q_dis*c3[i]
    S_pore = Area*k*(c_pore-c3[i])
    
    m3[i+1] = m3[i] + (S_pore + S_pit + S_mill - S_dis)*dt
    c3[i+1] = m3[i+1]/V0
    time3[i+1] = i*50/365 #time in years
    c_real_t = c_inf + (c0-c_inf)*math.exp(-lam*time3[i+1]*24*3600*365)
    error3[i+1] = (c3[i+1]-c_real_t)/c_real_t
    
## Plot the different

fig, (ax1,ax2) = plt.subplots(2, 1, figsize=(8, 8))

# First plot is the evolution of concentration

ax1.plot(time1, c1, label="Concentration - tstep = 0.1 day")
ax1.plot(time, c, label="Concentration - tstep = 1 day")
ax1.plot(time2, c2, label="Concentration - tstep = 10 days")
ax1.plot(time3, c3, label="Concentration - tstep = 50 days")
ax1.plot(time, c_real, label="Real solution")
ax1.set(xlabel="Time (years)",ylabel="Concentration (mg/L)")
ax1.legend(loc='upper center', bbox_to_anchor=(1.3, 1));

# Second plot is the evolution of the error

ax2.plot(time1, 100*error1, label="Rel error - tstep = 0.1 day")
ax2.plot(time, 100*rel_error, label="Rel error - tstep = 1 day")
ax2.plot(time2, 100*error2, label="Rel error - tstep = 10 days")
ax2.plot(time3, 100*error3, label="Rel error - tstep = 50 days")
ax2.set(xlabel="Time (years)",ylabel="Error (%)")
ax2.legend();



# %% {"lines_to_next_cell": 3}



