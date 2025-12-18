from django.urls import path
from Faculty import views

# Add your page urls here..

urlpatterns = [
    path('login/', views.fac_login, name='fac_login'),
    path('home/', views.fac_home, name='fac_home')
]