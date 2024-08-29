from people.models import StarWarsCharacter
from people.serializers import StarWarsCharacterSerializer
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class StarWarsCharacterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for viewing and filtering the StarWarsCharacters
    """

    serializer_class = StarWarsCharacterSerializer
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "home_world_name"]
    ordering_fields = ["name", "mass", "height"]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # print(f'Query_params: {self.request.query_params}')
        queryset = StarWarsCharacter.objects.all()
        params = self.request.query_params.dict()
        name = params.get("name")
        planet = params.get("planet")
        if name:
            # print(name)
            queryset = StarWarsCharacter.objects.filter(name__icontains=name)
        elif planet:
            # print(planet)
            queryset = StarWarsCharacter.objects.filter(
                home_world_name__icontains=planet
            ).all()
        return queryset

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def favorites(self, request):
        favorite_characters = request.user.favorites.all()
        serializer = self.get_serializer(favorite_characters, many=True)
        return Response(serializer.data)

    @favorites.mapping.post
    def add_favorites(self, request):
        favorites_ids = request.data
        found_starwars_characters = StarWarsCharacter.objects.filter(
            id__in=favorites_ids
        ).all()
        favorite_characters = request.user.favorites.all()
        union_set = favorite_characters.intersection(found_starwars_characters)
        if len(union_set):
            return Response(
                {
                    "message": "Can not add characters already in Favorites",
                    "characters":union_set.values_list(),
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )            
        if len(favorites_ids) != found_starwars_characters.count():
            return Response(
                {
                    "message": "Not Found all requested Characters",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )
        request.user.favorites.add(*found_starwars_characters)
        return Response(
            {
                "message": "Added Favorites",
                "status": status.HTTP_200_OK,
                "characters": found_starwars_characters.values_list(),
                "added_count": found_starwars_characters.count(),
            }
        )
