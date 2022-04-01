from django.urls import path
from . import views
from tourism.views import index

urlpatterns = [
    path('index', index, name='index'),
    path('hotel-form/', views.hotelform, name = 'hotel-form'),
]