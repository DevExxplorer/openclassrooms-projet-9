from django.contrib.auth import get_user_model
from datetime import datetime

def get_name_author(id_author):
    """
        Retourne le nom de l'auteur de la review

        Args:
            id_author (Number): Identifiant de l'auteur

        Returns:
            name_author: Retourne le nom de l'auteur
    """

    data_user = get_user_model()

    try:
        user = data_user.objects.get(id=id_author)

        if user.first_name and user.last_name:
            return f"{user.first_name} {user.last_name}"

        return user.username

    except data_user.DoesNotExist:
        return "Utilisateur inconnu"

# Utilisateur suivi
def get_user_subscriptions(authenticate_user):
    list_subscriptions = []

    subscriptions = authenticate_user.subscription.all()

    for subscription in subscriptions:
        list_subscriptions.append(subscription.user.id)

    return list_subscriptions

def update_format_date(date):
    formatted_date = date.strftime("%H:%M, %d %B %Y")
    months = {
        "January": "janvier",
        "February": "février",
        "March": "mars",
        "April": "avril",
        "May": "mai",
        "June": "juin",
        "July": "juillet",
        "August": "août",
        "September": "septembre",
        "October": "octobre",
        "November": "novembre",
        "December": "décembre"
    }

    for en, fr in months.items():
        formatted_date = formatted_date.replace(en, fr)

    return formatted_date