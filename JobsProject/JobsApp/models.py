from django.db import models

# Create your models here.
class IndoreJobs(models.Model):
    desgn=models.CharField(max_length=30)
    openings=models.IntegerField()
    location=models.CharField(max_length=40)
    qual=models.CharField(max_length=40)
    exp=models.CharField(max_length=20)
    contract=models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
