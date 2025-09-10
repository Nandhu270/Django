from django.shortcuts import render, get_object_or_404
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

from rest_framework import mixins,generics,viewsets

from blog.models import Blog,Comment
from blog.serializers import BlogSerializer,CommentSerializer

#Traditional View Method

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

#Class Based Api View

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
    
    def put(self,request,id):
        serializer = EmpSerializer(self.get_object(id),data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        self.get_object(id).delete()
        return Response({"res":"Deleted Succees"}, status=status.HTTP_200_OK)

"""

#Mixins Based View

class Empl(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class EmplID(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)    

"""

# Generic Api View
"""
class Empl(generics.ListAPIView, generics.CreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
(or)
   
class Empl(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmplID(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    lookup_field = 'pk'
(or)


class EmplID(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    lookup_field = 'pk'

"""


#ViewSet 

#Method - 1 :
"""

class ViewEmployee(viewsets.ViewSet):
    def list(self,request):
        emp = Emp.objects.all()
        serializer = EmpSerializer(emp,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer  = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        emp = get_object_or_404(Emp, pk=pk)
        serializer = EmpSerializer(emp)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        emp = get_object_or_404(Emp, pk=pk)
        serializer = EmpSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        emp = get_object_or_404(Emp, pk=pk)
        emp.delete()
        return Response(status=status.HTTP_200_OK)

"""

#Method - 2

class ViewEmployee(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


# Nested Serializer

class ViewBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ViewComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ViewDetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class ViewDetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
