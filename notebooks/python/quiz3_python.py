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
