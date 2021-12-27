from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from myapp.models import Contact

def index(request):
    if request.method=='POST':
        contact=Contact()
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.Post.get('email')
        comment = request.POST.get('comment')
        contact.fname = fname
        contact.lname = lname
        contact.email = email
        contact.comment = comment
        contact.save()
        return HttpResponse("<h1> Thanks for contact us </h1>")
    return render(request, 'index.html')

def contact_us(request):
    return HttpResponse("This Is contact page.")
    

 
