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
#       jupytext_version: 1.0.0-rc4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Finite-volumes-6---flux-boundary-conditions" data-toc-modified-id="Finite-volumes-6---flux-boundary-conditions-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Finite volumes 6 - flux boundary conditions</a></span></li><li><span><a href="#Learning-goals" data-toc-modified-id="Learning-goals-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Learning goals</a></span></li><li><span><a href="#Prescribed-flux-boundary-conditions" data-toc-modified-id="Prescribed-flux-boundary-conditions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Prescribed flux boundary conditions</a></span><ul class="toc-item"><li><span><a href="#Summary-of-finite-volume-equations-(1-d,-steady-state,-no-sources-within-the-volume)" data-toc-modified-id="Summary-of-finite-volume-equations-(1-d,-steady-state,-no-sources-within-the-volume)-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Summary of finite-volume equations (1-d, steady-state, no sources within the volume)</a></span><ul class="toc-item"><li><span><a href="#Fundamental-1-d-steady-state-FV-equation" data-toc-modified-id="Fundamental-1-d-steady-state-FV-equation-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Fundamental 1-d steady-state FV equation</a></span></li><li><span><a href="#In-terms-of-specific-fluxes-and-areas-of-finite-volume-faces-(for-regular-retangular-gridblocks):" data-toc-modified-id="In-terms-of-specific-fluxes-and-areas-of-finite-volume-faces-(for-regular-retangular-gridblocks):-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>In terms of specific fluxes and areas of finite-volume faces (for regular retangular gridblocks):</a></span></li><li><span><a href="#Location-of-flux-boundary-condition" data-toc-modified-id="Location-of-flux-boundary-condition-3.1.3"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Location of flux boundary condition</a></span></li><li><span><a href="#Implications-for-grid-and-boundary-condition-locations" data-toc-modified-id="Implications-for-grid-and-boundary-condition-locations-3.1.4"><span class="toc-item-num">3.1.4&nbsp;&nbsp;</span>Implications for grid and boundary condition locations</a></span></li><li><span><a href="#Example" data-toc-modified-id="Example-3.1.5"><span class="toc-item-num">3.1.5&nbsp;&nbsp;</span>Example</a></span></li><li><span><a href="#Prescribed-flux-boundary-condition-in-a-discrete-approximation" data-toc-modified-id="Prescribed-flux-boundary-condition-in-a-discrete-approximation-3.1.6"><span class="toc-item-num">3.1.6&nbsp;&nbsp;</span>Prescribed flux boundary condition in a discrete approximation</a></span></li><li><span><a href="#In-terms-of-concentrations-in-gridblocks:" data-toc-modified-id="In-terms-of-concentrations-in-gridblocks:-3.1.7"><span class="toc-item-num">3.1.7&nbsp;&nbsp;</span>In terms of concentrations in gridblocks:</a></span></li></ul></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Your-turn---general-case" data-toc-modified-id="Your-turn---general-case-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Your turn - general case</a></span></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Your turn</a></span></li></ul></li><li><span><a href="#2-D-steady-state" data-toc-modified-id="2-D-steady-state-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>2-D steady-state</a></span><ul class="toc-item"><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Your turn</a></span><ul class="toc-item"><li><span><a href="#Question" data-toc-modified-id="Question-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Question</a></span></li></ul></li></ul></li><li><span><a href="#Gridblock-example---flux-boundary-conditions" data-toc-modified-id="Gridblock-example---flux-boundary-conditions-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Gridblock example - flux boundary conditions</a></span><ul class="toc-item"><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Your turn</a></span></li></ul></li></ul></div>

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "23e3b21b30740ba649f35ea22cafd0d1", "grade": false, "grade_id": "cell-dce79936fd0d883b", "locked": true, "schema_version": 1, "solution": false}}
# ## Finite volumes 6 - flux boundary conditions

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "c4586e87242364afee2c4bb622195696", "grade": false, "grade_id": "cell-d4bd812411f942f2", "locked": true, "schema_version": 1, "solution": false}}
#
#
# ## Learning goals
# 1. Be able to apply flux boundary conditions to a finite volume approximation.
# 2. To be able to compute local and global mass balance from a finite-volume discrete approximation.
# 3. Justify the use of harmonic averaging for heterogeneous diffusion coefficients to maintain mass balance.
# 4. Be able to express a finite-volume formulation in integral notation and identify each term in the integral expression.
# 5. Be able to describe the steps required to develop a general finite volume approximation for arbitrarily shaped elements.
#
# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "14b6cc48dc2789d6ac14ecdcfbd3db50", "grade": false, "grade_id": "cell-0645cb40abb7dc85", "locked": true, "schema_version": 1, "solution": false}}
# ## Prescribed flux boundary conditions
#
# For many problems, a prescribed flux is a natural boundary condition:
# * for solute diffusion - it prescribes the rate at which solute is fluxing into the problem domain (eg sulfate).
# * for water flow, a flux boundary condition describes the rate at which water enters into the problem domain.
# * perhaps the most common is a **zero flux** boundary condition - where the boundary is prescribed to not allow flux of a quantity across the boundary.
#
# Well first review the fundamental FV equations and show that flux boundary conditions can be easily incorporated into our stencils.
#
# ### Summary of finite-volume equations (1-d, steady-state, no sources within the volume)
# ####  Fundamental 1-d steady-state FV equation
#
# We developed the finite-volume approximations starting from the fundamental conservation equation which is already written in terms of fluxes:
#
# \begin{align}
# \left(J_{EC}+J_{WC}\right) &= 0 \label{eq761}\\
# \end{align}
#
# #### In terms of specific fluxes and areas of finite-volume faces (for regular retangular gridblocks):
#
# \begin{align}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) = 0 \label{eq762}\\
# \end{align}
#
# If our gridblock C lies on the boundary, a **prescribed flux boundary condition** means that one fluxes entering the gridblock is prescribed (known).
#
# #### Location of flux boundary condition
#
# For our 1-d problem, with the fluxes aligned with the $x$ direction, we have something that looks like 
#
# ![pic02](figures/single_block_flux.png){width="20%"}
#
# The fluxes $j_{EC}$ and $j_{WC}$ enter at the **boundary** of  gridblock C - between EC and WC:
# ![pic03](figures/finite_volume_1d_uniform.png){width="20%"}
#
# It is therefore best to conceive of the fluxes as being located at the **boundary** between gridblocks.
#
# #### Implications for grid and boundary condition locations
#
# When we are modeling a physical system: 
# * we place the edge of the gridblock on the boundary if the boundary is a prescribed flux boundary; 
# * we place the node on the boundary if it is a prescribed concentration boundary. 
#
# ![pic04](figures/bc_location.png){width="40%"}
#
# #### Example 
#
# Consider our simple 5-node example. In the physical system to be modeled, a flux of $j=0.37\times 10^{-8}~mg/(s\cdot m^2)$ of sulfate is entering from the left of the domain and the concentration is prescribed (fixed) at $c=9 ~mg/L$ on the right boundary:
#
# ![pic05](figures/ex_bc_location.png){width="50%"}
#
#
#
# #### Prescribed flux boundary condition in a discrete approximation
#
# Prescribing a flux boundary condition is equivalent to prescribing the value of $j_{WC}$ or $j_{EC}$ in a discrete approximation. So in our example above, for gridblock 1, the equation would look like:
# \begin{align}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) = 0 \label{eq763}\\
# &\left(j_{21}+0.37\times 10^{-8}\right) (\Delta y) (\Delta z) = 0 \label{eq764}\\
# \end{align}
#
# Be careful with the signs! Is the sign correct for the flux if it is entering gridblock 1?
#
#
# #### In terms of concentrations in gridblocks:
#
# Below is the equation for a generic gridblock C in the middle of the mesh. Let's see below how to modify it for a flux boundary condition.
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) = 0 \label{eq765}\\
# \end{align}
#
# %% [markdown]
# ### Your turn
#
# For the 5-node example above, write the equation for gridblock 1,  where $\Delta x=1~m$, $\Delta y = 1.5~m$, $\Delta z = 2.0~m$, $D\theta=10^{-9}~m^2/s$ and the flux on the left edge of gridblock 1 is $j = 0.37\times 10^{-8}~ mg/(s\cdot m^2)$:
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) = 0 \label{eq766}\\\end{align}
#
#

