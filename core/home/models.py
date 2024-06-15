from django.db import models

# Create your models here.


class Student(models.Model):
    # id = models.AutoField()
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_address = models.TextField()
    student_age_address = models.ImageField()
    file = models.FileField()
    
    
    
    