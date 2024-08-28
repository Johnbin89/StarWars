from django.db import models
from django.contrib.auth.models import AbstractUser
from people.models import StarWarsCharacter



#https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    favorites = models.ManyToManyField(StarWarsCharacter, related_name='favorites', default=None, null=True)