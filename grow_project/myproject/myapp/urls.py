
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('fd_calc', views.fd_calc, name='fd_calc')
]