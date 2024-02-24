from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class appointmentViewsets(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.appointmentSerializers

    def get_queryset(self):
        queryset = super().get_queryset() #sohob gulo appointment k nea asbe
        patient_id = self.request.query_params.get('patient_id') #user er patient id k nea asbe url theka
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id) #patient id diye filter korbe appointment gulo
        return queryset