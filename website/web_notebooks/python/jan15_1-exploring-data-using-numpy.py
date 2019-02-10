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
#     toc_position:
#       height: 474px
#       left: 119px
#       top: 245px
#       width: 200.594px
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Exploring-data-using-NumPy" data-toc-modified-id="Exploring-data-using-NumPy-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exploring data using NumPy</a></span></li><li><span><a href="#What-is-NumPy?" data-toc-modified-id="What-is-NumPy?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is NumPy?</a></span></li><li><span><a href="#Reading-a-data-file-with-pandas" data-toc-modified-id="Reading-a-data-file-with-pandas-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Reading a data file with pandas</a></span><ul class="toc-item"><li><span><a href="#Importing-NumPy-and-pandas" data-toc-modified-id="Importing-NumPy-and-pandas-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Importing NumPy and pandas</a></span></li><li><span><a href="#Reading-data" data-toc-modified-id="Reading-data-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Reading data</a></span></li><li><span><a href="#Reading-a-data-file" data-toc-modified-id="Reading-a-data-file-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Reading a data file</a></span></li><li><span><a href="#Converting-to-a-numpy-ndarray" data-toc-modified-id="Converting-to-a-numpy-ndarray-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Converting to a numpy ndarray</a></span></li></ul></li><li><span><a href="#Exploring-our-dataset" data-toc-modified-id="Exploring-our-dataset-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Exploring our dataset</a></span><ul class="toc-item"><li><span><a href="#Checking-the-array-data-type" data-toc-modified-id="Checking-the-array-data-type-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Checking the array data type</a></span></li><li><span><a href="#Checking-the-data-array-type" data-toc-modified-id="Checking-the-data-array-type-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Checking the data array type</a></span></li><li><span><a href="#Checking-the-size-of-the-dataset" data-toc-modified-id="Checking-the-size-of-the-dataset-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Checking the size of the dataset</a></span></li></ul></li><li><span><a href="#Working-with-our-data---Index-slicing" data-toc-modified-id="Working-with-our-data---Index-slicing-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Working with our data - Index slicing</a></span><ul class="toc-item"><li><span><a href="#Subsetting-a-set-of-rows-in-an-array" data-toc-modified-id="Subsetting-a-set-of-rows-in-an-array-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Subsetting a set of rows in an array</a></span><ul class="toc-item"><li><span><a href="#Differences-from-matlab" data-toc-modified-id="Differences-from-matlab-5.1.1"><span class="toc-item-num">5.1.1&nbsp;&nbsp;</span>Differences from matlab</a></span></li></ul></li><li><span><a href="#Slicing-our-data-into-columns" data-toc-modified-id="Slicing-our-data-into-columns-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Slicing our data into columns</a></span></li><li><span><a href="#Checking-the-data-in-memory" data-toc-modified-id="Checking-the-data-in-memory-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Checking the data in memory</a></span></li></ul></li><li><span><a href="#Basic-data-calculations-in-NumPy" data-toc-modified-id="Basic-data-calculations-in-NumPy-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Basic data calculations in NumPy</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Data-type-conversions" data-toc-modified-id="Data-type-conversions-6.0.1"><span class="toc-item-num">6.0.1&nbsp;&nbsp;</span>Data type conversions</a></span></li></ul></li></ul></li></ul></div>
# %% [markdown]
# # Exploring data using NumPy
#
# Our first task in this week's lesson is to learn how to read and explore data files using [NumPy](http://www.numpy.org/).
# We are also going to need another module called [Pandas](https://pandas.pydata.org/) to get a csv file into numpy.  We are
# not going discuss pandas in this lesson, but you'll hear more about it later in the course.
#
# # What is NumPy?
#
# NumPy is a library for Python designed for efficient scientific (numerical) computing.
# It is an essential library in Python that is used under the hood in many other modules (including [Pandas](https://pandas.pydata.org/)).
# Here, we will get a sense of a few things NumPy can do.
# %% [markdown]
# # Reading a data file with pandas
#
# ## Importing NumPy and pandas
#
# Now we're ready to read in our temperature data file.
# First, we need to import the NumPy and pandas module.
# %%
import numpy as np  # noqa
import pandas as pd


