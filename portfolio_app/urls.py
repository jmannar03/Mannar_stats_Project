from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('projects/',views.current_Projects,name='projects'),
    path('characters/',views.current_Characters,name='characters'),
    path('projects/<int:pk>', views.ProjectListView.as_view(), name = 'project-detail'),
    path('characters/<int:pk>', views.CharacterListView.as_view(), name = 'character-list'),
    path('create_Character/', views.add_Character, name='create_Character'),
    path('create_Project/',views.add_Project,name='create_Project'),
    path('delete_Project/<str:pk>/', views.delete_Project, name= 'delete_Project'),
    path('delete_Character/<str:pk>/', views.delete_Character, name= 'delete_Character'),
    path('update_Character/<str:pk>/', views.update_Character, name= 'update_Character'),
    path('update_Project/<str:pk>/', views.update_Project, name= 'update_Project'),
    path('character_details/<int:pk>/', views.view_character, name='character_details'),
    path('project_details/<str:pk>/', views.view_project, name='project_details'),

]
