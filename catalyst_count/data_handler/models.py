from django.db import models

# Create your models here.

class Companies(models.Model):
    class Meta:
        db_table = "companies"

    #name,domain,year founded,industry,size range,locality,country,linkedin url,current employee estimate,total employee estimate
    name = models.CharField(max_length=100, null=False, blank=False)
    domain = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    linkedin_url = models.URLField(max_length=100)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()
