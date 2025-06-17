from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    payment_id = models.CharField(
        max_length=300, unique=True, verbose_name='ID do Pagamento')
    type = models.CharField(max_length=100, default='online',
                            verbose_name='Tipo do Pagamento')
    status = models.CharField(
        max_length=50, verbose_name='Status da Transação')
    status_detail = models.CharField(
        max_length=150, verbose_name='Detalhes da Transação')

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor Total')
    total_paid_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Total Pago')

    ticket_url = models.TextField(verbose_name='Link de Pagamento')

    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='payments', verbose_name='Usuário')

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['created_at']

    def __str__(self) -> str:
        return f'#{self.pk} - {self.user.email} - {self.total_amount}'
