from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from .forms import SignUp,Login,HomePost
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse


from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms


def index(request):
    return render(request,'home/home.html')


#for login
    
def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        
        if form.is_valid():
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form = Login()
            user = authenticate(username=username,password=password)
            
            context = {'form':form,'username':username,'user':user}
            
            if user is not None:
               auth_login(request,user)
               
               #return render(request,'home/includes/afterlogin.html',context)
               return HttpResponseRedirect('/home')
            else:

                    
                failed = "Invalid Username or Password"
                context = {'failed':failed,'form':form} 
                return render(request,'home/includes/login.html',context)


            
            
            
            
        
        
        
    
    
    else:
        
        
        form = Login()
        return render(request,'home/includes/login.html',{'form':form})

      
def logout(request):
    
    auth_logout(request)
    return HttpResponseRedirect('/home/login')
            
    

#for signup 
    
def signup(request):
    if request.method == "POST":
        #form = SignUp(request.POST)
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #user = authenticate(username = username,password = password)
            #auth_login(request,user)
            #form = SignUp()
        
        args = {'form':form}
        #return render(request,'home/includes/register.html',args)
        return redirect('login')
    
    else:
        #form = SignUp()
        form = UserCreationForm()
        return render(request,'home/includes/register.html',{'form':form})
    
    

def homepost(request):
    
    if request.method == "POST":
        form=HomePost(request.POST)
        
        if form.is_valid():
            form.save()
                      
            
        return HttpResponseRedirect('/home',)
    
    
    else:
    
        form = HomePost()
        post = "here it is"
        
        return render(request,'home/home.html',{'form':form,'post':post})
    
    
def showhomepost(request):
    
    
    post=HomePost.objects.get(name="hello")
    return render(request,'home/home.html',{'post':post})    