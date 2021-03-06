# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   nbsphinx:
#     execute: never
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: true
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position:
#       height: calc(100% - 180px)
#       left: 10px
#       top: 150px
#       width: 165px
#     toc_section_display: true
#     toc_window_display: true
# ---
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Create-a-simulated-dataset" data-toc-modified-id="Create-a-simulated-dataset-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Create a simulated dataset</a></span></li><li><span><a href="#Convert-to-a-dataframe" data-toc-modified-id="Convert-to-a-dataframe-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Convert to a dataframe</a></span><ul class="toc-item"><li><span><a href="#Q1:-Turn-uni_dist-into-a-dataframe-called-df" data-toc-modified-id="Q1:-Turn-uni_dist-into-a-dataframe-called-df-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Q1: Turn uni_dist into a dataframe called df</a></span></li></ul></li><li><span><a href="#Create-a-datetime-for-each-row" data-toc-modified-id="Create-a-datetime-for-each-row-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Create a datetime for each row</a></span></li><li><span><a href="#Make-time_list-the-index-to-the-dataframe" data-toc-modified-id="Make-time_list-the-index-to-the-dataframe-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Make time_list the index to the dataframe</a></span><ul class="toc-item"><li><span><a href="#Add-it-as-a-new-column" data-toc-modified-id="Add-it-as-a-new-column-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Add it as a new column</a></span></li><li><span><a href="#Q2----set-this-column-as-an-index" data-toc-modified-id="Q2----set-this-column-as-an-index-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Q2 -- set this column as an index</a></span></li></ul></li><li><span><a href="#Dataframe-grouping" data-toc-modified-id="Dataframe-grouping-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Dataframe grouping</a></span><ul class="toc-item"><li><span><a href="#Q3-write-a-function-that-rounds-a-column-value-to-1-decimal" data-toc-modified-id="Q3-write-a-function-that-rounds-a-column-value-to-1-decimal-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Q3 write a function that rounds a column value to 1 decimal</a></span></li><li><span><a href="#Q4-Add-a-new-column-called-&quot;mass_tenths&quot;-using-coarse_grain" data-toc-modified-id="Q4-Add-a-new-column-called-&quot;mass_tenths&quot;-using-coarse_grain-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Q4 Add a new column called "mass_tenths" using coarse_grain</a></span></li><li><span><a href="#Q5:-Group-the-measurements-on-mass_tenths" data-toc-modified-id="Q5:-Group-the-measurements-on-mass_tenths-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Q5: Group the measurements on mass_tenths</a></span></li></ul></li><li><span><a href="#Dataframe-input/output" data-toc-modified-id="Dataframe-input/output-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Dataframe input/output</a></span><ul class="toc-item"><li><span><a href="#Q6-Round-trip" data-toc-modified-id="Q6-Round-trip-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Q6 Round trip</a></span></li></ul></li><li><span><a href="#Quiz-4-question-4" data-toc-modified-id="Quiz-4-question-4-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Quiz 4 question 4</a></span><ul class="toc-item"><li><span><a href="#Question-4a-answer" data-toc-modified-id="Question-4a-answer-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Question 4a answer</a></span></li><li><span><a href="#Question-4b-answer" data-toc-modified-id="Question-4b-answer-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Question 4b answer</a></span></li></ul></li></ul></div>
# %%
import datetime as dt
import pprint
from datetime import timezone as tz

import numpy as np
import numpy.random as rn
import numpy.testing as nt
import pandas as pd

# %% [markdown]
# # Dataframe practice
#
# Learning objectives
#
# - Be able to use the apply method to execute a function on every row of a dataframe
# - Be able to add a column to a data frame and use groupby with that column to
#   group dataframe rows into subset dataframes
# - Be able to do simple statistics (mean, median, max, min, summary) on dataframes and dataframe series
# - Be able to construct dataframes from lists of tuples, lists of dictionaries, or numpy arrays using
#   from_records member function
# - Be able to create and work with python datetime objects
#

# %% [markdown]
# ## Create a simulated dataset
#
# This cell creates 3 columns: column 0 is temperatures
# in the range 263-283 K, column 1 is veloc in the range
# -100 to +100 dm/s, column 2 is mass in the range

# %%
my_seed = 5
rn.seed(my_seed)
uni_dist = rn.rand(25, 3)
uni_dist[:, :2] = (uni_dist[:, :2] - 0.5) * 2.0
temps = uni_dist[:, 0] * 10.0 + 273.0
veloc = uni_dist[:, 1] * 100.0
uni_dist[:, 0] = temps
uni_dist[:, 1] = veloc
print(uni_dist[:5, :])

# %% [markdown]
# ## Convert to a dataframe
#
# with columns=['temperature','veloc','mass']
#
# ### Q1: Turn uni_dist into a dataframe called df
#

# %%
# Q1 answer
columns = ["temperature", "veloc", "mass"]
df = pd.DataFrame(uni_dist, columns=columns)
df.head()


