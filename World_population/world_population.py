#imports relevants functions used within this file
import pandas as pd

#uses pandas to read csv file and skips first 4 rows as they do not contain any data
world_population = pd.read_csv("World_population/world_population.csv", skiprows=4)

#filters out the desired countries given within the countries list
countries=["United Kingdom","India","Malawi","World"]
world_population_filtered = world_population[world_population["Country Name"].isin(countries)]

#only selectes the year column and filters for values that are 1980 or after
year_cols = [c for c in world_population.columns if c.isdigit() and int(c) >=1980]

#keeps only the country name and selected year column
world_population_filtered = world_population_filtered[["Country Name"] + year_cols]

#converts from wide format to long format as original dataset contains multiple columns
world_population_long = world_population_filtered.melt(
    id_vars="Country Name",
    value_vars=year_cols,
    var_name="Year",
    value_name="Population"
)

#Sorts the data by country and year, making it easier for analysing data 
world_population_long = world_population_long.sort_values(
    by=["Country Name", "Year"],
    ascending=[True, True]
)

#validates datatype in year column to ensure all data values are integers
world_population_long["Year"] = world_population_long["Year"].astype(int)

print(world_population_long.head())

#saves cleaned dataset within given directory without index values
world_population_long.to_csv("World_population/new_world_population.csv",index = False)