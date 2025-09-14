from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('places_list', views.places_list, name='places_list'),
    path('new_place', views.new_place, name='new_place'),
    path('random_place', views.random_place, name='random_place'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)