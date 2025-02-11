from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todos/new/', views.todo_create, name='todo_create'),
    path('todos/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]