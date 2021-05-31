from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .sereializers import EmployeeSerializer
from .models import Employee


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('-date_joined')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
