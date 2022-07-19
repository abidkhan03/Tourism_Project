from django.contrib import admin
from .models import HotelOwner, HotelManager, CommonBathroom, CommonToilet, Bedrooms, HotelRegistration, HotelOwnerCombine

class HotelOwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'owner_ratio', 'owner_full_address', 'owner_telegraphic_address', 'owner_telephone')


admin.site.register(HotelOwner, HotelOwnerAdmin)
admin.site.register(HotelManager)
admin.site.register(CommonBathroom)
admin.site.register(CommonToilet)
admin.site.register(Bedrooms)
admin.site.register(HotelRegistration)
admin.site.register(HotelOwnerCombine)