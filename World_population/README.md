# World Population Dataset Cleaning

This folder contains the original World Population dataset (`world_population.csv`) along with the cleaned and reformatted dataset saved as `new_world_population.csv`. The main script `world_population.py` processes this data to provide a more analysis-ready format focused on selected countries and years.

---

## Features

- Reads the original dataset `world_population.csv` using pandas, skipping the first 4 metadata rows as they contain no data.
- Filters the data to include only the following countries:  
  - United Kingdom  
  - India  
  - Malawi  
  - World (aggregate)
- Selects only the year columns from 1980 onwards, focusing on recent data.
- Retains the `"Country Name"` column and the filtered year columns.
- Converts the dataset from wide format (one column per year) to long format with three columns:  
  - `"Country Name"`  
  - `"Year"`  
  - `"Population"`  
- Sorts the data by `"Country Name"` and `"Year"` in ascending order for easier analysis.
- Validates and converts the `"Year"` column to integer type.
- Saves the cleaned and transformed dataset to `new_world_population.csv` without the index column for simplicity.

---

## About the CSV Files

### Original Dataset: `world_population.csv`

- Contains 4 initial metadata rows that are skipped during loading.
- Wide format with separate columns for each year starting from 1960.
- Covers a comprehensive set of countries and regions worldwide.
- Reports total population counts.
- Includes some missing data cells.

### Cleaned Dataset: `new_world_population.csv`

- Filters to keep only select countries.
- Includes only data from 1980 onward.
- Data shown in long format ideal for time series and statistical analysis.
- Each row contains one country-year-population record.

---

## Design Decisions and Performance Justification

### Skipping Metadata

- Initial metadata rows are skipped on CSV loading to streamline data processing.

### Country and Year Filtering

- Limits data to relevant countries and recent years reduce unnecessary processing and file size.

### Wide to Long Format Conversion

- Using `pandas.melt` facilitates reshaping to an analysis-friendly format widely supported by visualisation and modeling tools.
- Vectorised transformation is efficient and scales well.

### Sorting and Data Type Consistency

- Sorted data improves readability and accelerates grouping/aggregation operations.
- Explicit integer type enforcement on `Year` minimises future errors.

### Clean CSV Export

- Saving without indices creates standardised files that are easier to handle in various environments.

---

## Interpretative Insights

This cleaned dataset standardises population data for key countries and global totals:

- The focus on 1980+ data aligns with most contemporary demographic and economic studies.
- The long format supports flexible queries like growth rates, country comparisons, and integration with other datasets (GDP, emissions).
- The structured and filtered data strongly supports reliable visualisations and forecasting.

---

## Requirements

- Python (latest recommended version).
- Library:
  - `pandas`