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
#   livereveal:
#     scroll: true
#     theme: solarized
#     transition: none
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
#       height: calc(100% - 180px)
#       left: 10px
#       top: 150px
#       width: 267.797px
#     toc_section_display: true
#     toc_window_display: true
# ---
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Exercise-1.1" data-toc-modified-id="Exercise-1.1-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exercise 1.1</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li><li><span><a href="#Exercise-1.2" data-toc-modified-id="Exercise-1.2-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Exercise 1.2</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-2.0.1"><span class="toc-item-num">2.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li><li><span><a href="#Exercise-1.3" data-toc-modified-id="Exercise-1.3-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Exercise 1.3</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li><li><span><a href="#Exercise-1.4" data-toc-modified-id="Exercise-1.4-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Exercise 1.4</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-4.0.1"><span class="toc-item-num">4.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li></ul></div>
# %% [markdown]
# # Exercise 1.1
#
# **a)** Create a variable `y` with a value of `7`
#
# The cell below is your first look at an autograded Jupyter notebook cell.  The ideas is that, until you replace the contents of that cell with your answer python will raise an error called "NotImplemented". Go ahead and remove replace that statement with your own answer.
# %% {"deletable": false, "lines_to_next_cell": 2, "nbgrader": {"checksum": "8c8fc363b8817c3e277e7070f77238ea", "grade": false, "grade_id": "cell-4835970fca5f66f9", "locked": false, "schema_version": 1, "solution": true}}
y = 7


# %% [markdown]
# Your statement should pass the following test:

# %% {"deletable": false, "editable": false, "lines_to_next_cell": 2, "nbgrader": {"checksum": "8ba1d78dad970b97cdfee8bacb09f270", "grade": true, "grade_id": "cell-9362f71eb05dffad", "locked": true, "points": 2, "schema_version": 1, "solution": false}}
from numpy.testing import assert_almost_equal

assert_almost_equal(y, 7, decimal=1)


# %% [markdown]
# **b)** Create a variable `two_y` with a value of `2 * y`

# %% {"deletable": false, "lines_to_next_cell": 2, "nbgrader": {"checksum": "c88a0b4b359bcbff4b440549d985d17b", "grade": true, "grade_id": "cell-ec6af3f7c1328375", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
two_y = 2 * y


# %% [markdown]
# **c)** Change the value of `y` to `9`. What is the value of `two_y` now, `14` or `18`?

# %% {"deletable": false, "lines_to_next_cell": 2, "nbgrader": {"checksum": "3a1108de203d53914adadecae637deb2", "grade": true, "grade_id": "cell-886acb4e6655300d", "locked": false, "points": 3, "schema_version": 1, "solution": true}}
y = 9
print(two_y)


# %% [markdown]
# `two_y` does not change, even when 'y' changes.

# %% [markdown]
# ### Bonus exercises

# %% [markdown]
# **d) Concatenating strings and integers**
#
# Assign a value of `2018` to the variable `year`. What happens if you use the `+` operator to add the string `'The year is '` with the variable `year`, as shown below? (*You'll need to copy the code below into a cell in your notebook in order to run it.*)
# ```python
# observation = 'The year is ' + year
# ```
# > You'll find you get an error message because Python doesn't know how to add an integer and a string together.
#
# You can use *typecasting* to change the type of an object in Python. For example, you can convert the integer `2018` to the string `'2018'` using the function `str()`. Try running the code below in your notebook and then display the value of the variable `observation`:
# ```python
# observation = 'The year is ' + str(year)
# ```
# - Now create a variable `num_bottles` with a value of `99` (integer) and a variable `song_words` with a value of `' bottles of beer on the wall'`.
# - Use the `+` operator and the `str()` function to concatenate `num_bottles` with `song_words` and confirm that it produces the output `'99 bottles of beer on the wall'`.

# %%
year = 2019
print("The year is " + str(year))

# %%
num_bottles = 99
song_words = " bottles of beer on the wall"
print(str(num_bottles) + song_words)

