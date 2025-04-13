from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from users.models.user_model import CustomUser


class CheckUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        email = data.get('email')

        if not email:
            return Response({"error": "El campo 'email' es obligatorio."}, status=HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email__iexact=email)

            user_data = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "password": user.password,
            }

            return Response({"success": "Usuario encontrado", "user": user_data}, status=HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=HTTP_400_BAD_REQUEST)