# %% [markdown]
# It should pass this test

# %%
nt.assert_allclose(df["veloc"][1], -2.3, rtol=0.1)

# %% [markdown]
# ## Create a datetime for each row
#
# Assume that each row represents a measurement, and that
# the measurements happened every 10 minutes atarting at
# 5 am UCT on March 25, 2019

# %%
start_time = dt.datetime(2019, 3, 25, 5, 0, 0, tzinfo=tz.utc)
interval = dt.timedelta(minutes=10)
print(f"start and time interval: {start_time} -- {interval}")
time_list = [start_time]
for tick in range(len(df) - 1):
    time_list.append(time_list[tick] + interval)
pprint.pprint(time_list[:5])

# %% [markdown]
# ## Make time_list the index to the dataframe
#
# ### Add it as a new column

# %%
df["date"] = time_list

# %% [markdown]
# ### Q2 -- set this column as an index
#
# google pandas.DataFrame.set_index for method arguments

# %%
# Q2 answer
df.set_index("date", inplace=True)
df.head()


# %% [markdown]
# Your dataframe should pass this assert.

# %%
target_row = start_time = dt.datetime(2019, 3, 25, 5, 40, 0, tzinfo=tz.utc)
nt.assert_allclose(df.loc[target_row]["temperature"], 271.8, rtol=1.0e-2)


# %% [markdown]
# ## Dataframe grouping
#
# ### Q3 write a function that rounds a column value to 1 decimal
#
# i.e. complete this function
#
# ```
# def coarse_grain(row,colname):
#     #
#     # input -- dataframe row called row and string colname
#     #
#     # returns -- row[colname] rounded to 1 decimal
#     return col_val
# ```

# %%
# Q3 answer
def coarse_grain(row, colname):
    col_val = np.around(row[colname], decimals=1)
    return col_val


# %% [markdown]
# Your function should pass this assert

# %%
the_row = df.iloc[2]
the_round = coarse_grain(the_row, "mass")
np.testing.assert_allclose(the_round, 0.3)

# %% [markdown]
# ### Q4 Add a new column called "mass_tenths" using coarse_grain
#
# i.e. use df.apply to run coarse_grain on the dataframe and add the result
# as the 'mass_tenths' column
#

# %%
# Q4 answer
df["mass_tenths"] = df.apply(coarse_grain, args=("mass",), axis=1)


# %% [markdown]
# You dataframe should now pass the following assert

# %%
nt.assert_allclose(df["mass_tenths"][3], 0.7)

# %% [markdown]
# ### Q5: Group the measurements on mass_tenths

# %% [raw]
# Use groups=df.groupby to create a DataFrameGroupBy object
# called groups indexed on mass_tenths
#
# Then find the median temperature, speed and mass of each group
# using the the_median=groups.median() method
#

# %%
# Q5 answer
groups = df.groupby("mass_tenths")
the_median = groups.median()

# %%
nt.assert_allclose(the_median.loc[0.2]["veloc"], 1.49, rtol=0.1)

# %%
groups.median()

# %% [markdown]
# ## Dataframe input/output
#
# ### Q6 Round trip
#
# Add a cell that fixes the following problem -- new_df is not
# the same as our original df after writing it out to csv

# %%
df.to_csv("test.csv")

# %%
new_df = pd.read_csv("test.csv")
new_df.head()

# %%
# Q6 answer
new_df = pd.read_csv("test.csv", index_col="date")
new_df.head()


# %%
target_row = start_time = dt.datetime(2019, 3, 25, 5, 40, 0, tzinfo=tz.utc)
nt.assert_allclose(df.loc[target_row]["temperature"], 271.8, rtol=1.0e-2)

# %% [markdown]
# ## Quiz 4 question 4
#
# Consider the following dataframe df, with rows, columns and index given by:

# %%
df.head()

# %% [markdown]
# **4a) In the space below write python statements (single lines) that would
# return the following:**
#
# - The row corresponding to March 25, 2019 at 5:30 am UCT
# - The temperature for March 25, 2019 at 5:10 am UCT
# - All temperatures in the dataframe
#

# %% [markdown]
# ### Question 4a answer

# %%
the_time = dt.datetime(2019, 3, 25, 5, 30, 0, tzinfo=tz.utc)
print(df.loc[the_time])

# %%
the_time = dt.datetime(2019, 3, 25, 5, 10, 0, tzinfo=tz.utc)
print(df.loc[the_time]["temperature"])

# %%
print(df["temperature"])

# %% [markdown]
# **4b) Write a python snippet that would use groupby to find
#   the median velocity for all objects with mass_tenths=0.7 kg for this
#   dataframe**

# %% [markdown]
# ### Question 4b answer

# %%
groups = df.groupby("mass_tenths")
median_df = groups.median()
print(median_df.loc[0.7]["veloc"])
