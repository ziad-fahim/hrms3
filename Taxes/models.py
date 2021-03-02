from django.db import models

# Create your models here.
class Taxes(models.Model):
    percent =  models.FloatField()
    start_range = models.IntegerField()
    end_range =  models.IntegerField(null=True)
    difference = models.IntegerField(null=True)
    tax = models.IntegerField(null=True)



