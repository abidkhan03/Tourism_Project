from django.urls import path
from . import views
from tourism.views import index

urlpatterns = [
    path('index', index, name='index'),
    path('travel-agency-form/', views.travelagencyform,  name = 'travel-agency-form'),
]