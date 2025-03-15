from django import forms


class LoginForm(forms.Form):
    """
    Formulaire de connexion

    Args:
        forms.Form: Classe parent permettant de créer un formulaire Django.
    """

    username = forms.CharField(
        label="name",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}),
    )
