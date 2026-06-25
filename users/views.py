from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


def register_view(request):

    form = RegisterForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        user = form.save()

        login(
            request,
            user
        )

        return redirect('/')

    return render(
        request,
        'users/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect('/')

    return render(
        request,
        'users/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('/')


@login_required
def profile_view(request):

    return render(
        request,
        'users/profile.html'
    )