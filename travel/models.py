from asyncio.windows_events import NULL
from audioop import maxpp
import imp
from pyexpat import model
from tkinter.tix import Tree
from django.db import models
import datetime

from django.forms import NullBooleanField

FRIMS_CHOICES = (
    ('proprietary','Proprietary'),
    ('partnership', 'Partnership'),
    ('private company','Private Company'),
    ('limited','Limited'),
    ('unlimited','Unlimited'),
)

class travelagency(models.Model):

    
    firm_name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    business_address = models.CharField(max_length=200)
    reside_in_pakistan = models.BooleanField()

    # If Reside outside of pakistan then There address and name below
    business_foreign_name = models.CharField(max_length=200, blank=True)
    business_foreign_address = models.CharField(max_length=200, blank=True)
    
    nature_of_firm = models.CharField(max_length=200, choices=FRIMS_CHOICES, default='private company')

    year_of_establishment = models.DateField(default=datetime.date.today)
    registration_copy = models.FileField(default=NULL)

    contact_number = models.IntegerField(default=0)
    cable_address = models.CharField(max_length=200, default=NULL)

    other_branch = models.BooleanField(default=False)
    branch_code = models.IntegerField(default=0)

    branch_address = models.CharField(max_length=200, default=NULL)

    investment = models.IntegerField(default=0)
    investment_copy = models.FileField(default=NULL)

#     # Bank Details
    banker_name = models.CharField(max_length=200, default=NULL)
    reference_letter_copy = models.FileField(default=NULL)

    auditor_name = models.CharField(max_length=30, default=NULL)
    auditor_number = models.IntegerField(default=0)
    auditors_address = models.CharField(max_length=200, default=NULL)

    # Staff
    Number_of_directors = models.IntegerField(default=1)
    Number_of_managers = models.IntegerField(default=1)
    Number_of_partners = models.IntegerField(default=1)
    general_staff = models.IntegerField(default=1)
    
    # Businesses
    business_1 = models.CharField(max_length=200, null=True)
    business_2 = models.CharField(max_length=200, null=True)
    business_3 = models.CharField(max_length=200, null=True)
    business_4 = models.CharField(max_length=200, blank=True)
    business_5 = models.CharField(max_length=200, blank=True)

    #Foreign Parnterships
    no_of_foreign_partnerships = models.IntegerField(blank=True, default=0)
    partnership_file = models.FileField(default=NULL)

    # Foreign Exchange Dealing
    foreign_dealing = models.BooleanField(default=False)
    # if yes:
    exchange_licence_number = models.IntegerField(blank=True, default=0)
    issue_date = models.DateField(blank=True, default=datetime.date.today)
    exchange_address = models.CharField(max_length=200, default=NULL)
    license_copy = models.FileField(blank=True)
    exchange_statment = models.FileField(blank=True)


    # Conviction of offence
    conviction_details = models.CharField(max_length=500,blank=True)

    #Business Plan 
    business_plan_copy = models.FileField(default=NULL)



# Assets Table 

class assets(models.Model):
    asset_1 = models.CharField(max_length=50)
    asset_2 = models.CharField(max_length=50)
    asset_3 = models.CharField(max_length=50)
    asset_4 = models.CharField(max_length=50)
    asset_5 = models.CharField(max_length=50)
    asset_6 = models.CharField(max_length=50)
    asset_7 = models.CharField(max_length=50)
    asset_8 = models.CharField(max_length=50)

    

# Director Table

class director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    years_of_experience = models.IntegerField(blank=True)
    qualification = models.CharField(max_length=30)

# Manager Table
class manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    years_of_experience = models.IntegerField(blank=True)
    qualification = models.CharField(max_length=30)


# Partner Table
class partner(models.Model):
    partner_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    years_of_experience = models.IntegerField(blank=True)
    qualification = models.CharField(max_length=30)