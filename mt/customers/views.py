from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from django.shortcuts import render

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
      customers = self.get_queryset()
      return render(request, 'customers/customer_list.html', {'customers': customers})

class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        customer = self.get_object()
        return render(request, 'customers/customer_detail.html', {'customer': customer})