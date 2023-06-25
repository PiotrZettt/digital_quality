from django.contrib import admin
from .models import Audit, Question, Answer


class AuditAdmin(admin.ModelAdmin):
    model = Audit
    list_display = ["title", "description", "auditor", "date_created"]


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ["audit", "question"]


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ["question", "answer"]


admin.site.register(Audit, AuditAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
