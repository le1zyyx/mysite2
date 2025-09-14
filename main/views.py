from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def places_list(request):
    return render(request, 'main/places_list.html')