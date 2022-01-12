from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class Provider(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    providerName = models.CharField(max_length=200)
    profilePic = models.ImageField(null=None, blank=True, default='logo2.png')
    businessName = models.CharField(max_length=250)
    businessProfile = models.ImageField(null=None, blank=True, default='home.png')
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=25)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio= models.IntegerField(default=0, null=True, blank=True)
    notes = models.TextField(blank=True, default=None, null=True)
  

    def __str__(self):
        return self.providerName


