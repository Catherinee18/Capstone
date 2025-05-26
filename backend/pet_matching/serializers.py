from rest_framework import serializers
from .models import PetMatchInteraction

class PetMatchInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetMatchInteraction
        fields = '__all__'
