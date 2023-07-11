from django.db import models

from stock_flow.models import Project

ANSWER_CHOICES = (("OK", "OK"), ("NOK", "NOT OK"), ("N/A", "NOT APPLICABLE"))


class PdiCheckList(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name


class PdiCheckPoint(models.Model):
    pdi_checklist = models.ForeignKey(PdiCheckList, on_delete=models.CASCADE, related_name="check_points")
    checkpoint = models.CharField(max_length=300)

    def __str__(self):
        return self.checkpoint


class PdiAnswer(models.Model):
    pdi_check_point = models.OneToOneField(PdiCheckPoint, on_delete=models.CASCADE, related_name="answer")
    answer = models.CharField(max_length=200, choices=ANSWER_CHOICES)
    comment = models.CharField(max_length=300)


class PdiCheckpointPictures(models.Model):
    check_point = models.ForeignKey(PdiCheckPoint, on_delete=models.CASCADE, related_name="pictures")
    picture = models.ImageField(upload_to="media")
