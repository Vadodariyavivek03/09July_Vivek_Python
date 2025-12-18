from django.shortcuts import render,redirect
from Final_Project import settings
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from random import *
from django.contrib import messages

otp = 0

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

# ----------------------------------------------------------------------------------------- #

def login(request):
    if request.method=='POST':
        u_email=request.POST["email"]
        u_password=request.POST["password"]
        
        user=UserSignup.objects.filter(email=u_email,password=u_password)
        userid=UserSignup.objects.get(email=u_email)
        
        if user:
            print("Login Successfully!")
            request.session["user"]=u_email
            request.session["userid"]=userid.id
            return redirect('/')
        else:
            print("Error!Login Faild...")
    return render(request,'login.html')

# ----------------------------------------------------------------------------------------- #

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()

            #send mail
            global otp
            otp = randint(11111, 99999)
            sub = "Your OTP Verification Code"

            mail_msg=f'''Dear User\nThanks for registration with us..!!\nYour Email Verification code is : {otp}.
            \nPlease verify your account and enjoy our services!\n\nThank & Regards
            \nNotesApp Team\n+91 94XXXXX524 | vivekvadodariya783@gmail.com'''

            from_email = "vivekvadodariya783@gmail.com"
            to_email = settings.EMAIL_HOST_USER

            send_mail(subject=sub, message=mail_msg, from_email=from_email, recipient_list=[to_email])

            # msg="OTP sent to your email successfully....!!"

            return redirect('otpverify')
        else:
            print(form.errors)

    return render(request,'signup.html')

# ----------------------------------------------------------------------------------------- #

def profile(request):
    uid = request.session.get("userid")
    user = UserSignup.objects.get(id=uid)

    if request.method=='POST':
        updateReq=SignupForm(request.POST,instance=user)

        if updateReq.is_valid():
            updateReq.save()
            print("Profile Updatetd!")
            return redirect("profile")
        else:
            print(updateReq.errors)

    return render(request,'profile.html',{'user':user})
   
# ----------------------------------------------------------------------------------------- #

def notes(request):
    user=request.session.get("user")
    note_user = UserSignup.objects.get(email=user)
    if request.method=='POST':
        form=NotesForm(request.POST, request.FILES)
        if form.is_valid():       
            x = form.save(commit=False)
            x.user = note_user
            x.save()
            messages.success(request, "Notes Uploaded Successfully")
        else:
            print(form.errors)
    return render(request, 'notes.html', {'user': user})

# ----------------------------------------------------------------------------------------- #

def about(request):
    return render(request, 'about.html')

# ----------------------------------------------------------------------------------------- #   

def contact(request):
    if request.method=='POST':
        inquiry=ContactForm(request.POST)
        if inquiry.is_valid():
            inquiry.save()
            
            #Success Email Sending

            sub="Thanks for contacting us"
            mail_msg=f'''Dear {inquiry.cleaned_data.get("fullname")},\nThanks for contacting us. We will get back to you soon.
            \n\nThank & Regards,\n\nNotesApp Team\n+91 94XXXXX524 | vivekvadodariya783@gmail.com'''
            from_email = "vivekvadodariya783@gmail.com"
            to_email = settings.EMAIL_HOST_USER
            send_mail(subject=sub, message=mail_msg, from_email=from_email, recipient_list=[to_email])

            messages.success(request, "Your message has been sent successfully")

        else:
            print(inquiry.errors)

    return render(request,'contact.html')

# ----------------------------------------------------------------------------------------- #

def userlogout(request):
    logout(request)
    return redirect('/')

# ----------------------------------------------------------------------------------------- #

def otpverify(request):
    global otp
    msg = ""

    if request.method == 'POST':
        if otp == int(request.POST["otp"]):
            messages.success(request, "Verification Successful")
            return redirect("login")
        else:
            msg = "Invalid OTP...!! Please try again....!"
            messages.error(request, msg)

    return render(request, 'otpverify.html', {'msg': msg})    

# ----------------------------------------------------------------------------------------- #








