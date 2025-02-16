from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
                message = 'Ce compte n\'existe pas'
        else:
            message = 'Identifiant ou Mot de passe invalide'
    else:
        form = LoginForm()
        message = ''

    return render(
        request,
        'app/home.html',
        {
            'form': form,
            'message': message
        }
    )
