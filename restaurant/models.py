import numbers
from django.db import models
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
from multiselectfield import MultiSelectField
# Create your models here.

class restraunt (models.Model):
    restraunt_name = models.CharField(max_length=100, null=True)
    establisment_date = models.DateField()
    commission_date = models.DateField()
    telex_num = models.IntegerField(null=True)
    telephone_num = models.IntegerField( null=True)
    address = models.TextField(max_length=100, null=True)
    telegraphic_num = models.IntegerField(null=True)

# location

    PROVINCE_CHOICES = (
    ('balochistan','BALOCHISTAN'),
    ('punjab', 'PUNJAB'),
    ('sindh','SINDH'),
    ('kpk','KPK'),
    ('fata','FATA'),
)
    province = models.CharField(max_length=100 , choices=PROVINCE_CHOICES, default='green')
    town = models.CharField(max_length=20 , null=True)
    street = models.CharField(max_length=100, null=True)

    OWNERSHIP_CHOICES = (
    ('proprietary','Proprietary'),
    ('partnership', 'Partnership'),
    ('private company','Private Company'),
    ('limited','Limited'),
    ('unlimited','Unlimited'),
)
    ownership = models.CharField(max_length=100 , choices=OWNERSHIP_CHOICES , null=True)

# Area
    total_area = models.IntegerField(null=True)
    area_of_kitchen = models.IntegerField(null=True)
    area_of_dining = models.IntegerField(null=True)
    seating_area = models.IntegerField(null=True)

# cost
    cost_of_furniture = models.IntegerField(null=True)
    cost_of_equipment = models.IntegerField(null=True)
    annual_rent = models.IntegerField(null=True)
    working_capital = models.IntegerField(null=True)
    total_investment = models.IntegerField(null=True)

# furniture
    number_of_floors = models.IntegerField(null=True)
    number_of_room = models.IntegerField(null=True)

    NATURE_OF_ROOM = (
    ('single bed room','SINGLE BED ROOM'),
    ('double bed room', 'DOUBLE BED ROOM'),
    ('suite room','SUITE ROOM'),
    
)


    nature_of_room = models.CharField(max_length=100 , choices=NATURE_OF_ROOM , null=True)

# Facilities

    FACILLTIES = (
        ('reception' , 'RECEPTION'),
        ('bill counter' , 'BILL COUNTER'),
        ('telephone' , 'TELEPHONE'),
        ('air-condition' , 'AIR-CONDITION'),
        ('heating' , 'HEATING'),
        ('cloak room' , 'CLOAK ROOM'),
        ('toilet' , 'TOILET'),
        ('car park' , 'CAR PARK'),
        ('entertainment' , 'ENTERTAINMENT'),

    )
    
    available_facilities = MultiSelectField(choices=FACILLTIES , null=True) 
    type_of_cuisine = models.CharField(max_length=100 , null=True)
    total_investment = models.IntegerField(null=True)



# manager-info

    total_number_mangers = models.IntegerField(null=True)
    professionally_trained = models.IntegerField(null=True)
    not_professionally = models.IntegerField(null=True)
    apprentices = models.IntegerField(null=True)
    english_knowing = models.IntegerField(null=True)


# Reception-info

    total_number_receptionists = models.IntegerField(null=True)
    professionally_trained = models.IntegerField(null=True)
    not_professionally = models.IntegerField(null=True)
    apprentices = models.IntegerField(null=True)
    english_knowing = models.IntegerField(null=True)

# Billing info

    total_number_billers = models.IntegerField(null=True)
    professionally_trained = models.IntegerField(null=True)
    not_professionally = models.IntegerField(null=True)
    apprentices = models.IntegerField(null=True)
    english_knowing = models.IntegerField(null=True)

# cooks info

    total_number_cooks = models.IntegerField(null=True)
    professionally_trained = models.IntegerField(null=True)
    not_professionally = models.IntegerField(null=True)
    apprentices = models.IntegerField(null=True)
    english_knowing = models.IntegerField(null=True)


# bearers info

    total_number_bearers = models.IntegerField(null=True)
    professionally_trained = models.IntegerField(null=True)
    not_professionally = models.IntegerField(null=True)
    apprentices = models.IntegerField(null=True)
    english_knowing = models.IntegerField(null=True)


#other info

    name_of_designation = models.CharField(max_length=100 , null=True)
    total_number_bearers = models.IntegerField(null=True)
    professionally_trained = models.IntegerField(null=True)
    not_professionally = models.IntegerField(null=True)
    apprentices = models.IntegerField(null=True)
    english_knowing = models.IntegerField(null=True)


# Rates Charged    
    RATES = (
        ('immeidiatly' , 'IMMEIDIATLY'),
        ('after dinner' , 'AFTER DINNER'),
    )

    rates = models.CharField(max_length=100 , choices=RATES , null=True)


class furniture_dining(models.Model):
    furniture_type = models.CharField(max_length=100 , null=True)


class furniture_kitchen(models.Model):
    furniture_type = models.CharField(max_length=100 , null=True)


# Number Of Owners

class ownership(models.Model):
    name_of_owner = models.CharField(max_length=100,  null=True)
    owner_percent = models.IntegerField(null=True)
    owner_address = models.TextField(max_length=100 , null=True)
    telegraphic_address = models.TextField(max_length=100, null=True)
    owner_telephone = models.IntegerField(null=True)

class manager(models.Model):
    name_of_manager = models.CharField(max_length=20, null=True)
    manager_percent = models.IntegerField(null=True)
    manager_address = models.TextField(max_length=100 , null=True)
    manager_telephone = models.IntegerField(null=True)
