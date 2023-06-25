from django.contrib import admin
from .models import Customer, Project, Part


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ["name"]


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["customer", "project_code", "name", "picture"]


class PartAdmin(admin.ModelAdmin):
    model = Part
    list_display = ["project", "serial_number"]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Part, PartAdmin)
