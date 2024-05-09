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

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for recipe in data:
                x = recipe['id']
                print(f"Recipe Name: {recipe['title']}")
                print(f"Image: {recipe['image']}")
                print(f"Author: {recipe['author']}")
                print(f"Calories: {recipe['calories']}")
                print(f"Total Fat: {recipe['fat']}")
                print(f"Protein: {recipe['protein']}")
                print(f"Carbohydrate: {recipe['carbs']}")
                print(f"Colesterol: {recipe['cholesterol']}")

                url2 = requests.get(f"https://api.spoonacular.com/recipes/{x}/information?apiKey={key}").json()
                print(f"Ready in Minutes: {url2['readyInMinutes']}")
                print(f"Number Of Serving People: {url2['servings']}")
                print("")
                print(f"Summary: {url2['summary']}")
                print(f"Dish Type: {url2['dishTypes']}")
                print("")
                
                url4 = requests.get(f"https://api.spoonacular.com/recipes/{x}/ingredientWidget.json?apiKey={key}").json()
                print("Ingredients:")
                for ingredient in url4.get('ingredients', []):
                    ingredient_name = ingredient.get('name', '')
                    if ingredient_name:
                        print(f"- {ingredient_name}")
                print("")
                url3 = requests.get(f"https://api.spoonacular.com/recipes/{x}/analyzedInstructions?apiKey={key}").json()
                for section in url3:
                    steps = section.get('steps', [])  # Extract the list of steps for each section
                    if steps:
                        print("Instructions:")  # Print the section (recipe) name if available
                        for step in steps:
                            step_number = step.get('number', '')
                            instruction = step.get('step', '')
                            if step_number and instruction:
                                print(f"Step {step_number}: {instruction}")
                

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
