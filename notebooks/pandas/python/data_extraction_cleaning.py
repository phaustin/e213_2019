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
#       jupytext_version: 1.0.3
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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Exploring-Environment-Canada-Weather-Data-with-Python-and-Jupyter-Notebooks" data-toc-modified-id="Exploring-Environment-Canada-Weather-Data-with-Python-and-Jupyter-Notebooks-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exploring Environment Canada Weather Data with Python and Jupyter Notebooks</a></span><ul class="toc-item"><li><span><a href="#Updates:" data-toc-modified-id="Updates:-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Updates:</a></span></li></ul></li><li><span><a href="#Part-I:-Data-Extraction-&amp;-Cleaning" data-toc-modified-id="Part-I:-Data-Extraction-&amp;-Cleaning-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Part I: Data Extraction &amp; Cleaning</a></span><ul class="toc-item"><li><span><a href="#Function-for-calling-the-Environment-Canada-API" data-toc-modified-id="Function-for-calling-the-Environment-Canada-API-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Function for calling the Environment Canada API</a></span></li><li><span><a href="#How-to-download-data-between-a-specified-date-range" data-toc-modified-id="How-to-download-data-between-a-specified-date-range-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>How to download data between a specified date range</a></span></li><li><span><a href="#Plot-average-data-and-a-rolling-average" data-toc-modified-id="Plot-average-data-and-a-rolling-average-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Plot average data and a rolling average</a></span></li><li><span><a href="#Fix-missing-data-points-by-interpolation" data-toc-modified-id="Fix-missing-data-points-by-interpolation-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Fix missing data points by interpolation</a></span></li><li><span><a href="#For-convenience:-Scrape-StationIDs-to-lookup-cities" data-toc-modified-id="For-convenience:-Scrape-StationIDs-to-lookup-cities-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>For convenience: Scrape StationIDs to lookup cities</a></span></li><li><span><a href="#Parsing-the-Environment-Canada-page-with-Beautiful-Soup" data-toc-modified-id="Parsing-the-Environment-Canada-page-with-Beautiful-Soup-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Parsing the Environment Canada page with Beautiful Soup</a></span></li><li><span><a href="#Filtering-Station-Data" data-toc-modified-id="Filtering-Station-Data-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Filtering Station Data</a></span></li><li><span><a href="#Looking-up-stations" data-toc-modified-id="Looking-up-stations-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Looking up stations</a></span></li><li><span><a href="#Download-Weather-Data" data-toc-modified-id="Download-Weather-Data-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Download Weather Data</a></span></li><li><span><a href="#Let's-plot-the-data-for-Whistler" data-toc-modified-id="Let's-plot-the-data-for-Whistler-2.10"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>Let's plot the data for Whistler</a></span></li><li><span><a href="#How-to-fix-missing-data-points-with-interpolation" data-toc-modified-id="How-to-fix-missing-data-points-with-interpolation-2.11"><span class="toc-item-num">2.11&nbsp;&nbsp;</span>How to fix missing data points with interpolation</a></span></li></ul></li><li><span><a href="#Exporting-Data" data-toc-modified-id="Exporting-Data-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Exporting Data</a></span></li></ul></div>
# %% [markdown]
# # Exploring Environment Canada Weather Data with Python and Jupyter Notebooks
#
# - By Siang Lim (wow@siang.ca) - December 3rd 2017
#
# This notebook demonstrates how to download Environment Canada's weather data using Python with popular data analysis libraries like pandas and Beautiful Soup. Read the accompanying blog post [here](https://www.ubcenvision.com/blog/2017/11/30/jupyter-part1.html) on the [UBC Envision](https://www.ubcenvision.com) website for more details.
#
# To run this notebook on the cloud, use [Binder](https://mybinder.org/) or the [Syzygy](http://intro.syzygy.ca/getting-started/) platform.
#
# Feel free to use, copy, paste, modify or distribute this notebook however you wish.
#
# *These examples are provided as-is with no guarantee that they will work in the future if Environment Canada modifies their API.*
#
# ## Updates:
# - October 4th 2018: Environment Canada API updated, we need to skip 15 rows instead of 16. `getHourlyData()` updated with skiprows=15
# %% [markdown]
# # Part I: Data Extraction & Cleaning
# %%
import datetime as dt
import re

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from bs4 import BeautifulSoup
from dateutil import rrule
from fuzzywuzzy import fuzz


# %% [markdown]
# ## Function for calling the Environment Canada API

