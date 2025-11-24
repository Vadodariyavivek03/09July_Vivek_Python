from django.shortcuts import render

# Create your views here.

def doctor_profile(request):

    doctor = {
    'name': 'Dr. Mitesh Shah',
    'specialty': 'Cardiologist',
    'experience': '10 years',
    'contact': 'miteshshah@example.com'
    }
    
    return render(request, 'index.html', {'doctor': doctor})