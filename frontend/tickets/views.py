from django.views.generic import ListView, DetailView
from tickets.models import Ticket


class TicketListView(ListView):
    """
    View para listar todos os ingressos
    """
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'


class TicketDetailView(DetailView):
    """
    View para exibir os detalhes de um ingresso específico
    """
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket'
