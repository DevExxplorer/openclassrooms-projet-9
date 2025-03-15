from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from authentificate.models import User
from followers.forms import SearchForm
from followers.utils.followers import list_followers
from .models import UserFollows
from django.contrib.auth.decorators import login_required
import json


@login_required
def page_views(request):
    """
    Vue qui affiche la liste des abonnements d'un utilisateur et permet d'ajouter un nouvel abonnement.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP

    Returns:
        HttpResponse: Retourne la page contenant la liste des abonnements et un formulaire de recherche.
    """
    authenticate_user = request.user
    list_users = list_followers(authenticate_user)
    form = SearchForm()

    return render(
        request,
        "followers/page.html",
        {"form": form, "list_users": list_users, "show_label": False},
    )


@login_required
def subscribe_user(request):
    """
    Vue fonctionnant avec ajax pour retrouver un utilisateur selon la recherche effectué dans le formulaire

    Args:
        request (HttpRequest): Objet représentant la requête HTTP

    Returns:
        JsonResponse: Retourne un booleen et l'id de l'utilisateur si le boolean est True
    """
    if request.method == "POST":
        data = json.loads(request.body)
        search_value = data.get("search_value")

        if search_value:
            try:
                followed_user = User.objects.get(username=search_value)

                if not UserFollows.objects.filter(
                    user=request.user, followed_user=followed_user
                ).exists():
                    UserFollows.objects.create(
                        user=request.user, followed_user=followed_user
                    )
                    return JsonResponse({"success": True, "user_id": followed_user.id})
                else:
                    return JsonResponse(
                        {
                            "success": False,
                            "message": "Vous suivez déjà cet utilisateur.",
                        }
                    )

            except Exception as e:
                print(f"Exception capturée : {type(e).__name__} - {e}")

        return JsonResponse(
            {"success": False, "message": "Valeur de recherche invalide."}
        )

    return JsonResponse({"success": False, "message": "Requête invalide."})


@login_required
def unsubscribe_user(request):
    """
    Vue qui permet à un utilisateur de se désabonner d'un autre utilisateur.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP

    Returns:
        JsonResponse: Réponse JSON indiquant le succès ou l'échec de l'opération.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")

            user_remove = get_object_or_404(
                UserFollows, user=request.user, followed_user_id=user_id
            )
            user_remove.delete()
            return JsonResponse(
                {"success": True, "message": "Utilisateur désabonné avec succès!"}
            )
        except json.JSONDecodeError:
            return JsonResponse(
                {"success": False, "error": "Format JSON invalide"}, status=400
            )
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse(
        {"success": False, "error": "Méthode non autorisée"}, status=405
    )
