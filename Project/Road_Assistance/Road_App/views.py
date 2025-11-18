from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

# ----------------------------------------------------------------------------------------- #

def login(request):

    if request.method == 'POST':
        em = request.POST.get('email')
        pa = request.POST.get('password')
        role = request.POST.get('role')  

        if not role:
            print("ERROR: No role received")
            return render(request, "login.html", {"error": "Role missing"})

        try:
            user = UserSignup.objects.get(email=em, password=pa, role=role)

            request.session['user'] = user.email
            request.session['role'] = user.role

            print("Login Successful!")

            if user.role == "user":
                return redirect("user_dashboard")

            if user.role == "mechanic":
                return redirect("mechanic_dashboard")

        except UserSignup.DoesNotExist:
            print("Invalid login")

    return render(request, "login.html")       

# ----------------------------------------------------------------------------------------- #

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            print("Sign Up Successfully!")
            return redirect("/login")   # after signup go to login
        
        else:
            print(form.errors)

    else:
        form = SignupForm()

    return render(request, 'signup.html', {"form": form})

# ----------------------------------------------------------------------------------------- #

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

# ----------------------------------------------------------------------------------------- #

def mechanic_dashboard(request):
    return render(request, 'mechanic_dashboard.html')

# ----------------------------------------------------------------------------------------- #

def user_logout(request):
    logout(request)
    return redirect('/login')

# ----------------------------------------------------------------------------------------- #