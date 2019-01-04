# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-to-computational-methods" data-toc-modified-id="Introduction-to-computational-methods-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to computational methods</a></span><ul class="toc-item"><li><span><a href="#Data-file" data-toc-modified-id="Data-file-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Data file</a></span></li><li><span><a href="#Algorithm" data-toc-modified-id="Algorithm-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Algorithm</a></span></li><li><span><a href="#Python-code" data-toc-modified-id="Python-code-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Python code</a></span></li><li><span><a href="#Python-modules/libraries" data-toc-modified-id="Python-modules/libraries-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Python modules/libraries</a></span></li><li><span><a href="#Handle-graphics-with-Matplotlib" data-toc-modified-id="Handle-graphics-with-Matplotlib-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Handle graphics with <code>Matplotlib</code></a></span></li></ul></li></ul></div>
# %% [markdown]
# # Introduction to computational methods
#
# This notebook introduces a python program to integrate daily average flow into and out of
# the tailings management facility (TMF), and the volume of water in the TMF through time.
#
# ## Data file
# This notebook assumes that a comma-separated variable (csv) file named `july2016-tmf-flow.csv`
# exists in the current working directory. The file contains three columns with headers:
#
# `date` `outflow` `inflow`
#
# The first 4 lines of the file are:
#
# `date,outflow,inflow
# 2016-07-01,0.0703,0.1181
# 2016-07-02,0.066,0.1121
# 2016-07-03,0.0621,0.1079`
#
# The data in the csv file is in the following format
#
# `date` is in `yyyy-mm-dd`
#
# `outflow` is the daily average outflow in $m^3/s$
#
# `inflow` is the daily average inflow in $m^3/s$
#
#
#
# ## Algorithm
# The volume of water in the TMF on day $t$ of the computation is $V(t)$, the daily average outflow is $Q_{out}$
# and the daily average inflow is $Q_{out}$
#
# The basic computational algorithm is:
#
# 1. Read in the date, $Q_{out}$ and $Q_{out}$ data from the file `july2016-tmf-flow.csv`.
# 2. Compute the change in volume over the day $\Delta V = (Q_{in} - Q_{out})\Delta t$
# 3. Update the volume of the TMF: $V(t+\Delta t) = V(t) + \Delta V$
# 4. Loop through all dates in the file until complete.
# %% [markdown]
# ## Python code
# We'll introduce python concepts as we go in the course, so we don't expect you to fully understand
# this code yet. We'll therefore only provide a cursory explanation here.
#
# %% [markdown]
# ## Python modules/libraries
# It is good practice to import libaries at the beginning of a program. Libaries are collections of python code.
#
# %%
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# %% [markdown]
# The `import` command tells python to import the library. The `as` specifies a user - chosen nickname for library
# to be used in this program. So for this program, the `numpy` library will also be known as `np`.
#
# We are importing four libraries or library sections:
#
# `numpy` is a library with numerical - related codes. We'll use it alot in the course.
#
# `pandas` is a libary with codes to manipulate tabular data, that is data organized in rows and columns.
#
# `matplotlib` is a vast library for plotting. We don't need the whole library, but only two subsections.
#
# `matplotlib.pyplot`, nicknamed `plt` is a subsection containing so-called handle graphics. We'll use it alot.
#
# `matplotlib.dates`,  which we nickname `mdates` is a specialty subsection containing code for manipulating date formats.
#

# %%
# use pandas to read in csv data
data_file = "july2016-tmf-flow.csv"
flow = pd.read_csv(data_file)

# %% [markdown]
# The `pd.read_csv` command from the `pandas` library reads all the rows and columns from the file `july2016-tmf-flow.csv`.
#
# We could have also written the command as `pandas.read.csv`, but we used our nickname `pd` to save some typing.
#
# Here we see the power of the pandas library. This command contains code to open the file, read in each line of data from the
# csv file,and then stores that data in a `dataframe` that we named `flow`. You can think of a `dataframe` as rows and
# columns of data. In our case, the data in the `dataframe` is dates, outflows and inflows.

# %%
# find number of days of data in file using shape method on dataframe named flow

n = flow.shape[0]
print(f"Number of days in file: {n}")

# %% [markdown]
# This line of code uses the `.shape` method, which returns the dimension (number of rows and columns) in the dataframe
# `flow`. `.shape[0]` is the number of rows, or in our case, the number of days of outflow and inflow data in the dataframe,
# which we assign to the variable `n`.
#
#

# %%
# allocate np arrays for time and volume for calculations -
# doing this in advance makes python run faster

v = np.zeros(n, float)

# %% [markdown]
# The function `zeros` from the numpy library creates an array of zeros. Python runs faster if the arrays used for computation
# are defined in advance, versus on the fly. Here we create an array `v` of `n` zeros of type `float`. Each element in
# `v` will store the volume of water in the TMF on a specific day.

