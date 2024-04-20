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

    def testProjectForm(self):
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

        box = driver.find_element(By.ID, 'id_has_DataSet')
        box.click()

        about_input = driver.find_element(By.ID, 'id_about')
        about_input.send_keys('starwars project')

        email_input = driver.find_element(By.ID, 'id_email')
        email_input.send_keys('jmannar2@uccs.edu')

    # Find and click the submit button
        submit_button = driver.find_element(By.NAME, 'Submit')
        submit_button.click()

        driver.get('http://127.0.0.1:8000/projects/')

        sleep(3)

    #how do I get to the character-list to see if the character was made in the test?

    # def testCharactersForm(self):
    #     driver = webdriver.Chrome()

    #     driver.get('http://127.0.0.1:8000/characters/')
    #     create_button = driver.find_element(By.ID,'createNew2')
    #     create_button.click()

    #     name_input = driver.find_element(By.ID,'id_name')
    #     name_input.send_keys('billy')

    #     height_input = driver.find_element(By.ID,'id_height')
    #     height_input.send_keys('23')

    #     mass_input = driver.find_element(By.ID,'id_mass')
    #     mass_input.send_keys('30')

    #     hairColor_input = driver.find_element(By.ID,'id_hair_color')
    #     hairColor_input.send_keys('brown')

    #     skinColor_input = driver.find_element(By.ID,'id_skin_color')
    #     skinColor_input.send_keys('brown')

    #     eyeColor_input = driver.find_element(By.ID,'id_eye_color')
    #     eyeColor_input.send_keys('blue')

    #     birthYear_input = driver.find_element(By.ID,'id_birth_year')
    #     birthYear_input.send_keys('2024')

    #     gender_input = driver.find_element(By.ID,'id_gender')
    #     gender_input.send_keys('male')

    #     homeworld_input = driver.find_element(By.ID,'id_homeworld')
    #     homeworld_input.send_keys('Alderran')

    #     species_input = driver.find_element(By.ID,'id_species')
    #     species_input.send_keys('clone')

    #     films_input = driver.find_element(By.ID,'id_films')
    #     films_input.send_keys('Revenge of the sith')

    #     name_input = driver.find_element(By.ID,'id_vehicles')
    #     name_input.send_keys('speeder')

    #     starShip_input = driver.find_element(By.ID,'id_starships')
    #     starShip_input.send_keys('Omicron class star fighter')

    #     submit = driver.find_element(By.NAME,'Submit')
    #     submit.click()

    #     driver.get('http://127.0.0.1:8000/characters/')

    #     sleep(3)

    def testLogin(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()

        username = driver.find_element(By.NAME, 'username')
        username.send_keys('newtry')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('CacaC00too321')

        submit_button = driver.find_element(By.ID, 'Submit')
        submit_button.click()

        sleep(3)

        driver.get('http://127.0.0.1:8000/')

        sleep(3)

    def testLogout(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        login_button = driver.find_element(By.ID, 'login')
        login_button.click()

        username = driver.find_element(By.NAME, 'username')
        username.send_keys('newtry')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('CacaC00too321')

        submit_button = driver.find_element(By.ID, 'Submit')
        submit_button.click()

        sleep(3)

        driver.get('http://127.0.0.1:8000/')

        logout_button = driver.find_element(By.ID, 'logout')
        logout_button.click()

        sleep(3)


        

        
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

class TestModels(TestCase):
    def testProject(self):
        self.project = Project.objects.create(
            name = 'helo world',
            has_DataSet = True,
            about = 'this is a project',
            email = 'bob@gmail'
        )
        self.assertEqual(self.project.name, 'helo world')
        self.assertTrue(self.project.has_DataSet)
        self.assertEqual(self.project.about, 'this is a project')
        self.assertEqual(self.project.email,'bob@gmail')
        #self.assertEqual(self.project.get_absolute_url(),'/project/1')


    # def testCharacter(self):
    #     self.Character = StarWarsCharacter.objects.create(
    #         name = 'john',
    #         height = 36,
    #         mass = 24,
    #         hair_color = 'brown',
    #         skin_color = 'tan',
    #         eye_color = 'blue',
    #         birth_year = '2004',
    #         gender = 'male',
    #         homeworld = 'kamino',
    #         species = 'human',
    #         films = 'return of the jedi',
    #         vehicles = 'none',
    #         starships = 'none',
    #     )
        



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
