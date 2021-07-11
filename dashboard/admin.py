from django.contrib import admin

# Register your models here.
from .models import DataCount, DashboardConfig

admin.site.register(DataCount)
admin.site.register(DashboardConfig)
