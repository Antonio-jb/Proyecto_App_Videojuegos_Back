from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from reviews.models import Review


class DeleteReviewView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, id):
        try:
            reviews = Review.objects.get(id=id)
            reviews.delete()
            return Response(
                {"success": "Review eliminada"},
                status=HTTP_200_OK
            )
        except:
            return Response(
                {"error": "Review no encontrada"},
                status=HTTP_400_BAD_REQUEST
            )