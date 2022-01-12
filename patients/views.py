from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient, Prescription, Note
from .forms import PatientForm, NoteForm, PrescriptionForm, FilledForm



# Create your views here.

# intro
def home(req):
    return render(req, 'patients/home.html' )

def about(req):
    return render(req, 'patients/about.html')

def signUp(req):
    return render(req, 'patients/signUp.html')


def loginUser(req):
    if req.method == "GET":
        return render(req, 'patients/login.html', {'form':AuthenticationForm()})
    else:
            # check if username and paswword 
            user= authenticate(req, username=req.POST['username'], password=req.POST['password'])
            if user is None:
               return render(req, 'patients/login.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
            else:
                login(req, user)
                return redirect('profile')  

def contact(req):
    return render(req, 'patients/contact.html')

def confirm(req):
    return render(req, 'patients/confirm.html')



# profile
@login_required
def profile(req):
    patients = Patient.objects.filter( user=req.user)
    return render(req, 'patients/profile.html', {'patients': patients})

# patients
@login_required
def all_patients(req):
    patients = Patient.objects.order_by('-date')[:6]
    return render (req, 'patients/all_patients.html', {'patients': patients})
@login_required
def view_patient(req, pk):
    patient = Patient.objects.get(id=pk)
    prescriptions = Prescription.objects.filter(patient=pk)
    notes = Note.objects.filter(patient=pk)
    return render(req,'patients/view_patient.html',{'patient':patient, 'prescriptions':prescriptions, 'notes':notes} )

@login_required
def add_patient(req):

    if req.method == 'POST':
        form = PatientForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'patients/profile.html', { 'success':"Patient Added Successfully!"})
    form = PatientForm()
    return render (req, 'patients/addPatient.html',{'form':form})

@login_required
def edit_patient(req, pk):
    patient = Patient.objects.get(id = pk)
    form = PatientForm(instance= patient)
    if req.method == 'POST':
        form = form(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'patients/profile.html', {'success':"Patient updated successfully"})
    return render (req,'patients/editPatient.html', {'form':form})

@login_required
def search_results(req):
    if req.method == 'POST':
        searched = req.POST.get('searched')
        patients = Patient.objects.filter(healthNumber__contains=searched)
        return render (req,'patients/searched.html',{'searched':searched,'patients':patients})
    else:
        return render (req,'patients/searched.html')

# prescriptions



@login_required
def create_prescription(req, pk):
  
    if req.method == 'POST':
        form = PrescriptionForm(req.POST)
        prescribed_by = req.user
        patient = Patient.objects.get(id=pk)
        if form.is_valid():
            script = form.save(commit=False)
            script.prescribed_by = prescribed_by
            script.patient = patient
            form.save()
            return render(req, 'patients/profile.html', {'success':"Patient prescription created successfully"})
    form = PrescriptionForm()
    return render(req, 'patients/create_prescription.html', {'form':form})

@login_required
def fill_prescription(req, pk):
    
    if req.method == 'POST':
        form = FilledForm(req.POST)
        filled_by = req.user
        prescription = Prescription.objects.get(id=pk)
        if form.is_valid():
             fill = form.save(commit=False)
             fill.filled_by = filled_by
             fill.prescription = prescription
             form.save()
             return render(req, 'patients/profile.html', {'success':"Patient prescription filled successfully"})
    form = FilledForm()       
    return render(req, 'patients/fill_prescription.html', {'form':form})

# notes
@login_required
def create_note(req, pk):
    if req.method == 'POST':
        form = NoteForm(req.POST)
        reviewer = req.user
        patient = Patient.objects.get(id=pk)
        if form.is_valid():
             note = form.save(commit=False)
             note.reviewer = reviewer
             note.patient = patient
             form.save()
             return render(req, 'patients/profile.html', {'success':"Patient notes successfully"})
    form = NoteForm()       
    return render(req, 'patients/create_note.html', {'form':form})




