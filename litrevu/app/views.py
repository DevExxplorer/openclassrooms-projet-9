from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SubscribeForm, LoginForm

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("flux")
            else:
                pass
        else:
            pass
    else:
        form = LoginForm(request.POST)

    return render(
        request,
        'app/home.html',
        {'form': form}
    )

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")
    else:
        form = SubscribeForm()

    return render(
        request,
        'app/subscribe.html',
        {'form': form}
    )

def flux(request):
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
    else:
        print('Error')

    return render(
        request,
        'app/flux.html',
    )