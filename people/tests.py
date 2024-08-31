from django.test import TestCase
import decimal
from people.models import StarWarsCharacter
from django.urls import reverse

class StarWarsCharacterModelTest(TestCase):
    DEFUALT_IMAGE = 'people/default.jpg'
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        StarWarsCharacter.objects.create(name='TestName',
                                                       height=175,
                                                       mass=decimal.Decimal(10),
                                                       hair_color='random',
                                                       skin_color='random',
                                                       eye_color='random',
                                                       birth_year=decimal.Decimal(50.2),
                                                       gender='male',
                                                       home_world_name='planet')

    def test_birth_year_digits(self):
        character = StarWarsCharacter.objects.get(id=1)
        birth_year_max_digits = character._meta.get_field('birth_year').max_digits
        birth_year_decimal_places = character._meta.get_field('birth_year').decimal_places
        self.assertEqual(birth_year_max_digits, 6)
        self.assertEqual(birth_year_decimal_places, 1)
        
    def test_mass_digits(self):
        character = StarWarsCharacter.objects.get(id=1)
        mass_max_digits = character._meta.get_field('mass').max_digits
        mass_decimal_places = character._meta.get_field('mass').decimal_places
        self.assertEqual(mass_max_digits, 6)
        self.assertEqual(mass_decimal_places, 1)

    def test_default_image(self):
        character = StarWarsCharacter.objects.get(id=1)
        self.assertEqual(character.image, self.DEFUALT_IMAGE)
        
    def test_detail_path(self):
        self.assertEqual(reverse('people-detail', args=[1]), '/api/people/1/')