# %% [markdown]
# That's it!
# NumPy is now ready to use.
# Notice that we have imported the NumPy module with the name `np`.

# %% [markdown]
# ## Reading data
#
# Below we will read the file data/Kumpula-June-2016-w-metadata.txt
#
# Use your cocalc file browser to open the file data/Kumpula-June-2016-w-metadata.txt in the data folder. You should see this:

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
# Note the format -- there is some header information we want to skip, the column names on line 9
# and then rows of data.  We will get a DataFrame with 4 columns -- the year/month/day, temperature on that day, and the historical maximum and minimum.

# %% [markdown]
# ## Reading a data file
#
# Now we'll read the file data into a pandas`DataFrame` object. Remember that python counts from 0, so the header
# on line 9 is at row 8 in python.

# %%
data_frame = pd.read_csv(
    "data/Kumpula-June-2016-w-metadata.txt", header=[8], skip_blank_lines=False
)
data_frame.head()


# %% [markdown]
# ## Converting to a numpy ndarray
#
# Since this notebook is focussed on numpy, not pandas, we want to get
# the data out of the pandas `DataFrame` into a numpy array to work with.  That's done using
# the values attribute

# %%
data = data_frame.values


# %% [markdown]
# Note, here we are doing two things:
#
# 1. creating the new object `data`
#    (unlike C where variables are explicitly declared before they are
#    used here, we create it dynamically, or on the fly)
#
# 2. We take the values from the dataframe and assign them to `data`
#    Also note that jupyter does not print out anything to see when we
#    assign a variable using an equals sign.  Only the last item in a
#    cell is printed automatically.  Printing any other variable requires
#    calling it with the print() function.

# %% [markdown]
# # Exploring our dataset
#
# A normal first step when you load new data is to explore the dataset a bit to understand what is there and its format.

# %% [markdown]
# ## Checking the array data type
#
# Perhaps as a first step, we can check the type of data we have in our NumPy array `data`. Try using google to find out how to check an object type in python.

# %%


# %% [markdown]
# You should cofirm that it's a NumPy *ndarray*, not much of a surprise here.

# %% [markdown]
# ## Checking the data array type
#
# The ndarray is a container -- it essentially points to a region of computer memory that holds a sequence of numbers represented as bit patterns.   Those bits can be interpreted floating point, integer, or boolean, and each number may occupy 1, 8, 16, 32 or 64 bits.  The ndarray object stores that information in an [attribute](http://blog.thedigitalcatonline.com/blog/2015/01/12/accessing-attributes-in-python/) called its `dtype` or data tipe
#
# Let’s now have a look at the data type in our ndarray.
# We can find this in the `dtype` attribute that is part of the ndarray data type, something that is known automatically for this kind of data.
#
# To summarize -- all python objects have a type.  Objects of type ndarray hold data with a particular dtype.  Every data element in an ndarray has the same dtype.

# %% [markdown]
# Print out the type of the data ndarray below.

# %% {"deletable": false, "nbgrader": {"checksum": "2cadd4c7ca4e8a6459448932e321495f", "grade": true, "grade_id": "cell-f6b1242c9096947a", "locked": false, "points": 1, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


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
# ## Checking the size of the dataset
#
# We can also check to see how many rows and columns we have in the dataset using the `shape` attribute.

# %% {"deletable": false, "nbgrader": {"checksum": "87c950fae79acb78e5080e8c51e7c832", "grade": true, "grade_id": "cell-8e8a48fd40a92660", "locked": false, "points": 1, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% [markdown]
# Here we see how there are 30 rows of data and 4 columns.

# %% [markdown]
# # Working with our data - Index slicing
#
# Let's have another quick look at our data.
#
# Need an explicit instruction. Maybe
#
# Just enter the name of the variable, `data` and run the cell to see the array.

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
# We can also use ranges of rows and columns using the `:` character. To get, for example
# the values from the first 3 columns of row 12, we could type
#
# `data[12, 0:3]`
#
# Below, enter the code to get the first 5 rows of values in column zero

# %%


