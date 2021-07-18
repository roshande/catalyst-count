import uuid
from django.db import models

# Create your models here.


class Companies(models.Model):
    class Meta:
        db_table = "companies"

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    domain = models.CharField(max_length=255, null=True, blank=True)
    year_founded = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    size_range = models.CharField(max_length=100, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.URLField(max_length=255)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()
