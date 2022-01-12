
from django.db.models import fields
from django.forms import ModelForm
from .models import Patient, Note, Prescription, Filled

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('body', 'value')

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ('medication', 'expires_on', 'notes')

class FilledForm(ModelForm):
    class Meta:
        model = Filled
        fields = '__all__'