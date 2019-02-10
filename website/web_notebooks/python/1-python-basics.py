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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Variables" data-toc-modified-id="Variables-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Variables</a></span></li><li><span><a href="#Naming-Variables" data-toc-modified-id="Naming-Variables-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Naming Variables</a></span></li><li><span><a href="#Data-Types" data-toc-modified-id="Data-Types-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Data Types</a></span></li><li><span><a href="#Strings" data-toc-modified-id="Strings-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Strings</a></span></li><li><span><a href="#Comparison-&amp;-Logic" data-toc-modified-id="Comparison-&amp;-Logic-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Comparison &amp; Logic</a></span></li><li><span><a href="#Conditionals" data-toc-modified-id="Conditionals-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Conditionals</a></span></li><li><span><a href="#Data-Types---Recap" data-toc-modified-id="Data-Types---Recap-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Data Types - Recap</a></span></li><li><span><a href="#Exercise-1.1" data-toc-modified-id="Exercise-1.1-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Exercise 1.1</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-8.0.1"><span class="toc-item-num">8.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li><li><span><a href="#Functions" data-toc-modified-id="Functions-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Functions</a></span></li><li><span><a href="#Built-In-Functions" data-toc-modified-id="Built-In-Functions-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Built-In Functions</a></span></li><li><span><a href="#Defining-Functions" data-toc-modified-id="Defining-Functions-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Defining Functions</a></span></li><li><span><a href="#Exercise-1.2" data-toc-modified-id="Exercise-1.2-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Exercise 1.2</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-12.0.1"><span class="toc-item-num">12.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li><li><span><a href="#Methods" data-toc-modified-id="Methods-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Methods</a></span></li><li><span><a href="#Lists" data-toc-modified-id="Lists-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>Lists</a></span><ul class="toc-item"><li><span><a href="#Slices" data-toc-modified-id="Slices-14.1"><span class="toc-item-num">14.1&nbsp;&nbsp;</span>Slices</a></span></li><li><span><a href="#Modifying-a-List" data-toc-modified-id="Modifying-a-List-14.2"><span class="toc-item-num">14.2&nbsp;&nbsp;</span>Modifying a List</a></span></li></ul></li><li><span><a href="#Loops" data-toc-modified-id="Loops-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>Loops</a></span></li><li><span><a href="#Exercise-1.3" data-toc-modified-id="Exercise-1.3-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>Exercise 1.3</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-16.0.1"><span class="toc-item-num">16.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li><li><span><a href="#Dictionaries" data-toc-modified-id="Dictionaries-17"><span class="toc-item-num">17&nbsp;&nbsp;</span>Dictionaries</a></span></li><li><span><a href="#Exercise-1.4" data-toc-modified-id="Exercise-1.4-18"><span class="toc-item-num">18&nbsp;&nbsp;</span>Exercise 1.4</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Bonus-exercises" data-toc-modified-id="Bonus-exercises-18.0.1"><span class="toc-item-num">18.0.1&nbsp;&nbsp;</span>Bonus exercises</a></span></li></ul></li></ul></li></ul></div>

# %% [markdown]
# # Variables
#
# Use `=` to **assign** a value to a variable.

# %%
x = 5

# %% [markdown]
# There are two options for displaying the value of `x`:

# %%
x

# %% [markdown]
# Or use the `print` function:

# %%
print(x)

# %% [markdown]
# A cell can contain multiple lines of code:

# %%
length = 10
width = 2.5

# %% [markdown]
# Text prefaced with `#` is a **comment**, which is a note to people reading the code and is ignored by Python.

# %%
# Calculate area of rectangle
area = length * width

# Display the area
area

# %% [markdown]
# What if we change the value of a variable?
# - Currently, `length` is 10 and `width` is 2.5

# %%
width = 3.5

# %%
area

# %%
length * width

# %% [markdown]
# If we go up to the previous cell that calculated the rectangle area, what is the output?

# %% [markdown]
# - The calculated area corresponds to the *new* value of `width` (3.5) even though the cell immediately above shows `width` being assigned a value of 2.5
# - Jupyter notebooks are nonlinear&mdash;a collection of cells that can be run out of order
#   - Need to be cautious when running cells out of order!
#   - It's good practice to periodically restart the kernel and run all cells in order

