#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query in an object-oriented manner.
"""

import requests

class RecipeFinder:
    def __init__(self, api_key):
        self.api_key = api_key

    def find_recipe_by_nutrients(self):
        url = "https://api.spoonacular.com/recipes/findByNutrients"
        params = {
            "apiKey": self.api_key,
            "minCholesterol": "0",
            "number": "1"
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data[0] if data else None
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

    def get_recipe_details(self, recipe_id):
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        params = {
            "apiKey": self.api_key
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data if data else None
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
    
    # Find a recipe based on nutrients
    nutrient_recipe = recipe_finder.find_recipe_by_nutrients()
    if nutrient_recipe:
        recipe_id = nutrient_recipe.get('id')
        
        # Get detailed information for the found recipe
        recipe_details = recipe_finder.get_recipe_details(recipe_id)
        if recipe_details:
            print(f"Recipe Name: {recipe_details.get('title')}")
            print(f"Image: {recipe_details.get('image')}")
            print(f"Calories: {recipe_details.get('calories')}")
            print(f"Total Fat: {recipe_details.get('fat')}")
            print(f"Protein: {recipe_details.get('protein')}")
            print(f"Carbohydrate: {recipe_details.get('carbs')}")
            print(f"Cholesterol: {recipe_details.get('cholesterol')}")
            print(f"Ready in Minutes: {recipe_details.get('readyInMinutes')}")
            print(f"Number Of Serving People: {recipe_details.get('servings')}")
            dish_types = recipe_details.get('dishTypes', [])
            if dish_types:
                print(f"Dish Type: {dish_types[0]}")
            print(f"Summary: {recipe_details.get('summary')}")
            
            # Output the ingredients
            print("Ingredients:")
            ingredient_data = recipe_details.get('extendedIngredients', [])
            for ingredient in ingredient_data:
                ingredient_name = ingredient.get('name', '')
                print(f"- {ingredient_name}")
            
            # Output the instructions
            print("Instructions:")
            instruction_data = recipe_details.get('analyzedInstructions', [])
            for section in instruction_data:
                steps = section.get('steps', [])
                for step in steps:
                    step_number = step.get('number', '')
                    instruction = step.get('step', '')
                    if step_number and instruction:
                        print(f"Step {step_number}: {instruction}")
