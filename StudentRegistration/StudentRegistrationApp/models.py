from django.db import models

# Create your models here.
class Registration(models.Model):
    ProfilePic=models.ImageField(upload_to="ProfilePic",default='')
    Name=models.CharField(max_length=50,default="")
    Branch=models.CharField(max_length=30,default="")
    Batch=models.IntegerField(default=0)

