from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentificate.models import User
from followers.forms import SearchForm
from followers.utils.followers_utils import list_followers, add_new_follower


@login_required
def page_views(request):
    """
    Vue permettant d'afficher une page avec un formulaire de recherche d'utilisateurs.
    """
    authenticate_user = request.user
    list_users = list_followers(authenticate_user)

    if request.method == 'POST':
        search_value = request.POST['search']

        try:
            user_follower = User.objects.get(username=search_value)
            message_form = add_new_follower(user_follower, authenticate_user)
        except User.DoesNotExist:
            message_form = 'L\'utilisateur que vous souhaitez suivre n\'existe pas.'

        # Réinitialiser le formulaire après soumission
        form = SearchForm()
    else:
        form = SearchForm(None)
        message_form = ""

    return render(
        request,
        'followers/page.html',
        {
            'form': form,
            'message_form': message_form,
            'list_users': list_users,
            'show_label': False
        }
    )

