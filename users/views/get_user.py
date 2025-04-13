from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from reviews.models import Review

class GetUsersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        try:
            review = Review.objects.get(slug=slug)
        except:
            return Response(
                {"error": "Review no encontrada"},
                status=HTTP_400_BAD_REQUEST
            )

        user_review = [{
            "name": review.user.name,
            "email": review.user.email,
        }]
        return Response({"user": user_review}, status=HTTP_200_OK)


