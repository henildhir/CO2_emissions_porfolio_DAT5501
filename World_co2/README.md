# CO2 Emissions per Capita Dataset Cleaning

This folder contains the original CO2 emissions dataset (`co2-emissions-per-capita.csv`) and the cleaned and reformatted new dataset (`new_co2_emissions_per_capita.csv`). The main script `co2_emissions.py` reads, filters, renames columns, and saves a cleaned version of the data for easier downstream analysis.

---

## Features

- Reads the original raw dataset from `World_co2/co2-emissions-per-capita.csv`.
- Filters data to retain records from **1980 and later** only, focusing on the modern period for meaningful analysis.
- Renames ambiguous column headers:
  - `"Entity"` to `"Country Name"`
  - `"Annual CO₂ emissions (per capita)"` to `"CO2 per capita"`
- Saves the cleaned dataset to a new CSV file `World_co2/new_co2_emissions_per_capita.csv` without the index column.
- Enables simplified and standardised data access for future visualisation and analysis steps.

---

## Design Decisions and Performance Justification

### Minimal and Clear Data Transformation

- Using pandas for efficient CSV reading, filtering, renaming, and writing operations.
- Filtering by the `"Year"` column early reduces data volume and speeds up subsequent processing.
- Column renaming ensures consistent and descriptive names, improving code readability and maintainability.

### Simple File I/O Workflow

- Original dataset is preserved unchanged in the `World_co2` folder.
- New cleaned dataset is saved alongside in the same folder, enabling version control and traceability.
- Using `index=False` in `to_csv` avoids unnecessary CSV index values.

---

### Interpretative Insights

This preprocessing step streamlines the CO2 emissions per capita data for improved analysis:

- By restricting to 1980 and onwards, it reflects more relevant recent trends and policy effects.
- Clear and uniform column names reduce confusion and error potential in scripts.
- Having a clean, focused dataset facilitates consistent input for plotting, regression models, or forecasting.
- Maintaining both original and cleaned datasets supports transparency and repeatability.

---

## Requirements

- Latest Python version.
- Library:
  - `pandas`