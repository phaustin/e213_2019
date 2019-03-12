# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Types-and-classes" data-toc-modified-id="Types-and-classes-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Types and classes</a></span></li><li><span><a href="#Class-variables" data-toc-modified-id="Class-variables-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Class variables</a></span></li><li><span><a href="#Instance-variables" data-toc-modified-id="Instance-variables-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Instance variables</a></span></li><li><span><a href="#Instance-methods" data-toc-modified-id="Instance-methods-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Instance methods</a></span><ul class="toc-item"><li><span><a href="#Passing-self-to-instance-methods" data-toc-modified-id="Passing-self-to-instance-methods-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Passing self to instance methods</a></span></li></ul></li><li><span><a href="#Your-turn" data-toc-modified-id="Your-turn-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Your turn</a></span></li><li><span><a href="#Solution" data-toc-modified-id="Solution-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Solution</a></span></li><li><span><a href="#Summary" data-toc-modified-id="Summary-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Summary</a></span></li><li><span><a href="#Appendix" data-toc-modified-id="Appendix-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Appendix</a></span><ul class="toc-item"><li><span><a href="#Further-reading" data-toc-modified-id="Further-reading-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Further reading</a></span></li><li><span><a href="#Internet-sources-for-the-definitions-used-in-this-notebook:" data-toc-modified-id="Internet-sources-for-the-definitions-used-in-this-notebook:-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Internet sources for the definitions used in this notebook:</a></span></li></ul></li></ul></div>
# %% [markdown]
# # Creating user-defined types
#
# This notebook shows how to use classes to compartmentalize information. The basic
# idea is to produce objects that can contain complex data (called *state*) but
# present a few simple, easily documented methods to access that data.
# %% [markdown]
# ## Types and classes
#
# In python, a type and a class are essentially synonyms.  Consider the following code example:
# %%


class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    def __init__(self, nx, ny, poro, wx, wy):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy


n_x = 20
n_y = 30
poro = 0.4
width_x = 10
width_y = 15
the_problem = Problem_Def(n_x, n_y, poro, width_x, width_y)


# %% [markdown]
# In words, we say that `the_problem` is an **instance** of type `Problem_Def`.  The instance is **constructed** by calling the special
# **instance method** `__init__` which is referred to as the **class constructor**.

# %% [markdown]
# ## Class variables
#
# Suppose we have some constants that we want to share among every
# instance of a class.  We guarantee that every instance has
# the same set of constants by making them **class variables**

# %%
class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    speed_of_light = 3.0e8  # m/s

    def __init__(self, nx, ny, poro, wx, wy):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy


# %% [markdown]
# Note the difference between prob1.wx and prob2.wx:

# %%
width_x = 200.0
prob1 = Problem_Def(n_x, n_y, poro, width_x, width_y)
width_x = 300
prob2 = Problem_Def(n_x, n_y, poro, width_x, width_y)
print(prob1.wx, prob1.speed_of_light, prob2.wx, prob2.speed_of_light)


# %% [markdown]
# ## Instance variables
#
# The whole point of constructing instances is to have them
# carry unique information.  Note that `__init__` has no return
# line.  This is because it doesn't return a value, instead it
# modifies the memory of the specific instance being constructed
# (called `self` ) by setting the instance variables to the values
# specified by the class constructor.  The `__init__` constructor is
# a regular python function, so it can take default values like this:

# %%
class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    speed_of_light = 3.0e8  # m/s

    def __init__(self, nx, ny, poro, wx=10, wy=10):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy


prob3 = Problem_Def(n_x, n_y, poro)
print(prob3.wx)


# %% [markdown]
# ## Instance methods
#
# A class can define functions (called `methods` when used in a class) in
# addition to its constructor.  This essentially solves the problem
# of passing many arguments to a function.  Consider this new
# method:

# %%
class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    speed_of_light = 3.0e8  # m/s

    def __init__(self, nx, ny, poro, wx=10, wy=10):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy

    def critical_coef(self):
        print(
            (
                "inside critical_coef\n"
                "note that I only need self\n"
                "to use all the information inside\n"
                "the instance\n\n"
            )
        )
        crit_num = self.nx * self.wx / self.poro
        return crit_num


