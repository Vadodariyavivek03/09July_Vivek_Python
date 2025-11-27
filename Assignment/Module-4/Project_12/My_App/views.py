from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})

def doctor_create(request):
    form = DoctorForm()
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    return render(request, "doctor_form.html", {"form": form})

def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    form = DoctorForm(instance=doctor)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    return render(request, "doctor_form.html", {"form": form})

def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method == "POST":
        doctor.delete()
        return redirect("doctor_list")
    return render(request, "doctor_delete.html", {"doctor": doctor})
