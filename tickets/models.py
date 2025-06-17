from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Preço')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em')

    class Meta:
        """
        Config metadados
        """
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['created_at']

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'
