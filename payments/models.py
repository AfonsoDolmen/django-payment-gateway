from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    payment_id = models.TextField(unique=True, verbose_name='ID do Pagamento')
    init_point = models.TextField(verbose_name='Link para Pagamento')

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
