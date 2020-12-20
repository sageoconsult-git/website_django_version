from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    account_type = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    stateorregion = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)

    class Meta:
        db_table = 'userdetails'

    def __str__(self):
        return self.first_name +" "+ self.last_name


class UnitDetails(models.Model):
    user = models.ForeignKey(to=UserDetails, on_delete=models.CASCADE, default=False)
    unit_name = models.CharField(max_length=200)
    unit_type = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    images = models.ImageField(upload_to="unitPhtos")
    lease_term = models.IntegerField()
    no_of_beds = models.CharField(max_length=200)
    no_of_baths = models.CharField(max_length=200)
    no_of_garages = models.CharField(max_length=200)
    unit_size = models.CharField(max_length=200)
    is_fully_furnished = models.CharField(max_length=1)
    unit_level = models.IntegerField()
    unit_is_available = models.CharField(max_length=1)
    unit_country = models.CharField(max_length=200)
    unit_stateorregion = models.CharField(max_length=200)
    unit_city = models.CharField(max_length=200)
    unit_listed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'UnitDetails'

    def __str__(self):      
        return self.unit_name



# class UnitLocation(models.Model):
#     unit = models.OneToOneField(UnitDetails, on_delete=models.CASCADE)
#     unit_country = models.CharField(max_length=200)
#     unit_stateorregion = models.CharField(max_length=200)
#     unit_city = models.CharField(max_length=200)

#     class Meta:
#         db_table = 'UnitLocation'

#     def __str__(self):
#         return self.unit_country



class UnitFeatures(models.Model):
    unit = models.OneToOneField(UnitDetails, on_delete=models.CASCADE)
    has_washer = models.CharField(max_length=1)
    has_internet = models.CharField(max_length=1)
    has_tv = models.CharField(max_length=1)
    has_parking = models.CharField(max_length=1)
    smoking_allowed = models.CharField(max_length=1)
    has_ac = models.CharField(max_length=1)
    has_balcony = models.CharField(max_length=1)
    has_pool = models.CharField(max_length=1)
 
    class Meta:
        db_table = 'UnitFeatures'

    #def __str__(self):
        
        


    
class RentApplication(models.Model):
    user = models.ForeignKey(to=UserDetails, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(6)
    employer_name = models.CharField(max_length=200)
    employer_phone = models.CharField(max_length=200)
    employment_start_date = models.DateField(6)
    position_held = models.CharField(max_length=200)
    monthly_income = models.CharField(max_length=200)
    verification_id_card = models.CharField(max_length=500)
    pay_stub = models.CharField(max_length=500)
    country = models.CharField(max_length=200)
    stateorregion = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField(null=True)
    application_date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'RentApplication'

    def __str__(self):
        return self.first_name +" "+ self.last_name



class Payment(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitDetails, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    payment_date = models.DateTimeField(6)


    class Meta:
        db_table = 'Payment'

    #def __str__(self):
        #return self.UserDetails.first_name +" "+ self.last_name