from rest_framework import parsers, permissions, renderers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Domain
from .serializers import ClientSerializer, DomainSerializer


class ClientSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.BasePermission]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    ordering_fields = ["id"]


class DomainSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    ordering_fields = ["id"]


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)

        return Response({"token": token.key, "user_id": user.id})
