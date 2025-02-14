from django.shortcuts import render, redirect
from .forms import TicketForm, ReviewForm

def display_ticket_form(request, form_number):
    title_form = (
        'Créer un ticket',
        'Créer un ticket et sa critique'
    )
    data_form = create_ticket_form(request, form_number)

    return render(
        request,
        'ticket/ticket-and-review-forms.html',
        {
            'title': title_form[form_number - 1],
            'form_ticket': data_form[0],
            'form_review': data_form[1] if data_form[1] else None,
            'show_label': True
        }
    )

def create_ticket_form(request, form_number):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST) if form_number == 2 else ''

        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            if review_form and review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.ticket = ticket
                review.save()
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm() if form_number == 2 else ''

    return ticket_form, review_form


'''
# Gestion des erreurs
try:
if not views[form_number - 1]:
return redirect('/404')
except (IndexError, KeyError):
return redirect('/404')
'''