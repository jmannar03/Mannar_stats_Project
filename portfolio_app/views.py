from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *

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

def add_Character(request):
    form = CharacterForm
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'my_project/create_form.html',context)

def add_Project(request):
    form = ProjectForm
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'my_project/crete_project_form.html',context)

def delete_Project(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'item':project}
    return render(request, 'my_project/delete_project.html',context)


def delete_Character(request,pk):
    character = StarWarsCharacter.objects.get(id=pk)
    if request.method == "POST":
        character.delete()
        return redirect('/')
    context = {'item':character}
    return render(request, 'my_project/delete_character.html',context)

def update_Project(request,pk):
    project=Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
      form = ProjectForm(request.POST,instance=project)
      if form.is_valid():
         form.save()
         return redirect('/')
    context = {'form':form}
    return render(request, 'my_project/update_project_form.html',context)

def update_Character(request,pk):
    character=StarWarsCharacter.objects.get(id=pk)
    form = CharacterForm(instance=character)
    if request.method == 'POST':
        #print('Printing POST: ',request.POST)
      form = CharacterForm(request.POST,instance=character)
      if form.is_valid():
         form.save()
         return redirect('/')
    context = {'form':form}
    return render(request, 'my_project/update_character_form.html',context)

def view_character(request):
    return render(request, 'my_project/view_character.html')

def view_project(request):
    return render(request, 'my_project/view_project.html')



