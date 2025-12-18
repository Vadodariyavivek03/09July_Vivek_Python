from django.urls import path
from Student import views

# Add your page urls here..

urlpatterns = [
    path('', views.index),
    path('login/', views.stu_login, name='stu_login'),
    path('register/', views.stu_register, name='stu_register'),
    path('logout/', views.stu_logout, name='stu_logout'),
    path('dashboard/', views.stu_dashboard, name='stu_dashboard'),
    path('about/', views.stu_about, name='stu_about'),
    path('profile/', views.stu_profile, name='stu_profile'),
    path('tasks/', views.tasks, name='tasks'),
    path('progress/', views.progress, name='progress'),
    path('courses/', views.courses, name='courses'),
    path('contact_us/', views.contact, name='contact'),
]