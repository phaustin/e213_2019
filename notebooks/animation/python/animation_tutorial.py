# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0-rc4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown]
# # Animation tutorial
#
# Source:  [Louis Tiao blogpost](http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-as-interactive-javascript-widgets/)
#
# %% [markdown]
# A while back I wrote a post on [Embedding Matplotlib Animations in Jupyter Noteboks](../embedding-matplotlib-animations-in-jupyter-notebooks), which became surprisingly popular. It outlined how to render [Matplotlib animations](https://matplotlib.org/api/animation_api.html) in the [Jupyter Notebook](http://jupyter.org/), by encoding it as a HTML5 video using the `to_html5_video` method introduced in the release of [Matplotlib 1.5](https://matplotlib.org/users/prev_whats_new/whats_new_1.5.html#display-hook-for-animations-in-the-ipython-notebook).
#
# Three years have gone by since then, and much has changed in the world of open-source scientific Python. [Matplotlib 2.1](https://matplotlib.org/users/prev_whats_new/whats_new_2.1.0.html#interactive-js-widgets-for-animation) was released towards the end of last year, and was the first release with major new features since 1.5. Among many significant enhancements, the release included the merge of Jake Vanderplas' [JSAnimation](https://github.com/jakevdp/JSAnimation) package, a tool for rendering Matplotlib animations as interactive JavaScript widgets.
#
# With this awesome addition, encapsulated in the new `to_jshtml` method,
# we are now able to embed an interactive JavaScript widget for playback of Matplotlib animations directly inside a Jupyter Notebook.
#
# In this post, we demonstrate how to use this method on the same example animation from my previous post, which was originally derived from an even earlier [post by Jake VanderPlas](http://jakevdp.github.io/blog/2013/05/12/embedding-matplotlib-animations/).
#
# <!-- TEASER_END -->
# %%
# %matplotlib inline
# %%
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib import animation
from matplotlib import rc

# %% [markdown]
# ## Creating the Animation
#
# First set up the figure, the axis, and the plot element we want to animate:

# %%
fig, ax = plt.subplots()

ax.set_xlim((0, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)


# %% [markdown]
# Define the initialization function, which plots the background of each frame:

# %%
def init():
    line.set_data([], [])
    return (line,)


# %% [markdown]
# Define the animation function, which is called for each new frame:

# %%
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return (line,)


# %% [markdown]
# Compile the animation. Setting `blit=True` will only re-draw the parts that have changed.

# %%
anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=100, interval=20, blit=True
)

# %% [markdown]
# ## Displaying the Animation
#
# Now we can display this `anim` object using IPython's HTML display method. For comparison, we first encode the animation and render it as an HTML5 video using the `to_html5_video` method, as covered in my previous post:

# %%
HTML(anim.to_html5_video())

# %% [markdown]
# Now to create an interactive JavaScript widget using the `to_jshtml` method:

# %%
HTML(anim.to_jshtml())

# %% [markdown]
# It's that simple!

# %% [markdown]
# ## Setting interactive Javascript widgets as the default HTML representation of Animation objects
#
# To support inline display of animations in the notebook, an [Animation](http://matplotlib.org/api/animation_api.html#matplotlib.animation.Animation) object comes with a `_repr_html_` method. However, it returns `None` by default:

# %%
# Initialize the Animation object again
anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=100, interval=20, blit=True
)

# %%
anim._repr_html_() is None

# %% [markdown]
# This means it won't automatically display the animation when referenced. Instead, it will just display its default HTML representation, which is just a string:

# %%
anim

# %% [markdown]
# To make the interactive JavaScript widget the default HTML representation, we just have to set the `animation.html` rc parameter, which now supports the values `none`, `jshtml` and `html5`. The default is `none`, performing no display. We simply need to set it to `jshtml`:

# %%
rc("animation", html="jshtml")

# %% [markdown]
# Note that this is equivalent to (and, in my opinion, neater than):
#
# ```Python
#  rcParams['animation.html'] = 'jshtml'
# ```
#
# Now we can just reference the Animation instance and display the widget inline:

# %% {"scrolled": false}
anim

# %% [markdown]
# ## Additional Resources
#
# Check out Jake's post titled [A Javascript Viewer for Matplotlib Animations](https://jakevdp.github.io/blog/2013/05/19/a-javascript-viewer-for-matplotlib-animations/) from 2013 for more information about this widget. I would also like to highlight the following StackOverflow  answers wherein I first learned about this new feature:
#
# - https://stackoverflow.com/a/43447370/1924843
# - https://stackoverflow.com/a/46878531/1924843
#
# To receive updates about more posts like this, follow me on [Twitter](https://twitter.com/louistiao) or [GitHub](https://github.com/ltiao)!
