from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import aboutpune
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def home(request):
    infor= aboutpune.objects.all()
    return render(request, 'index.html', {'infor':infor})

def register(request):
    if request.method=='POST':
        
        username=request.POST['first_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1== password2 :
                
            if User.objects.filter(username= username):
                messages.info(request, 'username taken')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'passsword not match')
            return redirect('register')
        
        
    else:

        return render(request, 'register.html')





def login(request):
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username= username, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'user not valid')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')