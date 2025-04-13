from django.urls import path
from videogames.views import GetVideogameByTitleView, GetAllVideogames, GetGenre

urlpatterns = [
    path('v1/videogames/get/<str:title>/', GetVideogameByTitleView.as_view(), name='get-videogame'),
    path('v1/videogames/get-videogames/', GetAllVideogames.as_view(), name='get-videogames'),
    path('v1/genre/get-genre/', GetGenre.as_view(), name='get-genre'),
]
