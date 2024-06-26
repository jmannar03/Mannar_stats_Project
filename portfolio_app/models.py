from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=100)
    has_DataSet = models.BooleanField(default = False)
    about = models.CharField(max_length=200, null=True, blank = True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

class StarWarsCharacter(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField(null=True)
    mass = models.FloatField(null=True)
    hair_color = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    homeworld = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    films = models.JSONField(null=True)
    vehicles = models.JSONField(null=True)
    starships = models.JSONField(null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('character-list', args=[str(self.id)])


# Create your models here.
