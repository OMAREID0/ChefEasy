#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query.
"""

import requests

key = "cfe4b169bfc24c4a99c6801be60b38b4"
#type = argv[1]

if __name__ == "__main__":
    url = f"https://api.spoonacular.com/recipes/complexSearch?query=dessert&number=2&apiKey={key}"

    try:
        response = requests.get(url)#, params=params)
        if response.status_code == 200:
            data = response.json()
            recipe_list = []  # List to store recipe dictionaries
            for recipe in data.get('results', []):
                recipe_list.append(recipe)  # Append each recipe dictionary to the list
                print(recipe_list) # Output each recipe dictionary
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
