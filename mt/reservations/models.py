from django.db import models
from customers.models import Customer
from tables.models import Table
import datetime

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField(default=datetime.time(12, 0))
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f'Reservation for {self.customer.name} on {self.date} at {self.time}'
    