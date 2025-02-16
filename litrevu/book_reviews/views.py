from django.shortcuts import render, redirect

from app.utils.helpers import get_user_subscriptions
from book_reviews.utils.reviews import add_ticket, add_review, get_followers_reviews, get_ticket_by_id


def flux_page(request):
    """
        Affichage de la page Flux

        Cette vue gère l'affichage de la page "Flux", qui peut contenir les
        dernières critiques de livres

        Args:
            request (HttpRequest): Requête HTTP.

        Returns:
            HttpResponse: return la page "flux.html".
    """
    user = request.user
    user_logged_in = user.id

    subscriptions = get_user_subscriptions(user)
    subscriptions.append(user_logged_in)

    posts = get_followers_reviews(subscriptions, user_logged_in)

    return render(
        request,
        'book_reviews/flux.html',
        {
            'posts': posts,
        }
    )

def new_ticket_page(request):
    data_review = add_ticket(request)

    if data_review['valid']:
        return redirect('flux')

    return render(
        request,
        'book_reviews/new_review.html',
        {
            'title': 'Créer un ticket',
            'tickets': data_review['form'],
            'show_label': True
        }
    )

def new_review_page(request, id_ticket=""):

    data_review = add_review(request)

    if data_review['valid']:
        return redirect('flux')

    if id_ticket != "":
        views_ticket = get_ticket_by_id(id_ticket, request.user.id)
        page = 'review_answer'
    else:
        views_ticket = data_review['ticket_form']
        page = 'review'

    return render(
        request,
        'book_reviews/new_review.html',
        {
            'title': 'Créer une critique',
            'tickets': views_ticket,
            'reviews': data_review['review_form'],
            'show_label': True,
            'page': page
        }
    )