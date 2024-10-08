from django.core.management.base import BaseCommand, CommandError
from people.models import StarWarsCharacter
import httpx
import decimal

class Command(BaseCommand):
    help = 'Add people from https://swapi.dev/api/people/' 

    def handle(self, *args, **options):
        try:
            for i in range(1, 10):
                result = httpx.get(f'https://swapi.dev/api/people/?page={i}', timeout=None)
                json_response = result.json()
                people_list = json_response['results']
                for character in people_list:
                    home_world_name = httpx.get(character['homeworld']).json()['name']
                    
                    #Adjust for ABY. BBY periods (+, -) https://starwars.fandom.com/wiki/Time
                    if (birth_year_str := character['birth_year'])[-3:] in  {'BBY', 'ABY'}:
                        period = birth_year_str[-3:]
                        birth_year = decimal.Decimal(birth_year_str[:-3]) if period == 'ABY' else decimal.Decimal(f'-{birth_year_str[:-3]}')
                    else:
                        birth_year = None #Keep NULL db entry for 'unknown'. 0 considered 0ABY
                    height = int(character['height']) if character['height'] != 'unknown' else None
                    mass = decimal.Decimal(character['mass'].replace(',' ,'')) if character['mass'] != 'unknown' else decimal.Decimal('0')
                    print(f'{character['name']}, {birth_year} ,{home_world_name}, height: {height}, mass = {mass}')
                    starwars_model = StarWarsCharacter(name=character['name'],
                                                       height=height,
                                                       mass=mass,
                                                       hair_color=character['hair_color'],
                                                       skin_color=character['skin_color'],
                                                       eye_color=character['eye_color'],
                                                       birth_year=birth_year,
                                                       gender=character['gender'],
                                                       home_world_name=home_world_name)
                    starwars_model.save()
                    

        except Exception as e:
            raise CommandError(f'Something bad hapenned: {e}')
        self.stdout.write(self.style.SUCCESS('Successfully added starwars characters!'))