# %% [markdown]
# # Naming Variables
#
# - Can only use letters, numbers and underscore `_`
# - Can't start with a number
#   - `day1` is ok, but `1day` will cause an error
# - Use descriptive names and separate words with an underscore (e.g. `first_name`, `land_area`)

# %%
avogadro = 6.02e23

# %% [markdown]
# Try typing `av` and then press `Tab` and see what happens

# %%


# %% [markdown]
# Auto-complete! One of the very handy features of IPython.

# %% [markdown]
# # Data Types
#
# So far we've worked two types of numbers in Python:
# - `int` (integer)
# - `float` (decimal numbers)

# %%
n = 42
pi = 3.14159

# %% [markdown]
# The type of a variable is determined by the value assigned to it
# - We can use the function `type` to find out the type

# %%
type(pi)

# %%
type(n)

# %% [markdown]
# # Strings
#
# - Text data is of the type `str`, which stands for **string**: a sequence of characters enclosed in single or double quotation marks
# - The characters in a string can be letters, numbers, punctuation, symbols, etc.

# %%
today = "Tuesday"
tomorrow = "Wednesday"

# %%
type(today)

# %% [markdown]
# Strings can be **concatenated** with the `+` operator:

# %%
statement = "Today is " + today
statement

# %%


# %% [markdown]
# # Comparison & Logic
#
# We can also use comparison and logic operators (`<`, `>`, `==`, `!=`, `<=`, `>=`, `and`, `or`, `not`), which will return either `True` or `False`.

# %%
year = 2018
year

# %%
year > 2000

# %%
year == 1990

# %% [markdown]
# Note the double equals sign above
# - Single equals sign `=` is for assigning a value to a variable
# - Double equals sign `==` is for *checking* if values are equal to each other

# %% [markdown]
# `not` reverses the outcome from a comparison.

# %%
not year == 1990

# %% [markdown]
# `and` checks if both comparisons are `True`.

# %%
3 < 4 and 5 > 10

# %% [markdown]
# `or` checks if *at least* one of the comparisons are `True`.
# - Below we're also taking the output of the comparison and assigning it to a variable `result`

# %%
result = 3 < 4 or 5 > 10
result

# %% [markdown]
# The resulting `True` or `False` value is of type `bool`, short for **Boolean**.

# %%
type(result)

# %% [markdown]
# As we'll see later, Boolean comparisons like these are important when extracting specific values from a larger set of values.

# %% [markdown]
# # Conditionals
#
# Another common use of Boolean comparison is with a conditional statement, where the code after the comparison only is executed if the comparison is `True`.

# %%
a = 12

if a < 10:
    print("a is less than 10")
else:
    print("a is greater than or equal to 10")

# %% [markdown]
# - Note the **indented** line after each colon `:`
# - Indentation is very important in Python!
# - In this example, indentation indicates which code is executed if the conditional statement is `True` and which code is executed if the conditional is not `True`

# %% [markdown]
# # Data Types - Recap
#
# - Integer (`int` &mdash; whole numbers)
# - Float (`float` &mdash; numbers containing decimals)
# - String (`str` &mdash; words, sentences, other text)
# - Boolean (`bool` &mdash; `True` or `False`)
# - and many others!

# %% [markdown]
# # Exercise 1.1
#
# **a)** Create a variable `y` with a value of `7`
#
# The cell below is your first look at an autograded Jupyter notebook cell.  The ideas is that, until you replace the contents of that cell with your answer python will raise an error called "NotImplemented". Go ahead and remove replace that statement with your own answer.

# %% {"deletable": false, "nbgrader": {"checksum": "8c8fc363b8817c3e277e7070f77238ea", "grade": false, "grade_id": "cell-4835970fca5f66f9", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% [markdown]
# You statement should pass the following test:

# %% {"deletable": false, "editable": false, "nbgrader": {"checksum": "8ba1d78dad970b97cdfee8bacb09f270", "grade": true, "grade_id": "cell-9362f71eb05dffad", "locked": true, "points": 2, "schema_version": 1, "solution": false}}
from numpy.testing import assert_almost_equal

assert_almost_equal(y, 7, decimal=1)


# %% [markdown]
# **b)** Create a variable `two_y` with a value of `2 * y`

