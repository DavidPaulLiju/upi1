from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    projects_finished = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
