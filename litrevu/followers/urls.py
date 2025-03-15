from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import subscribe_user, unsubscribe_user, page_views


urlpatterns = [
    path("", login_required(page_views), name="followers"),
    path("subscribe/", login_required(subscribe_user), name="subscribe"),
    path("unsubscribe/", login_required(unsubscribe_user), name="unsubscribe_user"),
]
