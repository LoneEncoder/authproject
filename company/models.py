from django.db import models
import uuid

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=255, null=True, blank=True)
    members = models.IntegerField(default=0)
    project_from_scratch = models.IntegerField(default=0)
    earns_upwork = models.IntegerField(default=0)
    benefits = models.CharField(max_length=255, null=True, blank=True)
    contact_us = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-updated"]

    def __str__(self):
        return self.name
