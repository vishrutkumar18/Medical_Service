# from django.conf import settings
from django.db import models


class Contact(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    feedback = models.TextField(max_length=50)


class Certi(models.Model):
    fullname = models.CharField(max_length=30, null=True)
    Email = models.EmailField(max_length=30, null=True)
    # Dob = models.DateField(input_formats=['%d-%m-%Y'])
    # Gender = models.CheckConstraint
    Number_of_Passport = models.CharField(max_length=30, null=True)
    Contact_number = models.CharField(max_length=30, null=True)
    Name_of_medical_examiner = models.TextField(max_length=30, null=True)
    Approvel_number = models.TextField(max_length=50, null=True)
    Job_title = models.TextField(max_length=50, null=True)
