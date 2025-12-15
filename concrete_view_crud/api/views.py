from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import  ListCreateAPIView  , RetrieveUpdateDestroyAPIView

#CRUD using only 2 classes

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

