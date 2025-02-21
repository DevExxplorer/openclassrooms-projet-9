from pprint import pprint

from django.shortcuts import render, redirect, get_object_or_404

from tickets.models import Ticket
from tickets.utils.forms import add_new_data
from tickets.utils.tickets_manager import update_data, get_posts


def tickets(request):
    """
        Vue qui affiche la liste des tickets.

        Args:
            request (HttpRequest): Objet représentant la requête HTTP

        Returns:
            Retourne la page Flux
    """
    page = request.GET.get('page', 'flux')
    posts = get_posts(request.user)

    return render(
        request,
        'tickets/posts.html',
        {
            'page': page,
            'posts': posts,
        }
    )

def posts(request):
    """
        Vue qui affiche la liste des posts.

        Args:
            request (HttpRequest): Objet représentant la requête HTTP

        Returns:
            Retourne la page Posts
    """
    page = request.GET.get('page', 'posts')
    posts = get_posts(request.user)

    return render(
        request,
        'tickets/posts.html',
        {
            'page': page,
            'posts': posts,
        }
    )

def new_ticket(request):
    """
        Vue qui affiche le formulaire pour créer un nouveau ticket

        Args:
            request (HttpRequest): Objet représentant la requête HTTP

        Returns:
            Retourne la page new_ticket.html
    """
    data_form = add_new_data(request)

    if data_form['valid']:
        return redirect('flux')

    return render(
        request,
        'tickets/new_ticket.html',
        {
            'title': 'Créer un ticket',
            'tickets': data_form['ticket_form'],
            'show_label': True
        }
    )

def new_review(request, ticket_pk=None):
    """
        Vue qui affiche le formulaire pour créer une nouvelle review

        En fonction de l'id_ticket le formulaire des tickets et modifier

        Args:
            request (HttpRequest): Objet représentant la requête HTTP
            id_ticket (int, optional): Id du ticket

        Returns:
            Retourne la page new_review.html
    """
    if ticket_pk:
        ticket_object = get_object_or_404(Ticket, id=ticket_pk)
        ticket = update_data(ticket_object, request.user)
        data_form = add_new_data(request, 'review', ticket)
        url_template = 'tickets/new_review.html'
    else:
        data_form = add_new_data(request, 'ticket_review')
        ticket = data_form['ticket_form']
        url_template = 'tickets/new_ticket_review.html'

    if data_form['valid']:
        return redirect('flux')

    return render(
        request,
        url_template,
        {
            'title': 'Créer une critique',
            'ticket': ticket,
            'review': data_form['review_form'],
            'show_label': True
        }
    )
