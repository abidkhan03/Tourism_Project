from django.shortcuts import render


def hotelform(request):
    return render(request, 'hotel-form.html') 
