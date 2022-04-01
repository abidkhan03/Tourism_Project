from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name='index'),
    path('touristGuide-form/', views.touristGuideForm, name = 'touristGuide-form'),
    path('forms/', views.forms, name = 'forms'),
    
    
]