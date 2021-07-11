from django.db import models

from rest_framework import serializers


class DashboardConfig(models.Model):
    week = models.IntegerField(default=20, blank=True, null=True)
    stage_week = models.IntegerField(default=6, blank=True, null=True)
    last_update = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.last_update)


class DataCount(models.Model):
    stage = models.CharField(max_length=40)
    pass_count = models.IntegerField()
    fail_count = models.IntegerField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.stage)


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCount
        fields = ('stage', 'pass_count', 'fail_count')
