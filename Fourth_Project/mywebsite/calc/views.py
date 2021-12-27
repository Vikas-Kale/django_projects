from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    context = {
        "variable1":"Vikas",
        "variable2" : "Ram"
    }
    return render(request, 'base.html',context)