from rest_framework import generics, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer
from customers.models import Customer
from tables.models import Table
from django.shortcuts import render

class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        # ... (ваш код)
        pass
    
    def get(self, request, *args, **kwargs):
        reservations = self.get_queryset()
        return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get(self, request, *args, **kwargs):
        reservation = self.get_object()
        return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

class UserReservations(generics.ListAPIView):
    serializer_class = ReservationSerializer
    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs['user_id']
        return Reservation.objects.filter(customer_id=user_id)

    def get(self, request, *args, **kwargs):
        reservations = self.get_queryset()
        return render(request, 'reservations/user_reservations.html', {'reservations': reservations})
    from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from customers.models import Customer
from tables.models import Table

class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get(self, request, *args, **kwargs):
        reservations = self.get_queryset()
        customers = Customer.objects.all()
        tables = Table.objects.all()
        return render(request, 'reservations/reservation_list.html', {'reservations': reservations, 'customers': customers, 'tables': tables})

    def post(self, request, *args, **kwargs):
        customer_id = request.POST.get('customer')
        table_id = request.POST.get('table')
        date = request.POST.get('date')
        time = request.POST.get('time')

        customer = Customer.objects.get(id=customer_id)
        table = Table.objects.get(id=table_id)

        Reservation.objects.create(customer=customer, table=table, date=date, time=time)
        return redirect('reservations') # Замените 'reservations' на URL вашего списка бронирований