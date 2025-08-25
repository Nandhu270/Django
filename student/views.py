from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def Home(request):
    student = [
        {"id":4,"name":"Nk"},
        {"id":5,"name":"Nk"},
        {"id":6,"name":"Nk"}
    ]
    return JsonResponse(student,safe=False)