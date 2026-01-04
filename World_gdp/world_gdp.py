#imports relevants functions used within this file
import pandas as pd

#uses pandas to read csv file and skips first 4 rows as they do not contain any data
world_gdp = pd.read_csv("World_gdp/world_gdp.csv", skiprows=4)

#filters out the desired countries given within the countries list
countries =["United Kingdom","India","Malawi","World"]
world_gdp_filtered=world_gdp[world_gdp["Country Name"].isin(countries)]

#only selectes the year column and filters for values that are 1980 or after
year_cols = [c for c in world_gdp_filtered.columns if c.isdigit() and int(c) >= 1980]
world_gdp_filtered=world_gdp_filtered[["Country Name"]+year_cols]

##converts from wide format to long format as original dataset contains multiple columns
world_gdp_long = world_gdp_filtered.melt(
    id_vars="Country Name",
    value_vars=year_cols,
    var_name="Year",
    value_name="GDP"
)

#sorts values bu country name and year in ascending order, easier for analysing data 
world_gdp_long = world_gdp_long.sort_values(
    by=["Country Name", "Year"],
    ascending=[True, True]
)

#validates datatype in year column to ensure all data values are integers
world_gdp_long["Year"] = world_gdp_long["Year"].astype(int)

#saves cleaned dataset within given directory without index values
world_gdp_long.to_csv(
    "World_gdp/new_world_gdp.csv",
    index=False  # this avoids saving the 0,1,2 index column
)

print(world_gdp_long.head())