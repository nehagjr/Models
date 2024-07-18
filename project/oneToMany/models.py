from django.db import models

# Create your models here.
class Department(models.Model):
    dep_nm=models.CharField(max_length=20)
    dep_desciption=models.CharField(max_length=20)
    

    def __str__(self):
        return str(self.dep_nm)
    

class Student(models.Model):
    Student_nm=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    dep_nm=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_nm    