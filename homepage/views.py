from django.shortcuts import render,redirect

# Create your views here.

def homepage(request):
    number = ['History','Science']
    #if user.is_valid():
        
        
        
    context = {'number':number}
    
    return render(request,'homepage/home.html',context)


    
    
    
    
       