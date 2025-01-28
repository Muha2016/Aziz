from django.urls import path
from .views import movies_list, movie_detail

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('<int:id>/', movie_detail, name='movie_detail'),
]
