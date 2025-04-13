from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from videogames.models import Videogame, Genre
from videogames.serializers import GetVideogameSerializer, GetGenreSerializer


class GetVideogameByTitleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, title):
        videogame = Videogame.objects.filter(title__icontains=title)
        if not videogame.exists():
            return Response({"error": "No se encontraron videojuegos con ese título"}, status=HTTP_400_BAD_REQUEST)

        serialized_videogame = GetVideogameSerializer(videogame, many=True)
        return Response(serialized_videogame.data, status=HTTP_200_OK)

class GetAllVideogames(APIView):
    def get(self, request):
        contents = Videogame.objects.all()
        serializer = GetVideogameSerializer(contents, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class GetGenre(APIView):
    def get(self, request):
        contents = Genre.objects.all()
        serializer = GetGenreSerializer(contents, many=True)
        return Response(serializer.data, status=HTTP_200_OK)