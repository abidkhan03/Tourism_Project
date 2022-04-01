
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def touristGuideForm(request):
    return render(request, 'touristGuide-form.html')


def forms(request):
    return render(request, 'forms.html')    


   




           


