from django.urls import path
from Agro_App import views

urlpatterns = [
   path('', views.login),
   path('signup/', views.signup, name='signup'),
   path('index/',views.index, name='index'),
   path('userlogout/',views.userlogout),
]
