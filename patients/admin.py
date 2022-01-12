from django.contrib import admin
from .models import Patient, Note, Prescription, Filled

# Register your models here.


# Register your models here.



admin.site.register(Patient)
admin.site.register(Note)
admin.site.register(Prescription)
admin.site.register(Filled)
admin.site.site_header = "medSafe Admin"
admin.site.site_title  =  "medSafe admin site"
admin.site.index_title  =  "medSafe Admin"
