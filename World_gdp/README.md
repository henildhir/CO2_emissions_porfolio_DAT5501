# World GDP Data Cleaning and Transformation

This folder contains the original World GDP dataset (`world_gdp.csv`) along with the cleaned and reformatted version saved as `new_world_gdp.csv`. The core script `world_gdp_cleaning.py` processes this data to produce a more analysis-ready format focused on select countries from 1980 onwards.

---

## Features

- Reads the original dataset `world_gdp.csv` using pandas, skipping the first 4 metadata rows that do not contain data.
- Filters data to include only the following countries:  
  - United Kingdom  
  - India  
  - Malawi  
  - World (aggregate)
- Selects only year columns for 1980 and later, removing older data to focus on modern historical period.
- Transforms the dataset from a wide format to a long format with three columns:  
  - `Country Name`  
  - `Year`  
  - `GDP`  
- Sorts the resulting data by `Country Name` and `Year` in ascending order for easier analysis.
- Converts year column data type to integer for consistency.
- Saves the cleaned dataset to `new_world_gdp.csv` without the index column for simpler downstream usage.

---

## Design Decisions and Performance Justification

### Skipping Metadata Rows

- Skipping the initial 4 rows on reading the CSV avoids processing non-data text, simplifying downstream handling.

### Filtering Relevant Countries Early

- Restricting to countries of interest minimises data size and speeds up processing.

### Selecting Years from 1980 Onwards

- Modern historical period is more useful and relevant for analysis and visualisation.

### Converting Wide to Long Format

- Long format is preferred for many pandas and visualisation libraries to process time series naturally.
- `pd.melt()` operation is vectorised and efficient on dataframes.

### Sorting and Type Conversion

- Sorting ensures consistent order for plotting and table generation.
- Explicit type casting prevents data inconsistencies or parsing errors later.

### Saving without Index Column

- Produces cleaner CSV files easier to share and read by other tools.

---

## Interpretative Insights

This preprocessing step prepares World GDP data for meaningful trend analysis:

- By focusing on key countries and the World aggregate, the dataset supports comparative economic analysis.
- The limitation to post-1980 data aligns with many climate and economic studies focusing on recent decades.
- Long format enables flexible slicing, aggregation, and joins with other datasets (e.g., emissions).
- Clean, standardised data lays the foundation for accurate visualisations and statistical modeling, enhancing insight reliability.

---

## Requirements

- latest python version
- Libraries:
  - `pandas`