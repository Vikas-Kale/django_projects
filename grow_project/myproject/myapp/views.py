from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'home':'active'}
    return render(request, 'index.html', context)

def fd_calc(request):
    context = {'fd_calc':'active'}
    return render(request, 'fd_calc.html',context)