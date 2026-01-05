# CO2 Emissions per Capita vs GDP per Capita – Scatter Plot and Linear Regression Analysis

This folder analyses the historical relationship between **CO2 emissions per capita** and **GDP per capita** for multiple countries and the world. It produces a two-panel figure that shows:

- A scatter plot of CO2 emissions per capita against GDP per capita over the last 10 years for selected countries with distinct colours.
- A linear regression plot for the world data, including the regression line, 95% confidence interval band, and Pearson correlation coefficient.

The output figure is saved as `Co2_emissions_vs_gdp_per_capita/co2_emissions_gdp_per_capita.png`.

The main script producing this visualisation is `co2_emissions_gdp_per_capita.py`.

---

## Features

- Reads the dataset from `analysis_dataset.csv`.
- Automatically creates the folder `Co2_emissions_vs_gdp_per_capita` if it does not exist.
- Filters dataset to the last 10 years of available data.
- Creates a scatterplot of CO2 emissions per capita vs GDP per capita with points coloured by country.
- Highlights specific countries with a custom colour palette:
  - United Kingdom (green)
  - World (red)
  - India (blue)
  - Malawi (orange)
- Computes Pearson correlation coefficient for World data.
- Fits and visualises an Ordinary Least Squares (OLS) linear regression for World data.
- Plots the regression line with a 95% confidence interval band.
- Adds clear axis labels, titles, gridlines, and legends on both plots.
- Annotates the scatter plot with the correlation coefficient.
- Ensures clean plot aesthetics with visible borders.
- Saves the plot as a PNG file in the designated folder.

---

## Design Decisions and Performance Justification

### Use of Vectorised Operations and Statsmodels.

- Data extracted as NumPy arrays for efficient numerical processing and statistical modeling.
- Regression fitted using `statsmodels.api.OLS` for reliable linear regression and confidence intervals.
- Pearson correlation calculated using SciPy for statistical accuracy.

### Clear Two-Panel Layout.

- The left panel provides a categorical scatterplot showing cross-country differences.
- The right panel offers a focused regression analysis for the World dataset.
- Using `plt.subplots(1, 2)` with a fixed figure size creates a concise and readable layout.

### Custom Colour Palette and Transparency.

- Choosing consistent colours for key countries improves interpretability.
- Alpha blending makes overlapping points discernible without overwhelming the plot.

### Efficient File and Folder Handling.

- Creates output folder programmatically if missing, ensuring reproducibility.
- Saves the figure once after all plotting is complete, reducing I/O overhead.

---

## Interpretative Insights

This two-part visualisation helps identify how CO2 emissions relate to national wealth levels over recent years and globally:

- The scatterplot reveals patterns and outliers in emissions relative to GDP per capita across different countries.
- The regression line and confidence band for the World data quantify the positive correlation between economic growth and emissions.
- The annotated Pearson coefficient (`r`) summarises the strength of this linear association.
- Insights from this plot can guide policymakers by showing how emissions scale with wealth and which countries deviate from expected trends.
- Visual separation of countries with distinct colours simplifies comparative analysis between developed (e.g., UK) and developing nations (e.g., Malawi, India).

---

## Requirements

- Latest Python version
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scipy`
  - `statsmodels`
  - `os`