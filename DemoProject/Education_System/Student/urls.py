from django.urls import path
from Student import views


urlpatterns = [
    path('', views.login),
    path('registration/', views.registration, name='registration'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]