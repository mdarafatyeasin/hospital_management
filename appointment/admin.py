from django.contrib import admin
from . import models

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_types', 'appointment_status', 'symptom', 'cancel']

    def doctor_name(self, obj):
        return obj.doctor.user.first_name

    def patient_name(self, obj):
        return obj.patient.user.first_name

admin.site.register(models.Appointment, AppointmentAdmin)