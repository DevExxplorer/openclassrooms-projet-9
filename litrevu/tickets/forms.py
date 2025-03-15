from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre", "description": "Description", "image": "Image"}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
        labels = {"headline": "Titre", "rating": "Note", "body": "Commentaire"}

    rating = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(6)],  # De 0 à 5
        widget=forms.RadioSelect(attrs={"class": "radio_input"}),
        required=True,
    )
    rating.label = "Note"
