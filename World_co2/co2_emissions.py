#imports relevants functions used within this file
import pandas as pd

#uses pandas to read csv file within desired directory
co2_emissions=pd.read_csv("World_co2/co2-emissions-per-capita.csv")

#filters data in year column for years 1980 and later, easier to analyse data
co2_emissions=co2_emissions[co2_emissions["Year"] >= 1980]

#renamed columns to better names, making analysing data easier 
co2_emissions=co2_emissions.rename(
    columns = {
        "Entity":"Country Name",
        "Annual CO₂ emissions (per capita)":"CO2 per capita",
    }
)

print(co2_emissions.head())

#saves csv file to desired directory excluding index values
co2_emissions.to_csv("World_co2/new_co2_emissions_per_capita.csv",index=False)