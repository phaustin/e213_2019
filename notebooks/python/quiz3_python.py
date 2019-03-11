# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,python//py:percent
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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Q2:-modify-Problem_Def-to-incorporate-get_spacing-as-an-instance-method" data-toc-modified-id="Q2:-modify-Problem_Def-to-incorporate-get_spacing-as-an-instance-method-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Q2: modify Problem_Def to incorporate get_spacing as an instance method</a></span></li></ul></div>
# %%

class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    nx: int
    ny: int
    poro: float
    wx: float
    wy: float

    def __init__(self, nx, ny, poro, wx, wy):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy


def get_spacing(nx=4, ny=3, poro=0.4, wx=10, wy=20):
    the_prob = Problem_Def(nx, ny, poro, wx, wy)
    delx = the_prob.wx / the_prob.nx
    dely = the_prob.wy / the_prob.ny
    return delx, dely


# %% [markdown]
# ## Q1:  what does the following print?

# %%
print(f"{get_spacing(nx=6)}")


# %% [markdown] {"trusted": false}
# ## Q2: modify Problem_Def to incorporate get_spacing as an instance method
#
#
# that is, create a version of Problem_Def for which the following will work::
#
#     the_instance = Problem_Def()
#     delx, dely = the_instance.get_spacing()
#
# where the new constructor has the signature::
#
#      def __init__(self,nx=4,ny=3,poro=0.4,wx=10,wy=20):
#         ...
#

# %%
class Problem_Def:
    """
    this class holds the specifcation for the domain,
    including the value of the porosity
    """

    nx: int
    ny: int
    poro: float
    wx: float
    wy: float

    def __init__(self, nx=4, ny=3, poro=0.4, wx=10, wy=20):
        self.nx = nx
        self.ny = ny
        self.poro = poro
        self.wx = wx
        self.wy = wy

    def get_spacing(self):
        delx = self.wx / self.nx
        dely = self.wy / self.ny
        return delx, dely


the_instance = Problem_Def()
delx, dely = the_instance.get_spacing()
print(delx, dely)

# %%
