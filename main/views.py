from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def places_list(request):
    return render(request, 'main/places_list.html')

def new_place(request):
    return render(request, 'main/new_place.html')

def random_place(request):
    return render(request, 'main/random_place.html')