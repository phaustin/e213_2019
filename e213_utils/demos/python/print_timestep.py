# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#read-in-all-matrices-for-two-timesteps-and-save-in-a-dict" data-toc-modified-id="read-in-all-matrices-for-two-timesteps-and-save-in-a-dict-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>read in all matrices for two timesteps and save in a dict</a></span></li></ul></div>
# %%
from pathlib import Path

import context
import numpy as np

from e213_utils.write_matrix import bmatrix

# %% [markdown]
# # read in all matrices for two timesteps and save in a dict

# %%
timesteps = context.demo_dir.glob("**/*npz")
all_timesteps = list(timesteps)
timestep_dict = {}
for item in all_timesteps:
    all_vars = np.load(item)
    the_time = all_vars["t"]
    time_name = f"t_{the_time}"
    print(time_name)
    timestep_dict[time_name] = dict(all_vars)

# %% [markdown]
# # format the A matrix for timestep 25

# %%
A = timestep_dict["t_25"]["A"]
print(bmatrix(A))

# %% [markdown]
# \begin{align*}
# A_{25}=
# \begin{bmatrix}
#   1. & 0. & 0. & ... & 0. & 0. & 0.\\
#   -4.32 & 8.64 & -4.32 & ... & 0. & 0. & 0.\\
#   0. & -4.32 & 8.64 & ... & 0. & 0. & 0.\\
#   ...\\
#   0. & 0. & 0. & ... & 8.64 & -4.32 & 0.\\
#   0. & 0. & 0. & ... & -4.32 & 8.64 & -4.32\\
#   0. & 0. & 0. & ... & 0. & 0. & 1.\\
# \end{bmatrix}
# \end{align*}

# %% [markdown]
# # Same for Aa

# %%
Aa = timestep_dict["t_25"]["Aa"]
print(bmatrix(Aa))

# %% [markdown]
# \begin{align*}
# Aa=
# \begin{bmatrix}
#   1.8 & 0. & 0. & ... & 0. & 0. & 0.\\
#   -4.32 & 9.44 & -4.32 & ... & 0. & 0. & 0.\\
#   0. & -4.32 & 9.44 & ... & 0. & 0. & 0.\\
#   ...\\
#   0. & 0. & 0. & ... & 9.44 & -4.32 & 0.\\
#   0. & 0. & 0. & ... & -4.32 & 9.44 & -4.32\\
#   0. & 0. & 0. & ... & 0. & 0. & 1.8\\
# \end{bmatrix}
# \end{align*}

# %% [markdown]
# # Now do timestep 26

# %%
Aa = timestep_dict["t_26"]["Aa"]
print(bmatrix(Aa))

# %% [markdown]
# \begin{align*}
# Aa_{26} =
# \begin{bmatrix}
#   1.8 & 0. & 0. & ... & 0. & 0. & 0.\\
#   -4.32 & 9.44 & -4.32 & ... & 0. & 0. & 0.\\
#   0. & -4.32 & 9.44 & ... & 0. & 0. & 0.\\
#   ...\\
#   0. & 0. & 0. & ... & 9.44 & -4.32 & 0.\\
#   0. & 0. & 0. & ... & -4.32 & 9.44 & -4.32\\
#   0. & 0. & 0. & ... & 0. & 0. & 1.8\\
# \end{bmatrix}
# \end{align*}
