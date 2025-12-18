from django.shortcuts import render, redirect
from User_App.models import *
from datetime import datetime 
from django.core.mail import send_mail
from Final_Project import settings
from django.contrib import messages
from User_App.forms import *
from django.db.models import Q

from User_App.views import notes


# Create your views here.

def admin_login(request):
    error_message = None

    if request.method == "POST":
        unm = request.POST['username'].strip()
        pwd = request.POST['password'].strip()
        
        if unm and pwd:
            if unm == 'admin' and pwd == 'admin@123':
                print(" Admin Login Successful..!! ")
                return redirect('admin_dashboard')
            else:
                error_message = "Invalid credentials...!! Please try again..."
                print(" Error :: Invalid credentials..!!")
        else:
            error_message = None
        
    return render(request, 'admin_login.html', {'error_message': error_message} )

# ----------------------------------------------------------------------------------------- #

def admin_dashboard(request):
    recent_users = UserSignup.objects.order_by('-id')[:5]
    total_users = UserSignup.objects.count()
    total_notes = mynotes.objects.count()
    total_inquiry = contact.objects.count()
    pending_status = mynotes.objects.filter(status='pending').count()

    context = {
        'recent_users': recent_users,
        'total_users': total_users,
        'total_notes': total_notes,
        'total_inquiry': total_inquiry,
        'pending_status': pending_status,
    }

    return render(request, 'admin_dashboard.html', context)

# ----------------------------------------------------------------------------------------- #

def admin_userdata(request):
    data=UserSignup.objects.all()

    search = request.POST.get("search")

    if search:
        users = UserSignup.objects.filter(fullname__icontains = search)
    else:
        users = UserSignup.objects.all()

    return render(request,'admin_userdata.html',{'data' : data, 'search' : search, 'users': users})

# ----------------------------------------------------------------------------------------- #

def admin_notesdata(request):
    notesdata=mynotes.objects.all()
    users = UserSignup.objects.all()

    query = request.GET.get("search", "")

    if query:
        notesdata = notesdata.filter(
            Q(user__fullname__icontains=query) |
            Q(title__icontains=query) |
            Q(desc__icontains=query) |
            Q(subject__icontains=query)
        )

    return render(request,'admin_notesdata.html',{'notesdata':notesdata, 'users': users})

# ----------------------------------------------------------------------------------------- #

def admin_logout(request):
    return redirect('admin_login')

# ----------------------------------------------------------------------------------------- #

def notes_approve(request, id):
    note = mynotes.objects.get(id=id)
    note.status = 'Approved'
    note.updated_at = datetime.now()
    note.save()

    # Email notification code
     
    subject = 'Your Note has been Approved'

    mail_msg = f'Dear {note.user.fullname},\n\nYour note titled "{note.title}" has been approved by the admin and is now available on the platform.\n\nThank you for your contribution!\n\nBest regards,\nAdmin Team'

    from_to = 'vivekvadodariya783@gmail.com'

    to_email = settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=mail_msg, from_email=from_to, recipient_list=[to_email])
    
    msg = "Note approved and user notified via email."
    messages.success(request, msg)

    return redirect('admin_notesdata')

# ----------------------------------------------------------------------------------------- #

def notes_reject(request, id):
    note = mynotes.objects.get(id=id)
    note.status = 'Rejected'
    note.updated_at = datetime.now()
    note.save()

    # Email notification code

    subject = 'Your Note has been Rejected'
   
    mail_msg = f'Dear {note.user.fullname},\n\nWe regret to inform you that your note titled "{note.title}" has been rejected by the admin.\n\nPlease review our submission guidelines and consider making necessary changes before resubmitting.\n\nBest regards,\nAdmin Team'
  
    from_to = 'vivekvadodariya783@gmail.com'
   
    to_email = settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=mail_msg, from_email=from_to, recipient_list=[to_email])
    
    msg = "Note rejected and user notified via email."
    messages.success(request, msg)

    return redirect('admin_notesdata')

# ----------------------------------------------------------------------------------------- #

def admin_settings(request):
    return render(request, 'admin_settings.html')

# ----------------------------------------------------------------------------------------- #

def admin_inquiry(request):
    inquiry_data = contact.objects.all()
    return render(request, 'admin_inquiry.html', {'inquiry_data': inquiry_data})

# ----------------------------------------------------------------------------------------- #

# def update_userdata(request, id):
#     user_data = UserSignup.objects.get(id=id)

#     if request.method == "POST":

#         form = SignupForm(request.POST, instance=user_data)

#         if form.is_valid():
#             form.save()
#             return redirect('admin_userdata')
#         else:
#             print(form.errors)

#     return redirect('admin_userdata')

def update_userdata(request, id):
    user_data = UserSignup.objects.get(id=id)

    if request.method == "POST":
        user_data.fullname = request.POST['fullname']
        user_data.email = request.POST['email']
        user_data.mobile = request.POST['mobile']
        user_data.save()

        edit_msg = "User data updated successfully...!!"
        messages.success(request, edit_msg)

        return redirect('admin_userdata')

    return redirect('admin_userdata')

# ----------------------------------------------------------------------------------------- #

def delete_userdata(request, id):
    user_data = UserSignup.objects.get(id=id)
    user_data.delete()
    return redirect('admin_userdata')

# ----------------------------------------------------------------------------------------- #

def upload_notes(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = UserSignup.objects.get(id=user_id)

        mynotes.objects.create(
            user=user,
            title=request.POST.get("title"),
            desc=request.POST.get("desc"),
            subject=request.POST.get("subject"),
            notes_file=request.FILES["notes_file"]
        )

        return redirect("admin_notesdata")
    
# ----------------------------------------------------------------------------------------- #
    
  
    




