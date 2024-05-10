#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query in an object-oriented manner.
"""

import requests

class RecipeFinder:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com/recipes/findByNutrients"

    def find_recipes_by_nutrients(self, min_cholesterol=0, number=1):
        params = {
            "apiKey": self.api_key,
            "minCholesterol": min_cholesterol,
            "number": number
        }
        listed_output = []

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                for recipe in data:
                    recipe_info = [
                        f"Recipe Name: {recipe['title']}",
                        f"Image: {recipe['image']}",
                    ]
                    listed_output.append(recipe_info)
                return listed_output
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

if __name__ == "__main__":
    key = "cfe4b169bfc24c4a99c6801be60b38b4"
    
    # Create an instance of RecipeFinder
    recipe_finder = RecipeFinder(api_key=key)
    
    # Find recipes by nutrients
    recipes = recipe_finder.find_recipes_by_nutrients(min_cholesterol=0, number=1)
    
    # Output the recipe information
    if recipes:
        for recipe_info in recipes:
            print("\n".join(recipe_info))
