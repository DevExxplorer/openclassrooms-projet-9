from django import forms
from .models import Ticket ,Review

class LoginForm(forms.Form):
    username = forms.CharField(
        label="name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
    )

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']