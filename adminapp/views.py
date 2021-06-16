from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmployeeSerializer, GameSerializer
from .models import Employee, Game
from rest_framework.authtoken import views


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('-employee_name')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-game_name')
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