# %% {"deletable": false, "nbgrader": {"checksum": "c88a0b4b359bcbff4b440549d985d17b", "grade": true, "grade_id": "cell-ec6af3f7c1328375", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


# %% [markdown]
# **c)** Change the value of `y` to `9`. What is the value of `two_y` now, `14` or `18`?

# %% {"deletable": false, "nbgrader": {"checksum": "3a1108de203d53914adadecae637deb2", "grade": true, "grade_id": "cell-886acb4e6655300d", "locked": false, "points": 3, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()


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

# %% [markdown]
# **f) Conditional statements**
#
# Create a conditional statement that prints `'Leap year'` if the value of the variable `year` is divisible by 4, and `'Not a leap year'` otherwise. Test your conditional statement by assigning different values to `year` and re-running the code.

# %% [markdown]
# # Functions
#
# - Functions are bundles of code that can be re-used
# - Python has many handy built-in functions, for example:
#   - `print`
#   - `type`
#   - `round`
#   - `abs`
#   - `sum`
# - You can also define your own functions

# %% [markdown]
# # Built-In Functions

# %%
round(3.14159)

# %% [markdown]
# Auto-complete works for functions too. Try typing `ro` followed by `Tab`.

# %%


# %% [markdown]
# - Inputs to a function are called **arguments**
# - Arguments can be required or optional
# - Functions **return** an output value or a `None` output
#   - `round(3.14159)` returns `3`
#   - `print('hello')` returns `None`

# %% [markdown]
# Use `?` after the function name to see the documentation. (remove the # to try this)

# %%
# round?

# %% [markdown]
# - Python documentation is sometimes helpful and sometimes totally confusing, especially when you're first learning the language
# - Other online resources can be much more helpful and easier to understand, for example:
#   - Tutorials
#   - Blog posts with examples and code
#   - Questions and answers posted on Stack Overflow and other forums
# - Think of Google search as an essential component in your Python workflow!

# %%
round(3.14159, 2)

# %% [markdown]
# When we call a function, what do we do with its output?

# %% [markdown]
# 1) We can simply display the output on the screen to see what it looks like:

# %%
round(1 / 3, 5)

# %% [markdown]
# 2) We can assign it to a variable so that we can use it elsewhere:

# %%
one_third = round(1 / 3, 5)
one_third


# %% [markdown]
# # Defining Functions
#
# - We can define functions anywhere in our code using the `def` keyword
# - The contents of the function are an **indented block**
# - Use the `return` keyword to return an output

# %%
def fraction(num, denom):
    result = num / denom
    return result


# %% [markdown]
# We can **call** our function by supplying input values in the same order they were defined above (numerator followed by denominator).
#
# - These inputs are referred to as **positional arguments**.

# %%
fraction(30, 7)

# %% [markdown]
# Or, we can use use the labels `num` and `denom` to specify input values in any order we want in our function call.
# - These inputs are referred to as **keyword arguments**.
#
# > Pro Tip: Auto-complete works for keyword arguments too!

# %%
fraction(denom=7, num=30)


# %% [markdown]
# Some terminology:
#
# - When we *define* a function, the inputs defined inside parentheses are called **parameters**
# - When we *call* a function, the input *values* we pass to the function are called **arguments**

# %% [markdown]
# We can also specify **default values** for inputs
# - When *defining* the function, these default input values must be listed *after* any inputs that don't have default values

# %%
def fraction_rounded(num, denom, ndigits=2):
    result = round(num / denom, ndigits)
    return result


# %%
fraction_rounded(denom=7, num=30)

# %%
fraction_rounded(denom=7, num=30, ndigits=6)


# %% [markdown]
# - It is helpful to include a description of the function.
# - There is a special syntax for this in Python that makes sure that the message shows up in the help message.

# %%
def fraction_rounded(num, denom, ndigits=2):
    """Return the fraction num/denom rounded to ndigits"""
    result = round(num / denom, ndigits)
    return result


# %% [markdown]
# The string between the `"""` is called the docstring and is shown in the help message, so it is important to write a clear description of the function here.

# %% [markdown]
# As with built-in functions, `?` can be used to get help for user defined functions.

# %%
# fraction_rounded?

# %% [markdown]
# The entire source code of a function can be displayed with `??` (if it is short enough)

# %%
# fraction_rounded??

# %% [markdown]
# Related functions can be bundled together in libraries (modules/packages)

