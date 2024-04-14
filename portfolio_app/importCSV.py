# starwars/management/commands/importcsv.py
import pandas as pd
from django.core.management.base import BaseCommand
from portfolio_app.models import StarWarsCharacter

class Command(BaseCommand):
    help = 'Import Star Wars characters from an Excel file (default: starwars.xlsx)'

    def handle(self, *args, **options):
        filename = "starwars.xlsx"
        try:
            # Read the Excel file into a pandas DataFrame
            df = pd.read_excel(filename)
            
            # Iterate over rows in the DataFrame and create StarWarsCharacter objects
            for index, row in df.iterrows():
                character = StarWarsCharacter.objects.create(
                    name=row['name'],
                    height=float(row['height']) if pd.notna(row['height']) else None,
                    mass=float(row['mass']) if pd.notna(row['mass']) else None,
                    hair_color=row['hair_color'],
                    skin_color=row['skin_color'],
                    eye_color=row['eye_color'],
                    birth_year=row['birth_year'],
                    gender=row['gender'],
                    homeworld=row['homeworld'],
                    species=row['species'],
                    films=row['films'],
                    vehicles=row['vehicles'],
                    starships=row['starships']
                )
                character.save()
                
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File {filename} not found'))