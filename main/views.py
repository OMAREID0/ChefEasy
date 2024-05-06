from django.shortcuts import render
from django.http import request
import requests
import json


# Create your views here.
def home_page(request):
    numbers = range(9)
    return render(request, 'home.html', {'numbers': numbers})

def recipe_page(request):
    return render(request, 'recipe.html')

def contact_page(request):
    return render(request, 'contact.html')