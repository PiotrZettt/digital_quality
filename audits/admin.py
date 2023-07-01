from django.contrib import admin

from .models import Answer, Audit, Question


class AuditAdmin(admin.ModelAdmin):
    model = Audit
    list_display = ["title", "description", "date_created"]


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ["audit", "question"]


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ["question", "answer"]


admin.site.register(Audit, AuditAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
