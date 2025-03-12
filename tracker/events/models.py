from django.db import models

# Create your models here.
from django.db import models


class Event(models.Model):
    event_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    url = models.URLField()
    user_agent = models.TextField()
    element = models.CharField(max_length=50, blank=True, null=True)
    element_id = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.event_type} at {self.timestamp}"
