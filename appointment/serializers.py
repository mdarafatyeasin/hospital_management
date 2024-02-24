from rest_framework import serializers
from . import models

# write your serializers on here
class appointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'
