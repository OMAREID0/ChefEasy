#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query.
"""

import requests
from sys import argv

key = "cfe4b169bfc24c4a99c6801be60b38b4"

if __name__ == "__main__":

    url4 = (f"https://api.spoonacular.com/recipes/716429/information?apiKey={key}")
    ingred_respose = requests.get(url4)
    ingred_data = ingred_respose.json()
    print(f"wess Name: {ingred_data['extendedIngredients']}")
