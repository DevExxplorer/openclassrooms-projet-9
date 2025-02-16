from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import SubscribeForm

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
        'authentificate/subscribe.html',
        {
            'form': form,
            'show_label': False
        }
    )
