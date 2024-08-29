from django.contrib import admin
from people.models import StarWarsCharacter
# Register your models here.

class StarWarsCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "height", "mass", "birth_year", "home_world_name")
    search_fields = ['name__icontains', 'home_world_name__icontains']

admin.site.register(StarWarsCharacter, StarWarsCharacterAdmin)