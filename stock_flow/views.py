from rest_framework import viewsets, permissions
from .models import Customer, Part, Project
from .serializers import CustomerSerializer, ProjectSerializer, PartSerializer


class CustomerSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    ordering_fields = ['id']


class ProjectSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    ordering_fields = ['id']


class PartSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    ordering_fields = ['id']
