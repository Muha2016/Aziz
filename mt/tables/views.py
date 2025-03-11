from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from reservations.models import Reservation
from django.shortcuts import render

class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request, *args, **kwargs):
        tables = self.get_queryset()
        return render(request, 'tables/table_list.html', {'tables': tables})

class AvailableTables(generics.ListAPIView):
    serializer_class = TableSerializer
    def get_queryset(self):
        date_str = self.request.query_params.get('date')
        if not date_str:
            return Table.objects.filter(is_available=True)

        try:
          date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
          return Table.objects.none()

        reserved_tables = Reservation.objects.filter(date=date).values_list('table', flat=True)
        return Table.objects.filter(is_available=True).exclude(id__in=reserved_tables)

    def get(self, request, *args, **kwargs):
        tables = self.get_queryset()
        return render(request, 'tables/available_tables.html', {'tables': tables})