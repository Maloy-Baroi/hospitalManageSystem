from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from App_main.models import *


# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Appointment, AppointmentAdmin)


class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass


admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
