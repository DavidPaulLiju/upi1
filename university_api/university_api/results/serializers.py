from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'salary', 'projects_finished', 'experience', 'nationality', 'gender', 'age', 'feature1', 'feature2', 'feature3', 'feature4']
