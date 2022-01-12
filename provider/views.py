from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Provider
from .forms import ProviderForm

# from .forms import PatientForm, NoteForm, PrescriptionForm, FilledForm

# Create your views here.

def profile(req,pk):
    profile = Provider.objects.get(id = pk)
    return render(req, 'provider/profile.html', {'profile':profile} )

@login_required
def editProfile(req,pk):
    profile = Provider.objects.get(id = pk)
    form = ProviderForm(instance=profile)

    if req.method=='POST':
        form = form(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'provider/profile.html', {'success':"Profle Updated Successfully"})

    form = ProviderForm(instance=profile)
    return render(req, 'provider/editProfile.html', {'form':form} )
        

@login_required
def createProfile(req,pk):
    form = ProviderForm()
    if req.method == 'POST':
        try:
            form.save()
            return render(req, 'provider/profile.html', {'success':"Profle Created Successfully"})
        except IntegrityError:
            return render(req, 'provider/newProfile.html', {'error':"Error Please Try Again", 'form': form})
        
        
    return render(req, 'provider/newProfile.html', {'form':form})