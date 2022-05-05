from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
#from django.contrib.auth import get_user_model
#User=get_user_model()
#class User(AbstractUser):
#    is_patient=models.BooleanField(default=False)
#    is_doctor=models.BooleanField(default=False)
#    is_admin=models.BooleanField(default=False)

#    def __str__(self):
#        return "@{}".format(self.username)

class Patient(models.Model):
    user = models.OneToOneField(User,related_name='patient',null=True,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    dob = models.DateField(null=True)
    age=models.PositiveIntegerField(null=True, blank=True)
    bld_grp=(
            (1, 'A+'),
            (2, 'A-'),
            (3, 'B+'),
            (4, 'B−'),
            (5, 'AB+'),
            (6,'AB−'),
            (7,'O+'),
            (8,'O−'))
    blood_grp=MultiSelectField(choices=bld_grp, null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    gender=(
        (1,'FEMALE'),
        (2,'MALE'),
        (3,'OTHER'),
        )
    gnd=MultiSelectField(choices=gender)
    ph_no=models.CharField(max_length=15,null=False, blank=False, unique=True)
    email_id=models.EmailField(max_length=50, unique=True)
    sts=(
        (1,'First Dose'),
        (2,'Second Dose'),
        )
    vacc_sts=MultiSelectField(choices=sts)
    def __str__(self):
        return self.fname+" "+self.lname
    def get_absolute_url(self):
        return reverse('chms:patient_dashboard', kwargs={'pk':self.pk})

class Doctor(models.Model):
    user = models.OneToOneField(User,related_name='doctor',null=True,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20,null=True)
    gender=(
        (1,'FEMALE'),
        (2,'MALE'),
        (3,'OTHER'),
        )
    gnd=MultiSelectField(choices=gender)
    ph_no=models.CharField(max_length=15,null=False, blank=False, unique=True)
    email_id=models.EmailField(max_length=254, unique=True)
    specialist=models.CharField(max_length=20)

    def __str__(self):
        return self.fname+" "+self.lname

class Bed(models.Model):
    bed_number=models.CharField(max_length=50)
    patient= models.ForeignKey("Patient", on_delete=models.CASCADE,null=True)
    rtype=(
           (1,'PRIVATE ROOM'),
           (2,'EMEREGENCY WARD'),
           (3,'COVID-19 WARD'),
           (4,'3-BED SHARED'),
    )
    room_type=MultiSelectField(choices=rtype)

    def __str__(self):
        return self.bed_number

class Appointment(models.Model):
    patient = models.ForeignKey("Patient",related_name="patient",on_delete=models.CASCADE,null=True)
    doctor= models.ForeignKey("Doctor",related_name='doctor', on_delete=models.CASCADE,null=True)
    app_date=models.DateField(null=True)
    app_time=models.TimeField(null=True)
    desc=models.TextField()

    def get_absolute_url(self):
        return reverse("chms:appointment_list",kwargs={'pk':self.pk})


class Shift(models.Model):
    doctor = models.ForeignKey("Doctor",null=True, on_delete=models.CASCADE)
    sdate=models.DateTimeField(null=False)
    stime=models.DateTimeField()
