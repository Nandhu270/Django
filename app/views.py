from django.shortcuts import render
from employee.models import Employee

def home(request):
    employees = Employee.objects.all()
    
    context = {
        'employees' : employees,
    }

    return render(request,'home.html',context)