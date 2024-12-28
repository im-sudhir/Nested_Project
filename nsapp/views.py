from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication


class WriteByAdminOnly(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if request.method=='GET':
            return True
        if request.method=='POST' or request.method=='PUT' or request.method=='DELETE':
            if user.is_superuser:
                return True
        return False
        

# Instructor Views
class InstructorListView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

# Course Views
class CourseListView(generics.ListCreateAPIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated,WriteByAdminOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all() 
