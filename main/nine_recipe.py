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
        "number": "9", 
    }
    listed_output = []
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for recipe in data:
                recipe_info = [
                    f"Recipe Name: {recipe['title']}",
                    f"Image: {recipe['image']}",
                ]
                
                listed_output.append(recipe_info)
                print (listed_output)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
