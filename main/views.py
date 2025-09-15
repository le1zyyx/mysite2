from django.shortcuts import render

def index(request):
    data = {
        'title': 'My favourite places in Kyiv'
    }
    return render(request, 'main/index.html', data)

def places_list(request):
    return render(request, 'main/places_list.html')

def new_place(request):
    return render(request, 'main/new_place.html')

def random_place(request):
    return render(request, 'main/random_place.html')