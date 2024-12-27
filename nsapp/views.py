from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class InstructorListView(generics.ListCreateAPIView):
    serializer_class= InstructorSerializer
    queryset= Instructor.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=InstructorSerializer
    queryset=Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    serializer_class= CourseSerializer
    queryset= Course.objects.all()
