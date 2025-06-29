from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Patient(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100, default='Unknown')
    discharge_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.name



class Room(models.Model):
    ROOM_TYPES = [
        ('General', 'General'),
        ('ICU', 'ICU'),
        ('Private', 'Private'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"


    
class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ambulance(models.Model):
    vehicle_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_number


class PatientDocument(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    document = models.FileField(upload_to='patient_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.document.name}"
