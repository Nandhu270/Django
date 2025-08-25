from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from employee.models import Employee
# Create your views here.

def show(request,id):
        # emp = Employee.objects.get(id = id)
        emp = get_object_or_404(Employee,id=id)
        context = {
                'emp' : emp,
        }
        return render(request,'detail.html',context)
