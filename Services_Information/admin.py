from django.contrib import admin
from .models import Service, Project, Team_Member, Appointment, Newsletter

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Team_Member)
admin.site.register(Appointment)
admin.site.register(Newsletter)


# Register your models here.
