from django.urls import path
from Agro_App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.login),
   path('signup/', views.signup, name='signup'),
   path('index/',views.index, name='index'),
   path('userlogout/',views.userlogout),
   path('profile/', views.profile, name='profile'),
   path('profile/delete-photo/', views.delete_photo, name='delete_photo'),
   path('products/', views.products, name='products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)