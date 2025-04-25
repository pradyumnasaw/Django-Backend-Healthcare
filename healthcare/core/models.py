from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'patient'

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'doctor'

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
    
    class Meta:
        db_table = 'patient_doctor_mapping'
        unique_together = ('patient', 'doctor') 