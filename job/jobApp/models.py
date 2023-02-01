from django.db import models

# Create your models here.
class Applicant(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    meritalstatus = models.CharField(max_length=100)
    phonenumber = models.IntegerField()