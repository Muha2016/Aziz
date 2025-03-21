from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Добавление корневого URL
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
]