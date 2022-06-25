from django.urls import path
from . import views
from tourism.views import index

urlpatterns = [
    path('index', index, name='index'),
    path('hotel-form/', views.hotelform, name = 'hotel-form'),
    # path('hotel-form/ajax/', views.hotelformAjax, name = 'hotelformajax'),
    # path('hotel-formajax/', views.hotelformajax, name = 'hotel-formajax'),
]