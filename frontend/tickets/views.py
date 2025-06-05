from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tickets.models import Ticket


class TicketListView(LoginRequiredMixin, ListView):
    """
    View para listar todos os ingressos
    """
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        """
        Retorna os ingressos pelo filtro
        """
        search = self.request.GET.get('search', '')

        # Se houver busca, filtra os ingressos pelo nome
        if search:
            return Ticket.objects.filter(name__icontains=search).order_by('-created_at')

        # Caso contrário, retorna todos os ingressos
        return Ticket.objects.all()


class TicketDetailView(LoginRequiredMixin, DetailView):
    """
    View para exibir os detalhes de um ingresso específico
    """
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket'
