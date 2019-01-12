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

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Processing-data-with-NumPy" data-toc-modified-id="Processing-data-with-NumPy-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Processing data with NumPy</a></span><ul class="toc-item"><li><span><a href="#Calculating-with-NumPy-arrays" data-toc-modified-id="Calculating-with-NumPy-arrays-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Calculating with NumPy arrays</a></span><ul class="toc-item"><li><span><a href="#Creating-arrays" data-toc-modified-id="Creating-arrays-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Creating arrays</a></span></li><li><span><a href="#Calcuating-values-using-other-arrays" data-toc-modified-id="Calcuating-values-using-other-arrays-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Calcuating values using other arrays</a></span></li></ul></li><li><span><a href="#Filtering-data" data-toc-modified-id="Filtering-data-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Filtering data</a></span><ul class="toc-item"><li><span><a href="#Using-data-masks" data-toc-modified-id="Using-data-masks-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Using data masks</a></span></li></ul></li><li><span><a href="#Removing-missing/bad-data" data-toc-modified-id="Removing-missing/bad-data-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Removing missing/bad data</a></span></li><li><span><a href="#Rounding-and-finding-unique-values" data-toc-modified-id="Rounding-and-finding-unique-values-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Rounding and finding unique values</a></span><ul class="toc-item"><li><span><a href="#Finding-unique-values" data-toc-modified-id="Finding-unique-values-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Finding unique values</a></span></li></ul></li><li><span><a href="#Saving-our-data-to-a-file" data-toc-modified-id="Saving-our-data-to-a-file-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Saving our data to a file</a></span><ul class="toc-item"><li><span><a href="#Re-creating-our-2D-data-array" data-toc-modified-id="Re-creating-our-2D-data-array-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Re-creating our 2D data array</a></span></li><li><span><a href="#Saving-our-data" data-toc-modified-id="Saving-our-data-1.5.2"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Saving our data</a></span></li></ul></li></ul></li></ul></div>

# %% [markdown]
# # Processing data with NumPy
#
# Now you should know the basics of the data structures in NumPy and how to explore your data using some tools that are provided by NumPy.
# Next, we continue to explore some of the basic data operations that are regularly needed when doing data analysis.
#
# Let’s first import NumPy, read the same data as before, and sort it into column arrays to have a clean start.

# %%
import numpy as np

# %%
fp = '../Kumpula-June-2016-w-metadata.txt'
data = np.genfromtxt(fp, skip_header=9, delimiter=',')

# %%
date = data[:, 0]
temp = data[:, 1]
temp_max = data[:, 2]
temp_min = data[:, 3]

# %% [markdown]
# ## Calculating with NumPy arrays
#
# One of the most common things to do in NumPy is to create new arrays based on calculations between different other arrays (columns).
#
# ### Creating arrays
#
# Arrays can be created in several ways.
# A common approach is to create an array of zeros with the same length as other existing arrays.
# This can be thought of as a blank space for calculations.

# %%


# %%


# %% [markdown]
# So, what just happened?
# We created a new array of zeros using the NumPy `zeros()` function, which takes the size of the array as a parameter.
# In our case, we've given the size to be the length of the `date` array.
# In other words, `len(date)`.

# %% [markdown]
# ### Calcuating values using other arrays
#
# We can now use our new `diff` array to calculate something useful, such as the difference between the `temp_max` and `temp_min` values for each row in our data.
# How do we do that?
# It's easy.

# %%


# %%


# %% [markdown]
# We simply subtract `temp_min` from `temp_max`.
#
# In fact, we don't even need to create the array first.
# Let's consider another example of calculating the difference between the daily mean temperature and the minimum temperature.
# We can calculate that simply as follows.

# %%


# %%


# %% [markdown]
# When we subtract one NumPy array from another, NumPy is smart enough to automatically create a new array to store the output.
# We can confirm this by checking the type of the `diff_min` array.

# %%


# %% [markdown]
# As one final example, let's consider converting temperatures in Fahrenheit to Celsius.
# We can store the results as `temp_celsius`.

# %%


# %%


# %% [markdown]
# Again, since we use a NumPy ndarray in the calculation, a ndarray is output.

# %% [markdown]
# ## Filtering data
#
# Another common thing to do with data is to look for a subset of the data that match some criterion.
# For example, we might want to create an array called `w_temps` that contains "warm" temperatures, those above 15°C.
# We can do that as follows.

# %%


# %%


