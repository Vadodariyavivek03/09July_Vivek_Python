from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        
        user=UserSignup.objects.filter(email=em,password=pa)
        if user:
            print("Login Successfully!")
            request.session['user']=em
            return redirect('index')
        else:
            print("Error!Login faild...")

    return render(request,'login.html')

# ------------------------------------------------------------------------------------------- #

def signup(request):
    if request.method == "POST":

        form=SignupForm(request.POST) 
        if form.is_valid():
            form.save()
            print("Sign Up Successfully")
            return redirect("/")
        else:
            print(form.errors)
    return render(request, 'signup.html')

# ------------------------------------------------------------------------------------------- #

def index(request):
    user = request.session.get('user')
    return render(request,'index.html',{'user': user})

# ------------------------------------------------------------------------------------------- #

def userlogout(request):
    logout(request)
    return redirect('/')

# ------------------------------------------------------------------------------------------- #

def profile(request):
    user = request.session.get("user")   
    
    if not user:
        return redirect("login")  
    
    user_record = UserSignup.objects.get(email=user)

    profile, created = Profile.objects.get_or_create(user=user_record)

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name")
        profile.phone = request.POST.get("phone")
        profile.address = request.POST.get("address")

        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES["profile_image"]

        if request.FILES.get("land_document"):
            profile.land_document = request.FILES["land_document"]

        if request.FILES.get("id_document"):
            profile.id_document = request.FILES["id_document"]

        profile.save()
        messages.success(request, "Profile Updated Successfully") 
        return redirect("profile")

    return render(request, "profile.html", {"profile": profile, "user": user})

# ------------------------------------------------------------------------------------------- #

def delete_photo(request):
    user = request.session.get("user")
    user_record = UserSignup.objects.get(email=user)

    profile = Profile.objects.get(user=user_record)

    if profile.profile_image:
        profile.profile_image.delete(save=False)
        profile.profile_image = None
        profile.save()

    messages.success(request, "Profile photo removed")
    return redirect("profile")

# ------------------------------------------------------------------------------------------- #

def products(request):
    return render(request,'products.html')

# ------------------------------------------------------------------------------------------- #