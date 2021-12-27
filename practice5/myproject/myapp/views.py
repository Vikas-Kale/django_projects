from django.shortcuts import render

# Create your views here.


def index(request):
    render (request,'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.isvalid():
            form.save()
            return render(request,'save.html')

    else:
        form = ContactUsForm():
        return render(request, 'contact.html',{form:'form'})

        
    render(request,'contact.html')

    