# %%
# Call Environment Canada API
# Returns a dataframe of data
def getHourlyData(stationID, year, month):
    base_url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
    query_url = "format=csv&stationID={}&Year={}&Month={}&timeframe=1".format(
        stationID, year, month
    )
    api_endpoint = base_url + query_url
    return pd.read_csv(api_endpoint, skiprows=15)


# %% [markdown]
# ## How to download data between a specified date range

# %%
stationID = 51442
start_date = dt.datetime.strptime("Jun2015", "%b%Y")
end_date = dt.datetime.strptime("Jun2016", "%b%Y")

frames = []
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    df = getHourlyData(stationID, dt.year, dt.month)
    frames.append(df)

weather_data = pd.concat(frames)
weather_data["Date/Time"] = pd.to_datetime(weather_data["Date/Time"])
weather_data["Temp (°C)"] = pd.to_numeric(weather_data["Temp (°C)"])

# %% [markdown]
# ## Plot average data and a rolling average
# Notice the broken lines, they indicate missing data points.

# %%
sns.set_style("whitegrid")
fig = plt.figure(figsize=(15, 5))
plt.plot(
    weather_data["Date/Time"], weather_data["Temp (°C)"], "-o", alpha=0.8, markersize=2
)
plt.plot(
    weather_data["Date/Time"],
    weather_data["Temp (°C)"].rolling(window=250, center=False).mean(),
    "-k",
    alpha=1.0,
)
plt.ylabel("Temp (°C)")
plt.xlabel("Time")

# %% [markdown]
# ## Fix missing data points by interpolation

# %%
# Don't really care about accuracy right now, use simple linear interpolation
weather_data["Temp (°C)"] = weather_data["Temp (°C)"].interpolate()

# %% [markdown]
# Then plot the data again:

# %% {"scrolled": true}
sns.set_style("whitegrid")
fig = plt.figure(figsize=(15, 5))
plt.plot(
    weather_data["Date/Time"], weather_data["Temp (°C)"], "-o", alpha=0.8, markersize=2
)
plt.plot(
    weather_data["Date/Time"],
    weather_data["Temp (°C)"].rolling(window=250, center=False).mean(),
    "-k",
    alpha=1.0,
)
plt.ylabel("Temp (°C)")
plt.xlabel("Time")

# %% [markdown]
# ## For convenience: Scrape StationIDs to lookup cities
# This section demonstrates a simple Python script for scraping StationIDs from Environment Canada using Beautiful Soup.
#
# The stationIDs are provided by province in this Environment Canada [page](http://climate.weather.gc.ca/historical_data/search_historic_data_e.html). Environment Canada limits the number of rows in the search results to 100 entries. This script loops through all pages and grabs the StationID, Station Name, Intervals and Year Range.
#

# %%
# Specify Parameters
province = "BC"  # Which province to parse?
start_year = "2006"  # I want the results to go back to at least 2006 or earlier
max_pages = (
    5
)  # Number of maximum pages to parse, EC's limit is 100 rows per page, there are about 500 stations in BC with data going back to 2006

# Store each page in a list and parse them later
soup_frames = []

for i in range(max_pages):
    startRow = 1 + i * 100
    print("Downloading Page: ", i)

    base_url = "http://climate.weather.gc.ca/historical_data/search_historic_data_stations_e.html?"
    queryProvince = "searchType=stnProv&timeframe=1&lstProvince={}&optLimit=yearRange&".format(
        province
    )
    queryYear = "StartYear={}&EndYear=2017&Year=2017&Month=5&Day=29&selRowPerPage=100&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongMin=0&txtCentralLongSec=0&".format(
        start_year
    )
    queryStartRow = "startRow={}".format(startRow)

    response = requests.get(
        base_url + queryProvince + queryYear + queryStartRow
    )  # Using requests to read the HTML source
    soup = BeautifulSoup(response.text, "html.parser")  # Parse with Beautiful Soup
    soup_frames.append(soup)

# %% [markdown]
# ## Parsing the Environment Canada page with Beautiful Soup

# %%
# Empty list to store the station data
station_data = []

