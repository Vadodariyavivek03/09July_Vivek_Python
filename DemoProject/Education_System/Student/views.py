from django.shortcuts import render, redirect
from random import *
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    error = None

    if request.method == "POST":
        u_email = request.POST["email"]
        u_password = request.POST["password"]

        # Try to find user
        user = Student.objects.filter(email=u_email, password=u_password).first()

        if user:
            print("Login Successfully!")
            request.session["user"] = user.email
            request.session["userid"] = user.id
            return redirect('index')
        else:
            print("Error! Login Failed...")
            error_msg = "Invalid email or password"
            messages.error()

    return render(request, 'login.html', {'error': error})

def registration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(forms.error)
    
    return render(request,'registration.html')

def logout(request):
    return redirect('/')

def profile(request):
    return render(request, 'profile.html')





