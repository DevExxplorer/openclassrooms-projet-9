const page = document.querySelector('.posts')

if (page){
    const tickets = page.querySelectorAll('.post')

    tickets.forEach((ticket) => {
        const btn = ticket.querySelector('.delete')

        if (btn) {
            btn.addEventListener('click', (e) => {
                e.preventDefault()

                const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
                const deleteUrl = btn.getAttribute('href');
                const divMessage = document.querySelector('.message-alert span')
                const idTicket = btn.dataset ? btn.dataset.postId : ''

                // Requete AJAX en utilisant fetch
                fetch(deleteUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        btn.closest('.post').remove();
                        deleteChildsTicket(tickets, idTicket)
                        divMessage.innerHTML = 'Le post a bien été supprimé'
                        divMessage.classList.add('validate')
                    } else {
                        divMessage.innerHTML = 'Un erreur est surevenue : le ticket n\'a pas été supprimé'
                        divMessage.classList.add('error')
                    }
                })
                .catch(error => {
                    divMessage.innerHTML = 'Une erreur est survenue'
                    console.error('Erreur AJAX :', error);
                    divMessage.classList.add('error')
                });
            })
        }
    })
}

/**
 * On vérifie si le ticket à des reviews et on les supprime
 * @param tickets
 * @param idTicket
 */
function deleteChildsTicket(tickets, idTicket) {
    tickets.forEach(ticket => {
        if (ticket.dataset && ticket.dataset.ticketId) {
            if (ticket.dataset.ticketId === idTicket) {
                ticket.remove()
            }
        }
    })
}