from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="projects")
    project_code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="media/", blank=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="parts")
    serial_number = models.CharField(max_length=200)
    stage = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    dispatch_date = models.DateField(blank=True)

    def __str__(self):
        return self.serial_number
