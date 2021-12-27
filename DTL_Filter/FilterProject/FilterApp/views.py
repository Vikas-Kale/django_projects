from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'filterapp/index.html',{'course':'Django'})

def lenth_calc(request):
    data = {
        'name':'Vikas',
        'Address' :'Pune'
    }
    
    return render(request, 'filterapp/len.html',{'data':data})