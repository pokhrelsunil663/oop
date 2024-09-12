from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentDataView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer