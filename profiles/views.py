from rest_framework import permissions, viewsets

from .models import Profile
from .serializers import ProfileSerializer


class ProfileSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.order_by("id")
    serializer_class = ProfileSerializer
    ordering_fields = ["id"]
