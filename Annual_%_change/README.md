# CO2 Emissions per Capita and GDP per Capita – Annual Percentage Change Analysis

This project analyses how **World CO2 emissions per capita** and **World GDP per capita** have changed annually since 1980, with a particular focus on the **2008 financial crisis**. The analysis is part of a broader business problem: understanding how global economic shocks affect emissions, which is relevant for firms and investors exposed to carbon‑intensive activities and transition risk.

The main script described here is `annual_%_change.py`. It produces a figure with two time‑series plots:

1. Annual % change in world CO₂ emissions per capita  
2. Annual % change in world GDP per capita  

A grey shaded band highlights the period 2008–2009 to show the impact of the financial crisis on both series.

---

## Features

- Loads data from `analysis_dataset.csv`
- Filters data for a specified list of countries (default: `["World"]`)
- Calculates:
  - Annual % change in **CO₂ per capita (Trillions)**  
  - Annual % change in **GDP per capita**
- Produces a figure with 2 subplots:
  1. Annual % change in CO₂ emissions per capita since 1980  
  2. Annual % change in GDP per capita since 1980
- Highlights the 2008–2009 financial crisis period with a shaded region and label
- Saves the figure as `co2_gdp_annual_%_change.png` inside the `Annual_%_change/` folder

---

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `matplotlib`
  - `os` (standard library)

Install dependencies (if needed):

```bash
pip install pandas matplotlib

## Expected Data Format

The script expects a CSV file named **`analysis_dataset.csv`** with at least these columns:

| Column name                    | Type    | Description                                  |
|--------------------------------|---------|----------------------------------------------|
| `Country Name`                 | string  | Country or region name                       |
| `Year`                         | integer | Calendar year (e.g. 1980, 1981, …)           |
| `CO2 per capita (Trillions)`   | numeric | CO₂ emissions per capita (trillions)         |
| `GDP per capita`               | numeric | GDP per capita                               |

Additional notes:

- `Year` is converted to numeric with `errors="coerce"`, so invalid values become `NaN`.
- Each country/region should have multiple years of data so that the percentage change can be calculated.

---

## How It Works

1. **Read and prepare data**

   ```python
   dataset = pd.read_csv("analysis_dataset.csv")
   dataset["Year"] = pd.to_numeric(dataset["Year"], errors="coerce")