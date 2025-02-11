from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('threads/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('threads/new/', views.thread_create, name='thread_create'),
    path('threads/<int:pk>/edit/', views.thread_edit, name='thread_edit'),
    path('threads/<int:pk>/delete/', views.thread_delete, name='thread_delete'),
    path('threads/<int:thread_pk>/post/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
]