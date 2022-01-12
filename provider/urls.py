
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include





  
   
 


from . import views 

urlpatterns = [
    path('provider/<int:pk>/', views.profile, name='publicProfile'),
    path('create_profile/<int:pk>/', views.createProfile, name='createProfile'),
    path('edit_profile/<int:pk>/', views.editProfile, name='editProfile'),
]
