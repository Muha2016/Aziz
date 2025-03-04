from django.urls import path
from .views import TableList, AvailableTables

urlpatterns = [
    path('', TableList.as_view()),
    path('available/', AvailableTables.as_view()),
]