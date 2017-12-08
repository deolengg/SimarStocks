from __future__ import unicode_literals

from django.db import models
# Create your models here.

class GraphToDisplay(models.Model):
    date = models.CharField(max_length=42)
    three = models.FloatField()
    twelve = models.FloatField()
    thirtySix = models.FloatField()

