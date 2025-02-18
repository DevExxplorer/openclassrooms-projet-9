from tickets.forms import TicketForm, ReviewForm

def add_new_data(request, type_data='ticket', ticket=None):
    """
        Fonction permettant de gérer l'ajout d'un nouveau ticket, d'une review ou des deux à la fois.

        En fonction du type de données spécifié (`type_data`), la fonction initialise et traite les formulaires
        pour la création d'un ticket, d'une review ou d'une review associée à un nouveau ticket.

        Args:
            request (HttpRequest): Requête HTTP envoyée par l'utilisateur.
            type_data (str, optional): Type de donnée à traiter. Peut être 'ticket', 'review' ou 'ticket_review'.
                - 'ticket' : Création d'un nouveau ticket.
                - 'review' : Ajout d'une review à un ticket existant.
                - 'ticket_review' : Création d'un ticket et d'une review en même temps.
            ticket (Ticket, optional): Instance de Ticket à laquelle associer une review (nécessaire pour 'review').

        Returns:
            dict: Contient les formulaires
    """
    valid = False
    ticket_form = None
    review_form = None

    if request.method == 'POST':
        # Initialisation des formulaires
        if type_data in ['ticket', 'ticket_review']:
            ticket_form = TicketForm(request.POST, request.FILES)
        if type_data in ['review', 'ticket_review']:
            review_form = ReviewForm(request.POST)

        # Traitement selon le type
        if type_data == 'ticket':
            if ticket_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()
                valid = True

        elif type_data == 'review':
            if ticket and review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.ticket = ticket
                review.save()
                valid = True

        elif type_data == 'ticket_review':
            if ticket_form.is_valid() and review_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()

                review = review_form.save(commit=False)
                review.user = request.user
                review.ticket = ticket
                review.save()
                valid = True

    else:
        # Initialisation des formulaires pour affichage
        if type_data in ['ticket', 'ticket_review']:
            ticket_form = TicketForm()
        if type_data in ['review', 'ticket_review']:
            review_form = ReviewForm()

    return {
        'ticket_form': ticket_form,
        'review_form': review_form,
        'valid': valid
    }
