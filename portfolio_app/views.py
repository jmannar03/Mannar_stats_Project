from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views import generic
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='user-login')
def index(request):
    return render (request, 'my_project/index.html')
    # studentActivePortfolios = Project.objects.select_related('portfolio').all().filter(project__has_DataSet=True)
    # print("Active portfolio query set:", studentActivePortfolios)
    # return render(request, 'portfolio_app/index.html', {'studentActivePortfolios': studentActivePortfolios})

#@login_required(login_url='user-login')
def current_Projects(request):
    activeProjects = Project.objects.filter(has_DataSet=True)
    print("List of projects with a dataset query set:", activeProjects)
    return render (request, 'my_project/display_projects.html', {'activeProjects': activeProjects})

#@login_required(login_url='user-login')
def current_Characters(request):
    allCharacters = StarWarsCharacter.objects.all()
    print("list of all characters in dataset: ", allCharacters)
    return render (request, 'my_project/display_characters.html', {'allCharacters': allCharacters})

class ProjectListView(generic.DetailView):
    model = Project

class CharacterListView(generic.DetailView):
    model = StarWarsCharacter

@login_required(login_url='user-login')
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

#@login_required(login_url='user-login')
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

@login_required(login_url='user-login')
def delete_Project(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')
    context = {'item':project}
    return render(request, 'my_project/delete_project.html',context)

@login_required(login_url='user-login')
def delete_Character(request,pk):
    character = StarWarsCharacter.objects.get(id=pk)
    if request.method == "POST":
        character.delete()
        return redirect('/')
    context = {'item':character}
    return render(request, 'my_project/delete_character.html',context)

@login_required(login_url='user-login')
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

@login_required(login_url='user-login')
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

@login_required(login_url='user-login')
def view_character(request, pk):

    # Retrieve the StarWarsCharacter object by its ID
    character = StarWarsCharacter.objects.get(id=pk)
    
    # Render the template with the character object
    return render(request, 'my_project/view_character.html', {'character': character})

    # return render(request, 'my_project/view_character.html')

@login_required(login_url='user-login')
def view_project(request,pk):
    project = Project.objects.get(id=pk)
    
    # Render the template with the character object
    return render(request, 'my_project/view_project.html', {'project': project})
    #return render(request, 'my_project/view_project.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username OR Password is incorrect')
            
    context = {}
    return render(request, 'my_project/login.html', context)

def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created in database for ' + user)
            return redirect('user-login')

    context = {'form':form}
    return render(request, 'my_project/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('user-login')




