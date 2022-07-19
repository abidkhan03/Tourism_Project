import datetime
import numbers
from django.db import models
from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser
from django.forms import CharField, DateField
from multiselectfield import MultiSelectField


# Owner Class
class HotelOwner(models.Model):
    owner_name = models.CharField(max_length=30, null=True)
    owner_ratio = models.CharField(max_length=30, null=True)
    owner_full_address = models.CharField(max_length=200, null=True)
    owner_telegraphic_address = models.CharField(max_length=200, null=True)
    owner_telephone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.owner_name

# Hotel Manager Class
class HotelManager(models.Model):
    manager_name = models.CharField(max_length=30, null=True)
    manager_ratio = models.CharField(max_length=30, null=True)
    manager_full_address = models.CharField(max_length=200, null=True)
    manager_telephone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.manager_name

# Common Places Class
class CommonBathroom(models.Model):
    bathroom_no = models.CharField(max_length=10, null=True, blank=True) # Common Bathroom no
    bathroom_floor = models.CharField(max_length=20, null=True, blank=True) # Common Floor No
    
    # common_place_id = models.ForeignKey(HotelRegistration, on_delete=models.CASCADE) # common place foreign key attach to hotel registration
class CommonToilet(models.Model):
    toilet_no = models.CharField(max_length=10, null=True, blank=True) #Common Toilet No
    toilet_floor = models.CharField(max_length=20, null=True, blank=True) # Floor No
# Furniture and Fixtures
class Bedrooms(models.Model):
    bedrooms_type = models.CharField(max_length=100 , null=True, default='Wood', blank=True) # Bedrooms
    rooms_type = models.CharField(max_length=100, null=True, default='Wood', blank=True) # Common Rooms
    corridors_type = models.CharField(max_length=100, null=True, default='Wood', blank=True) # Corridors and Galleries
    attached_bathroom_type = models.CharField(max_length=100, null=True, default='Tile', blank=True) # bathroom attached with bedrooms
    bathrooms_type = models.CharField(max_length=100, null=True, default='Tile, blank=True') # common bathrooms
    toilets_type = models.CharField(max_length=100, null=True, default='Tile', blank=True) # common toilots
    cuisine_name = models.CharField(max_length=100, null=True, default='Roast', blank=True) # cuisine served


