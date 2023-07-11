from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="projects")
    project_internal_code = models.CharField(max_length=20, blank=True)
    project_customer_code = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="media/", blank=True)

    def __str__(self):
        return self.name


class CycleStage(models.Model):
    cycle_stage_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cycle_stage_name


class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name


class PartStatus(models.Model):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name


class Part(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="parts")
    serial_number = models.CharField(max_length=200)
    stage = models.ForeignKey(CycleStage, on_delete=models.CASCADE, related_name="parts")
    location = models.CharField(Location, on_delete=models.CASCADE, related_name="parts")
    status = models.ForeignKey(PartStatus, on_delete=models.CASCADE, related_name="parts")
    dispatch_date = models.DateField(blank=True)

    def __str__(self):
        return self.serial_number
