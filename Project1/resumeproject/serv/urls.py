from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('services/',views.services,name='services')
]
