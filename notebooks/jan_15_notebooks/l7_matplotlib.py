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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Plotting-with-Matplotlib" data-toc-modified-id="Plotting-with-Matplotlib-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Plotting with Matplotlib</a></span><ul class="toc-item"><li><span><a href="#Our-dataset" data-toc-modified-id="Our-dataset-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Our dataset</a></span></li><li><span><a href="#Getting-started" data-toc-modified-id="Getting-started-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Getting started</a></span><ul class="toc-item"><li><span><a href="#Loading-the-data-with-NumPy" data-toc-modified-id="Loading-the-data-with-NumPy-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Loading the data with NumPy</a></span></li><li><span><a href="#Loading-the-data-with-Pandas" data-toc-modified-id="Loading-the-data-with-Pandas-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Loading the data with Pandas</a></span></li></ul></li><li><span><a href="#Our-first-plot" data-toc-modified-id="Our-first-plot-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Our first plot</a></span></li><li><span><a href="#Basic-plot-formatting" data-toc-modified-id="Basic-plot-formatting-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Basic plot formatting</a></span><ul class="toc-item"><li><span><a href="#Embiggening*-the-plot" data-toc-modified-id="Embiggening*-the-plot-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Embiggening* the plot</a></span></li><li><span><a href="#Adding-text-labels-to-a-plot" data-toc-modified-id="Adding-text-labels-to-a-plot-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Adding text labels to a plot</a></span></li><li><span><a href="#Changing-the-axis-ranges" data-toc-modified-id="Changing-the-axis-ranges-1.4.3"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Changing the axis ranges</a></span></li></ul></li><li><span><a href="#Bar-plots-in-Matplotlib" data-toc-modified-id="Bar-plots-in-Matplotlib-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Bar plots in Matplotlib</a></span></li><li><span><a href="#Saving-your-plots-as-image-files" data-toc-modified-id="Saving-your-plots-as-image-files-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Saving your plots as image files</a></span></li></ul></li></ul></div>

# %% [markdown]
# # Plotting with Matplotlib
#
# Though there are many options for plotting data in Python, we will be using [Matplotlib](https://matplotlib.org/).
# In particular, we will be using the `pyplot` module in Matplotlib, which provides MATLAB-like plotting.
# The reason for this is simple: Matplotlib is the most common module used for plotting in Python and many examples of plotting you may find online will be using Matplotlib.

# %% [markdown]
# ## Our dataset
#
# For our first lesson plotting data using Matplotlib we will again be using the weather data file from Lesson 5.
#
# - The data file (`Kumpula-June-2016-w-metadata.txt`) is in the `data` subdirectory.
# - It contains observed daily mean, minimum, and maximum temperatures from June 2016 recorded from the Kumpula weather observation station in Helsinki. It is derived from a data file of daily temperature measurments downloaded from the [US National Oceanographic and Atmospheric Administration’s National Centers for Environmental Information climate database](https://www.ncdc.noaa.gov/cdo-web/).
#
# ## Getting started
#
# Let's start by importing the pyplot submodule of Matplotlib.

# %%


# %% [markdown]
# Note again that we are renaming the Matplotlib pyplot submodule when we import it.
# Perhaps now it is more clear why you might want to rename a module on import.
# Having to type `matplotlib.pyplot` every time you use one of its methods would be a pain.
#
# ### Loading the data with NumPy
#
# Those who have learned to use NumPy should load their data as follows.
#
# To start, we will need to import NumPy.

# %%
import numpy as np

# %% [markdown]
# Now we can read in the data file in the same way we have for Lesson 5.

# %%
fp = 'data/Kumpula-June-2016-w-metadata.txt'
data = np.genfromtxt(fp, skip_header=9, delimiter=',')

# %% [markdown]
# As you may recall, we will now have a data file with 4 columns.
# Let's rename each of those below.

# %%
date = data[:, 0]
temp = data[:, 1]
temp_max = data[:, 2]
temp_min = data[:, 3]

# %% [markdown]
# ### Loading the data with Pandas
#
# Those who have learned to use Pandas should load their data as follows.
#
# To start, we will need to import Pandas.

# %%
import pandas as pd

# %% [markdown]
# Now we can read in the data file in the same way we have for Lesson 5.

# %%
dataFrame = pd.read_csv('data/Kumpula-June-2016-w-metadata.txt', skiprows=8)

# %% [markdown]
# OK, great.
# One thing we'll do a bit differently this week is that we're going to split the data from `dataFrame` into separate Pandas value arrays so we can plot things in the same way as with NumPy.
# We can split the data into separate series as follows:

# %%
date = dataFrame['YEARMODA'].values
temp = dataFrame['TEMP'].values
temp_max = dataFrame['MAX'].values
temp_min = dataFrame['MIN'].values

# %% [markdown]
# The `.values` attribute of a Pandas series returns only the numerical values of the given series, not the index list.

# %% [markdown]
# ## Our first plot
#
# OK, so let’s get to plotting! We can start by using the Matplotlib plt.plot() function.

# %%


# %% [markdown]
# If all goes well, you should see the plot above.
#
# OK, so what happened here?
# Well, first we assigned the values we would like to plot, the year and temperature, to the variables `x` and `y`.
# This isn’t necessary, *per se*, but does make it easier to see what is plotted.
# Next, it is perhaps pretty obvious that `plt.plot()` is a function in pyplot that produces a simple *x*-*y* plot.
# Conveniently, plots are automatically displayed in Jupyter notebooks, so there is no need for the additional `plt.show()` function you might see in examples you can find online.

# %% [markdown]
# ## Basic plot formatting
#
# We can make our plot look a bit nicer and provide more information by using a few additional pyplot options.

# %%


