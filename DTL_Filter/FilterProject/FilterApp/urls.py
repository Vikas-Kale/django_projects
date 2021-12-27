from django.urls import path
from . import views
urlpatterns = [
    path('Home/',views.index),
    path('Length/',views.lenth_calc),
]