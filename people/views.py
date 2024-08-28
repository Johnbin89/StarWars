from people.models import StarWarsCharacter
from people.serializers import StarWarsCharacterSerializer
from rest_framework import viewsets, permissions, filters
#from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class StarWarsCharacterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for viewing and filtering the StarWarsCharacters
    """
    serializer_class = StarWarsCharacterSerializer
    #https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'home_world_name']
    ordering_fields = ['name', 'mass', 'height']
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        #print(f'Query_params: {self.request.query_params}')
        queryset = StarWarsCharacter.objects.all()
        params = self.request.query_params.dict()
        name = params.get("name")
        planet = params.get("planet")
        if name:
            #print(name)
            queryset = StarWarsCharacter.objects.filter(name__icontains=name)
        elif planet:
            #print(planet)
            queryset = StarWarsCharacter.objects.filter(home_world_name__icontains=planet).all()
        return queryset
    
class FavoritesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for viewing the favorites Characters 
    for current user.
    """
    serializer_class = StarWarsCharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.favorites.all()