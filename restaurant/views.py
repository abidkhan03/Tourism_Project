from django.shortcuts import render
from django.urls import reverse



def restrauntform(request):
    return render(request, 'restraunt-form.html')   
