from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from chms.models import Patient,Doctor,Appointment,Bed,Shift
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,FormView
from django import forms
from chms.forms import PatientCreateForm,DoctorCreateForm,AppointmentCreateForm,BedCreateForm,ShiftsCreateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from chms.models import Patient,Doctor,Appointment,Bed
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

class TestPageView(TemplateView):
    template_name='chms/test.html'

class ThanksPageView(TemplateView):
    template_name='chms/thanks.html'

def PatientCreate(request):
    context={}
    if request.method == 'POST':
        form=PatientCreateForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password=password)
            user=User.objects.create_user(username=username,password=password)
            user.save()
            form.save()
            messages.success(request,'account created successfully')
            patient=form.save()
            patient.save()
            messages.success(request, 'account created successfully')
            return redirect('login')
    else:
       form=PatientCreateForm()
    context['form']=form
    return render(request,"chms/patient_register.html", context)

@login_required(login_url='login')
def PatientDashboard(request):
    return render(request,'chms/patient_dashboard.html')

@login_required(login_url='login')
def PatientUpdateView(request,username):
    patient=get_object_or_404(Patient,username=username)
    form=PatientCreateForm(request.POST or None,instance=patient)
    context={}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("chms:patient_dashboard")
    return render(request,'chms/patient_update.html',{'form':form})

def PatientListView(request):
    context={}
    patients=Patient.objects.all()
    context['patients']=patients
    return render(request,'chms/patient_list.html',context)


class PatientDetailView(LoginRequiredMixin,DetailView):
    model=Patient

#class PatientList(LoginRequiredMixin,ListView):
#    return render(request,"chms/register.html", context)

class PatientProfile(LoginRequiredMixin,TemplateView):
    pass


def DoctorCreate(request):
    context={}
    if request.method == 'POST':
        form=DoctorCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            specialist=form.cleaned_data['specialist']
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password=password)
            user=User.objects.create_user(username=username,password=password)
            user.save()
            form.save()
            messages.success(request,'account created successfully')
            return redirect('login')
    else:
       form=DoctorCreateForm()
    context['form']=form
    return render(request,"chms/doctor_register.html", context)

@login_required(login_url='login')
def DoctorDashboard(request):
    return render(request,'chms/doctor_dashboard.html')

@login_required(login_url='login')
def DoctorUpdateView(request,username):
    doctor=get_object_or_404(Doctor,username=username)
    form=DoctorCreateForm(request.POST or None,instance=doctor)
    context={}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("chms:doctor_dashboard")
    return render(request,'chms/doctor_update.html',{'form':form})

def DoctorAppointmentListView(request,username):
    context={}
    doctor = Doctor.objects.filter(username__iexact=username)
    appointment=Appointment.objects.all()
    context['appointment']=appointment
    return render(request,'chms/appointment_list_doctor.html',context)

def ConfirmAppointment(request,pk):
    return render(request,'chms/confirm_appointment.html')

def DoctorListView(request):
    context={}
    doctor= Doctor.objects.all()
    context['doctor']=doctor
    return render(request,'chms/doctor_list.html',context)

@login_required
def AppointmentCreate(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username).first()
    doctor=Doctor.objects.all()
    if request.method == 'POST':
        form = AppointmentCreateForm(request.POST,instance=patient)
        if form.is_valid():
            form.save(commit=False)
            doctor=form.cleaned_data['doctor']
            app_date=form.cleaned_data['app_date']
            app_time=form.cleaned_data['app_time']
            desc=form.cleaned_data['desc']
            appointment=authenticate(request)
            appointment=Appointment.objects.create(patient=patient,doctor=doctor,app_date=app_date,app_time=app_time,desc=desc)
            appointment.save()
            form.save()
            messages.success(request,'appointment created')
            return redirect('chms:list_appointment',username=username)
    else:
        form = AppointmentCreateForm()
    context['form']=form
    return render(request,'chms/appointment_create.html',context)

def AppointmentListView(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username)
    doctor=Doctor.objects.all()
    appointment=Appointment.objects.all()
    context['appointment']=appointment
    return render(request,'chms/appointment_list.html',{'appointment':appointment,'patient':patient,'doctor':doctor})

def AppointmentDeleteView(request,pk):
    #patient = Patient.objects.filter(username__iexact=username)
    appointment=Appointment.objects.get(pk=pk)
    appointment.delete()
    return redirect("chms:list_appointment",pk)

@login_required
def BedCreate(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username).first()
    if request.method == 'POST':
        form = BedCreateForm(request.POST,instance=patient)
        if form.is_valid():
            form.save(commit=False)
            bed_number=form.cleaned_data['bed_number']
            room_type=form.cleaned_data['room_type']
            bed=authenticate(request)
            bed=Bed.objects.create(patient=patient,bed_number=bed_number,room_type=room_type)
            bed.save()
            form.save()
            messages.success(request,'bed booked')
            return redirect('chms:list_bed',username=username)
    else:
        form = BedCreateForm()
    context['form']=form
    return render(request,'chms/bed_create.html',context)

def BedListView(request,username):
    context={}
    patient = Patient.objects.filter(username__iexact=username)
    bed=Bed.objects.all()
    context['bed']=bed
    return render(request,'chms/bed_list.html',context)

def BedDeleteView(request,pk):
    bed=Bed.objects.get(pk=pk)
    bed.delete()
    return redirect("chms:list_bed",pk)

def ShiftsListView(request,username):
    context={}
    doctor= Doctor.objects.filter(username__iexact=username)
    shift=Shift.objects.all()
    context['shift']=shift
    return render(request,'chms/shifts_list.html',context)


@login_required(login_url='login')
def AdminDashboard(request):
    return render(request,'chms/admin_dashboard.html')

def UserListView(request):
    context={}
    users=User.objects.all()
    context['users']=users
    return render(request,'chms/users_list.html',context)

def UserDeleteView(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect("chms:user_list",pk)

@login_required
def ShiftCreate(request,username):
    context={}
    doctor = Doctor.objects.all()
    if request.method == 'POST':
        form = ShiftsCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            s_date=form.cleaned_data['s_date']
            s_time=form.cleaned_data['s_time']
            shift=authenticate(request)
            shift=Shift.objects.create(doctor=doctor,s_date=s_date,s_time=s_time)
            shift.save()
            form.save()
            messages.success(request,'Shift booked')
            return redirect('chms:shift_list',username=username)
    else:
        form = ShiftsCreateForm()
    context['form']=form
    return render(request,'chms/shift_create.html',context)
