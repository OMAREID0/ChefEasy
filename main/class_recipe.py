#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query in an object-oriented manner.
"""

import requests

class RecipeInfoFinder:
    # Define the API key as a class attribute
    api_key = "cfe4b169bfc24c4a99c6801be60b38b4"

    def find_recipe_by_nutrients(self):
        url = "https://api.spoonacular.com/recipes/findByNutrients"
        params = {
            "apiKey": self.api_key,
            "minCholesterol": "0",
            "number": "2"
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

    def get_recipe_details(self, recipe_id):
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

    def get_recipe_info(self):
        recipe_info_dict = {}
        nutrient_recipes = self.find_recipe_by_nutrients()
        if nutrient_recipes:
            for recipe in nutrient_recipes:
                recipe_id = recipe.get('id')
                recipe_details = self.get_recipe_details(recipe_id)
                if recipe_details:
                    recipe_info = {
                        "title": recipe_details.get('title'),
                        "image": recipe_details.get('image'),
                        "calories": recipe_details.get('calories'),
                        "total_fat": recipe_details.get('fat'),
                        "protein": recipe_details.get('protein'),
                        "carbohydrate": recipe_details.get('carbs'),
                        "cholesterol": recipe_details.get('cholesterol'),
                        "ready_in_minutes": recipe_details.get('readyInMinutes'),
                        "servings": recipe_details.get('servings'),
                        "dish_type": recipe_details.get('dishTypes', [])[0] if recipe_details.get('dishTypes') else None,
                        "summary": recipe_details.get('summary'),
                        "ingredients": [ingredient.get('name', '') for ingredient in recipe_details.get('extendedIngredients', [])],
                        "instructions": []
                    }
                    instruction_data = recipe_details.get('analyzedInstructions', [])
                    for section in instruction_data:
                        steps = section.get('steps', [])
                        for step in steps:
                            step_number = step.get('number', '')
                            instruction = step.get('step', '')
                            if step_number and instruction:
                                recipe_info["instructions"].append(f"Step {step_number}: {instruction}")
                    recipe_info_dict[recipe_id] = recipe_info

        return recipe_info_dict
