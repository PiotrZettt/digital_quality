from django.db import models

from accounts.models import User


class Audit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    auditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="audits")
    date_created = models.DateField(auto_now=True)


class Question(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=300)


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="answer")
    answer = models.BooleanField()
    comment = models.CharField(max_length=300, default="")


class Picture(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="pictures")
    picture = models.ImageField(upload_to="media")
