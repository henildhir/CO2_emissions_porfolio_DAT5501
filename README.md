# Carbon Dioxide per Capita Emissions and GDP per Capita Analysis Portfolio

## Project Overview and Business Problem

This project investigates the critical relationship between CO2 emissions, economic development, and population growth to support informed decision-making on climate policy and sustainable development.  

The primary business problem addressed is understanding how CO2 emissions per capita evolve with economic growth (GDP per capita) and demographic changes across different countries and global aggregates. Identifying these patterns and forecasting future trends helps stakeholders—policy makers, environmental agencies, and businesses—to evaluate the effectiveness of climate agreements, anticipate emissions trajectories, and design targeted interventions that balance economic growth with environmental sustainability.

This portfolio accompanies a detailed report which contextualises these analyses, highlights key insights, and discusses implications for international climate strategy.

---

## Project Structure and Folder Descriptions

The project is organised into thematic folders containing datasets, scripts, and visualisations focused on various aspects of CO2 emissions and socioeconomic metrics:

### 1. `Key figure`  
Produces key visualisations tracking CO2 emissions per capita over time, annotated with significant historical events like the 2015 Paris Agreement, to frame emissions trends in policy context

### 2. `Annual_%_change`  
Contains scripts and outputs analysing yearly percentage changes in CO2 emissions per capita for specified countries, providing insights into temporal trends and volatility

### 3. `Co2_emissions_forecast`  
Focuses on forecasting CO2 emissions per capita over the next decade using polynomial trend fitting for countries like the United Kingdom, India, Malawi, and global data ("World")

### 4. `Co2_emissions_vs_gdp_per_capita`  
Analyses the correlation and relationship between CO2 emissions per capita and GDP per capita through scatterplots and linear regression models, highlighting economic-environmental dynamics

### 5. `World_co2`  
Includes the original and cleaned CO2 emissions per capita datasets spanning multiple decades, along with scripts for data preparation and cleaning

### 6. `World_gdp`  
Holds original and prepared GDP datasets with time series data for selected countries, facilitating economic growth analysis in conjunction with emissions

### 7. `World_population`  
Contains population datasets, both raw and cleaned, enabling demographic context to be integrated into emissions and economic analyses

---

## Central Dataset: `analysis_dataset.csv`

At the core of this portfolio lies the `analysis_dataset.csv`, a dataset combining CO2 emissions, GDP per capita, and population indicators for selected countries and the world. This unified dataset serves as the foundational data source across multiple analysis scripts and visualisations, ensuring a consistent base for comparative and forecasting studies.

Supporting scripts like `analysis_dataset.py` perform data extraction, cleaning, and preparation steps to maintain data integrity and usability across the project.

---

## Interpretative Insights

Within each subfolder, an interpretative insight section is included at the bottom of the README file. This section provides additional detail and context about the graphs, linking them to historical events and geopolitical factors. These insights help synthasise and support the overall report's conclusions.
---

## Unit Test

This unit test in python file `` checks that the core analysis dataset has the expected dataframe and data types.

-`def setUp(self)`
  - Builds a small DataFrame with `Country Name`, `Year`, `CO2 per capita (Trillions)`, and `GDP` for two countries and several years

- `test_required_columns_present_and_count`
  - Verifies that the mandatory columns `Year`, `Country Name`, and `CO2 per capita (Trillions)` are present, and that the dataset has at least these three columns (additional columns are allowed)

- `test_column_dtypes_are_correct`
  - Ensures:
    - `Year` is integer-like
    - `CO2 per capita (Trillions)` is numeric (int or float)
    - `Country Name` is a string/object column

Unit tests like these are important in this project because they guarantee that data cleaning and transformation steps behave as expected, and they catch datframes or type issues early before they can corrupt analyses, visualisations, or forecasting results.

---

## Conclusion

This comprehensive project portfolio integrates diverse data sources and analytical techniques to explore how global and national CO2 emissions relate to economic and demographic factors. It provides valuable insights for environmental policy and sustainable development strategy formulation.