# %% [markdown]
# **e) Other mathematical operators**
#
# What are the results of the following operations?
#
# - `9 % 3`
# - `10 % 3`
# - `11 % 3`
#
# How about the above operations with the `%` operator replaced with the `//` operator (e.g. `9 // 3`)? Based on these results, what do you think the `%` and `//` operators do? [(Hint)](https://jakevdp.github.io/WhirlwindTourOfPython/04-semantics-operators.html).

# %%
print(9 % 3, 10 % 3, 11 % 3)
print(9 // 3, 10 // 3, 11 // 3)

# %% [markdown]
# The `%` operator is a modular division. `a % b` returns the remainder of `a / b`.
#
# The `//` operator is floor divison. `a // b` returns `a / b` rounded down to the nearest integer.

# %% [markdown]
# **f) Conditional statements**
#
# Create a conditional statement that prints `'Leap year'` if the value of the variable `year` is divisible by 4, and `'Not a leap year'` otherwise. Test your conditional statement by assigning different values to `year` and re-running the code.

# %%
year_to_test = 2016
if year_to_test % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# %% [markdown]
# # Exercise 1.2
#
# **a)** Write a function which takes an input of temperature in degrees Celsius, and returns an output of temperature in degrees Fahrenheit (multiply the temperature in degrees C by 1.8 and add 32)

# %% {"deletable": false, "nbgrader": {"checksum": "ee6c5d820c0f971fbb62517cc5a4f5eb", "grade": true, "grade_id": "cell-ef51470651518f36", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
def celsius_to_fahrenheit(temp_C):
    return temp_C * 1.8 + 32


# %% [markdown]
# b) Use this function to convert 15 C to Fahrenheit, and assign the output to a variable temp_F

# %% {"deletable": false, "nbgrader": {"checksum": "6d0de1b7be4203dc903d5a2fc9b4c766", "grade": false, "grade_id": "cell-ec6800b6465d8a7b", "locked": false, "schema_version": 1, "solution": true}}
temp_C = 15
temp_F = celsius_to_fahrenheit(temp_C)

from numpy.testing import assert_almost_equal

assert_almost_equal(temp_F, 59.0, decimal=1)

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "23b5eba537eb3db8f3db1f83a8f30dac", "grade": true, "grade_id": "cell-7aeb0c61250c5a72", "locked": true, "points": 2, "schema_version": 1, "solution": false}}
# This cell contains a hiddent test that calls your function with another value for temp_celsius


# %% [markdown]
# ### Bonus exercises
#
# **c)** Create a new function based on your function from part (a), which converts the temperature from Celsius to Fahrenheit and also prints a message about the temperature:
# - If the input temperature is less than 10 C, it prints `'Chilly!'`,
# - Otherwise, it prints `'OK'`.
#
# Call the function with different input temperatures to test it.

# %%
def is_it_chilly(temp_C):
    if temp_C < 10:
        print("Chilly!")
    else:
        print("OK")
    return temp_C * 1.8 + 32


# %%
temp_F = is_it_chilly(8)

# %%
temp_F = is_it_chilly(50)

# %% [markdown]
# **d)** Modify your function from part (c) so that it accepts a second input called `temp_chilly`, which is used for the "chilly" temperature threshold (instead of always using 10 C). Test the function by calling it with various values for each of the two inputs.

# %%
def how_chilly(temp_C, temp_chilly=10):
    if temp_C < temp_chilly:
        print("Chilly!")
    else:
        print("OK")
    return temp_C * 1.8 + 32


# %%
temp_F = how_chilly(8, 5)

# %%
temp_F = how_chilly(8)

# %% [markdown]
# Here, `temp_chilly` is an optional paramter. If we specify a value, such as `5`, then `5` becomes the temperature threshold. Otherwise, it assumes the default value of `10`.

# %% [markdown]
# # Exercise 1.3
#
# **a)** Create a list called `numbers` containing the values: `7, -4, 1e8, 8.3, 287, 29, -2.5, 9.8`

# %%
numbers = [7, -4, 1e8, 8.3, 287, 29, -2.5, 9.8]

# %% [markdown]
# **b)** Display a slice of `numbers` containing the last 3 items

