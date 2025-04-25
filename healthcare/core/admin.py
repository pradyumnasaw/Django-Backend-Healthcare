from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'user')  
    search_fields = ('name',)  

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')  
    search_fields = ('name', 'specialty')  


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor')  
    search_fields = ('patient__name', 'doctor__name')  