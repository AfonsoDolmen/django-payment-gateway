from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('paid', 'Pago'),
        ('failed', 'Falhou'),
        ('cancelled', 'Cancelado'),
    ]

    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name='orders', verbose_name='Ingresso')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', verbose_name='Usuário')
    quantity = models.IntegerField(default=1, verbose_name='Quantidade')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em')

    class Meta:
        """
        Config metadados
        """
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['created_at']

    def __str__(self) -> str:
        return f'#{self.pk} - {self.user.email}'

    @property
    def total_value(self) -> float:
        """
        Calcula o preço total com base na quantidade
        """
        return self.quantity * self.ticket.price
