"""medSafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include





  
   
 


from patients import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/',views.signUp, name='signUp'),
    path('login/', views.loginUser, name="login"),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('confirm/,', views.confirm, name="confirm"),

    # user
    path('profile/',views.profile,name='profile'),

    # patients
    path('addPatient/', views.add_patient, name="addPatient"),
    path('searchResults/', views.search_results,name="search_results"),
    path('view_patient/<str:pk>/',views.view_patient, name='view_patient'),
    path('edit_patient/<str:pk>/',views.edit_patient, name='edit_patient'),
    # path('allPatients/',view.allPatients, name='allPatients'),
    # path('viewPatient/<int:pk>/', view.viewPatient, name="viewPatient"),
    # path('patients/', include('patients.urls')),

    # prescriptions

    path('create_prescription/<str:pk>/', views.create_prescription, name="create_prescription"),
    path('fill_prescription/<str:pk>/', views.fill_prescription, name="fill_prescription"),

    # notes

    path('create_note/<str:pk>/', views.create_note, name="create_note"),

    # profiles

    path('profile/', include('provider.urls')),

    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