prob4 = Problem_Def(n_x, n_y, poro)
crit_condition = prob4.critical_coef()
print(f"crit_condition={crit_condition}")


# %% [markdown]
# ### Passing self to instance methods
#
# Python made the design decision to require that all instance
# methods take self as their first parameter, even though it
# isn't needed when you actually call the method. A language like C++ made
# a different decision -- its version of `self`, called `this`,
# isn't needed in c++ method signatures.   This rationale for this difference is an example of
# this line from the *Zen of Python*:
#
# **Explicit is better than implicit**
#

# %% [markdown]
# ## Your turn
#
# In the cell below add two new instance methods to the
# `Problem_Def` class:
#
# * `to_dict`: a method that returns a dictionary containing the
#   5 data members of the instance
#
# * `from_dict`: a method that takes a dictonary with the five
#   data members and returns an new instance of type `Problem_Def`
#
# * Test that you can **round trip** an instance of your class by
#   saving it as a dict, then using that dict to construct a new
#   class instance
#
# * Note that `from_dict` doesn't need any information from the instance
#   in order to create a new object.  This is outside the scope of
#   this course, but if/when you learn more about object-oriented
#   programming you'll see that `from_dict` is an example of a function that should
#   be written as a class method, not an instance method.

# %%

# %% [markdown]
# ## Solution

# %%
class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    speed_of_light = 3.0e8  # m/s

    def __init__(self, nx, ny, poro, wx=10, wy=10):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy

    def from_dict(self, input_dict):
        nx = input_dict["nx"]
        ny = input_dict["ny"]
        poro = input_dict["poro"]
        wx = input_dict["wx"]
        wy = input_dict["wy"]
        return Problem_Def(nx, ny, poro, wx, wy)

    def to_dict(self):
        out_dict = dict(nx=self.nx, ny=self.ny, poro=self.poro, wx=self.wx, wy=self.wy)
        return out_dict


prob5 = Problem_Def(n_x, n_y, poro, width_x, width_y)
dict5 = prob5.to_dict()
prob6 = prob5.from_dict(dict5)


# %% [markdown]
# ## Summary
#
# * Python uses user-defined types, called classes, to solve the
#   problem of *information hiding*, i.e. organizing information so that
#   it can be compartmentalized, reducing the complexity of
#   code.
#
# * We don't need to use inheritence in this course, but it is a big
#   part of what makes objects useful.  It allows us to extend other
#   peoples classes without touching their original source code.
#   This is called the "open/closed principal", i.e. objects should
#   be open to extension while being closed to modification.

# %% [markdown]
# ## Appendix
#
# ### Further reading
#
# Again, not needed for this course, but useful if you want to understand
# the main parts of python or other object-oriented languages
#
# * [Chapter15 of How to think like a computer scientist](http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html)
#
# * [Module 4 of Python like you mean it](https://www.pythonlikeyoumeanit.com/module_4.html)

# %% [markdown]
# ### Internet sources for the definitions used in this notebook:
#
# From https://docs.python.org/3/tutorial/classes.html
#
# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
#
# From: https://www.tutorialspoint.com/python/python_classes_objects.htm
#
# Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
#
# Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
#
# Instantiation − The creation of an instance of a class.
#
# Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
#
# Data member − A class variable or instance variable that holds data associated with a class and its objects.
#
# Function overloading − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.
#
# Instance variable − A variable that is defined inside a method and belongs only to the current instance of a class.
#
# Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.
#
# Method − A special kind of function that is defined in a class definition.
#
# Object − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.
#
# Operator overloading − The assignment of more than one function to a particular operator.
#
# Creating Classes
# The class statement creates a new class definition. The name of the class immediately
# follows the keyword class followed by a colon as follows:
#
#     class ClassName:
#       "Optional class documentation string"
#        class body
#
# The class has a documentation string, which can be accessed via ClassName.__doc__.
#
# The class body consists of all the component statements defining class members, data attributes and functions.
