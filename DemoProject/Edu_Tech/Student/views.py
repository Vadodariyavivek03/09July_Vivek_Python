from django.shortcuts import render, redirect
from .forms import *
# from django.contrib.auth import logout
# from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

# ----------------------------------------------------------------------------------- #

def stu_login(request):
    role = request.POST.get("role", "Student")

    if request.method == "POST":
        u_email = request.POST['email']
        u_password = request.POST['password']

        if role == "Student":
            user = Student.objects.filter(email=u_email, password=u_password)
            userid=Student.objects.get(email=u_email)

            if user:
                print("Login Successfully..!!")

                request.session['user'] = u_email
                request.session["userid"]=userid.id

                return redirect('stu_dashboard')
            
            else:
                print("Error..!! Failed to Login..!!")
            
    return render(request, 'login.html', {"role": role})

# ----------------------------------------------------------------------------------- #

def stu_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/?role=student')
        else:
            print(form.errors)
            
    return render(request, 'register.html')

# ----------------------------------------------------------------------------------- #

def stu_logout(request):
    return redirect('stu_login')

# ----------------------------------------------------------------------------------- #

def stu_dashboard(request):
    return render(request, 'dashboard.html')

# ----------------------------------------------------------------------------------- #

def stu_about(request):
    return render(request, 'about.html')

# ----------------------------------------------------------------------------------- #

def stu_profile(request):
    user_id = request.session.get("userid")

    if not user_id:
        return redirect("stu_login")

    student = Student.objects.get(id=user_id)

    if request.method =="POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()
            print("Profile Updated Successfully...!!")
            return redirect("stu_profile")
        else:
            print(form.errors)

    else:
        form = ProfileEditForm(instance=student)

    context = {
        "student": student,
        "form" : form,
        "courses": student.courses.all() if hasattr(student, "courses") else []
    }

    return render(request, "profile.html", context)

# ----------------------------------------------------------------------------------- #

def tasks(request):
    return render(request, 'tasks.html')

# ----------------------------------------------------------------------------------- #

def progress(request):
    return render(request, 'progress.html')

# ----------------------------------------------------------------------------------- #

def courses(request):
    return render(request, 'courses.html')

# ----------------------------------------------------------------------------------- #

def contact(request):
    if request.method == "POST":
        inquiry=ContactForm(request.POST)

        if inquiry.is_valid():
            inquiry.save()
        else:
            print(inquiry.errors)
            
    return render(request, 'contact_us.html')

# ----------------------------------------------------------------------------------- #


