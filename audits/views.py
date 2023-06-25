from rest_framework import viewsets, permissions
from .models import Audit, Question, Answer
from .serializers import AuditSerializer, QuestionSerializer, AnswerSerializer


class AuditSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    ordering_fields = ["id"]


class QuestionSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    ordering_fields = ["id"]


class AnswerSerializerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    ordering_fields = ["id"]


