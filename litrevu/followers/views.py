from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from authentificate.models import User
from followers.forms import SearchForm
from followers.utils.followers import list_followers, add_new_follower
from .models import UserFollows
import json

def page_views(request):
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
    print(list_users)
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

def unsubscribe_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')

            try:
                user_remove = get_object_or_404(UserFollows, user=request.user, followed_user_id=user_id)
                user_remove.delete()
                return JsonResponse({'success': True, 'message': 'Utilisateur désabonné avec succès!'})
            except User.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Utilisateur non trouvé'}, status=404)

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'}, status=405)