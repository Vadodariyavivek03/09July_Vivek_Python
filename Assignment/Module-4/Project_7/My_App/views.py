from django.shortcuts import render
from .models import Doctor

# Create your views here.

def doctor_info(request):

    doctor = Doctor(
        name='Dr. Mitesh Shah',
        specialization='Cardiology',
        experience=15,
        contact='mitesh.shah@example.com'
    )

    context = {
        'name': doctor.name,
        'specialization': doctor.specialization,
        'experience': doctor.experience,
        'contact': doctor.contact,
    }

    return render(request, 'doctor_info.html', context)