# %%
# print  the columns in the dataframe
print(f"Columns in csv file: {flow.columns}")

# convert column called date to pandas date format
# and store in column called yearmonthday

flow["yearmonthday"] = pd.to_datetime(flow["date"])

# see the data in the column yearmonthday
print(f"type of the timestap object: {type(flow['yearmonthday'][0])}")


# %% [markdown]
# We first print the names of the columns in the dataframe that were read in from the `csv` file.
# We do this using the `.columns` method on the `flow` dataframe; that is `flow.columns` returns the indices of
# the columns in the dataframe.
#
# The command `flow["yearmonthday"] = pd.to_datetime(flow["date"]` uses the pandas method `.to_datetime`
# to convert the data in the column indexed with `date` in the dataframe `flow` to a date format that pandas
# understands, and then stores those panda dates in the dataframe `flow` in a new column with index `yearmonthday`.
#
# We then print out the type of the data in the column `yearmonthday` to prove that it is now a date.

# %%
# set volume in TMF at time zero to 8.1 x 10^6 m^3

v[0] = 8.1e6

"""
loop through and compute volume through time
since flow is in m^3/s, and flows are daily average flows, must convert
to m^3 in a day by multiplying by 86400 s/d
"""
seconds_per_day = 86400.0
for i in range(n - 1):
    v[i + 1] = v[i] + (flow["inflow"][i] - flow["outflow"][i]) * seconds_per_day


# %% [markdown]
# This is the guts of the computation. We first set the volume in the TMF at time zero to $8.1\times 10^6 m^3$.
#
# Then we loop through the days in the dataframe and compute the change in volume over each day as described above:
# $V(t+\Delta t) = V(t) + (Q_{in} - Q_{out})\Delta t$, where $\Delta t$ is $86400$ seconds (one day).
#
# In python we use a `for` loop. The command `for i in range(n - 1):` sets `i` to `0`, then enters the loop and when finished the loop,
# sets `i` to `1`, enters the loop,..., `n-1`.
# On the last time through the loop, `i=n-1` so that when we compute`v[i+1]` for the last time, we are computing `v[n]`.
#
# The rest of the code is used to generate the plot of outflow and inflow over time in on subplot,
# and volume of water in the TMF over time in another subplot.

# %%
# call a figure with two plots, vertically stacked, sharing x axis

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 8))

# format for the x axis label to be month - day eg 07-03 for July 3
# format string for dates that will be plotted on the x axis

myFmt = mdates.DateFormatter("%m-%d")

# in the plot ax, plot outflow and inflow as separate lines

ax1.plot(flow["yearmonthday"], flow["outflow"], label="Outflow")
ax1.plot(flow["yearmonthday"], flow["inflow"], label="Inflow")
ax1.set(ylabel="flow $m^3/s$")
ax1.legend()

# set format string for the major labels on the x axis

ax1.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()

# in second plot, plot the volume in TMF in m^3, which is stored in the array v

ax2.plot(flow["yearmonthday"], v, label="Volume in TMF")
ax2.set(xlabel="date", ylabel="Volume in TMF $m^3$")
ax2.legend()


# %% [markdown]
# ## Handle graphics with `Matplotlib`
#
# Python's `matplotlib` package is massive and can be confusing. We hope that by showing you
# the essentials in this course, you can later learn what you need on your own.
#
# The first thing we do here is call into existence a `figure`, which is a place to put plots,
# and tell python that we want two subplots, confusingly called `axes`, to go into the figure.
#
# (if you want more details right away, see https://realpython.com/python-matplotlib-guide/)
#
# The command `fig, (ax1,ax2) = plt.subplots(2,1, sharex=True)` calls the `subplots` function
# from `matplotlib.pyplot` library, nicknamed in our code as `plt` hence the function
# name `plt.subplots`. The `2, 1` argument indicates we want the subplots in 2 rows, 1 column,
# and the `sharex=True` indicates both plots share the same x axis.  The two axes objects are *unpacked*
# into the two variables ax1 and ax2.

# %% [markdown]
# The two plots (axes) we created are here
# referenced as `ax1` and `ax2`. Axes are a special
# object type in python. We then apply methods (functions specific to a particular object type)
# to the axes to create the plots, adding data, formating etc with a sequence of methods.
# When we have finished, we use the function `plt.show()` to show the plots.
#
# In the code above we first set the format for the dates on the x axis using the function `mdates.DateFormatter`.
#
# Then we create the plot referred to by `ax1`. We first plot the outflow, then inflow data.
# We then set a label for the y axis to $flow~ m^3/s$.
#
# We then indicate that legend should appear in the plot.
#
#
# The next commands are used to format the x axis, which are dates (the plots show flows versus date)
# `ax2.xaxis.set_major_formatter(myFmt)
#
# fig.autofmt_xdate()'
#

# %% [markdown]
# Finally, plot the second plot, referred to as `ax2`.
