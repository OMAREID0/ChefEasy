#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query in an object-oriented manner.
"""

import requests

class RecipeSearcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com/recipes/complexSearch"

    def search_recipes(self, query, number=2):
        url = f"{self.base_url}?query={query}&number={number}&apiKey={self.api_key}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                recipe_list = data.get('results', [])  # List to store recipe dictionaries
                return recipe_list
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return []

if __name__ == "__main__":
    key = "cfe4b169bfc24c4a99c6801be60b38b4"

    # Create an instance of RecipeSearcher
    recipe_searcher = RecipeSearcher(api_key=key)
    
    # Search for vegan recipes
    query = "meat"
    recipes = recipe_searcher.search_recipes(query=query, number=2)
    
    # Output the recipe information
    for recipe in recipes:
        print(f"Recipe Name: {recipe['title']}")
        print(f"Image: {recipe['image']}")
