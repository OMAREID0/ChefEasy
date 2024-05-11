from django.shortcuts import render
from .class_recipe import RecipeInfoFinder
from django.http import request
import requests
import json


# Create your views here.
def home_page(request):
    recipe_finder = RecipeInfoFinder()

    recipes = recipe_finder.find_recipe_by_nutrients()

    print(recipes)
    return render(request, 'home.html')

def recipe_page(request):
    # Create an instance of RecipeInfoFinder
    recipe_finder = RecipeInfoFinder()

    # Get recipe information
    recipe_info_dict = recipe_finder.get_recipe_info()
    print(recipe_info_dict)

    # Render the data in a template
    return render(request, 'recipe.html', recipe_info_dict)

def contact_page(request):
    return render(request, 'contact.html')