# %% [markdown]
# Not bad, right?
#
# In fact, we don't even necessarily need the lower bound for this slice of data because NumPy will assume it for us if we don't list it.
# Let's see another example.
#
# ## Subsetting a set of rows in an array
#
# Can you figure out how to see the first 5 rows of data (all columns)? Note, if you put the colon `:` in the array index, python will give you all rows or columns. Eg `data[1,:]` will give you all columns from row 1.

# %% [markdown]
# ### Differences from matlab
#
# Note a couple of important difference from matlab.  In python:
#
# 1. The first item in an array is at index 0, not 1
#
# 1. The slice [0:5] has 5 elements: 0,1,2,3,4.
#
# 1. Index numbers can be negative: if  an  array a contains `a= [0,1,2,3,4]`,
#    then `a[-1]` contains 4, `a[-2]` contains 3, etc. Try creating a
#    array below with numpy.arange and accessing various elements in the
#    cell below.  What happens if you try an index beyond the end of the
#    array?

# %%
import numpy


# %% [markdown]
# Here, the lower bound of the index range `0` is assumed and we get all rows up to (but not including) index `5`.

# %% [markdown]
# ## Slicing our data into columns
#
# Now let's use the ideas of index slicing to cut our 2D data into 4 separate columns that will be easier to work with.
#
# As you might recall from the header of the file, we have 4 data values: `YEARMODA`, `TEMP`, `MAX`, and `MIN`.
# We can exract all of the values from a given column by not listing and upper or lower bound for the index slice.
#
# Create a new array called `dateYMD` from the first column of the `data`.

# %%


# %% [markdown]
# Note, as mentioned above, python does not print out anything when we assign a variable with an equals sign.

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
# ## Checking the data in memory
#
# We can see the types of data we have defined at this point, the variable names, and their types using the `%whos` magic command.
# This is quite handy. Enter the command below and see what you get.
# For technical reasons we need to comment out the line below when we generate this notebook.  Uncomment it and run the cell.

# %%
# #%whos


# %% [markdown]
# # Basic data calculations in NumPy
#
# NumPy ndarrays have a set of attributes they know about themselves and methods they can use to make calculations using the data.
# Useful methods include `mean()`, `min()`, `max()`, and `std()` (the standard deviation). The general format to use a method is `objectname.method()`. Our objects include the numpy arrays that we created above.
#
# For example, can you find the mean temperature in the dataset? Do that in the cell below and save it in a variable called `mean_temp`

# %% {"deletable": false, "nbgrader": {"checksum": "43b79b746157c9914dc1f1b22b944e4d", "grade": false, "grade_id": "cell-30fa61c4d9885e32", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "139becefcdbacb3e90022117e1e369e6", "grade": true, "grade_id": "cell-2228c250f4ae5124", "locked": true, "points": 2, "schema_version": 1, "solution": false}}

# %% [markdown]
# How about the maximum maximum temperature? Remember that you've read
# the daily climatological maximum from column 2 above.  Save the maximum
# of that column as the variable temp_max below.

# %% {"deletable": false, "nbgrader": {"checksum": "1a0c8f566a4d13940d33d1e24521a023", "grade": false, "grade_id": "cell-82f413cb6f6dd708", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "fa61a0331a955bffa4a1001fa405a468", "grade": true, "grade_id": "cell-d02f83d1a2eb8333", "locked": true, "points": 2, "schema_version": 1, "solution": false}}

# %% [markdown]
# ### Data type conversions
#
# Lastly, we can convert our ndarray data from one data type to another using the `astype()` method.
# As we see in the output from `%whos` above, our `date` array contains `float64` data, but it was simply integer values in the data file.
#
# For example to convert to a `numpy` array named `varname1` to `float64` and assign it to `varname2` use
# `varname2 = varname1.astype("float64")`. Note, in python, you can do this in place, that is if `varname1` and `varname2`
# are the same, the net effect is to convert the type of `varname1`.
#
# Can you figure out how to convert `dateYMD` to integers using `astype()`?

# %%


# %% [markdown]
# Check the dtype attribute to confirm


# %%


# %% [markdown]
# Now we see our dates as whole integer values.

# %%
dateYMD

# %%
