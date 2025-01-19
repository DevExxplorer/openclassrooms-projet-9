from django.contrib import admin
from django.urls import path
from app import views as app_views
from authentificate import views as auth_views
from ticket import views as ticket_views
from error import views as error_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app_views.home, name="home"),
    path("inscription/", auth_views.subscribe),
    path("creation-ticket/<int:form_number>", login_required(ticket_views.display_ticket_form)),
    path("flux/", app_views.flux, name="flux"),
    path("404/", error_views.error),
]