# %% [markdown]
# # Exercise 1.2
#
# **a)** Write a function which takes an input of temperature in degrees Celsius, and returns an output of temperature in degrees Fahrenheit (multiply the temperature in degrees C by 1.8 and add 32)

# %% {"deletable": false, "nbgrader": {"checksum": "ee6c5d820c0f971fbb62517cc5a4f5eb", "grade": true, "grade_id": "cell-ef51470651518f36", "locked": false, "points": 2, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# %% [markdown]
# b) Use this function to convert 15 C to Fahrenheit, and assign the output to a variable temp_F

# %% {"deletable": false, "nbgrader": {"checksum": "6d0de1b7be4203dc903d5a2fc9b4c766", "grade": false, "grade_id": "cell-ec6800b6465d8a7b", "locked": false, "schema_version": 1, "solution": true}}
# YOUR CODE HERE
raise NotImplementedError()

# You code sould pass the following test:
from numpy.testing import assert_almost_equal

assert_almost_equal(temp_F, 59.0, decimal=1)
print(convert_celsius(30))

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

# %% [markdown]
# **d)** Modify your function from part (c) so that it accepts a second input called `temp_chilly`, which is used for the "chilly" temperature threshold (instead of always using 10 C). Test the function by calling it with various values for each of the two inputs.

# %% [markdown]
# # Methods
#
# A **method** is a function that is "attached" to a Python object
# - e.g. String methods: `upper`, `lower`, `capitalize`, `replace`, `strip`, and many more
# - We use **dot notation** to access an object's methods
#
# > Note: Methods are a feature of *object oriented programming*, which we won't delve into here, but for more details, check out [this tutorial](https://www.datacamp.com/community/tutorials/python-oop-tutorial).

# %%
message = "Hello world."
message.upper()

# %% [markdown]
# Did our variable `message` change?

# %%
message

# %% [markdown]
# Auto-complete works on methods too
# - Try typing `message.` (including the dot at the end) and then press `Tab` and see what happens

# %%


# %%
new_message = message.replace("world", "universe")
new_message

# %% [markdown]
# Is the `replace` method case sensitive?

# %%
message.replace("hello", "hi")

# %% [markdown]
# Methods can be **chained** together:

# %%
shouting = message.upper().replace(".", "!!!")
shouting

# %% [markdown]
# # Lists
#
# **Lists** are a common data structure to hold an ordered sequence of elements.

# %%
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
planets

# %%
prime_numbers = [2, 3, 5, 7, 11, 13]
prime_numbers

# %%
different_data_types = [3.14, "Canada", 62 / 7, 1729]
different_data_types

# %% [markdown]
# Lists can be added together with the `+` operator:

# %%
planets + prime_numbers

# %% [markdown]
# You can use the function `len` to get the length of a list

# %%
len(planets)

# %% [markdown]
# Each element in a list can be accessed by an **index**.
# - Note that Python indexes start with 0 instead of 1.

# %% [markdown]
# ![](img/list_index.png)

# %%
planets[0]

# %%
planets[3]

# %% [markdown]
# How can we access the element `'Earth'` from the list `planets`?

# %%


# %% [markdown]
# How can we access the last element in the list `planets`?

# %%


# %% [markdown]
# What happens if we try to access `planets[10]`?

# %%


# %% [markdown]
# Notice that for indexing we use square brackets `[]` whereas for function calls we use parentheses `()`. This is one of the (many) features that makes Python code easy to read.
#
# ```python
# thing1 = something(5)
# thing2 = something_else[5]
# ```

# %% [markdown]
# Without having any other information about the code above, we already know that `something` is a *function*, whereas `something_else` is a *data structure* (such as a list).
# > Of course, it's good practice to give your functions and variables descriptive names, unlike the cryptic code above!

# %% [markdown]
# ## Slices
#
# Multiple elements in a list can be selected via **slicing**.

# %% [markdown]
# ![](img/list_index.png)

# %%
planets[1:3]

# %% [markdown]
# Slicing is inclusive of the start of the range and exclusive of the end, so the slice `planets[1:3]` includes all elements from index 1 up to&mdash;but not including&mdash;index 3

# %% [markdown]
# Either the start or the end number of the range can be excluded to include all items to the beginning or end of the list, respectively.

