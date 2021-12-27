from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from calc.models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        contact_us = Contact()
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact_us.save()
        return HttpResponse('<h1> Thanks For Contact Us </h1>')

    return render(request, 'contact.html')
