from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register_patient(request):

    if request.method == 'POST':
        return HttpResponse('Patient registered successfully!')
    
    return render(request, 'index.html')