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
# <div class="toc"><ul class="toc-item"><li><span><a href="#What-makes-code-beautiful?" data-toc-modified-id="What-makes-code-beautiful?-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>What makes code beautiful?</a></span></li><li><span><a href="#Some-rules-of-thumb" data-toc-modified-id="Some-rules-of-thumb-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Some rules of thumb</a></span><ul class="toc-item"><li><span><a href="#Some-docstring-examples" data-toc-modified-id="Some-docstring-examples-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Some docstring examples</a></span></li></ul></li><li><span><a href="#Type-systems" data-toc-modified-id="Type-systems-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Type systems</a></span><ul class="toc-item"><li><span><a href="#Example-of-strong-typing" data-toc-modified-id="Example-of-strong-typing-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Example of strong typing</a></span><ul class="toc-item"><li><span><a href="#Your-turn----rewrite-the-cell-above-with-a-cast-that-makes-it-work" data-toc-modified-id="Your-turn----rewrite-the-cell-above-with-a-cast-that-makes-it-work-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Your turn -- rewrite the cell above with a cast that makes it work</a></span></li></ul></li><li><span><a href="#Example-of-dynamic-typing" data-toc-modified-id="Example-of-dynamic-typing-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Example of dynamic typing</a></span></li><li><span><a href="#Type-summary" data-toc-modified-id="Type-summary-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Type summary</a></span></li></ul></li><li><span><a href="#Flexible-functions" data-toc-modified-id="Flexible-functions-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Flexible functions</a></span><ul class="toc-item"><li><span><a href="#See:-vanderplas-Section-6--for-an-explantion-of-*args-and-**kwargs" data-toc-modified-id="See:-vanderplas-Section-6--for-an-explantion-of-*args-and-**kwargs-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>See: <a href="https://jakevdp.github.io/WhirlwindTourOfPython/08-defining-functions.html" target="_blank">vanderplas Section 6</a>  for an explantion of <code>*args</code> and <code>**kwargs</code></a></span></li><li><span><a href="#What-is-going-on-under-the-hood" data-toc-modified-id="What-is-going-on-under-the-hood-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>What is going on under the hood</a></span></li></ul></li><li><span><a href="#Number-1-python-&quot;gotcha&quot;" data-toc-modified-id="Number-1-python-&quot;gotcha&quot;-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Number 1 python "gotcha"</a></span><ul class="toc-item"><li><span><a href="#Note-that-the-id-of-the-default-list-is-the-same-for-each-call!" data-toc-modified-id="Note-that-the-id-of-the-default-list-is-the-same-for-each-call!-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Note that the id of the default list is the same for each call!</a></span></li><li><span><a href="#The-preferred-approach----use-None-as-a-default-value" data-toc-modified-id="The-preferred-approach----use-None-as-a-default-value-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>The preferred approach -- use None as a default value</a></span></li></ul></li><li><span><a href="#Duck-typing-and-type-casting" data-toc-modified-id="Duck-typing-and-type-casting-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Duck typing and type casting</a></span><ul class="toc-item"><li><span><a href="#Your-turn:--in-the-cell-below,-use-numpy.asarray-to-cast-the-argument-to-an-array" data-toc-modified-id="Your-turn:--in-the-cell-below,-use-numpy.asarray-to-cast-the-argument-to-an-array-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Your turn:  in the cell below, use numpy.asarray to cast the argument to an array</a></span></li></ul></li></ul></div>
# %% [markdown]
# # Wrting python functions
# %% [markdown]
# ## What makes code beautiful?
#
# Reference:  [Chapter 29 of Beautiful Code](http://webcat2.library.ubc.ca/vwebv/holdingsInfo?searchId=169488&recCount=100&recPointer=1&bibId=9436527) by Yukihiro Matsumoto:
# "Treating code as an essay"
#
# - Brevity -- no unnecessary information -- DRY "don't repeat yourself"
#
# - Familiarity  -- use familiar patterns
#
# - Simplicity
#
# - Flexibilty -- simple things should be simple, complex things should be possible
#
# - Balance
#
# Coding is a craft, like writing, cooking or furniture making.  You develop a sense of balance
# by following master craftspeople in an apprenticeship.  One of the big benefits of github is that
# it gives you a chance to interact with very good programmers in an informal apprenticeship.
#
# %% [markdown]
# ## Some rules of thumb
#
# 1.  Functions in a program play the role of paragraphs in an essay.  They should express a single idea clearly.
#
# 1.  That means they should not be longer than a single screen.  Paging is distracting and breaks your concentration.  It shouldn't take more than 1 minute to understand what a function does.
#
# 1.  Not every function has to be documented, but you should be able to summarize any function you write in a clear, concise, docstring.
#
# 1.  The best documentation is a working test case.
#
# 1.  You should think about how your function might change in the future, and design in some degree of flexibility.
#
# 1.  Functions should have a single entry and a single exit
#
# 1.  Whenever possible functions should be free of side effects.  Exceptions to this rule include opening and writing files to disk, and modifying large arrays in place to avoid a copy.
#
# 1.  If you do modify an erray that is passed as a function argument, return that array to signal the change.  In python there is no performance penalty for this, because the array is not copied, instead, a new
# name is assigned and python now knows that two names point to the same array.  When in doubt,
# use the `id` function to get the memory location of the new name and the old name -- they should be
# identical
#
# ###  Some docstring examples
#
# 1.  Formatted: https://phaustin.github.io/a301_code/codedoc/full_listing.html#a301.landsat.toa_radiance.calc_radiance_8
#
# 1.  Source: https://phaustin.github.io/a301_code/_modules/a301/landsat/toa_radiance.html#calc_radiance_8
# %% [markdown]
# ## Type systems
#
# In order to understand python functions, it helps to understand how python handles types.
#
# Compare C and python:
#
# * C: Strongly typed, statically typed
#
# * Python: Stongly typed, dynamically typed
# %% [markdown]
# ### Example of strong typing
#
# The following cell will raise a TypeError in python.  This will also fail to compile in C
# %%
a = 5
try:
    b = 5 + "3"