# %%
print(numbers[-3:])

# %% [markdown]
# **c)** Loop over the items in `numbers` to print out each item multiplied by 10

# %%
for item in numbers:
    print(item * 10)

# %% [markdown]
# ### Bonus exercises
#
# **d) Creating a sequence of integers**
#
# The built-in function `range` produces a sequence of integers from a specified start (inclusive) to stop (exclusive). This can be helpful when we want to loop over a long sequence of numbers without manually creating a list of those numbers. Try copying the code below into your notebook and running it to see how it works:
#
# ```python
# for num in range(7, 16):
#     print(num)
# ```
#
# Using the code above as a guide, and also using the techniques from previous bonus exercise 1.1(d) for concatenating an integer variable with a string:
# - Create a `for` loop that loops over a sequence of years from 1938 up to and including 2012, and for each year in the sequence, prints `'The year is '` plus the current value of the year.

# %%
for num in range(1938, 2013):
    print("The year is " + str(num))

# %% [markdown]
# **e) Negative indices**
#
# - Display the item at index `-1` of your list `numbers` from part (a).
# - How about index `-2`, `-3`, etc?
# - What do you conclude about negative indices?

# %%
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

# %% [markdown]
# **f) More about slices**
#
# - Display the slices `numbers[::2]`, `numbers[1:6:2]`, and `numbers[::-1]`.
# - What do you conclude about the number after the second colon?
# - How would you slice `numbers` to display every 3rd item starting from index 1?

# %%
print(numbers[::2])
print(numbers[1:6:2])
print(numbers[::-1])

# %% [markdown]
# To slice `numbers` to display every 3rd item starting from index 1:

# %%
print(numbers[1::3])

# %% [markdown]
# **g) Indexing with strings**
#
# Create a variable `city` with a value of `'Vancouver'`.
# - Display the values of `city[0]` and `city[3:7]`.
# - What do you conclude about indexing string variables?
# - What happens if you try to assign `city[6] = 'Q'`?

# %%
city = "Vancouver"
print(city[0])
print(city[3:7])

# %%
# city[6] = 'Q'
# print(city)

# %% [markdown]
# Unlike lists, strings do not support item assignment. This block is commented out to not throw any errors. Try uncommenting it.

# %% [markdown]
# # Exercise 1.4
#
# a) In the `fruit_colors` dictionary:
# - Change the color of `apple` to `'red'`
# - Add an item with key `'plum'` and value of `'purple'`
# - Display the updated `fruit_colors` dictionary

# %%
fruit_colors = {"banana": "yellow", "strawberry": "red", "apple": "green"}

# %%
fruit_colors["apple"] = "red"
fruit_colors["plum"] = "purple"
print(fruit_colors)

# %% [markdown]
# b) Loop through the `fruit_colors` dictionary and print the fruit name (key) only if its color (value) is `'red'`.

# %%
for fruit in fruit_colors:
    if fruit_colors[fruit] == "red":
        print(fruit)

# %% [markdown]
# ### Bonus exercises
#
# c) Create a new *empty* dictionary `groceries` with the syntax `groceries = {}` and then display `groceries`. Add a key `'eggs'` with a value of `12` and display the updated `groceries` dictionary.

# %%
groceries = {}
print(groceries)

# %%
groceries["eggs"] = 12
print(groceries)

# %% [markdown]
# d) Create a new dictionary `squares` whose keys are the integers `1`, `2`, `3`, `4`, `5`, and the value for each key is the key squared (so for key `1`, the value is `1`; for key `2`, the value is `4`; etc.).
# - Hint: See if you can find a couple of different ways to accomplish this task. One approach might involve a list along with an empty dictionary and a `for` loop.

# %%
### There are two way to accomplish this. First, using brute force:
squares_1 = {}
for i in range(1, 6):
    squares_1[i] = i ** 2

### The second is more pythonic and uses comprehension. Notice how we remove the loop. This makes it run faster, and is much easier to read.
squares_2 = {i: i ** 2 for i in range(1, 6)}

# %%
print(squares_1)
print(squares_2)

# %%
