document.addEventListener('DOMContentLoaded', () => {
    subscribe()
    unsubscribe()
})

/**
 * Ajout d'un nouvelle abonné
 */
function subscribe() {
    const followerSearch = document.querySelector('.followers__research')

    if (followerSearch) {
        const form = followerSearch.querySelector('form');
        const submitForm = form.querySelector('input[type="submit"]')

        submitForm.addEventListener('click', (e) => {
            e.preventDefault()

            const searchInput = form.querySelector('input[type="search"]')
            const messageDiv = followerSearch.querySelector('.message')
            const searchValue = searchInput.value
            const viewSubscribe = document.querySelector('.followers__subscribe')
            const listSubscribe = viewSubscribe.querySelector('.list_users');
            const messageSubscribe = viewSubscribe.querySelector('.message');

            // Requete AJAX en utilisant fetch
            fetch('/abonnements/subscribe/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({
                    'search_value': searchValue,
                })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        messageDiv.innerHTML = 'Utilisateur ajouté à vos abonnés suivis !';
                        messageDiv.classList.add('validate');
                        listSubscribe.insertAdjacentHTML("beforeend",
                            `
                            <div class="list_users__item">
                                <div class="name"><span>${searchValue}</span></div>
                                <div class="link unsubscribe">
                                    <a href="#" data-user_id="${data.user_id}" title="Se désabonner">Désabonner</a>
                                </div>
                            </div>
                        `)
                        messageSubscribe.innerHTML = ''

                        unsubscribe()
                    } else {
                        messageDiv.innerHTML = 'Utilisateur non trouvé ou déjà suivi.';
                        messageDiv.classList.add('error');
                    }
                })
                .catch(error => {
                    messageDiv.innerHTML = 'Erreur technique. Veuillez contacter un admin!'
                    messageDiv.classList.add('error')
                    console.error('Erreur AJAX :', error);
                });
        })
    }
    }

/**
 * Suppression d'un abonné
 */
function unsubscribe(){
    const followers = document.querySelector('.followers__subscribe')

    if (followers){
        const lists_users = followers.querySelectorAll('.list_users__item');

        lists_users.forEach((element) => {
            const btn_unsubscribe = element.querySelector('.unsubscribe')
            btn_unsubscribe.addEventListener('click', (e) => {
                e.preventDefault()

                const link = btn_unsubscribe.querySelector('a')
                const user_id = link.dataset.user_id
                const messageDiv = followers.querySelector('.message')

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
                        messageDiv.innerHTML = 'Utilisateur désabonné avec succès!'
                        messageDiv.classList.add('validate')
                        element.remove();
                    } else {
                        messageDiv.innerHTML = 'Erreur lors du désabonnement'
                        messageDiv.classList.add('error')
                    }
                })
                .catch(error => {
                    messageDiv.innerHTML = 'Erreur technique. Veuillez contacter un admin!'
                    messageDiv.classList.add('error')
                    console.error('Erreur AJAX :', error);
                });
            })
        })
    }
}


/*
* Token nécessaire pour envoyer des requetes POST sécurisées
* */
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}