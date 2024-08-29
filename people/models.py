from django.db import models

DEFUALT_IMAGE = 'people/default.jpg'

def generate_filename(self, filename):
    url = f'people/{self.name}/{filename}'
    return url
    
class StarWarsCharacter(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    height = models.IntegerField(null=True)
    mass = models.DecimalField(max_digits=6, decimal_places=1,null=True)
    hair_color = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    birth_year = models.DecimalField(max_digits=6, decimal_places=1, null=True) #https://starwars.fandom.com/wiki/Time
    gender_choices = [
        ('male', 'male'),
        ('female', 'female'),
        ('n/a', 'n/a'),
    ]
    gender = models.CharField(max_length=30, choices=gender_choices)
    home_world_name = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(upload_to=generate_filename, verbose_name="Character Image", default=DEFUALT_IMAGE)
    