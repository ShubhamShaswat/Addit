# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 19:10:55 2018

@author: Shubham
"""

""" Django Forms"""

from django import forms
from .models import SignUp,Login,HomePost

from django.contrib.auth.forms import UserCreationForm



#for login

class Login(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':' username'}),label='')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','placeholder':' password'}),label='')
    
    class Meta:
        model = Login
        fields = ['username','password']


# for signup
class UserCreationForm(UserCreationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':' username'}),label='')
        password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','placeholder':' password'}),label='')


    
    
class SignUp(forms.ModelForm):
    
    #name = forms.CharField(max_length=50)
    #username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput,label='password')
    cnf_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = SignUp
        fields = ['name','username','password','cnf_password']
    

class HomePost(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'write something here'}),label='')
    
    class Meta:
        model = HomePost
        fields= ['post']