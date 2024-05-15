#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query in an object-oriented manner.
"""

import requests

class RecipeNine:
    # Define the API key as a class attribute
    api_key = "cfe4b169bfc24c4a99c6801be60b38b4"

    def recipe_nutrients(self):
        url = "https://api.spoonacular.com/recipes/findByNutrients"
        params = {
            "apiKey": self.api_key,
            "minCholesterol": "0",
            "number": "9"
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data if data else {}
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return {}
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return {}

    def recipe_details(self, recipe_id):
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        params = {
            "apiKey": self.api_key
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data if data else {}
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return {}
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return {}

    def nine_recipe_info(self):
        simple_recipe_info_dict = {}
        nutrient_recipes = self.recipe_nutrients()
        if nutrient_recipes:
            for recipe in nutrient_recipes:
                recipe_id = recipe.get('id')
                recipe_details = self.recipe_details(recipe_id)
                if recipe_details:
                    simple_recipe_info = {
                        'id': recipe_id,
                        'title': recipe_details.get('title'),
                        'image': recipe_details.get('image'),
                        'ready_in_minutes': recipe_details.get('readyInMinutes'),
                        'servings': recipe_details.get('servings')
                    }
                    simple_recipe_info_dict[recipe_id] = simple_recipe_info

        return simple_recipe_info_dict
