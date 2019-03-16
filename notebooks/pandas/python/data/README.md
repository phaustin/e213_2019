**File:** `weather_YVR.csv`

**Data source:** http://climate.weather.gc.ca/historical_data/search_historic_data_e.html

**Description:** Environment Canada daily weather data for Vancouver Airport station 1938-2017. For details of data processing, see the notebooks in the `wrangling-env-canada` folder.

---

**File:** `gapminder_world_data_2018.csv`

**Data sources**:
- Original data: https://www.gapminder.org/about-gapminder/
- Merged data: https://github.com/UofTCoders/2018-09-10-utoronto

**Description:** Gapminder data about countries around the world, for the year 2018.

| Column                | Description                        |
|-----------------------|------------------------------------|
| country               | Country name                       |
| population            | Population in the country |
| region                | Continent the country belongs to   |
| sub_region            | Sub regions as defined by          |
| income_group          | Income group [as specified by the world bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/378833-how-are-the-income-group-thresholds-determined)                  |
| life_expectancy       | The average number of years a newborn child would <br>live if mortality patterns were to stay the same |
| gdp_per_capita         | GDP per capita (in USD) adjusted <br>for differences in purchasing power|
| children_per_woman    | Number of children born to each woman|
| child_mortality       | Deaths of children under 5 years <br>of age per 1000 live births|
| pop_density           | Average number of people per km$^2$|

---

**File:** `country_capitals.csv`

**Data source:** http://techslides.com/list-of-countries-and-capitals

**Description:** Latitudes and longitudes of capital cities for countries around the world. Since the CSV file linked on the website had some formatting issues that interfered with data parsing, I copied the HTML table from the website into a spreadsheet to generate the CSV file, and also removed any rows with "N/A" listed for the capital city.