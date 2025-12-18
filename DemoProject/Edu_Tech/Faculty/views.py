from django.shortcuts import render, redirect
from Student.models import *
from Student.forms import *

# Create your views here.

def fac_login(request):
    role = request.POST.get("role", "Faculty")

    if request.method == "POST":
        u_email = request.POST['email']
        u_password = request.POST['password']

        if role == "Faculty":
            if u_email == 'faculty' and u_password == 'faculty@123':
                request.session["role"] = "faculty"
                request.session["user"] = "Faculty"
                print(" Faculty Login Successfully..!! ")
                return redirect('fac_home')
            else:
                print(" Error :: Invalid credentials..!!")
            
    return render(request, 'faculty/login.html', {"role": role})

# ---------------------------------------------------------------------------- #

def fac_home(request):
    if request.session.get("role") != "faculty":
        return redirect("/faculty/login/")
    return render(request, "faculty/home.html")
