from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    context = { "home" : "active"}
    return render(request, 'core/home.html',context)

def contact(request):
    context = { "contact" : "active"}
    return render(request, 'core/contact.html',context)

def sendmail(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
        subject,
        message,
        'kalevikas7798@gmail.com',
        ['vkale4938@gmail.com'],
        fail_silently=False,
        )
        messages.info(request, "Your responce is submitted Successfully\n\n We send you an email with details.")
        return render(request, 'core/contact.html')
    else:
        messages.info(request,"Mail not send")
        return render(request, 'core/contact.html')