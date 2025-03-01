from django.contrib import admin
from django.urls import path, include
from app import views as app_views
from authentificate import views as auth_views
from tickets import views as tickets_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def custom_logout(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect("home")  # Redirige vers la page d'accueil

urlpatterns = [
    # Home
    path("", app_views.home, name="home"),

    # Authentification
    path("inscription/", auth_views.subscribe, name="subscription"),
    path("logout/", custom_logout, name="logout"),

    # Admin
    path("admin/", admin.site.urls, name="admin"),

    # Flux et Posts
    path("flux/", login_required(tickets_views.tickets), name="flux"),
    path("posts/", login_required(tickets_views.posts), name="posts"),

    # Tickets
    path('tickets/creation/', login_required(tickets_views.new_ticket), name='ticket_create'),
    path('ticket/modification/<int:ticket_pk>', login_required(tickets_views.update_ticket), name='ticket_update'),
    path('ticket/<int:ticket_pk>/review/', login_required(tickets_views.new_review), name='ticket_review_create'),
    path('ticket/<int:id_post>/delete/', login_required(tickets_views.delete_post), name='delete_ticket'),

    # Critiques
    path('review/creation/', login_required(tickets_views.new_review), name='review_create'),
    path('review/modification/<int:review_pk>', login_required(tickets_views.update_review), name='review_update'),
    path('review/<int:id_post>/delete/', login_required(tickets_views.delete_post), name='delete_review'),

    # Abonnements
    path("abonnements/", include("followers.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)