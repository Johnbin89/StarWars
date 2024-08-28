from people.models import StarWarsCharacter
from rest_framework import serializers

class StarWarsCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarWarsCharacter
        fields = '__all__'