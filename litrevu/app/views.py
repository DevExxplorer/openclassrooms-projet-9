from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, TicketForm, ReviewForm

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

def flux(request):
    if request.user.is_authenticated:
        pass
    else:
        print('Error')

    return render(
        request,
        'app/flux.html',
    )

def new_ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            # Sauvegarder le Ticket
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            # Sauvegarder la Review liée au Ticket
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect('home')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(
        request,
        'app/creation-ticket.html',
        {
            'ticket_form': ticket_form,
            'review_form': review_form,
        }
    )