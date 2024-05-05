#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query in an object-oriented way.
"""

import requests
from sys import argv

class SearchCategory:
    def __init__(self, key):
        self.key = key
        self.base_url = "https://api.spoonacular.com/recipes/complexSearch"

    def category_search(self, rec_type, number):
        
        params = {
        "apiKey": self.key,
        "type": rec_type,
        "number" : number,
    }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get('results', [])
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return []

if __name__ == "__main__":

    api_key = "cfe4b169bfc24c4a99c6801be60b38b4"
    rec_type = argv[1]
    number = int(argv[2])

    search_category = SearchCategory(api_key)
    recipes = search_category.category_search(rec_type, number)

    for recipe in recipes:
        print(recipe)  # Output each recipe dictionary
