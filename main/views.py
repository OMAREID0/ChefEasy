from django.shortcuts import render
from .class_recipe import RecipeInfoFinder
from django.http import request
import requests
import json


# Create your views here.
def home_page(request):
    numbers = range(9)
    return render(request, 'home.html', {'numbers': numbers})

def recipe_page(request):
    # Create an instance of RecipeInfoFinder
    recipe_finder = RecipeInfoFinder()

    # Get recipe information
    recipe_info = recipe_finder.get_recipe_info()
    print(recipe_info[634927].get('title'))

    # Render the data in a template
    return render(request, 'recipe.html', {'recipe_info': recipe_info})

def contact_page(request):
    return render(request, 'contact.html')
