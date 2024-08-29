from people.models import StarWarsCharacter
from people.serializers import StarWarsCharacterSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
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
    
    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def favorites(self, request):
        favorite_characters = request.user.favorites.all()
        serializer = self.get_serializer(favorite_characters, many=True)
        return Response(serializer.data)