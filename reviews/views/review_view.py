from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from reviews.models import Review
from reviews.serializers.ReviewSerializer import *
from users.models import CustomUser
from videogames.models import Genre


class CreateReviewView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')
        stars = data.get('stars')

        try:
            genre_name = data.get('genre')
            genre = Genre.objects.get(name=genre_name)  # Buscar género por nombre

            # user_email = data.get('user')
            # user = CustomUser.objects.get(email=user_email)  # Buscar usuario por email

            review_data = {
                'title': title,
                'description': description,
                'stars': stars,
                'genre': genre.id,
            }

            serializer = AddNewReviewSerializer(data=review_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "Review creada correctamente"}, status=HTTP_201_CREATED)
            else:
                return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

        except Genre.DoesNotExist:
            return Response({"error": "El género especificado no existe"}, status=HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "El usuario especificado no existe"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Error inesperado: {str(e)}"}, status=HTTP_400_BAD_REQUEST)
        

class FindReviewByDateView(APIView):
    def post(self, request):
        data = request.data
        print("Datos recibidos:", request.data)
        serializer = ReviewDateFilterSerializer(data=data)

        if serializer.is_valid():
            date = serializer.validated_data['date']
            reviews = Review.objects.filter(date=date)

            if not reviews.exists():
                return Response({"error": "No se encontraron reviews para la fecha proporcionada."}, status=HTTP_400_BAD_REQUEST)

            return Response({"success": "Reviews encontradas", "reviews": list(reviews.values())}, status=HTTP_200_OK)
        else:
            print("Errores detectados:", serializer.errors)
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)


class FindReviewByGenreView(APIView):
    def post(self,request):
        data = request.data
        genre = data.get('genre')
        serializer = ReviewGenreFilterSerializer(data=data)
        if serializer.is_valid():
            review = Review.objects.filter(genre=genre)
            return Response({"success": "Reviews found", "reviews": review.values()}, status=HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

class FindReviewByTitleView(APIView):
    def post(self,request):
        data = request.data
        title = data.get('title')
        serializer = ReviewTitleFilterSerializer(data=data)
        if serializer.is_valid():
            review = Review.objects.filter(title__icontains=title)
            return Response({"success": "Reviews found", "reviews": review.values()}, status=HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

class EditReviewView(APIView):
    def post(self, request, id):
        data = request.data
        review = Review.objects.filter(id=id).first()
        if not review:
            return Response({"error": "Review no encontrada"}, status=HTTP_404_NOT_FOUND)

        try:
            genre_name = data.get('genre')
            genre = Genre.objects.get(name=genre_name)
            data['genre'] = genre.id

            serializer = UpdateReviewSerializer(review, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "Review editada correctamente"}, status=HTTP_200_OK)
            else:
                return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)
        except Genre.DoesNotExist:
            return Response({"error": "El género especificado no existe"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Error inesperado: {str(e)}"}, status=HTTP_400_BAD_REQUEST)


class GetAllReviews(APIView):
    def get(self, request):
        contents = Review.objects.all()
        serializer = GetReviewSerializer(contents, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
        