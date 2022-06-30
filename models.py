from django.db import models


class Membership_Registration(models.Model):
     First_Name=models.CharField(max_length=20)
     Second_Name=models.CharField(max_length=20)
     Last_Name=models.CharField(max_length=30)
     Date_of_Birth=models.DateField()
     Phone_Number=models.CharField(max_length=12)
     Email_Adress=models.CharField(max_length=50)
     Registration_Date=models.DateTimeField(auto_now=True)
     NIN=models.CharField(max_length=14, null=False, Blank=False)
     Village_Type_choices=[
          ('Aunga','Aunga'),
          ('Idache','Idache'),
          ('Libua','Libua')

     ]
     Village=models.CharField(max_length=40, Village_Type_choices, default=Aunga)
     Parish_Type_Choices=[
          
     ]




