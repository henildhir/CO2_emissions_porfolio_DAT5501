# CO2 Emissions per Capita and GDP per Capita – Annual Percentage Change Analysis

This folder fits polynomial trends to historical **CO₂ emissions per capita** for several countries and produces a line chart that shows:

- Past CO2 emissions per capita (historical trend)
- Predicted CO2 emissions per capita for the next 10 years

The output figure is saved as `Co2_emissions_forecast/co2_emissions_forecasting.png`

The main script described here is `co2_emissions_forecast.py`. It produces a forecast figure for the next 10 years for the following cases

1. United Kingdom
2. World (global analysis)
3. India
4. Malawi

## Features

- Reads historical data from `analysis_dataset.csv`
- Converts `Year` to numeric to allow time‑series plotting
- Forecasts CO₂ emissions per capita for
  - United Kingdom
  - World
  - India
  - Malawi
- Uses different polynomial degrees per country (e.g. UK: 2, India: 2, World: 1, Malawi: 1) to better match each historical pattern
- Plots:
  - Solid lines for historical trend
  - Dashed lines for 10‑year forecasts
  - Scatter points for original observations
- Adds labels, grid, legend and a vertical line marking the start of the forecast period

---

## Design Decisions and Performance Justification

### Vectorised numeric operations (NumPy + pandas)
- Training data (`Year`, `CO2 per capita (Trillions)`) is extracted as NumPy arrays and fitted with `np.polyfit` / `np.poly1d`
- These functions operate on whole arrays at once and are implemented in C, which is faster and more scalable than computing polynomial regression inside Python loops

### Per‑country loop with pre‑defined degrees
- A single loop over `countries` applies the same logic to each dataset, while `degrees[country]` provides the appropriate polynomial order
- This keeps the code short and avoids duplicated blocks, while making it easy to add more countries without increasing runtime complexity significantly

### Single figure, multiple lines
- `plt.figure(figsize=(10, 6))` creates a single canvas where all countries’ historical and forecast lines are drawn
- Drawing everything on one figure is more efficient than creating multiple figures and reduces rendering overhead, particularly when more countries or years are added

### Minimal I/O
- The CSV is loaded once and the chart is saved once. All forecasting and plotting is done in memory, which is faster than repeatedly reading/writing intermediate files

---

### Interpretative Insight

The forecast chart allows comparison of how CO2 emissions per capita may evolve in economies at different development stages. For example, if the UK and the World curves start to flatten or decline while India and Malawi continue to rise, this suggests that future global emissions pressure may increasingly come from rapidly developing countries. The visual separation between historical (solid) and forecast (dashed) lines clearly shows where projections begin and helps distinguish model‑based expectations from observed data.

---

## Unit Test

This unit test in file `test_co2_emissions.py `verifies the preprocessing and forecasting pipeline for CO2 emissions data

- `def setUp(self)`
  - Creates a small pandas DataFrame with sample CO2 per capita data, converts the Year column to numeric, and stores it for reuse in all tests

- `test_data_handling_and_types`
  - Ensures the Year column is numeric and contains no missing values. This validates basic data integrity before any modeling

- `test_prepare_country_data_output_types`
  - Uses `prepare_country_data` to filter the dataset for a given country ("World")

- Runs `fit_and_forecast` with a polynomial degree of 2 and validates forecasting output:
  - Forecast arrays have the expected length relative to the training data
  - Historical forecast years do not exceed the max training year, and future forecast years are strictly greater
  - All forecast values are finite (no NaN or inf).
  - These tests collectively confirm that the data pipeline, model preparation, and forecast outputs are structurally correct and numerically sound

---

## Requirements

- latest python version
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `os`