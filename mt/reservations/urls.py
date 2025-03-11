from django.urls import path
from .views import ReservationListCreate, ReservationDetail, UserReservations

urlpatterns = [
    path('', ReservationListCreate.as_view(), name='reservations'),
    path('<int:pk>/', ReservationDetail.as_view(), name='reservation_detail'),
    path('user/', UserReservations.as_view(), name='user_reservations'),
]
from django.urls import path
from .views import ReservationListCreate, ReservationDetail, UserReservations

urlpatterns = [
    path('', ReservationListCreate.as_view(), name='reservations'),
    path('add', ReservationListCreate.as_view(), name='reservations_add'),
    path('<int:pk>/', ReservationDetail.as_view(), name='reservation_detail'),
    path('user/', UserReservations.as_view(), name='user_reservations'),
]