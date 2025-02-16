from app.utils.helpers import get_name_author, update_format_date
from book_reviews.forms import TicketForm, ReviewForm
from book_reviews.models import Ticket, Review

def add_ticket(request):
    valid = False

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            valid = True
    else:
        form = TicketForm()

    return {
        'form': form,
        'valid': valid
    }

def add_review(request):
    valid = False

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid():
            book_reviews = ticket_form.save(commit=False)
            book_reviews.user = request.user
            book_reviews.save()

            if review_form and review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.ticket = book_reviews
                review.save()
                valid = True
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return {
        'ticket_form': ticket_form,
        'review_form': review_form,
        'valid': valid
    }

def get_followers_reviews(list_subscriptions, user_logged_in):
    data = []
    tickets = Ticket.objects.all()

    if tickets:
        for ticket in tickets:
            if ticket.user.id in list_subscriptions:
                data.append(get_data_ticket(ticket, user_logged_in))

    return data

def get_data_ticket(ticket, user_logged_in):
    # Récupération de la date au bon format
    date_formatted = update_format_date(ticket.time_created)
    ticket.date = date_formatted

    # Ajout du type de post
    ticket.type = 'ticket'

    # Ajout du nom de l'auteur
    ticket.author = get_name_author(ticket.user_id)

    # Booleen pour savoir si le message a été écrit par l'utilisateur connecté
    ticket.user_logged_in = True if user_logged_in == ticket.user.id else False,

    # Vérifie si une review existe pour ce ticket
    if ticket.reviews.exists():
        review = ticket.reviews.first()
        review.date = update_format_date(review.time_created)
        review.author = get_name_author(review.user_id)
        ticket.type = 'review'

        ticket.review = review

    return ticket


def get_ticket_by_id(id_ticket, user_logged_in):
    ticket = Ticket.objects.filter(id=id_ticket).first()
    data_ticket = get_data_ticket(ticket, user_logged_in)
    return data_ticket
