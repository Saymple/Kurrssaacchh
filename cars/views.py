from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Car
from .forms import CarForm


def home(request):

    cars = Car.objects.filter(
        is_active=True
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'cars/home.html',
        {
            'cars': cars
        }
    )


def car_detail(request, pk):

    car = get_object_or_404(
        Car,
        pk=pk
    )

    return render(
        request,
        'cars/detail.html',
        {
            'car': car
        }
    )


@login_required
def car_create(request):

    form = CarForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        car = form.save(
            commit=False
        )

        car.owner = request.user

        car.save()

        return redirect('/')

    return render(
        request,
        'cars/create.html',
        {
            'form': form
        }
    )


@login_required
def car_delete(request, pk):

    car = get_object_or_404(
        Car,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':

        car.delete()

        return redirect('/')

    return render(
        request,
        'cars/delete.html',
        {
            'car': car
        }
    )