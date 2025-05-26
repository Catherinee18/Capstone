from rest_framework import viewsets, permissions
from .models import GroomingAppointment
from .serializers import GroomingAppointmentSerializer

class GroomingAppointmentViewSet(viewsets.ModelViewSet):
    queryset = GroomingAppointment.objects.all()
    serializer_class = GroomingAppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter(pet__owner=self.request.user)