# %% [markdown]
# Here, we see only the temperatures above 15°C, as expected.
#
# It is also possible to combine multiple criteria at the same time.
# Here, we select temperatures above 15 degrees that were recorded in the second half of June in 2016 (i.e. `date >= 20160615`).
# Combining multiple criteria can be done with the `&` operator (logical AND) or the `|` operator (logical OR).
# Notice, that it is useful to separate the different clauses inside parentheses `()`.

# %%


# %%


# %% [markdown]
# With two constraints on the data, that `temp_celsius` must be greater that 15°C and `date` must be on or after June 15, 2016 (i.e., `20160615`), we get a smaller subset of the original data.

# %% [markdown]
# ### Using data masks
#
# The filtering examples above are nice, but what if we would like to identify the dates with temperatures above 15°C and keep only those dates in our other data columns, such as `date`, `temp`, etc.
# How can we do that?
#
# In order to do that, we will need to use a *mask* array.
# A mask array is basically a boolean (True/False) array that can be used to take a subset of data from other arrays.
# Let's consider our example of warm temperatures once again.
# Rather than extracting `w_temps` directly, we can start by identifying the values in `temp_celsius` where the value is above 15°C (`True`) or less than or equal to 15°C (`False`).
# The logic is quite similar to before.

# %%


# %%


# %% [markdown]
# Now we see a list of `True` and `False` values in an array of the same size as `temp_celsius`.
# This array shows us whether the condition we stated is `True` or `False` for each index.
#
# Now, if we wanted to know the dates when the temperature was above 15°C, we can simply take the values from the `date` array using the mask we just created.

# %%


# %%


# %% [markdown]
# Cool, right?
# Now we see only the subset of dates that match the condition of having a temperature above 15°C, and the lengths of `w_temps` and `w_temp_dates` are the same, meaning we know both the date that the temperature exceeded 15°C and the temperature itself.

# %%


# %%


# %% [markdown]
# ## Removing missing/bad data
#
# In some cases, a data file might contain missing values or values that cannot be read.
# These may be replaced by `nan` values when you look at your data.
# `nan` stands for "not a number", and often we want to get rid of these things.
#
# Let's consider a case where we have an array `bad_data` that is full of zeros, has the same size as `date` and the other arrays from our data file, and the first 5 rows have `nan` values.

# %%


# %%


# %%


# %% [markdown]
# You can see the problem clearly.
#
# If we wanted to include values for the `date` column that only correspond to locations in `bad_data` where we do not have a `nan` value, we can use the `isfinite()` function in NumPy.
# `isfinite()` checks to see if a value is defined (i.e., is not `nan` or infinite (`inf`).
# Let's make a mask with `bad_data`.

# %%


# %%


# %% [markdown]
# We see the expected results.
# If we want now to include only the dates with good data, we can use the mask as we did before.

# %%


# %%


# %% [markdown]
# ## Rounding and finding unique values
#
# It is possible to round values easily using the `round()` method for NumPy arrays.
# Let's round our temperatures in Celsius to zero decimal places.

# %%


# %%


# %% [markdown]
# ### Finding unique values
#
# We can find unique values in an array using the `unique()` function.

# %%


# %%


# %% [markdown]
# Now we do not see any repeated values in our rounded temperatures.

# %% [markdown]
# ## Saving our data to a file
#
# Finally we can save our modified data to a file for future use.
# We'll need to do a few steps to get there, however.

# %% [markdown]
# ### Re-creating our 2D data array
#
# As you have seen, we have mostly worked with single columns after reading in our data.
# We can recreate a 2D data structure by stacking these columns back together.
#
# For example, let's put together our `date`, `temp`, and `temp_celsius` columns in a new data array called `new_data`.
# We can start by stacking the data together using the `vstack()` function.

# %%


# %%


# %% [markdown]
# Now we have our data back in a single array, but something isn't quite right.
# The columns and rows need to be flipped.
# We can do this using the `transpose()` function.

# %%


# %%


# %% [markdown]
# That's better!

# %% [markdown]
# ### Saving our data
#
# With the data in the correct format, we can now save it to a file using the `savetxt()` function.
# Let's save our data to a file called `converted_temps.csv`, where the `.csv` indicates the data values are separated by commas (comma-separated values).

# %%


# %% [markdown]
# Cool.
# We have now saved the array `new_data` to the file `converted_temps.csv` with commas between the values (using the `delimiter=','` parameter).
