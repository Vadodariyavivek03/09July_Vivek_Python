from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor

def index(request):
    doctors = Doctor.objects.all()
    return render(request, "index.html", {"doctors": doctors})

def add_doctor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        specialty = request.POST.get("specialty")
        phone = request.POST.get("phone")

        doctor = Doctor.objects.create(
            name=name, specialty=specialty, phone=phone
        )

        return JsonResponse({
            "id": doctor.id,
            "name": doctor.name,
            "specialty": doctor.specialty,
            "phone": doctor.phone,
            "success": True
        })

def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":
        doctor.name = request.POST.get("name")
        doctor.specialty = request.POST.get("specialty")
        doctor.phone = request.POST.get("phone")
        doctor.save()

        return JsonResponse({
            "id": doctor.id,
            "name": doctor.name,
            "specialty": doctor.specialty,
            "phone": doctor.phone,
            "success": True
        })

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()

    return JsonResponse({"success": True})
