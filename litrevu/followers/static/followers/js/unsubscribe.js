const followers = document.querySelector('.followers')

if (followers){
    const lists_users = followers.querySelectorAll('.list_users__item');

    lists_users.forEach((element) => {
        const btn_unsubscribe = element.querySelector('.unsubscribe')
        btn_unsubscribe.addEventListener('click', (e) => {
            e.preventDefault()

            const link = btn_unsubscribe.querySelector('a')
            const user_id = link.dataset.user_id

            // Requete AJAX en utilisant fetch
            fetch('/abonnements/unsubscribe/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({ user_id: user_id })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Utilisateur désabonné avec succès!')
                    element.remove();
                } else {
                    alert('Erreur lors du désabonnement');
                }
            })
            .catch(error => {
                console.error('Erreur AJAX :', error);
                alert('Une erreur est survenue');
            });
        })
    })
}

/*
* Token nécessaire pour envoyer des requetes POST sécurisées
* */
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}