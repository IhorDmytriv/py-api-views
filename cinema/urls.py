from django.urls import path

from cinema.views import MovieList, MovieDetail, GenreList, GenreDetail

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]

app_name = "cinema"
