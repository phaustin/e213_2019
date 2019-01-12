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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Exploring-data-using-NumPy" data-toc-modified-id="Exploring-data-using-NumPy-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exploring data using NumPy</a></span><ul class="toc-item"><li><span><a href="#What-is-NumPy?" data-toc-modified-id="What-is-NumPy?-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What is NumPy?</a></span></li><li><span><a href="#Preparation-(the-key-to-success)" data-toc-modified-id="Preparation-(the-key-to-success)-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Preparation (the key to success)</a></span></li><li><span><a href="#Reading-a-data-file-with-NumPy" data-toc-modified-id="Reading-a-data-file-with-NumPy-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Reading a data file with NumPy</a></span><ul class="toc-item"><li><span><a href="#Importing-NumPy" data-toc-modified-id="Importing-NumPy-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Importing NumPy</a></span></li><li><span><a href="#Reading-a-data-file" data-toc-modified-id="Reading-a-data-file-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Reading a data file</a></span></li><li><span><a href="#Inspecting-our-data-file" data-toc-modified-id="Inspecting-our-data-file-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>Inspecting our data file</a></span></li><li><span><a href="#Reading-our-data-file,-round-2" data-toc-modified-id="Reading-our-data-file,-round-2-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>Reading our data file, round 2</a></span></li></ul></li><li><span><a href="#Exploring-our-dataset" data-toc-modified-id="Exploring-our-dataset-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Exploring our dataset</a></span><ul class="toc-item"><li><span><a href="#Checking-the-array-data-type" data-toc-modified-id="Checking-the-array-data-type-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Checking the array data type</a></span></li><li><span><a href="#Checking-the-data-array-type" data-toc-modified-id="Checking-the-data-array-type-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Checking the data array type</a></span></li><li><span><a href="#Checking-the-size-of-the-dataset" data-toc-modified-id="Checking-the-size-of-the-dataset-1.4.3"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Checking the size of the dataset</a></span></li><li><span><a href="#Working-with-our-data---Index-slicing" data-toc-modified-id="Working-with-our-data---Index-slicing-1.4.4"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>Working with our data - Index slicing</a></span></li><li><span><a href="#Slicing-our-data-into-columns" data-toc-modified-id="Slicing-our-data-into-columns-1.4.5"><span class="toc-item-num">1.4.5&nbsp;&nbsp;</span>Slicing our data into columns</a></span></li><li><span><a href="#Checking-the-data-in-memory" data-toc-modified-id="Checking-the-data-in-memory-1.4.6"><span class="toc-item-num">1.4.6&nbsp;&nbsp;</span>Checking the data in memory</a></span></li><li><span><a href="#Basic-data-calculations-in-NumPy" data-toc-modified-id="Basic-data-calculations-in-NumPy-1.4.7"><span class="toc-item-num">1.4.7&nbsp;&nbsp;</span>Basic data calculations in NumPy</a></span></li><li><span><a href="#Data-type-conversions" data-toc-modified-id="Data-type-conversions-1.4.8"><span class="toc-item-num">1.4.8&nbsp;&nbsp;</span>Data type conversions</a></span></li></ul></li></ul></li></ul></div>

# %% [markdown]
# # Exploring data using NumPy
#
# Our first task in this week's lesson is to learn how to read and explore data files using [NumPy](http://www.numpy.org/).
# Reading data files using NumPy will make life a bit easier compared to the traditional Python way of reading data files.
# If you're curious about that, you can check out some of the lesson materials from past years about [reading data in the Pythonic way](https://geo-python.github.io/2018/2017/lessons/L5/reading-data-from-file.html).
#
# ## What is NumPy?
#
# NumPy is a library for Python designed for efficient scientific (numerical) computing.
# It is an essential library in Python that is used under the hood in many other modules (including [Pandas](https://pandas.pydata.org/)).
# Here, we will get a sense of a few things NumPy can do.

# %% [markdown]
# ## Preparation (the key to success)
#
# Presumably you have already opened this Jupyter notebook (if not, do so now using one of the links above), and our first task is to change the working directory to the one containing the files for this week's lesson (in this case the `numpy` directory.
# You can do that by first checking which directory Jupyter is operating in using the `%ls` IPython magic command.

# %%
# %ls

# %% [markdown]
# If you see files like `1-Exploring-data-using-numpy.ipynb`, you're all set.
# If not, you can change the working directory using the `%cd` magic command.
# For example,

# %%


