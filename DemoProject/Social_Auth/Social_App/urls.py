from django.urls import path
from Social_App import views

# Add your page urls here..

urlpatterns = [
    path('', views.login),
    path('index/', views.index, name='index'),
]