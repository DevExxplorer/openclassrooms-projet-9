from django.shortcuts import get_object_or_404
from django.db.models import Value, CharField
from app.utils.helpers import update_format_date, get_name_author
from followers.models import UserFollows
from tickets.models import Ticket, Review


def get_posts(user):
    """
        Récupère et met à jour les tickets et reviews de la base de données.

        Args:
          user (User): Utilisateur actuellement connecté.

        Returns:
          list: Liste triée des tickets et reviews, classés par date de création décroissante.
    """

    # Récupération des tickets et reviews en fonction des abonnés suivi
    followed_users = UserFollows.objects.filter(user=user).values_list('followed_user', flat=True)
    followed_users = list(followed_users) + [user.id]
    tickets = Ticket.objects.filter(user__in=followed_users).annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user__in=followed_users).annotate(content_type=Value('REVIEW', CharField()))

    # Transformation des données (mise à jour avec la fonction update_data)
    posts = []

    # Mise à jour des tickets
    for ticket in tickets:

        updated_ticket = update_data(ticket, user)

        # On controle que l'utilisateur n'a pas deja laissé une review au ticket
        ticket.has_review = Review.objects.filter(ticket=ticket, user=user).exists()

        posts.append(updated_ticket)

    # Mise à jour des reviews
    for review in reviews:
        updated_review = update_data(review, user)
        review.ticket.has_review = Review.objects.filter(ticket=review.ticket, user=user).exists()
        posts.append(updated_review)

    # Fusionner tickets et reviews en une seule liste et tri par date
    posts_sorted = sorted(posts, key=lambda post: post.time_created, reverse=True)

    return posts_sorted

def update_data(data, user):
    """
        Met à jour les données d'un ticket ou d'une critique en ajoutant des informations formatées.

        Args:
            data (Ticket | Review): Instance du modèle Ticket ou Review à mettre à jour.
            user (User): Utilisateur actuellement connecté.

        Returns:
            Ticket | Review: L'instance mise à jour avec les nouvelles informations.
    """
    data.date = update_format_date(data.time_created)
    data.author = get_name_author(data.user_id)
    data.user_logged_in = user.id != data.user.id

    if isinstance(data, Review):
        ticket = data.ticket

        if data.content_type == 'REVIEW':
            if hasattr(ticket, 'image') and ticket.image:
                data.image = ticket.image
            else:
                data.image = ''

    return data
