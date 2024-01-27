from django.shortcuts import render
from .models import Cars
from math import ceil
from django.contrib.auth.decorators import login_required


def cars_list(request):
    all_cars = []

    # Handling search parameters
    car_make = request.GET.get('car_make', '')
    car_brand = request.GET.get('car_brand', '')

    # Filtering based on search parameters
    if car_make or car_brand:
        cars = Cars.objects.filter(car_make__icontains=car_make, car_brand__icontains=car_brand).all()
    else:
        cars = Cars.objects.all()

    categories = cars.values("car_make", "id")
    unique_categories = {item["car_make"] for item in categories}

    for car_make in unique_categories:
        cars_by_category = cars.filter(car_make=car_make).all()
        num_cars = len(cars_by_category)
        num_slides = num_cars // 4 + ceil((num_cars / 4) - (num_cars // 4))
        all_cars.append([cars_by_category, range(1, num_slides), num_slides])

    params = {"all_cars": all_cars}
    return render(request, "cars/cars_list.html", params)


@login_required(login_url='login')
def index(request):
    return render(request, 'cars/index.html')
