from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView , ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView , RetrieveUpdateDestroyAPIView

#get all the data
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Create data
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# get single object
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# update data
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#Delete data
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer







