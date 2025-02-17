from followers.models import UserFollows


def add_new_follower(user_follower, authenticate_user):
    """
       On ajoute l'utilisateur recherché dans la BDD
       On vérifie avant que que l'utilisateur recherché ne soit pas celui connecté
       et que l'utilisateur existe bien dans la BBD

        Args:
            user_follower (str): user follower.
            authenticate_user (class): class authenticate user.

        Returns:
            message: user message.
    """

    if user_follower != authenticate_user:
        if not UserFollows.objects.filter(user=authenticate_user, followed_user=user_follower).exists():
            UserFollows.objects.create(user=authenticate_user, followed_user=user_follower)

            message = f"L\'utilisateur {user_follower} vient d'être ajouté à votre liste"
        else:
            message = f"L'utilisateur {user_follower} est déjà suivi"
    else:
        message = f"Vous ne pouvez pas vous ajouter vous même !"

    return message

def list_followers(authenticate_user):
    """
        Génere une liste avec deux tableaux:
         - Les utilisateurs que l'on suit (following)
         - Les utilisateurs qui nous suivent (followed)

        Args:
            authenticate_user (class): class authenticate user.

        Returns:
            list: liste des utilisateurs.
    """

    list_users = {
        'followed': [],
        'following': []
    }

    # Utilisateur suivi
    users_following = authenticate_user.following.all()

    for user_following in users_following:
        list_users['following'].append(user_following.followed_user.username)

    # Utilisateur qui nous suit
    users_followed = authenticate_user.subscription.all()

    for user_followed in users_followed:
        list_users['followed'].append(user_followed.user.username)

    '''
    # Remplace les listes vides par un message
    if not list_users['following']:
        list_users['following'] = "Aucun abonnement"
    if not list_users['followed']:
        list_users['followed'] = "Aucun abonné"
    '''

    return list_users