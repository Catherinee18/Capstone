from rest_framework import serializers
from .models import GroomingAppointment

class GroomingAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroomingAppointment
        fields = '__all__'
        read_only_fields = ['status']
