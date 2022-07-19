from django.shortcuts import render
from .models import HotelOwner, HotelManager, CommonBathroom, CommonToilet, Bedrooms, HotelRegistration, HotelOwnerCombine
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# def hotelform(request):
#     return render(request, 'hotel-form.html')

def hotelform(request):
    if request.method == 'POST':
        # print(request.POST)
        data =request.POST
        # print( request.FILES )
        files = request.FILES
        
        owners = zip(data.getlist('ownerName'), data.getlist('ownerRatio'), data.getlist('ownerAddress'), data.getlist('ownerTelegraphAddress'), data.getlist('ownerTelephoneNo'))
        managers = zip(data.getlist('managerName'), data.getlist('managerRatio'), data.getlist('managerAddress'), data.getlist('managerTelephoneNo'))
        bathrooms = zip(data.getlist('commonBathroomNo'), data.getlist('bathroomFloorNo'))
        toilets = zip(data.getlist('commonToiletNo'), data.getlist('toiletFloorNo'))
        furnitures = zip(data.getlist('bedroomType'), data.getlist('roomType'), data.getlist('corridors'), data.getlist('attachedBathroom'), data.getlist('commonToilet'), data.getlist('cuisineName'))

        hotel_registration = HotelRegistration(
                    hotel_name=data['hotel_name'],
                    establishment_year=data['establishment_year'],
                    commision_date=data['commission_date'],
                    telex_number=data['telex_number'],
                    phone_number=data['telephone_no'],
                    hotel_address=data['hotel_address'],
                    telegraphic_address=data['telegraph_address'],
                    province=data['province'],
                    town=data['town'],
                    street=data['street_no'],
                    ownership_nature=data['ownership_nature'],
                    hotel_area=data['hotel_area'],
                    covered_area=data['hotel_covered_area'],
                    area_type=data['hotel_area_type'],
                    land_cost=data['land_cost'],
                    building_cost=data['building_cost'],
                    furniture_cost=data['furniture_cost'],
                    equipment_cost=data['equipment_cost'],
                    working_capital=data['working_capital'],
                    total_investment=data['total_investment'],
                    floor_numbers=data['floors_number'],
                    room_numbers=data['floor_rooms_no'],
                    room_nature=data['room_nature'],
                    visitor_room_detail=data['visitors_room_detail'],
                    visitor_room_area=data['visitor_room_area'],
                    reception_hall_detail=data['reception_hall_detail'],
                    reception_hall_area=data['reception_hall_area'],
                    cloak_room_detail=data['cloak_room_detail'],
                    cloak_room_area=data['cloak_room_area'],
                    reading_room_detail=data['reading_room_detail'],
                    reading_room_area=data['reading_room_area'],
                    restaurant_detail=data['restaurant_detail'],
                    restaurant_area=data['restaurant_area'],
                    staircase_no=data['staircase_no'],
                    lifts_no=data['lifts_no'],
                    car_park=data['car_park'],
                    area_of_compound=data['compound_area'],
                    area_of_garden=data['garden_area'],
                    construction_completion_date=data['completion_date'],
                    renovation_last_date=data['renovation_date'],
                    building_files=files['attach_file'],
                    phones_provided=data['telephones_provided'],
                    hotel_premises=data['hotel_premises'],
                    restaurant_name=data['restaurant_name'],
                    restaurant_detail_files=files['attach_restaurant_detail'],
                    monthly_guests=data['monthly_guests'],
                    business_season=data['business_season'],
                    # owner_id=owner_data
                    )
        hotel_registration.save()
        # owners_list=[]
        for owner in owners:
            owner_data = HotelOwner.objects.create(
                    owner_name=owner[0],
                    owner_ratio=owner[1],
                    owner_full_address=owner[2], 
                    owner_telegraphic_address=owner[3],
                    owner_telephone=owner[4]
                )
            owner_data.save()
            
            # owners_list.append(owner_data)
            


        for manager in managers:
            manager_data = HotelManager.objects.create(
                        manager_name=manager[0],
                        manager_ratio=manager[1],
                        manager_full_address=manager[2],
                        manager_telephone=manager[3]
                    )
            manager_data.save()

        for bathroom in bathrooms:
            bathroom_data = CommonBathroom.objects.create(bathroom_no=bathroom[0],
                                bathroom_floor=bathroom[1])
            bathroom_data.save();

        for toilet in toilets:
            toilet_data = CommonToilet.objects.create(toilet_no=toilet[0],
                                toilet_floor=toilet[1])
            toilet_data.save()
        
        for furniture in furnitures:
            # print(furniture)
            furniture_data = Bedrooms.objects.create(
                            bedrooms_type=furniture[0],
                            rooms_type=furniture[1],
                            corridors_type=furniture[2],
                            attached_bathroom_type=furniture[3],
                            bathrooms_type=furniture[4],
                            toilets_type=furniture[5],
                            cuisine_name=furniture[6]
                        )
            furniture_data.save()
        print("attach file print.. ",files['attach_file'])
        # hotel_registration.save()
        # hotel_registration.owner_id.add(*owners_list)
        # for i in hotel_registration.owner_id.all():
        HotelOwnerCombine.objects.create(
                hotel_id=hotel_registration,
                owner_id=owner_data,
                manager_id=manager_data,
                bathroom_id = bathroom_data, 
                toilet_id = toilet_data,
                bedrooms_id = furniture_data
                ).save()
        
        
        
        

        return JsonResponse({'status': 1}) 
    else:
        return render(request, 'hotel-form.html')
