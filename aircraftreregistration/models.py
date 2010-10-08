from django.db import models

class Timeline(models.Model):
    issuance_month = models.PositiveIntegerField()
    certificate_expiration = models.DateField()
    reapplication_start = models.DateField()
    reapplication_end = models.DateField()
