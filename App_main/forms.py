from django import forms
from django.contrib.auth.forms import User, UserCreationForm
from App_main.models import *


# for admin signup
class AdminSignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


# for student related form
class DoctorUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['address', 'mobile', 'department', 'status', 'profile_pic']


# for teacher related form
class PatientUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class PatientForm(forms.ModelForm):
    # this is the extrafield for linking patient and their assigend doctor
    # this will show dropdown __str__ method doctor model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId = forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),
                                              empty_label="Name and Department", to_field_name="user_id")

    class Meta:
        model = Patient
        fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']


class AppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),
                                      empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId = forms.ModelChoiceField(queryset=Patient.objects.all().filter(status=True),
                                       empty_label="Patient Name and Symptoms", to_field_name="user_id")

    class Meta:
        model = Appointment
        fields = ['description', 'status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),
                                      empty_label="Doctor Name and Department", to_field_name="user_id")

    class Meta:
        model = Appointment
        fields = ['description', 'status']


# for contact us page
class ContactusForm(forms.ModelForm):

    class Meta:
        model = FeedBack
        fields = "__all__"