# %% [markdown]
# ### Your turn - general case
#
# Modify the equation below for the general case where the flux from W is prescribed to be $j_{WC} = f$, $f>0$. 
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) = 0 \label{eq767}\\\end{align}

# %% [markdown]
# ### Your turn
#
# Modify the generic equation below for the case where the flux from E is prescribed to be $j_{EC} = 0$, (no-flux boundary condition): 
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z) = 0 \label{eq768}\\
# \end{align}

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "aea22a90f55505b222840f87ab5cfd75", "grade": false, "grade_id": "cell-06ed146490002c3a", "locked": true, "schema_version": 1, "solution": false}}
# ## 2-D steady-state
#
# In 2-D, the general stencils for an interior gridblock C in terms of total flux, specific flux and concentrations are:
# \begin{align}
# &\left(J_{EC}+J_{WC} + J_{NC}+J_{SC}\right) = 0 \label{eq769}\\
# \end{align}
#
# \begin{align}
# &\left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) +\left(j_{NC}+j_{SC}\right) (\Delta x) (\Delta z)  = 0 \label{eq7610}\\
# \end{align}
#
#
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z)
# +\left(D\theta {c_N - c_C \over \Delta y} +   D\theta {c_S - c_C \over \Delta y}   \right) (\Delta x) (\Delta z)= 0 \label{eq7611}\\
# \end{align}
#
#
# ![pic05](figures/2d_flux.png){width="20%"}
#
# %% [markdown]
# ### Your turn
#
# Modify each of the three equations below for the situation where there is no flux to or from gridblocks N and S:
#
# \begin{align}
# \left(J_{EC}+J_{WC} + J_{NC}+J_{SC}\right) = 0 \label{eq7612}\\
# \end{align}
#
# \begin{align}
# \left(j_{EC}+j_{WC}\right) (\Delta y) (\Delta z) +\left(j_{NC}+j_{SC}\right) (\Delta x) (\Delta z)  = 0 \label{eq7613}\\
# \end{align}
#
# \begin{align}
# &\left(D\theta {c_E - c_C \over \Delta x} +   D\theta {c_W - c_C \over \Delta x}   \right) (\Delta y) (\Delta z)
# +\left(D\theta {c_N - c_C \over \Delta y} +   D\theta {c_S - c_C \over \Delta y}   \right) (\Delta x) (\Delta z)= 0\label{eq7614}\\
# \end{align}
#
# #### Question
# The result should be a familiar stencil. What is it?

