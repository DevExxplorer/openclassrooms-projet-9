from django.contrib import admin
from .models import User, Ticket, Review

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Review)
