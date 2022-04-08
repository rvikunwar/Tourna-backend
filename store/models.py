from django.db import models
from django.contrib.auth.models import User

REGISTRATION_CHOICES=(
    ('1','OPEN'),
    ('2','CLOSED')
)

class Tournament(models.Model):
    name=models.CharField(max_length=100,null=True)
    date_time=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=2000,null=True)
    timeline=models.TextField(max_length=2000,null=True,blank=True)
    submission=models.TextField(max_length=2000,null=True,blank=True)
    rules=models.TextField(max_length=2000,null=True,blank=True)
    registration=models.TextField(max_length=200,null=True,blank=True)
    contact=models.CharField(max_length=100,null=True,blank=True)
    amount=models.IntegerField(null=True)
    prize=models.IntegerField(null=True)
    open_closed=models.CharField(
        max_length = 20,
        choices = REGISTRATION_CHOICES,
        default = '1'
        )
    link=models.CharField(max_length=400,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


class Contact(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=30,blank=False)
    phone_no=models.IntegerField(null=False)
    message=models.TextField(max_length=1000,blank=False)
    
    

   
