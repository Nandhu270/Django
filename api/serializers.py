from rest_framework import serializers
from student.models import Student
from emp.models import Emp

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"