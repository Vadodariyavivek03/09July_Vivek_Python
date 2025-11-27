from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_doctor/', views.add_doctor, name="add_doctor"),
    path('edit_doctor/<int:id>/', views.edit_doctor, name="edit_doctor"),
    path('delete_doctor/<int:id>/', views.delete_doctor, name="delete_doctor"),
]