# %%
planets[:2]

# %% [markdown]
# ## Modifying a List
#
# - Lists are modified "in place"

# %%
planets[3] = "MARS!"
planets

# %% [markdown]
# We can use methods such as `append` and `remove` to add or remove items from a list
#
# - As with string methods, list methods use dot notation

# %%
planets.append("Uranus")
planets

# %% [markdown]
# # Loops
#
# A loop can be used to access the elements in a list or other Python data structure one at a time.

# %%
for planet in planets:
    print(planet)

# %% [markdown]
# The variable `planet` is re-created for every iteration in the loop until the list `planets` has been exhausted.

# %% [markdown]
# Operations can be performed on elements inside loops:

# %%
for planet in planets:
    print("I live on " + planet)

# %% [markdown]
# # Exercise 1.3
#
# **a)** Create a list called `numbers` containing the values: `7, -4, 1e8, 8.3, 287, 29, -2.5, 9.8`

# %% [markdown]
# **b)** Display a slice of `numbers` containing the last 3 items

# %% [markdown]
# **c)** Loop over the items in `numbers` to print out each item multiplied by 10

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
#
# > In a later bonus exercise, we'll use this loop for downloading Environment Canada weather data!

# %% [markdown]
# **e) Negative indices**
#
# - Display the item at index `-1` of your list `numbers` from part (a).
# - How about index `-2`, `-3`, etc?
# - What do you conclude about negative indices?

# %% [markdown]
# **f) More about slices**
#
# - Display the slices `numbers[::2]`, `numbers[1:6:2]`, and `numbers[::-1]`.
# - What do you conclude about the number after the second colon?
# - How would you slice `numbers` to display every 3rd item starting from index 1?

# %% [markdown]
# **g) Indexing with strings**
#
# Create a variable `city` with a value of `'Vancouver'`.
# - Display the values of `city[0]` and `city[3:7]`.
# - What do you conclude about indexing string variables?
# - What happens if you try to assign `city[6] = 'Q'`?

# %% [markdown]
# # Dictionaries
#
# A **dictionary** is a data structure that holds pairs of objects - keys and values.

# %%
fruit_colors = {"banana": "yellow", "strawberry": "red"}
fruit_colors

# %% [markdown]
# - Dictionaries work a lot like lists - except that they are indexed with **keys**.
# - Think about a key as a unique identifier for a set of values in the dictionary.
# - Keys can only have particular types - they have to be "hashable".
#   - Strings and numeric types are acceptable, but lists aren't.

# %%
fruit_colors["banana"]

# %% [markdown]
# To add an item to the dictionary, a value is assigned to a new dictionary key.

# %%
fruit_colors["apple"] = "green"
fruit_colors

# %% [markdown]
# Using loops with dictionaries iterates over the keys by default.

# %%
for fruit in fruit_colors:
    print(fruit + " is " + fruit_colors[fruit])

# %% [markdown]
# Trying to use a non-existing key, e.g. from a typo, throws an error message.

# %%
fruit_colors["bannana"]

# %% [markdown]
# This is an error message, commonly referred to as a "traceback". This message pinpoints what line in the code cell resulted in an error when it was executed, by pointing at it with an arrow (`---->`). This is helpful in figuring out what went wrong, especially when many lines of code are executed simultaneously.

# %% [markdown]
# # Exercise 1.4
#
# a) In the `fruit_colors` dictionary:
# - Change the color of `apple` to `'red'`
# - Add an item with key `'plum'` and value of `'purple'`
# - Display the updated `fruit_colors` dictionary

# %% [markdown]
# b) Loop through the `fruit_colors` dictionary and print the fruit name (key) only if its color (value) is `'red'`.

# %% [markdown]
# ### Bonus exercises
#
# c) Create a new *empty* dictionary `groceries` with the syntax `groceries = {}` and then display `groceries`. Add a key `'eggs'` with a value of `12` and display the updated `groceries` dictionary.

# %% [markdown]
# d) Create a new dictionary `squares` whose keys are the integers `1`, `2`, `3`, `4`, `5`, and the value for each key is the key squared (so for key `1`, the value is `1`; for key `2`, the value is `4`; etc.).
# - Hint: See if you can find a couple of different ways to accomplish this task. One approach might involve a list along with an empty dictionary and a `for` loop.
