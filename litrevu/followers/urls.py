from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import unsubscribe_user, page_views

urlpatterns = [
    path("", login_required(page_views), name="followers"),
    path("unsubscribe/", login_required(unsubscribe_user), name="unsubscribe_user"),
]