for soup in soup_frames:  # For each soup
    forms = soup.findAll(
        "form", {"id": re.compile("stnRequest*")}
    )  # We find the forms with the stnRequest* ID using regex
    for form in forms:
        try:
            # The stationID is a child of the form
            station = form.find("input", {"name": "StationID"})["value"]

            # The station name is a sibling of the input element named lstProvince
            name = (
                form.find("input", {"name": "lstProvince"})
                .find_next_siblings("div")[0]
                .text
            )

            # The intervals are listed as children in a 'select' tag named timeframe
            timeframes = form.find("select", {"name": "timeframe"}).findChildren()
            intervals = [t.text for t in timeframes]

            # We can find the min and max year of this station using the first and last child
            years = form.find("select", {"name": "Year"}).findChildren()
            min_year = years[0].text
            max_year = years[-1].text

            # Store the data in an array
            data = [station, name, intervals, min_year, max_year]
            station_data.append(data)
        except IndexError:
            pass

# Create a pandas dataframe using the collected data and give it the appropriate column names
stations_df = pd.DataFrame(
    station_data, columns=["StationID", "Name", "Intervals", "Year Start", "Year End"]
)
stations_df.head()

# %% [markdown]
# ## Filtering Station Data
# For example, to show only stations with hourly data, use the map() function.

# %%
# Show only data with hourly intervals
hourly_stations = stations_df.loc[stations_df["Intervals"].map(lambda x: "Hourly" in x)]
hourly_stations.head()

# %% [markdown]
# ## Looking up stations
# Now that we have the stationIDs, we can use Fuzzywuzzy and fuzzy string matching to lookup the station IDs with the city names. Here are 2 examples

# %%
# Find the stations that are in Whistler
string = "Whistler"
tolerance = 90

hourly_stations[
    hourly_stations["Name"].apply(lambda x: fuzz.token_set_ratio(x, string)) > tolerance
]

# %%
# Find the stations that are in Vancouver
string = "Vancouver"
tolerance = 90

hourly_stations[
    hourly_stations["Name"].apply(lambda x: fuzz.token_set_ratio(x, string)) > tolerance
]

# %% [markdown]
# ## Download Weather Data
# Now that we know the station ID, we can use our getHourlyData() function to call the Environment Canada API with the station ID that we found.
#
# Here's how we get Whistler data from November 2016 to November 2017:

# %%
# Get Whistler weather data for November 2016 to November 2017
stationID = 43443
start_date = dt.strptime("Nov2016", "%b%Y")
end_date = dt.strptime("Nov2017", "%b%Y")

frames = []
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
    df = getHourlyData(stationID, dt.year, dt.month)
    frames.append(df)

whistler = pd.concat(frames)
whistler["Date/Time"] = pd.to_datetime(whistler["Date/Time"])
whistler["Temp (°C)"] = pd.to_numeric(whistler["Temp (°C)"])
whistler.head()

# %% [markdown]
# ## Let's plot the data for Whistler

# %%
sns.set_style("whitegrid")
fig = plt.figure(figsize=(15, 5))
plt.plot(whistler["Date/Time"], whistler["Temp (°C)"], "-o", alpha=0.8, markersize=2)
plt.plot(
    whistler["Date/Time"],
    whistler["Temp (°C)"].rolling(window=250, center=False).mean(),
    "-k",
    alpha=1.0,
)
plt.ylabel("Temp (°C)")
plt.xlabel("Time")

# %% [markdown]
# ## How to fix missing data points with interpolation

# %%
# Find the number of rows with a 'M' for missing temperature flag, or NaN for the actual temperature value
print(
    "Missing data rows: ",
    whistler.loc[
        (~whistler["Temp Flag"].isnull()) | (whistler["Temp (°C)"].isnull())
    ].shape[0],
)

# Do interpolation
whistler["Temp (°C)"] = whistler["Temp (°C)"].interpolate()

# Did we fix everything?
print("Missing data rows: ", whistler.loc[(whistler["Temp (°C)"].isnull())].shape[0])

# %% [markdown]
# Re-plot the data

# %% {"scrolled": true}
sns.set_style("whitegrid")
fig = plt.figure(figsize=(15, 5))
plt.plot(whistler["Date/Time"], whistler["Temp (°C)"], "-o", alpha=0.8, markersize=2)
plt.plot(
    whistler["Date/Time"],
    whistler["Temp (°C)"].rolling(window=250, center=False).mean(),
    "-k",
    alpha=1.0,
)
plt.ylabel("Temp (°C)")
plt.xlabel("Time")

# %% [markdown]
# # Exporting Data

# %% [markdown]
# We'll export the dataframes in CSV format so we don't have to re-download the data every time we restart Jupyter:

# %%
stations_df.to_csv("stations.csv")
whistler.to_csv("whistler.csv")
