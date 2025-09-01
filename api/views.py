from django.shortcuts import render
from django.http import JsonResponse

from student.models import Student
from .serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from emp.models import Emp
from .serializers import EmpSerializer
from django.http import Http404

@api_view(["GET","POST"])
def Home(request):
    if request.method == "GET":
        student = Student.objects.all()
        # print(student)
        # student_list = list(student.values())
        # print(student_list)
        # return JsonResponse(student_list,safe=False)
        # print(serializer.data)
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def FetchByid(request,id): 
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        res = {"response":"Student Not Found"}
        return Response(res,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == "DELETE":
        student.delete()
        return Response({"res":"Deleted record Successfully"}, status=status.HTTP_204_NO_CONTENT)


class Employees(APIView):
    def get(self,request):
        emp = Emp.objects.all()
        serializer = EmpSerializer(emp,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)
    
class EmployeeId(APIView):

    def get_object(self,id):
        try:
            return Emp.objects.get(pk=id)
        except Emp.DoesNotExist:
            raise Http404
        
    def get(self,request,id):
        serializer = EmpSerializer(self.get_object(id))
        return Response(serializer.data,status=status.HTTP_200_OK)


        