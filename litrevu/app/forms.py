from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SubscribeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nom d\'utilisateur'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Mot de passe'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmez le mot de passe'})
        self.fields['username'].help_text = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

class LoginForm(forms.Form):
    username = forms.CharField(label="name", max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
    )