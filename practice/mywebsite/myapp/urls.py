from django.contrib import admin
from django.urls import path

from .views import index,about,contact_us,information

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about',about, name='about'),
    path('contact_us',contact_us, name='contact'),
    path('information',information,name='info')
]