# %% [markdown]
# This should produce the plot above.
#
# Now we see our temperature data as a red dashed line with circles showing the data points.
# This comes from the additional `ro--` used with `plt.plot()`.
# In this case, `r` tells the `plt.plot()` function to use red color, `o` tells it to show circles at the points, and `--` says to use a dashed line.
# You can use `help(plt.plot)` to find out more about formatting plots.
# Better yet, check out the [documentation for `plt.plot()` online](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html).
# We have also added a title and axis labels, but their use is straightforward.

# %% [markdown]
# ### Embiggening\* the plot
#
# While the plot sizes we're working with are OK, it would be nice to have them displayed a bit larger.
# Fortunately, there is an easy way to make the plots larger in Jupyter notebooks.
# To set the default plot size to be larger, simply run the Python cell below.

# %%
plt.rcParams['figure.figsize'] = [12, 6]

# %% [markdown]
# The cell above sets the default plot size to be 12 inches wide by 6 inches tall.
# Feel free to change these values if you prefer.
#
# To test whether this is working as expected, simply re-run one of the earlier cells that generated a plot.
#
# \* To *[embiggen](https://en.oxforddictionaries.com/definition/embiggen)* means to enlarge.
# It's a perfectly [cromulent](https://en.oxforddictionaries.com/definition/cromulent) word.

# %% [markdown]
# ### Adding text labels to a plot
#
# Adding text to plots can be done using `plt.text()`.
#
# ```python
# plt.text(20160604.0, 68.0, 'High temperature in early June')
# ```
#
# This will display the text "High temperature in early June" at the location `x = 20160604.0` (i.e., June 4, 2016), `y = 68.0` on the plot.
# We'll see how to do this in a live example in just a second.
# With our approach to plotting thus far, the commands related to an individual plot should all be in the same Python cell.

# %% [markdown]
# ### Changing the axis ranges
#
# Changing the plot axes can be done using the `plt.axis()` function.
#
# ```python
# plt.axis([20160601, 20160615, 55.0, 70.0])
# ```
#
# The format for `plt.axis()` is `[xmin, xmax, ymin, ymax]` enclosed in square brackets (i.e., a Python list).
# Here, the *x* range would be changed to the equivalents of June 1, 2016 to June 15, 2016 and the *y* range would be 55.0-70.0.
# The complete set of commands to plot would thus be:

# %%
plt.plot(x, y, 'ro--')
plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [°F]')



# %% [markdown]
# ## Bar plots in Matplotlib
#
# In addition to line plots, there are many other options for plotting in Matplotlib.
# Bar plots are one option, which can be used quite similarly to line plots.

# %%

plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [°F]')
plt.text(20160604.0, 68.0, 'High temperature in early June')
plt.axis([20160601, 20160615, 55.0, 70.0])

# %% [markdown]
# You can find more about how to format bar charts on the [Matplotlib documentation website](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html?highlight=matplotlib%20pyplot%20bar#matplotlib.pyplot.bar).

# %% [markdown]
# ## Saving your plots as image files
#
# Saving plots created using Matplotlib done several ways.
# The recommendation for use outside of Jupyter notebooks is to use the `plt.savefig()` function.
# When using `plt.savefig()`, you simply give a list of commands to generate a plot and list `plt.savefig()` with some parameters as the last command.
# The file name is required, and the image format will be determined based on the listed file extension.
#
# Matplotlib plots can be saved in a number of useful file formats, including PNG, PDF, and EPS.
# PNG is a nice format for raster images, and EPS is probably easiest to use for vector graphics.
# Let's check out an example and save our lovely bar plot.

# %%
plt.bar(x, y)
plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [°F]')
plt.text(20160604.0, 68.0, 'High temperature in early June')
plt.axis([20160601, 20160615, 55.0, 70.0])


# %% [markdown]
# If you refresh your **Files** tab on the left side of the JupyterLab window you should now see `bar-plot.png` listed.
# We could try to save another version in higher resolution with a minor change to our plot commands above.

# %%
plt.bar(x, y)
plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [°F]')
plt.text(20160604.0, 68.0, 'High temperature in early June')
plt.axis([20160601, 20160615, 55.0, 70.0])


# %% [markdown]
# <hr>
#
# #### Task 1: Plotting like the "pros"
#
# We’re only introducing a tiny amount of what can be done with pyplot.
# In most cases, when we would like to create some more complicated type of plot, we would search using [Google](https://www.google.fi/) or visit the [Matplotlib plot gallery](http://matplotlib.org/gallery.html).
# The great thing about the [Matplotlib plot gallery](http://matplotlib.org/gallery.html) is that not only can you find example plots there, but you can also find the Python commands used to create the plots.
# This makes it easy to take a working example from the gallery and modify it for your use.
#
# ![The Matplotlib plot gallery](img/matplotlib-gallery.png)
#
# Your job in this task is to:
#
# 1. Visit the [Matplotlib plot gallery](http://matplotlib.org/gallery.html)
# 2. Find an interesting plot and click on it
# 3. Copy the code you find listed beneath the plot on the page that loads
# 4. Paste that into an Python cell in this notebook and run it to reproduce the plot
#
# After you have reproduced the plot, you are welcome to try to make a small change to the plot commands and see what happens.
# For this, you can simply edit the Python cell contents and re-run.
#
# <hr>

# %% [markdown]
# #### Task 2: Plotting only part of a dataset
#
# For this task, you should use the values for arrays `x` and `y` calculated earlier in this part of the lesson, and use `plt.axis()` to limit the plot to the following *x* and *y* ranges: *x = June 7-14*, *y = 45.0-65.0*.
#
# - What do you expect to see in this case?
#
# **Note**: In order to get the plot to display properly, you will need to first type in the `plt.plot()` command, then `plt.axis()`.
