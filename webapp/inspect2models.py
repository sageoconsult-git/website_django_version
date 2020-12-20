from django.db import models
from django.contrib.auth.models import User


class Careers(models.Model):
    application_id = models.AutoField(primary_key=True)
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'careers'


class ContactUs(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    enquiry_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'contact_us'
