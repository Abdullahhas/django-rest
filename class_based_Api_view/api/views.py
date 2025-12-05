from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer

# Create your views here.


class StudentApi(APIView):
    def get(self , request , format = None):
        id =  request.data.get('id')
        if id is not None:
           stu = Student.objects.get(id = id)
           serializer = StudentSerializer(stu)
           return Response(serializer.data)
       

        stu = Student.objects.all() 
        serializer = StudentSerializer(stu , many = True)
        return Response(serializer.data)
    
    def post(self , request , format = None):
        data = request.data
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)
    
    def put(self , request , format = None):
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu  , data= request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)
    
    def delete(self , request , format = None):
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg' : 'data deleted'})










       
    
    
        
    

           