except TypeError:
    print("caught a TypeError -- won't work")

# %% [markdown]
# #### Your turn -- rewrite the cell above with a cast that makes it work

# %% [markdown]
# ### Example of dynamic typing
#
# The following cell will run in python, but would fail to compile in C
# because it reassigns the type of a

# %%
a = 5
print(f"the type of a is {type(a)}")
a = "5"
print(f"now the type of a is {type(a)}")


# %% [markdown]
# ### Type summary
#
# - Python is strongly typed, which means that it won't coerce a type into another type
#   without an explicit cast.  ("Explicit is better than implicit")
#
# - Python is dynamically typed, which means that a variable name is attached to an instance
#   of an object, but not to the object's type, so the name can be reassigned to an
#   instance of a different type.

# %% [markdown]
# ## Flexible functions

# %% [markdown]
# ###  See: [vanderplas Section 6](https://jakevdp.github.io/WhirlwindTourOfPython/08-defining-functions.html)  for an explantion of `*args` and `**kwargs`

# %%
def fibonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L


# %%
fibonacci(10)

# %%
fibonacci(10, b=3, a=1)


# %% [markdown]
# ### What is going on under the hood

# %% [markdown]
# Now rewrite this to be fully flexible -- this is what
# the default arguments code is actually doing:

# %%
def fibonacci_raw(*args, **kwargs):
    print(f"I got args={args} and kwargs={kwargs}")
    N = args[0]
    L = []
    #
    # the dictionary "get" method takes a second
    # argument which is the default value
    # that is returned when the dictionary key is missing
    #
    a = kwargs.get("a", 0)
    b = kwargs.get("b", 1)
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L


# %%
fibonacci_raw(10, b=3, a=1, bummer=True)

# %%
fibonacci_raw(10)


# %% [markdown]
# ## Number 1 python "gotcha"
#
# As noted here, there is a subtle issue with using default arguments
# that are not numbers or strings.  Bottom line, do not do this.
#
# https://docs.python-guide.org/writing/gotchas/
#
# Here's an example of how you can get bitten:

# %%
def append_to(element, to_list=[]):
    to_list.append(element)
    print(f"\ncalling with element={element}, the id of to_list is {id(to_list)}\n")
    return to_list


my_list = append_to(12)
print(f"first time I call the function I get {my_list}")

my_other_list = append_to(42)
print(f"second time I call the function I get {my_other_list}")


# %% [markdown]
# ### Note that the id of the default list is the same for each call!
#
# This is generally not what you expect, because you'll get different behaviour with identical
# inputs.  This violates "no side effects" and also "familiarity"

# %% [markdown]
# ### The preferred approach -- use None as a default value
#
# If you want the list to be created fresh by default, then test for None and create it.
#
# Note that now the two lists have different ids.

# %%
def append_to(element, to_list=None):
    if to_list is None:
        to_list = []
    to_list.append(element)
    print(f"\ncalling with element={element}, the id of to_list is {id(to_list)}\n")
    return to_list


my_list = append_to(12)
print(f"first time I call the function I get {my_list}")

my_other_list = append_to(42)
print(f"second time I call the function I get {my_other_list}")

# %% [markdown]
# ## Duck typing and type casting
#
# Consider the following function:

# %%
import numpy as np


def trysort(mylist):
    #
    # this assumes mylist is a "duck" with a sort method
    #
    mylist.sort()
    print(f"inside trysort, mylist is {mylist}")
    return mylist


trysort([3, 2, 1])
trysort(np.array([3, 2, 1]))
try:
    trysort((3, 2, 1))
except AttributeError:
    print("last example failed, tuple has no sort method")

# %% [markdown]
# This is an example of "duck typing"
#
# ```
# If it walks like duck, and quacks like a duck
# then it's a duck
# ```
#
# This function fails because the tuple object has no sort method

# %% [markdown]
# ### Your turn:  in the cell below, use numpy.asarray to cast the argument to an array

# %%

# %% [markdown]
# ## writing tests
#
# Python has an extensive testing framework called [pytest](https://docs.pytest.org/en/latest/).  This
# is overkill for this class, but we can capture the spririt of pytest by writing test functions
# with asserts
#
# ### Example

# %%
from numpy.testing import assert_allclose


def test_fib():
    #
    # deliberately insert a wrong result
    #
    result = fibonacci(10, b=3, a=1)
    result[0] = 5
    answer = [2, 4, 7, 11, 18, 29, 47, 76, 123, 199]
    assert_allclose(result, answer)


test_fib()


# %% [markdown]
# ### Sumary for testing
#
# When we start writing python modules, we can use pytest to search through the file, find any
# functions with the word "test" in their name, and run those tests, generating a report
