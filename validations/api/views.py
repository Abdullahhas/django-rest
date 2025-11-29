from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# CRUD
@csrf_exempt
def std_api(request):
    if request.method == 'GET':
        student_id = request.GET.get('id')

        if (student_id):
            student = Student.objects.get(id = student_id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type = 'application/json')
        

        students = Student.objects.all()
        serializer = StudentSerializer(students , many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data , content_type = 'application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'msg' : 'Data inserted'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data , content_type = 'application/json')   
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == "PUT":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {'msg' : 'Data Updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data , content_type = 'application/json')  


    if request.method == 'DELETE':
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        response = {'msg' : 'Data Deleted'}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data , content_type = 'application/json')  
