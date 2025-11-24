from django.urls import path
from My_App import views

urlpatterns = [
   path('', views.doctor_profile, name='doctor_profile'),
]
