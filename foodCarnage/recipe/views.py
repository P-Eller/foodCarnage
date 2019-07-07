from django.shortcuts import render
from recipe.models import Recipe
# Create your views here.

def index(request):
    return render(request,'recipe/index.html')

def add_recipe(request):
    return render(request,'recipe/index.html')
