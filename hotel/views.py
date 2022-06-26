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
            # print(form['hotel_name'])
            # print(form['establishment_year'])
            # print(form['commission_date'])
            # print(form['telex_number'])
            # print(form['telephone_no'])
            # print(form['hotel_address'])
            # print(form['telegraph_address'])
            # print(form['province'])
            # print(form['town'])
            # print(form['street_no'])
            # print(form['ownership_nature'])

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
