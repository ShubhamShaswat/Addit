from django.db import models
from django import forms
from django.contrib.auth.models import User



# Create your models here.

#for Signup


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    
    
        
    def __str__(self):
        return self.username
        
        
class SignUp(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    cnf_password = models.CharField(max_length=100,default = 'pass')
    
    
    def __str__(self):
        return self.name
    
class HomePost(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    post = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user
    
    
    
    
    