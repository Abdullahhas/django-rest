from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , UpdateModelMixin, RetrieveModelMixin,DestroyModelMixin



# List and Create - PK not required
class LCStudentAPI(ListModelMixin , CreateModelMixin , GenericAPIView):
    queryset = Student.objects.all() #Each view is independent, and DRF needs to know which data this specific view is allowed to work with. thats why we have to write every time
    serializer_class = StudentSerializer
    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)
    
    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)
    



# Reterive , Update , Destroy - PK required
class RUDtudentAPI(UpdateModelMixin ,RetrieveModelMixin , DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self , request , *args , **kwargs):
        return self.update(request , *args , **kwargs)
    
    def get(self , request , *args , **kwargs):
        return self.retrieve(request , *args , **kwargs)

    def delete(self , request , *args , **kwargs):
        return self.destroy(request , *args , **kwargs)
    

