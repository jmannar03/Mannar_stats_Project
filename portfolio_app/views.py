from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.
def index(request):
    return render (request, 'my_project/index.html')
    # studentActivePortfolios = Project.objects.select_related('portfolio').all().filter(project__has_DataSet=True)
    # print("Active portfolio query set:", studentActivePortfolios)
    # return render(request, 'portfolio_app/index.html', {'studentActivePortfolios': studentActivePortfolios})

def current_Projects(request):
    activeProjects = Project.objects.filter(has_DataSet=True)
    print("List of projects with a dataset query set:", activeProjects)
    return render (request, 'my_project/display_projects.html', {'activeProjects': activeProjects})

def current_Characters(request):
    allCharacters = StarWarsCharacter.objects.all()
    print("list of all characters in dataset: ", allCharacters)
    return render (request, 'my_project/display_characters.html', {'allCharacters': allCharacters})

class ProjectListView(generic.DetailView):
    model = Project

class CharacterListView(generic.DetailView):
    model = StarWarsCharacter
