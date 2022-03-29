from django.db import models

# Create your models here.

class Student(models.Model):
    pic=models.ImageField(upload_to="propics",null=True,blank=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