# %% [markdown]
# The command above gives an error in this case because we're in a different directory, but you get the point.
# If you need some additional help to get into the right working directory, you can refer back to the lesson on functions where we covered changing the working directory in more detail.

# %% [markdown]
# ## Reading a data file with NumPy
#
# ### Importing NumPy
#
# Now we're ready to read in our temperature data file.
# First, we need to import the NumPy module.

# %%


# %% [markdown]
# That's it!
# NumPy is now ready to use.
# Notice that we have imported the NumPy module with the name `np`.

# %% [markdown]
# ### Reading a data file
#
# Now we'll read the file data into a variable called `data`.
# We can start by defining the location (filepath) of the data file in the variable `fp`.

# %%


# %% [markdown]
# Now we can read the file using the NumPy `genfromtxt()` function.

# %%


# %% [markdown]
# `np.genfromtxt()` is a general function for reading data files separated by commas, spaces, or other common separators.
# For a full list of parameters for this function, please refer to the [NumPy documentation for numpy.genfromtxt()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html).
#
# Here we use the function simply by giving the filename as an input parameter.
# If all goes as planned, you should now have a new variable defined as `data` in memory that contains the contents of the data file.
# You can check the the contents of this variable by typing the following:

# %%


# %% [markdown]
# ### Inspecting our data file
#
# Hmm...something doesn't look right here.
# You were perhaps expecting some temperature data, right?
# Instead we have only a list of `nan` values.
#
# `nan` stands for "not a number", and might indicate some problem with reading in the contents of the file.
# Looks like we need to investigate this further.
#
# We can begin our investigation by opening the data file in JupyterLab by right-clicking on the `Kumpula-June-2016-w-metadata.txt` data file and selecting **Open**.
#
# ![Opening a file in JupyterLab](../img/open-text-file.png)
#
# You should see something like the following:

# %% [raw]
# # Data file contents: Daily temperatures (mean, min, max) for Kumpula, Helsinki
# #                     for June 1-30, 2016
# # Data source: https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND
# # Data processing: Extracted temperatures from raw data file, converted to
# #                  comma-separated format
# #
# # David Whipp - 02.10.2017
#
# YEARMODA,TEMP,MAX,MIN
# 20160601,65.5,73.6,54.7
# 20160602,65.8,80.8,55.0
# ...

# %% [markdown]
# We can observe a few important things:
#
# - There are some metadata at the top of the file (a *header*) that provide basic information about its contents and source.
#   This isn’t data we want to process, so we need to skip over that part of the file when we load it.
#     - We can skip the top header lines in the file using the `skip_header` parameter.
# - The values in the data file are separated by commas.
#     - We can specify the value separator using the `delimiter` parameter.
# - The top row of values below the header contains names of the column variables.
#     - We'll deal with those later.

# %% [markdown]
# ### Reading our data file, round 2
#
# Let's try reading again with this information in mind.

# %%


# %% [markdown]
# Note that we now skip the header lines (first 9 lines) using `skip_header=9` and tell NumPy the files is comma-separated using `delimiter=','`.
#
# Let's print out the contents of `data` now and see how things look.

# %%


# %% [markdown]
# That's more like it.
#
# OK, so let's review what just happened.
# Well, the file data was read into a NumPy *ndarray*, which is a type of NumPy *n*-dimensional structure used for storing data like a matrix.
# What?!?
# Yeah, in our case we have a two dimensional data struture similar to a spreadsheet.
# Everything is together in a single large data structure at the moment, but we'll see later in the lesson how to divide up our data and make interacting with it easier.
#
# Now we can move on to exploring our data.

# %% [markdown]
# #### Checking data file formats
#
# The example above, trying to read a datafile with some header text (the metadata in this case), is *very* common.
# Reading data into NumPy is pretty easy, but it helps to have a sense of what the datafile looks like before you try to read it.
# The challenge can be that large datafiles might not nicely (or quickly) load into the JupyterLab editor, so it might be better to look at only the top 5-10 lines of the file rather than loading the entire thing.
# Fortunately, there are solutions to that problem.
#
# When you're trying to think over how to read in a data file you can take advantage of common command-line tools like **head**.
# **head** is a simple program to read lines from the start of a data file and print them to the screen.
# You can use **head** from the command line in JupyterLab by first opening a JupyterLab terminal from the JupyterLab menu bar (**File** -> **New** -> **Terminal**).
# Once in the terminal, you can simply navigate to the directory containing your datafile and type **head** followed by the file name:
#
# ```bash
# $ head Kumpula-June-2016-w-metadata.txt
# # Data file contents: Daily temperatures (mean, min, max) for Kumpula, Helsinki
# #                     for June 1-30, 2016
# # Data source: https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND
# # Data processing: Extracted temperatures from raw data file, converted to
# #                  comma-separated format
# #
# # David Whipp - 02.10.2017
#
# YEARMODA,TEMP,MAX,MIN
# 20160601,65.5,73.6,54.7
# ```
#
# As you can see, **head** gives you the first 10 lines of the file by default.
# You can use the `-n` flag to get a larger or smaller number of lines.
#
# ```bash
# $ head -n 5 Kumpula-June-2016-w-metadata.txt
# # Data file contents: Daily temperatures (mean, min, max) for Kumpula, Helsinki
# #                     for June 1-30, 2016
# # Data source: https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND
# # Data processing: Extracted temperatures from raw data file, converted to
# #                  comma-separated format
# ```

