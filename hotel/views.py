from django.shortcuts import render
from .models import HotelOwner, HotelManager, CommonBathroom, CommonToilet, Bedrooms, HotelRegistration
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# def hotelform(request):
#     return render(request, 'hotel-form.html')

def hotelform(request):
    if request.method == 'POST':
        # print(request.POST)
        data =json.loads(json.dumps(request.POST))

        for i in data:
            j = json.loads(i)
            form = dict(j)

            hotel_registration = HotelRegistration.objects.create(
                        hotel_name=form['hotel_name'],
                        establishment_year=form['establishment_year'],
                        commision_date=form['commission_date'],
                        telex_number=form['telex_number'],
                        phone_number=form['telephone_no'],
                        hotel_address=form['hotel_address'],
                        telegraphic_address=form['telegraph_address'],
                        province=form['province'],
                        town=form['town'],
                        street=form['street_no'],
                        ownership_nature=form['ownership_nature'],
                        hotel_area=form['hotel_area'],
                        covered_area=form['covered_area'],
                        area_type=form['area_type'],
                        land_cost=form['land_cost'],
                        building_cost=form['building_cost'],
                        furniture_cost=form['furniture_cost'],
                        equipment_cost=form['equipment_cost'],
                        working_capital=form['working_capital'],
                        total_investment=form['total_investment'],
                        floor_numbers=form['floors_number'],
                        room_numbers=form['floor_rooms'],
                        room_nature=form['room_nature'],
                        )
            print(form['visitor_room'])
            print(form['visitor_room_area'])
            print(form['reception_detail'])
            print(form['reception_area'])
            print(form['cloak_detail'])
            print(form['cloak_area'])
            print(form['reading_detail'])
            print(form['reading_area'])
            print(form['restaurant_detail'])
            print(form['restaurant_area'])
            print(form['staircase'])
            print(form['lifts'])
            print(form['car_parking'])
            print(form['compound_area'])
            print(form['garden_area'])
            print(form['completion_date'])
            print(form['renovation_date'])
            # print(form['attach_file'])
            print(form['provided_phones'])
            print(form['hotel_premises'])
            print(form['restaurant_name'])
            # print(form['restaurant_file'])
            print(form['monthly_guests'])
            print(form['business_season'])


            for owner in form['owners'] :
                owner_data = HotelOwner.objects.create(owner_name=owner['name'], 
                                    owner_ratio=owner['ratio'], 
                                    owner_full_address=owner['address'], 
                                    owner_telegraphic_address=owner['telegraph'], 
                                    owner_telephone=owner['telephone'])
                owner_data.save()

            for manager in form['managers'] :
                manager_data = HotelManager.objects.create(manager_name=manager['managerName'],
                                    manager_ratio=manager['managerRatio'],
                                    manager_full_address=manager['managerAddress'],
                                    manager_telephone=manager['managerTelephone'])
                manager_data.save()

            for bathroom in form['bathrooms']:
                # print(bathroom)
                bathroom_data = CommonBathroom.objects.create(bathroom_no=bathroom['bath_No'],
                                    bathroom_floor=bathroom['floor_No'])
                bathroom_data.save()

            for toilet in form['toilets']:
                # print(toilet)
                toilet_data = CommonToilet.objects.create(toilet_no=toilet['toilet_No'],
                                    toilet_floor=toilet['floor_No'])
                toilet_data.save()
            
            for furniture in form['furniture']:
                # print(furniture)
                furniture_data = Bedrooms.objects.create(
                                bedrooms_type=furniture['bedroom'],
                                rooms_type=furniture['room'],
                                corridors_type=furniture['corrridor'],
                                attached_bathroom_type=furniture['attach_bath'],
                                bathrooms_type=furniture['common_bath'],
                                toilets_type=furniture['common_toilet'],
                                cuisine_name=furniture['cuisine']
                            )
                furniture_data.save()


        return JsonResponse({'status': 1}) 
    else:
        return render(request, 'hotel-form.html')
