from django.test import TestCase, Client
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from django.urls import reverse
from .models import *
import json
from time import *
from selenium.webdriver.common.by import By




class TestForms(LiveServerTestCase):
    def testModel(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        assert "Welcome to my data analytics app" in driver.title

    def testCharacterForm(self):
        #print('we are in tests')
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/projects/')
        sleep(4)
        create_button = driver.find_element(By.ID,'createNew')
        create_button.click()

        sleep(4)

         # Find the input fields and fill them with values
        name_input = driver.find_element(By.ID, 'id_name')
        name_input.send_keys('Justin')

        about_input = driver.find_element(By.ID, 'id_about')
        about_input.send_keys('starwars project')

        email_input = driver.find_element(By.ID, 'id_email')
        email_input.send_keys('jmannar2@uccs.edu')

    # Find and click the submit button
        submit_button = driver.find_element(By.NAME, 'Submit')
        submit_button.click()

        # name = driver.find_element(By.NAME,'username')
        # sleep(2)
        # name.send_keys('Justin')
        # #dataset = driver.find_element_by_name('has_DataSet')
        # about = driver.find_element(By.NAME,'about').send_keys('starwars project')
        # sleep(2)
        # email = driver.find_element(By.NAME,'email').send_keys('jmannar2@uccs.edu')
        # sleep(2)
        # submit_button = driver.find_element_by_name('Submit')
        # submit_button.click()


    #     #character_List = driver.find_element_by_
    #     # name.send_keys('Justin')
    #     # #dataset.
    #     # about.send_keys('I am in star wars')
    #     # email.send_keys('jmannar2@uccs.edu')

        
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



# name = models.CharField(max_length=100)
#     height = models.FloatField(null=True)
#     mass = models.FloatField(null=True)
#     hair_color = models.CharField(max_length=50)
#     skin_color = models.CharField(max_length=50)
#     eye_color = models.CharField(max_length=50)
#     birth_year = models.CharField(max_length=20)
#     gender = models.CharField(max_length=10)
#     homeworld = models.CharField(max_length=100)
#     species = models.CharField(max_length=100)
#     films = models.JSONField(null=True)
#     vehicles = models.JSONField(null=True)
#     starships = models.JSONField(null=True)

#class TestForms():


    
    
    #def test
# Create your tests here.
