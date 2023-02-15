from django.db import models

# Create your models here.
# class detail:
#     id:int
#     name:str
#     email:str
#     pincode:int

class student(models.Model):
    name=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)