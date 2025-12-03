from django.db import models

# Create your models here.

class Emmployer(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=50,null=False)
    emp_email=models.EmailField(max_length=100,default="emp@org.com")
    emp_mob=models.CharField(max_length=10,unique=True)