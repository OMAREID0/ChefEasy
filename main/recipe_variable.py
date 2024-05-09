#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query.
"""

import requests


key = "cfe4b169bfc24c4a99c6801be60b38b4"

if __name__ == "__main__":
    url = f"https://api.spoonacular.com/recipes/findByNutrients?apiKey={key}"

    params = {
        "minCholesterol": "0",
        "number": "1", 
    }
    output_list = []
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for recipe in data:
                x = recipe['id']
                recipe_info = [
                    f"Recipe Name: {recipe['title']}",
                    f"Image: {recipe['image']}",
                    f"Calories: {recipe['calories']}",
                    f"Total Fat: {recipe['fat']}",
                    f"Protein: {recipe['protein']}",
                    f"Carbohydrate: {recipe['carbs']}",
                    f"Cholesterol: {recipe['cholesterol']}"
                ]
                
                url2 = requests.get(f"https://api.spoonacular.com/recipes/{x}/information?apiKey={key}").json()
                recipe_info.append(f"Ready in Minutes: {url2['readyInMinutes']}")
                recipe_info.append(f"Number Of Serving People: {url2['servings']}")
                recipe_info.append(f"Summary: {url2['summary']}")
                
                
                url3 = requests.get(f"https://api.spoonacular.com/recipes/{x}/ingredientWidget.json?apiKey={key}").json()
                for ingredient in url3.get('ingredients', []):
                    ingredient_name = ingredient.get('name', '')
                    if ingredient_name:
                        recipe_info.append(f"- {ingredient_name}")

                url4 = requests.get(f"https://api.spoonacular.com/recipes/{x}/analyzedInstructions?apiKey={key}").json()
                for section in url4:
                    steps = section.get('steps', [])  # Extract the list of steps for each section
                    if steps:
                        for step in steps:
                            step_number = step.get('number', '')
                            instruction = step.get('step', '')
                            if step_number and instruction:
                                recipe_info.append(f"Step {step_number}: {instruction}")
                
                output_list.append(recipe_info)
                print (output_list)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
