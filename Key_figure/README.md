# CO2 Emissions per Capita Over Time - Line Graph Analysis

This folder visualises the historical trend of **CO2 emissions per capita (tonnes)** for multiple countries from 1980 onwards. It produces a time series line plot with distinct markers and colours for each country, highlighting emission changes over time. The plot also marks the significant historical event of the **2015 Paris Agreement** with a vertical dashed line.

The output figure is saved as `Key figure/key_figure.png`.

The main script responsible for this visualisation is `key_figure.py`.

---

## Features

- Reads data from `analysis_dataset.csv`
- Plots CO2 emissions per capita over time using Seaborn’s `lineplot`
- Displays emissions trends for multiple countries distinguished by colour and markers:
  - United Kingdom
  - World
  - India
  - Malawi
- Adds clear axis labels, plot title, and gridlines with moderate transparency
- Draws a vertical dashed line at year 2015 representing the Paris Agreement milestone
- Customises the legend to reorder entries to match narrative/report order
- Saves the resulting figure as a PNG to a programmatically created folder `Key figure`

---

## Design Decisions and Performance Justification

### Efficient Use of Seaborn and Matplotlib

- The choice of `sns.lineplot` simplifies plotting multiple time series grouped by country
- Line markers and linewidth are adjusted to improve readability of trends and data points

### Explicit Legend Management

- Programmable legend ordering ensures logical narrative flow for report readers
- Extracting and rebuilding handles and labels avoids manual legend entry duplication

### Highlighting a Key Historical Event

- Adding a vertical line at 2015 (Paris Agreement) visually connects emissions trends with policy milestones
- Dashed grey line keeps the annotation visible

### Folder Creation and File Saving

- Output folder is created automatically if missing, ensuring reproducibility
- Single save operation after full figure creation minimises I/O overhead

---

## Interpretative Insights

This timeline plot clearly communicates the evolving CO2 emissions landscape across different regions:

- Enables comparison of emissions trajectories since 1980 among developed (UK), global aggregate (World), and developing countries (India, Malawi)
- The Paris Agreement marker helps correlate emissions changes with international climate policy efforts
- Temporal trends highlight where emissions growth is accelerating or plateauing, informing climate strategy and risk assessment
- Differentiated colours and markers allow quick identification and comparison of country-level patterns

---

## Unit Test

This unit test in python file `test_key_figure.py` validates the structure and data types of the analysis dataset before it is used elsewhere

- `def setUp(self)`
  - Creates a small sample DataFrame with columns: "Country Name", "Year", "CO2 per capita (Trillions)", and "GDP" for two countries and several years

- `test_sample_data_structure_and_dtypes`
  - Ensures basic dataset integrity:
    - Required columns (Country Name, Year, CO2 per capita (Trillions)) all exist
    - Year values are integers
    - CO2 per capita (Trillions) values are numeric
    - Country Name values are strings/objects
    - None of the required fields contain null values

- `test_column_dtypes_are_correct`
  - Re-checks column types in a focused way:
  - Year column must be integer dtype
  - CO2 per capita (Trillions) must be numeric
  - Country Name must be string/object

These tests are crucial to ensure the integrity of the dataset passing through and ensuring correct outputs

---

## Requirements

- Latest Python version
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `os`