# %% [markdown] {"deletable": false, "editable": false, "nbgrader": {"checksum": "65b96ce5b84939b6a466399725c0d09a", "grade": false, "grade_id": "cell-147565dbbdc2e7b0", "locked": true, "schema_version": 1, "solution": false}}
# ## Gridblock example - flux boundary conditions
#
# Let's write the equations for the 5-gridblock example from before, now with a flux boundary condition as shown (note $x$ and $y$ coordinate directions are as indicated,with $z$ into the page).
#
# ![pic06](figures/5node-flux-bc.png){width="50%"}
#
# The total length of the domain is $2~m$ in the $x$ direction, each gridblock is the same size and porosity and diffusion coefficient are spatially homogeneous:
# * $\Delta x=2/4.5 = 0.44~ m$
# * $\Delta y=0.3~m$
# * $\Delta z=0.5~m$
# * $D=2\times 10^{-10}~m^2/s$
# * $\theta = 0.25$
#
# Note that the *edge* of gridblock 1 is on the physical boundary whereas the node of gridblock 5 is on the physical boundary. Accordingly, there are 4.5 gridblocks across the 2-m domain, so each gridblock is 0.44 m in the x direction.
#

# %% [markdown]
# ### Your turn
#
# 1. Write the equations for the unknowns in the problem.
# 2. Solve the system of equations for the unknown concentrations. *(If you are doing this by hand, note that you can rescale any equation by dividing or multiplying all terms in the equation by the same number. Often it is convenient to divide all terms by the coefficient of the unknown on the "diagonal" - for equation number $n$, the diagonal is the coefficient that multiplies $c_n$.)*
# 3. In the cell below, report the concentration you computed in gridblock 1.
# 4. In the cell after that, use concentration values to compute the magnitude (i.e. a positive number) of the specific flux (in $mg/(s\cdot m^2)$) between gridblocks 4 and 5.
#

# %% {"deletable": false, "nbgrader": {"checksum": "33c79d7fd4c53b408b398e833fb3f680", "grade": true, "grade_id": "cell-ed1e0939f8b22f3c", "locked": false, "points": 5, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% [markdown] {"deletable": false, "nbgrader": {"checksum": "ec104f50c4023cbc45217d72eb8244d9", "grade": true, "grade_id": "cell-2d0e2bfde6d37dd2", "locked": false, "points": 3, "schema_version": 1, "solution": true}}
# 2a. Fill out the following A and b matrices for this problem, overwriting the non-zero values with your coefficients:
#
# ```
# A=
#
#  [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
#     
# b = [0. 0. 0. 0. 0.]    
# ```
#
# YOUR ANSWER HERE

# %% {"deletable": false, "nbgrader": {"checksum": "10f2cee16a67a505f06e05ae1dd509f8", "grade": true, "grade_id": "cell-1e73cc8d67fe6e28", "locked": false, "points": 5, "schema_version": 1, "solution": true}}
# 2b. solve the equations you just wrote down for the concentration c in steadcy state
# 
# Our solution in this cell follows the same pattern as the week6_assign.  That is,
# we defined a function called build_1d_matrix_source that produce a 5x5 matrix A
# and a 5x1 vector b, such that the 5 cell concentrations c can be found with the 
# following python code
#
# A,b = build_1d_matrix_source(...)
# c = np.linalg.solve(A, b)
#
# You can also show your hand calculations here.  If you do it by hand
# leave the concentrations in a list named c, so we can check the values
# like this
# 
# c=[c1,c2,c3,c4,c5]
#
# we will check your c[0]=c1 value against ours in a test below.
#

# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "nbgrader": {"checksum": "0be6182d8f2b81e81f7bdbd2184e5703", "grade": true, "grade_id": "cell-ccc57bfb8daad1dc", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
# In this cell show that for you value of the c vector, you do in fact get:
# A@c=b  (either by hand or with python code in this cell)

# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "c5e54a54db9da62a985f0c61d84190ca", "grade": true, "grade_id": "cell-27049aa4e7116667", "locked": true, "points": 2, "schema_version": 1, "solution": false}}
# 3. We check your c[0] for cell 1 here



# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "8a172c5987eb7c601b7b9373f0cc57c5", "grade": true, "grade_id": "cell-6f2482c5bcd0cee8", "locked": true, "points": 2, "schema_version": 1, "solution": false}}
# 4. We check your value for the flux between grid blocks 4 and 5 (c[3] and c[4])

