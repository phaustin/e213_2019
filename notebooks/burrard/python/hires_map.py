# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Read-the-geotiff-with-rasterio" data-toc-modified-id="Read-the-geotiff-with-rasterio-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Read the geotiff with rasterio</a></span></li><li><span><a href="#Locate-UBC-on-the-map" data-toc-modified-id="Locate-UBC-on-the-map-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Locate UBC on the map</a></span><ul class="toc-item"><li><span><a href="#Mapped-image-with-no-coastline" data-toc-modified-id="Mapped-image-with-no-coastline-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Mapped image with no coastline</a></span></li><li><span><a href="#Read-the-shape-file-and-add-the-coastline-to-the-image" data-toc-modified-id="Read-the-shape-file-and-add-the-coastline-to-the-image-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Read the shape file and add the coastline to the image</a></span></li></ul></li></ul></div>
# %% [markdown]
# # Introduction
#
# Below we read in the small Vancouver image we wrote out in the image_zoom notebook, and put it on a map with a UTM-10N crs.  We then add a high resolution coastline read from the openstreetmap coastline database.
# %%
import pprint

import cartopy
import context
import rasterio
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from pyproj import Proj
from pyproj import transform as proj_transform


# %% [markdown]
# # Read the geotiff with rasterio

# %%
tif_filename = context.root_dir / "small_file.tiff"
with rasterio.open(tif_filename) as raster:
    affine_transform = raster.transform
    crs = raster.crs
    profile = raster.profile
    refl = raster.read(1)
refl.shape

# %%
print(f"profile: \n{pprint.pformat(profile)}")

# %% [markdown]
# # Locate UBC on the map
#
# We need to project the center of campus from lon/lat to UTM 10N x,y using pyproj.transform

# %%
p_utm = Proj(crs)
p_latlon = Proj(proj="latlong", datum="WGS84")
ubc_lon = -123.2460
ubc_lat = 49.2606
ubc_x, ubc_y = proj_transform(p_latlon, p_utm, ubc_lon, ubc_lat)
height, width = refl.shape
ubc_ul_xy = affine_transform * (0, 0)
ubc_lr_xy = affine_transform * (width, height)
ubc_ul_xy, ubc_lr_xy

# %% [markdown]
# ## Mapped image with no coastline
#
# Sanity check to make sure we've got the right image

# %%
vmin = 0.0
vmax = 0.5
the_norm = Normalize(vmin=vmin, vmax=vmax, clip=False)
palette = "viridis"
pal = plt.get_cmap(palette)
pal.set_bad("0.75")  # 75% grey for out-of-map cells
pal.set_over("w")  # color cells > vmax red
pal.set_under("k")  # color cells < vmin black
cartopy_crs = cartopy.crs.epsg(crs.to_epsg())
fig, ax = plt.subplots(1, 1, figsize=[15, 25], subplot_kw={"projection": cartopy_crs})
image_extent = [ubc_ul_xy[0], ubc_lr_xy[0], ubc_lr_xy[1], ubc_ul_xy[1]]
ax.imshow(
    refl,
    origin="upper",
    extent=image_extent,
    transform=cartopy_crs,
    cmap=pal,
    norm=the_norm,
)
ax.plot(ubc_x, ubc_y, "ro", markersize=25)
ax.set_extent(image_extent, crs=cartopy_crs)

# %% [markdown]
# ## Read the shape file and add the coastline to the image
#
# Note that PlateCarree is another name for WGS84 datum, simple lat/lon which is the projection of the coastlines-split-4326 shapefile.

# %%
from cartopy.io import shapereader

shape_project = cartopy.crs.PlateCarree()
shp = shapereader.Reader(str(context.coastlines_dir / "lines.shp"))
for record, geometry in zip(shp.records(), shp.geometries()):
    ax.add_geometries(
        [geometry], shape_project, facecolor="none", edgecolor="red", lw=2
    )
display(fig)

# %%
fig.savefig("ubc_map.png")
