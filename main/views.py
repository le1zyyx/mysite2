from django.shortcuts import render, redirect
import random

def index(request):
    data = {'title': 'My favourite places in Kyiv'}
    return render(request, 'main/index.html', data)

def places_list(request):
    return render(request, 'main/places_list.html')

def new_place(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        rating = request.POST.get('rating', '').strip()

        errors = {}
        if not name:
            errors['name'] = "Назва не може бути порожньою"
        try:
            rating_val = int(rating)
            if rating_val < 1 or rating_val > 5:
                errors['rating'] = "Рейтинг має бути від 1 до 5"
        except ValueError:
            errors['rating'] = "Рейтинг має бути числом від 1 до 5"

        if not errors:
            return redirect('home')

        return render(request, 'main/new_place.html', {
            'errors': errors,
            'name': name,
            'rating': rating
        })

    return render(request, 'main/new_place.html')

def random_place(request):
    places = [
        "Ботанічний сад ім.Гришка",
        "Пузата Хата",
        "Multiplex",
        "WakeHub"
    ]
    selected_place = None
    if request.method == "POST":
        selected_place = random.choice(places)

    return render(request, 'main/random_place.html', {'selected_place': selected_place})
