from django.urls import path
from My_App import views

urlpatterns = [
   path('', views.index, name='index'),
]
