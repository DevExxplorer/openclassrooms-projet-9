from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
    )
