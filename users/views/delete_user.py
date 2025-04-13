from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from users.models import CustomUser


class DeleteUserView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, email):
        try:
            user = CustomUser.objects.get(email=email)
            user.delete()
            return Response(
                {"success": "Usuario eliminado"},
                status=HTTP_200_OK
            )
        except:
            return Response(
                {"error": "Usuario no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )