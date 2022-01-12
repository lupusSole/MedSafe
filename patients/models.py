from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL


# Create your models here.

class Patient(models.Model):
    joined = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    healthNumber = models.CharField(max_length=25)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio= models.IntegerField(default=0, null=True, blank=True)
    notes = models.TextField(blank=True, default=None, null=True)
  

    def __str__(self):
        return self.healthNumber


class Note(models.Model):
    VOTE_TYPE = {
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),

    }
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Prescription(models.Model):
   
    prescribed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.CharField(max_length=500)
    upc = models.CharField(max_length=500, default="1345-7654-193307")
    fills = models.ManyToManyField('Filled', blank=True)
    is_filled = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    prescribed_on = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateTimeField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.medication


class Filled(models.Model):
    filled_by = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    filled_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   





