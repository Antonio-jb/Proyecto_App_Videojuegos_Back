from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from users.models.user_model import CustomUser
from django.shortcuts import get_object_or_404


class UpdateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, id):
        data = request.data
        user = get_object_or_404(CustomUser, id=id)

        if 'email' in data:
            if CustomUser.objects.filter(email=data['email']).exclude(id=user.id).exists():
                return Response({"error": "El email ya está en uso por otro usuario."}, status=HTTP_400_BAD_REQUEST)

        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'phone' in data:
            user.phone = data['phone']
        if 'password' in data:
            user.set_password(data['password'])

        if request.user.is_superuser:
            if 'is_active' in data:
                user.is_active = data['is_active']
            if 'is_staff' in data:
                user.is_staff = data['is_staff']
            if 'is_superuser' in data:
                user.is_superuser = data['is_superuser']

        try:
            user.save()
            return Response({"success": "Usuario actualizado correctamente"}, status=HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Error al actualizar el usuario: {str(e)}"}, status=HTTP_400_BAD_REQUEST)
