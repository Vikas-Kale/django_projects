from django.http import HttpResponse

def name(request):
    return HttpResponse("<b> My Name is Vikas.</b>")

def course(request):
    return HttpResponse("Course is <b>Python</b>")

def 