from django.urls import path

from users.views import GetUsersView, CheckUserView, DeleteUserView, UpdateUserView
from users.views.create_user import CreateNewUserView

urlpatterns = [
    path("v1/review/<slug:slug>/user/", GetUsersView.as_view(), name="get-user"),
    path("v1/create-user/", CreateNewUserView.as_view(), name="create-user"),
    path("v1/get-user/", CheckUserView.as_view(), name="user"),
    path("v1/delete-user/<str:email>/", DeleteUserView.as_view(), name="delete-user"),
    path("v1/update-user/<int:id>/", UpdateUserView.as_view(), name="update-user")
]