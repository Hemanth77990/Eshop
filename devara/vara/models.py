from django.db import models

# Create your models here.
class course(models.Model):
    top=models.CharField(max_length=200)
    img=models.ImageField(upload_to='photos/')
    course=models.CharField(max_length=200)
    fees=models.IntegerField()
    

