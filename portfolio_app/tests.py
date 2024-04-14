from django.test import TestCase, Client
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from django.urls import reverse
from .models import *
import json



class modelTest(LiveServerTestCase):
    def testModel(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        assert "Welcome to my data analytics app" in driver.title
        
class TestViews(TestCase):

    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('projects'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_project/display_projects.html')

    def test_character_list_GET(self):
        client = Client()
        response = client.get(reverse('characters'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_project/display_characters.html')

    
    
    #def test
# Create your tests here.
