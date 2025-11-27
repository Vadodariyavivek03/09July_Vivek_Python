from django.urls import path
from My_App import views

urlpatterns = [
        path('', views.index, name='index'),
        path('signup/', views.signup, name='signup'),
        path('home/',views.home, name='home'),
        path('userlogout/',views.userlogout , name='userlogout'),
]