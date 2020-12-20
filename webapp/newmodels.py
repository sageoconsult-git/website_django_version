# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 15)
    account_type = models.CharField(max_length = 10)
    country = models.CharField(max_length=50)
    stateOrregion = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    class Meta:
        db_table = "UserDetails"


    #def __str__(self):
        #return self.user.username
    
    
   

