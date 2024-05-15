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
        recipe_dict = {}

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                for recipe in data:
                    recipe_info = {
                        "Recipe Name": recipe['title'],
                        "Image": recipe['image'],
                        "Calories": recipe['calories'],
                        "Total Fat": recipe['fat'],
                        "Protein": recipe['protein'],
                        "Carbohydrate": recipe['carbs'],
                        "Cholesterol": recipe['cholesterol']
                    }
                    recipe_dict[recipe['id']] = recipe_info
                return recipe_dict
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None
