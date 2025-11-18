from django.urls import path
from Road_App import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('mechanic_dashboard/', views.mechanic_dashboard, name='mechanic_dashboard'),
    path('logout/', views.user_logout, name='logout'),
]
