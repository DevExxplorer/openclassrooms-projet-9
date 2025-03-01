from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket, Review
from tickets.utils.forms import add_new_data
from tickets.utils.tickets_manager import update_data, get_posts

@login_required
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

@login_required
def posts(request):
    """
        Vue qui affiche la liste des posts.

        Args:
            request (HttpRequest): Objet représentant la requête HTTP

        Returns:
            Retourne la page Posts
    """
    data_posts = get_posts(request.user, 'posts')

    return render(
        request,
        'tickets/posts.html',
        {
            'page': 'posts',
            'posts': data_posts,
        }
    )

@login_required
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
        'tickets/create/new_ticket.html',
        {
            'title': 'Créer un ticket',
            'tickets': data_form['ticket_form'],
            'show_label': True
        }
    )

@login_required
def new_review(request, ticket_pk=None):
    """
        Vue qui affiche le formulaire pour créer une nouvelle review

        En fonction de l'id_ticket le formulaire des tickets et modifier

        Args:
            request (HttpRequest): Objet représentant la requête HTTP
            ticket_pk (int, optional): Id du ticket

        Returns:
            Retourne la page new_review.html
    """
    if ticket_pk:
        ticket_object = get_object_or_404(Ticket, id=ticket_pk)
        ticket = update_data(ticket_object, request.user)
        data_form = add_new_data(request, 'review', ticket)
        url_template = 'tickets/create/new_review.html'
    else:
        data_form = add_new_data(request, 'ticket_review')
        ticket = data_form['ticket_form']
        url_template = 'tickets/create/new_ticket_review.html'

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

@login_required
def update_ticket(request, ticket_pk):
    ticket = get_object_or_404(Ticket, id=ticket_pk)
    data_form = add_new_data(request, 'ticket', ticket)

    if data_form['valid']:
        return redirect('posts')

    return render(
        request,
        'tickets/update/update_ticket.html',
        {
            'title': 'Modifier votre ticket',
            'field': data_form['ticket_form'],
            'show_label': True
        }
    )

@login_required
def update_review(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)
    ticket = review.ticket
    ticket = update_data(ticket, request.user)
    data_form = add_new_data(request, 'review', ticket, review)

    if data_form['valid']:
        return redirect('posts')

    return render(
        request,
        'tickets/update/update_review.html',
        {
            'title': 'Modifier votre critique',
            'ticket': ticket,
            'review': data_form['review_form'],
            'show_label': True
        }
    )

@login_required
def delete_post(request, id_post):
    view_name = request.resolver_match.view_name

    if request.method == 'POST':
        if view_name == 'delete_ticket':
            post = get_object_or_404(Ticket, id=id_post)
        elif view_name == 'delete_review':
            post = get_object_or_404(Review, id=id_post)
        else:
            return

        post.delete()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)
