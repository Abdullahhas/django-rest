from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def crud(request):
    if request.method == "GET":
        id = request.GET.get('id')

        if id :
            student = Student.objects.get(id = id)
            serializer =  StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type = 'application/json')
        
        student = Student.objects.all()
        print("complex data : ",student)
        serializer =  StudentSerializer(student , many = True)
        print("serializer or dict : ",serializer.data)
        json_data = JSONRenderer().render(serializer.data)
        print("json data : ",json_data)
        return HttpResponse(json_data , content_type = 'application/json')
    

    if request.method == 'POST':
        json_data = request.body
        print("Json data :" , json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print("python data or dict : " , python_data)
        serializer = StudentSerializer(data = python_data)
        print("Complex or deserialized data : ", serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type = 'application/json')


    if request.method == "PUT":
        json_data = request.body
        print("Json data :" , json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print("python data or dict : " , python_data)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu , data = python_data , partial = True)
        print("Complex or deserialized data : ", serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type = 'application/json')


    if request.method == "DELETE":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print("python data or dict : " , python_data)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg' 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data , content_type = 'application/json')




