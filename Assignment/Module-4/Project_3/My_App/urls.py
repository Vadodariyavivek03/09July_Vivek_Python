from django.urls import path
from My_App import views

urlpatterns = [
    path('', views.register_patient, name='register_patient'),
]