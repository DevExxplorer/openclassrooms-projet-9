from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SubscribeForm


def subscribe(request):
    """
    Vue qui affiche la page d'inscription

    Args:
        request (HttpRequest): Objet représentant la requête HTTP
    """
    if request.method == "POST":
        form = SubscribeForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")
    else:
        form = SubscribeForm()

    return render(
        request, "authentificate/subscribe.html", {"form": form, "show_label": False}
    )
