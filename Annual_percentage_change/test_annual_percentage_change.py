#imports all relevant libraries
import unittest
import pandas as pd
import numpy as np
import matplotlib

#This imports the python file located within this folder
import annual_percentage_change as ac  

class TestAnnualPercentChange(unittest.TestCase):
    #This function creates a sample dataset that contains relevant datavalues and datatypes
    def setUp(self):
        self.sample_data = pd.DataFrame({
            "Country Name": ["World", "World", "World", "CountryA", "CountryA"],
            "Year": [2000, 2001, 2002, 2000, 2001],
            "CO2 per capita (Trillions)": [1.0, 1.1, 1.2, 0, 0],
            "GDP per capita": [1000, 1100, 1210, 500, 0]
        })

    #This function filters out for the desired country and tests for different use cases for percentage change
    def test_filter_and_calculate_percentage_change(self):
        countries = ["World"]
        result = ac.filter_and_calculate(self.sample_data, countries)

        # Only rows in result must have countries that have been asked for
        self.assertTrue(result["Country Name"].isin(countries).all())

        # Percentage changes: first row per country is NaN
        first_idx = result.index[0]
        self.assertTrue(np.isnan(result.loc[first_idx, "CO2_percentage_change"]))
        self.assertTrue(np.isnan(result.loc[first_idx, "GDP_percentage_change"]))

        # Second row has around 10% change for World
        self.assertAlmostEqual(result.loc[first_idx+1, "CO2_percentage_change"], 10.0, places=2)
        self.assertAlmostEqual(result.loc[first_idx+1, "GDP_percentage_change"], 10.0, places=2)

    #tests for any values that have 0 percentage change 
    def test_zero_and_constant_values(self):
        countries = ["CountryA"]
        result = ac.filter_and_calculate(self.sample_data, countries)
        first_idx = result.index[0]
        self.assertTrue(np.isnan(result.loc[first_idx, "CO2_percentage_change"]))
        col = result["CO2_percentage_change"].iloc[1]
        self.assertTrue(np.isnan(col) or np.isinf(col))

    #tests for a basic plot structure, validating whether a plot has been created 
    def test_create_plot_structure(self):
        countries = ["World", "CountryA"]
        data = ac.filter_and_calculate(self.sample_data, countries)
        fig, ax = ac.create_plots(data, countries)
        # assert figure and axes created as expected
        self.assertEqual(len(ax), 2)
        self.assertTrue(hasattr(fig, "savefig"))
        # basic labels presence checks (string contains)
        self.assertIn("Year", ax[0].get_xlabel())
        self.assertIn("% change", ax[0].get_ylabel())
        self.assertIn("Year", ax[1].get_xlabel())
        self.assertIn("% change", ax[1].get_ylabel())

if __name__ == "__main__":
    unittest.main()