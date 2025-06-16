from django.views.generic import ListView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from orders.models import Order
from tickets.models import Ticket


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        """
        Retorna apenas os registros criados pelo usuário
        """
        return super().get_queryset().filter(user=self.request.user)


class OrderCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Captura o id do ingresso e cria um novo pedido
        """
        # Captura o ID do ingresso
        ticket_id = request.POST.get('ticket_id', '')
        ticket = get_object_or_404(Ticket, id=ticket_id)

        try:
            # Verifica se já há um pedido do mesmo ingresso
            order_exists = Order.objects.filter(
                ticket=ticket, user=self.request.user).exists()

            if not order_exists:
                # Cria um novo pedido no banco
                Order.objects.create(
                    ticket=ticket,
                    user=self.request.user,
                    status='pending',
                )

                return redirect(reverse_lazy('list-orders'))

            return redirect(reverse_lazy('ticket-list'))
        except Exception as e:
            return redirect(reverse_lazy('ticket-list'))


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('list-orders')

    def get(self, request, *args, **kwargs):
        super().delete(request)

        return redirect(reverse_lazy('list-orders'))
