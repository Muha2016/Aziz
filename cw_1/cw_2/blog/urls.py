from django.urls import path
from .views import articles_list, article_detail

urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('<int:id>/', article_detail, name='article_detail'),
]
