from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from rest_framework import viewsets

class studentModelViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class=studentSerializer
