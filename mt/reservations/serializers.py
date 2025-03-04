from rest_framework import serializers
from .models import Reservation
from customers.models import Customer
from tables.models import Table

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        