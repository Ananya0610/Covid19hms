from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='chms'

urlpatterns=[
    path("login/",auth_views.LoginView.as_view(template_name="chms/patient_login.html"),name="login_patient"),
    path("logout/", auth_views.LogoutView.as_view(template_name="chms/thanks.html"), name="logout"),
    path("register/patient/",views.PatientCreate,name='register_patient'),
    path("dashboard/patient/",views.PatientDashboard,name='patient_dashboard'),
    path("dashboard/patient/update/<str:username>/",views.PatientUpdateView,name='patient_update'),
    path("dashboard/doctor/patient/list/",views.PatientListView,name='patient_list'),
    path('dashboard/<int:pk>/detail',views.PatientDetailView.as_view(),name='patient_detail'),
    path("test/",views.TestPageView.as_view(),name="test"),
    path("thanks/",views.ThanksPageView.as_view(),name="thanks"),

    path("create/appointment/<str:username>/",views.AppointmentCreate,name="create_appointment"),
    path("dashboard/patient/list/appointment/<str:username>/",views.AppointmentListView,name="list_appointment"),
    #path('',views.AppointmentListView.as_view(),name='appointment_list'),
    #path("update/appointment/",views.AppointmentUpdate,name="update_appointment"),
    path("delete/appointment/<int:pk>/",views.AppointmentDeleteView,name="delete_appointment"),

    path("create/bed/<str:username>/",views.BedCreate,name="create_bed"),
    path("list/bed/<str:username>/",views.BedListView,name="list_bed"),
    #path("update/appointment/",views.AppointmentUpdate,name="update_appointment"),
    path("delete/bed/<int:pk>/",views.BedDeleteView,name="delete_bed"),

    path("login/",auth_views.LoginView.as_view(template_name="chms/doctor_login.html"),name="login_doctor"),
    path("register/doctor/",views.DoctorCreate,name='register_doctor'),
    path("dashboard/doctor/",views.DoctorDashboard,name='doctor_dashboard'),
    path("dashboard/doctor/update/<str:username>/",views.DoctorUpdateView,name='doctor_update'),
    path("list/doctor/",views.DoctorListView,name='doctor_list'),
    path("dashboard/doctor/list/appointment/<str:username>/",views.DoctorAppointmentListView,name="appointment_doctor"),
    path("confirm/<int:pk>/",views.ConfirmAppointment,name='confirm_appointment'),
    path("dashboard/doctor/list/shifts/<str:username>/",views.ShiftsListView,name="shifts_list"),


    path("login/",auth_views.LoginView.as_view(template_name="chms/admin_login.html"),name="login_admin"),
    path("dashboard/admin/",views.AdminDashboard,name='admin_dashboard'),
    path("list/users/",views.UserListView,name="user_list"),
    path("delete/users/<int:pk>/",views.UserDeleteView,name="delete_user"),
    #path("create/shift/<str:username>/",views.ShiftCreate,name="create_shift"),
    #path('list/shifts/<str:username>/',views.ShiftsListView,name="list_shifts"),
]
