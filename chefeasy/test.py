#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query.
"""

import requests
from sys import argv

key = "cfe4b169bfc24c4a99c6801be60b38b4"


if __name__ == "__main__":
    url = f"https://api.spoonacular.com/recipes/1697541/information?apiKey={key}"


    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Ready in Minutes: {data['readyInMinutes']}")
            print(f"Ready in Minutes: {data['servings']}")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
