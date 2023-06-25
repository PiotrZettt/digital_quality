from django.urls import include, path
from rest_framework import routers

from .views import AuditSerializerViewSet, QuestionSerializerViewSet, AnswerSerializerViewSet

router = routers.DefaultRouter()

router.register(r"audits", AuditSerializerViewSet)
router.register(r"questions", QuestionSerializerViewSet)
router.register(r"answers", AnswerSerializerViewSet)


urlpatterns = [path("api/", include(router.urls))]
