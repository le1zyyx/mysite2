from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('places_list', views.places_list)
]