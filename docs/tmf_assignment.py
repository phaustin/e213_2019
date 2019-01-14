# -*- coding: utf-8 -*-
# ---
# jupyter:
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
# %% [markdown] {"toc": true, "lines_to_next_cell": 0}
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
# To compute the concentration of sulfate in the TMF water, we need to
# know where it is coming from and going to and use that knowledge to
# develop a conceptual model and then computational model.
#
# The figure below is a conceptual sketch of the main sources and losses
# of sulfate in the TMF water:
#
# ![](figures/tmf_box.png)
#
# 1)  From the pit. To keep the pit dry, water is constantly pumped out of
#     the pit and put into the TMF at a rate $Q_{\text{pit}}$
#     $m^{3}/s$ The pit water has a sulfate concentration of
#     $c_{\text{pit}}\ mg/L$.
#
# 2)  From the mill. The tailings are pumped into the TMF as a slurry of
#     tailings particles (fine, sand-size ground rock) and water. Assume
#     that the water from the mill enters the TMF at a rate of
#     $Q_{\text{mill}}\ m^{3}/s$ (of water), with a sulfate
#     concentration of $c_{\text{mill}}\ mg/L.$
#
# 3)  Diffusing from the tailings porewater at the bottom of the TMF into
#     the water column above. Sulfate dissolves from the tailings
#     particles into the adjacent porewater by oxidation of the sulfide
#     minerals in the particles. Because the ratio of rock to water is
#     high in the tailings sediments at the bottom, the porewater sulfate
#     concentration in the tailings, $c_{\text{pore}}$ , is always
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
# > where $j_{\text{pore}}\ mg/(s \cdot m^{2})$ is the flux rate of
# > sulfate per unit area of the bottom of the TMF and $k$ is the flux
# > coefficient with units of $L/(s \cdot m^{2})$ . To compute
# > $J_{\text{pore},}$the total mass flux rate for the whole TMF, with
# > units of $\frac{\text{mg}}{s}$, we must multiple the rate per unit
# > area $j_{\text{area}}$ by the total area of the TMF bottom
# > $A_{\text{bottom}}\ $ in $m^{2}$ :
#
# $J_{\text{pore}} = A_{\text{bottom}}{\times j}_{\text{pore}}$
#
# 4)  Leaving via the discharge ditch. Sulfate leaves the TMF with the
#     water that is discharged at a rate $Q_{\text{discharge}}\ m^{3}/s$
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
# | Symbol                   | Units                 | Description                                                  | Value                   |
# | ------------------------ | --------------------- | ------------------------------------------------------------ | ----------------------- |
# | $c_{\text{pit}}$       | $mg/L$              | Concentration of sulfate in pit water (assume constant)      | $50$                  |
# | $Q_{\text{pit}}$       | $m^{3}/s$           | Flow rate of water from the pit into TMF (assume constant)   | 0.030                   |
# | $c_{\text{mill}}$      | $mg/L$              | Concentration of sulfate in mill water (assume constant)     | $700$                 |
# | $Q_{\text{mill}}$      | $m^{3}/s$           | Flow rate of water from mill into TMF (assume constant)      | 0.014                   |
# | $Q_{\text{discharge}}$ | $m^{3}/s$           | Flow rate of water from TMF to environment (assume constant) | 0.044                   |
# | $c_{\text{pore}}$      | $mg/L$              | Concentration of sulfate in porewater at bottom of pond      | 2000                    |
# | $k$                    | $L/(s \cdot m^{2})$ | Flux coefficient from porewater to water column              | $2.5 \times 10^{- 5}$ |
# | $A_{\text{bottom}}$    | $m^{2}$             | Total area of TMF bottom                                     | $3 \times 10^{5}$     |
# | $V_{\text{TMF}}$       | $m^{3}$             | Volume of water in TMF at start of simulation                | $8.1 \times 10^{6}$   |
# | $c_{0}$                | $mg/L$              | Concentration of sulfate in TMF water at start of simulation | $93$                  |
#
# **Model**
#
# (to be finished)
#
# Assume all parameters are constant
#
# Use Euler’s method with daily time steps
#
# Compute concentrations for 3 years
#
# Plot concentration in TMF versus time
#
# Plot cumulative sulfate discharged to environment versus time
#
#
