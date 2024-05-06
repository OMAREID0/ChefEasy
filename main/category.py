#!/usr/bin/python3
"""
Using the Spoonacular API to search for recipes based on a query.
"""

import requests
from sys import argv

key = "cfe4b169bfc24c4a99c6801be60b38b4"
type = argv[1]

if __name__ == "__main__":
    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={key}"

    #&type={type}&number=3

    params = {
        "query": argv[1],
        "number" : argv[2],
        "minServings" : "1",
        "maxCarbs" : "50"
        #"maxReadyTime" : argv[3]
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for recipe in data.get('results', []):
                print(recipe) # Output each recipe dictionary
            #print(data)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
