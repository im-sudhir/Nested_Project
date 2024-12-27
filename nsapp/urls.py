from django.urls import path
from .views import *

urlpatterns = [
    path('instructors', InstructorListView.as_view()),
    path('instructors/<int:pk>', InstructorDetailView.as_view()),
    path('courses', CourseListView.as_view()),
]
