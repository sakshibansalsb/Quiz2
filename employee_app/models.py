from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    date_joined = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()
