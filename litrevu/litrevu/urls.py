from django.contrib import admin
from django.urls import path
from app import views as app_views
from authentificate import views as auth_views
from book_reviews import views as book_reviews_views
from followers import views as followers_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect("home")  # Redirige vers la page d'accueil

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app_views.home, name="home"),
    path("inscription/", auth_views.subscribe),
    path("flux/", login_required(book_reviews_views.flux_page), name="flux"),
    path("creation-ticket/", login_required(book_reviews_views.new_ticket_page), name="creation-ticket"),
    path("creation-critique/", login_required(book_reviews_views.new_review_page), name="creation-critique"),
    path("creation-critique/<int:id_ticket>/", login_required(book_reviews_views.new_review_page), name="creation-critique-answer"),
    path("abonnements/", login_required(followers_views.page_views)),
    path("logout/", custom_logout, name="logout"),
]