# %% [markdown]
# ## Exploring our dataset
#
# So this is a big deal for us.
# We now have some basic Python skills and the ability to read in data from a file for processing.
# A normal first step when you load new data is to explore the dataset a bit to understand what is there and its format.

# %% [markdown]
# ### Checking the array data type
#
# Perhaps as a first step, we can check the type of data we have in our NumPy array `data`.

# %%


# %% [markdown]
# It's a NumPy *ndarray*, not much surprise here.

# %% [markdown]
# ### Checking the data array type
#
# Let’s now have a look at the data types in our ndarray.
# We can find this in the `dtype` attribute that is part of the ndarray data type, something that is known automatically for this kind of data.

# %%


# %% [markdown]
# Here we see the data are floating point values with 64-bit precision.

# %% [markdown]
# <div class="alert alert-info">
#
# **Note:**
#
# There are some exceptions, but normal NumPy arrays will all have the same data type.
#
# </div>

# %% [markdown]
# ### Checking the size of the dataset
#
# We can also check to see how many rows and columns we have in the dataset using the `shape` attribute.

# %%


# %% [markdown]
# Here we see how there are 30 rows of data and 4 columns.

# %% [markdown]
# ### Working with our data - Index slicing
#
# Let's have another quick look at our data.

# %%


# %% [markdown]
# This is OK, but we can certainly make it easier to work with.
# We can start by slicing our data up into different columns and creating new variables with the column data.
# Slices from our array can be extracted using the *index values*.
# In our case, we have two indices in our 2D data structure.
# For example, the index values `[2,0]`

# %%


# %% [markdown]
# give us the value at row 2, column 0.
#
# We can also use ranges of rows and columns using the `:` character.
# For example, we could get the first 5 rows of values in column zero by typing

# %%


# %% [markdown]
# Not bad, right?
#
# In fact, we don't even necessarily need the lower bound for this slice of data because NumPy will assume it for us if we don't list it.
# Let's see another example.

# %%


# %% [markdown]
# Here, the lower bound of the index range `0` is assumed and we get all rows up to (but not including) index `5`.

# %% [markdown]
# ### Slicing our data into columns
#
# Now let's use the ideas of index slicing to cut our 2D data into 4 separate columns that will be easier to work with.
# As you might recall from the header of the file, we have 4 data values: `YEARMODA`, `TEMP`, `MAX`, and `MIN`.
# We can exract all of the values from a given column by not listing and upper or lower bound for the index slice.
# For example,

# %%


# %%


# %% [markdown]
# OK, this looks promising.
# Let's quickly handle the others.

# %%
temp = data[:, 1]
temp_max = data[:, 2]
temp_min = data[:, 3]

# %% [markdown]
# Now we have 4 variables, one for each column in the data file.
# This should make life easier when we want to perform some calculations on our data.

# %% [markdown]
# ### Checking the data in memory
#
# We can see the types of data we have defined at this point, the variable names, and their types using the `%whos` magic command.
# This is quite handy.

# %%


# %% [markdown]
# ### Basic data calculations in NumPy
#
# NumPy ndarrays have a set of attributes they know about themselves and methods they can use to make calculations using the data.
# Useful methods include `mean()`, `min()`, `max()`, and `std()` (the standard deviation).
# For example, we can easily find the mean temperature.

# %%


# %% [markdown]
# ### Data type conversions
#
# Lastly, we can convert our ndarray data from one data type to another using the `astype()` method.
# As we see in the output from `%whos` above, our `date` array contains `float64` data, but it was simply integer values in the data file.
# We can convert `date` to integers by typing

# %%


# %%


# %%


# %% [markdown]
# Now we see our dates as whole integer values.
