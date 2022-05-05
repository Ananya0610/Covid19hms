from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from chms.models import Patient,Doctor,Appointment,Bed,Shift,User

bld_grp=(
        (1, 'A+'),
        (2, 'A-'),
        (3, 'B+'),
        (4, 'B−'),
        (5, 'AB+'),
        (6,'AB−'),
        (7,'O+'),
        (8,'O−'))
gender=(
    (1,'FEMALE'),
    (2,'MALE'),
    (3,'OTHER'),
    )

sts=(
    (1,'First Dose'),
    (2,'Second Dose'),
    )
rtype=(
       (1,'PRIVATE ROOM'),
       (2,'EMEREGENCY WARD'),
       (3,'COVID-19 WARD'),
       (4,'3-BED SHARED'),
)
sps=(
     (1,'Orthopedics'),
     (2,'Gynecology'),
     (3,'Dermatology'),
     (4,'Pediatrics'),
     (5,'Radiology'),
     (6,'Ophthalmology'),
     (7,'ENT'),
     (8,'Neurology'),
     (9,'Urology'),
     (10,'Surgery'),

)


class PatientCreateForm(forms.ModelForm):
    fname=forms.CharField(label="First Name")
    lname=forms.CharField(label="Last Name")
    dob = forms.DateField(label="Date Of Birth (yyyy-mm-dd)")
    blood_grp=forms.CharField(label="Blood Group",widget=forms.Select(choices=bld_grp))
    gnd=forms.CharField(label="Gender",widget=forms.Select(choices=gender))
    ph_no=forms.CharField(label="Phone Number")
    email_id=forms.EmailField(label="Email")
    vacc_sts=forms.CharField(label="Vaccination Status",widget=forms.Select(choices=sts))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = models.Patient
        fields = ['fname','lname','username','dob','age','blood_grp','gnd','ph_no','email_id','vacc_sts']

        def save(self, commit=True):
            user = super(PatientCreateForm,self).save(commit=False)
            user.username = self.cleaned_data["username"]
            user.password=self.cleaned_data['password']
            if commit:
                user.save()
            return user


class DoctorCreateForm(forms.ModelForm):
    fname=forms.CharField(label="First Name")
    lname=forms.CharField(label="Last Name")
    gnd=forms.CharField(label="Gender",widget=forms.Select(choices=gender))
    ph_no=forms.CharField(label="Phone Number")
    email_id=forms.EmailField(label="Email")
    specialist=forms.CharField(label="Doctor's Specialization",widget=forms.Select(choices=sps))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = models.Doctor
        fields = ['fname','lname','username','gnd','ph_no','email_id','specialist']

        def save(self, commit=True):
            user = super(DoctorCreateForm, self).save(commit=False)
            user.username = self.cleaned_data["username"]
            user.password=self.cleaned_data['password']
            if commit:
                user.save()
            return user

class AppointmentCreateForm(forms.ModelForm):
    #patient= forms.ModelMultipleChoiceField(queryset=Patient.objects.all())
    class Meta:
        model = models.Appointment
        fields = ['patient','doctor','app_date','app_time','desc']

        def save(self, commit=True):
            appointment = super(AppointmentCreateForm,self).save(commit=False)
            if commit:
                appointment.save()
            return appointment


class BedCreateForm(forms.ModelForm):
    room_type=forms.CharField(label="Room Type",widget=forms.Select(choices=rtype))
    class Meta:
        model = models.Bed
        fields = ['bed_number','patient','room_type']

        def save(self, commit=True):
            bed = super(BedCreateForm, self).save(commit=False)
            #user.username = self.cleaned_data["username"]
            #user.password=self.cleaned_data['password']
            if commit:
                bed.save()
            return bed

class ShiftsCreateForm(forms.ModelForm):
    sdate=forms.DateTimeField(label='Shift Date')
    stime=forms.DateTimeField(label='Shift Time')
    class Meta:
        model = models.Shift
        fields = ['doctor','sdate','stime']

        def save(self, commit=True):
            shift = super(ShiftsCreateForm,self).save(commit=False)
            if commit:
                shift.save()
            return shift
