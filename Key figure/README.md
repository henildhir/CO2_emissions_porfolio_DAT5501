# CO2 Emissions per Capita Over Time - Line Graph Analysis

This folder visualises the historical trend of **CO2 emissions per capita (tonnes)** for multiple countries from 1980 onwards. It produces a time series line plot with distinct markers and colours for each country, highlighting emission changes over time. The plot also marks the significant historical event of the **2015 Paris Agreement** with a vertical dashed line.

The output figure is saved as `Key figure/key_figure.png`.

The main script responsible for this visualisation is `key_figure.py`.

---

## Features

- Reads data from `analysis_dataset.csv`.
- Plots CO2 emissions per capita over time using Seaborn’s `lineplot`.
- Displays emissions trends for multiple countries distinguished by colour and markers:
  - United Kingdom
  - World
  - India
  - Malawi
- Adds clear axis labels, plot title, and gridlines with moderate transparency.
- Draws a vertical dashed line at year 2015 representing the Paris Agreement milestone.
- Customises the legend to reorder entries to match narrative/report order.
- Saves the resulting figure as a PNG to a programmatically created folder `Key figure`.

---

## Design Decisions and Performance Justification

### Efficient Use of Seaborn and Matplotlib

- The choice of `sns.lineplot` simplifies plotting multiple time series grouped by country.
- Line markers and linewidth are adjusted to improve readability of trends and data points.

### Explicit Legend Management

- Programmable legend ordering ensures logical narrative flow for report readers.
- Extracting and rebuilding handles and labels avoids manual legend entry duplication.

### Highlighting a Key Historical Event

- Adding a vertical line at 2015 (Paris Agreement) visually connects emissions trends with policy milestones.
- Dashed grey line keeps the annotation visible

### Folder Creation and File Saving

- Output folder is created automatically if missing, ensuring reproducibility.
- Single save operation after full figure creation minimises I/O overhead.

---

## Interpretative Insights

This timeline plot clearly communicates the evolving CO2 emissions landscape across different regions:

- Enables comparison of emissions trajectories since 1980 among developed (UK), global aggregate (World), and developing countries (India, Malawi).
- The Paris Agreement marker helps correlate emissions changes with international climate policy efforts.
- Temporal trends highlight where emissions growth is accelerating or plateauing, informing climate strategy and risk assessment.
- Differentiated colours and markers allow quick identification and comparison of country-level patterns.

---

## Requirements

- Latest Python version.
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `os`