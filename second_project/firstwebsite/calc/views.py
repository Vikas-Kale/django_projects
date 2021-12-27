from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable1":"This is sent.",
        "variable2":"Vikas Is Great!",
        "variable3":"Python Is Amazing."
    }
    return render(request, 'index.html',context)

    # return HttpResponse("This is home page.")

def about(request):
    return HttpResponse("This is about page.")

def services(request):
    return HttpResponse("This is services")

def contacts(request):
    return HttpResponse("This is contact page.")