# Hotel Registration Class
class HotelRegistration(models.Model):

    hotel_name = models.CharField(max_length=100) # Name of the hotel
    establishment_year = models.DateField() # year of establishment
    commision_date = models.DateField(null=True) # data of commission    
    telex_number = models.CharField(max_length=20, null=True, default="") # Telex number
    phone_number = models.CharField(max_length=20, default="")# Telephone Number
    hotel_address = models.CharField(max_length=100) # Address
    telegraphic_address = models.CharField(max_length=100 , null=True) # Telegraphic Address

    # Location information
    province = models.CharField(max_length=100 , null=True)
    town = models.CharField(max_length=100 , null=True)
    street = models.CharField(max_length=100 , null=True)
    ownership_nature = models.CharField(max_length=100 , null=True) # ownership nature

    # Land information
    hotel_area = models.CharField(max_length=50, null=True, default='') # Area of Hotel
    covered_area = models.CharField(max_length=50, null=True, default='') # Covered Area
    area_type = models.CharField(max_length=100 , null=True, default='') # Area Type

    # cost information
    land_cost = models.CharField(max_length=20 , null=True) # Cost of Land
    building_cost = models.CharField(max_length=20 , null=True) # Cost of building
    furniture_cost = models.CharField(max_length=20 , null=True) # cost of furniture & Fixtures
    equipment_cost = models.CharField(max_length=20 , null=True) # cost of equipment
    working_capital = models.CharField(max_length=20 , null=True) # working capital
    total_investment = models.CharField(max_length=20 , null=True)




    # Building information
    floor_numbers = models.CharField(max_length=100 , null=True, blank=True, default='1') # number of floors
    room_numbers = models.CharField(max_length=100 , null=True, blank=True, default='1') # Number of rooms on each floor

    
    NATURE_OF_ROOM = (
    ('single bed room','SINGLE BED ROOM'),
    ('double bed room', 'DOUBLE BED ROOM'),
    ('suite room','SUITE ROOM'),  
)
    room_nature =  models.CharField(max_length=100 , choices=NATURE_OF_ROOM , null=True)  # nature of room

    # Public Rooms
    visitor_room_detail = models.CharField(max_length=200, null=True)
    visitor_room_area = models.CharField(max_length=100, null=True)
    reception_hall_detail = models.CharField(max_length=200, null=True)
    reception_hall_area = models.CharField(max_length=100, null=True)
    cloak_room_detail = models.CharField(max_length=200, null=True)
    cloak_room_area = models.CharField(max_length=100, null=True)
    reading_room_detail = models.CharField(max_length=200, null=True)
    reading_room_area = models.CharField(max_length=100, null=True)
    restaurant_detail = models.CharField(max_length=200, null=True)
    restaurant_area = models.CharField(max_length=100, null=True)

    # Below from Common Toilets No
    staircase_no = models.CharField(max_length=20, null=True, default='') # No. Of Staircase:
    lifts_no = models.CharField(max_length=20, null=True, default='') # No. Of Lifts:
    car_park = models.CharField(max_length=20, null=True, default='') # Car Park (Lease Indicate Capacity):
    area_of_compound  = models.CharField(max_length=50, null=True, default='') # Area of Compund:
    area_of_garden = models.CharField(max_length=100, null=True, default='') # Area Of Garden (If any):
    construction_completion_date = models.DateField(null=True, default=None) # Date of Completion of Construction :
    renovation_last_date = models.DateField(null=True, default=datetime.date(2010, 1, 1))# Last Date of Renovation (If Any):
    building_files = models.FileField(upload_to='building_files/', null=True, blank=True, default=None) # Please Attach a Plan of The Buildings
    phones_provided = models.CharField(max_length=100, null=True)
    hotel_premises = models.CharField(max_length=100, null=True)

    # Is restaurant attached with hotel
    restaurant_name = models.CharField(max_length=100, null=True) # Restaurant Name
    restaurant_detail_files = models.FileField(upload_to='restaurant_files/', null=True) # Please Attach Restaurant Details

    monthly_guests = models.CharField(max_length=100, null=True)
    business_season = models.CharField(max_length=100, null=True)

    # Foreighn Keys
    # owner_id = models.ForeignKey(HotelOwner, related_name='owner_id', on_delete=models.CASCADE, null=True)
    # manager_id = models.ForeignKey(HotelManager, on_delete=models.CASCADE, related_name='manager_id')
    # common_bathroom_id = models.ForeignKey(CommonBathroom, on_delete=models.CASCADE, related_name='common_bathroom_id')
    # common_toilet_id = models.ForeignKey(CommonToilet, on_delete=models.CASCADE, related_name='common_toilet_id')
    # bedrooms_id = models.ForeignKey(Bedrooms, on_delete=models.CASCADE, related_name='bedrooms_id')
    
    
    def __str__(self):
        return self.hotel_name

    # class Meta:
    #     ordering = ('hotel_name',)



class HotelOwnerCombine(models.Model):
    owner_id = models.ForeignKey(HotelOwner, models.CASCADE, db_column='owner_id')
    manager_id = models.ForeignKey(HotelManager, models.CASCADE, db_column='manager_id')
    common_bathroom_id = models.ForeignKey(CommonBathroom, on_delete=models.CASCADE, db_column='bathroom_id')
    common_toilet_id = models.ForeignKey(CommonToilet, on_delete=models.CASCADE, db_column='toilet_id')
    bedrooms_id = models.ForeignKey(Bedrooms, on_delete=models.CASCADE, db_column='bedrooms_id')
    hotel_id = models.ForeignKey(HotelRegistration, models.DO_NOTHING, db_column='hotel_id')

    class Meta:
        # managed = False
        db_table = 'hotelcombineddata'
        unique_together = (('owner_id', 'manager_id', 'common_bathroom_id', 'common_toilet_id', 'bedrooms_id', 'hotel_id'),)







 


 


